#!/usr/bin/env bash
# Publish a complete source snapshot as a PR branch in an already-created repo.
# Preserves the remote's history and never forces a push to main.
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="${1:-kennedys0/taste-engine}"
[[ "$REPO" =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]] || { echo 'Expected owner/repo' >&2; exit 2; }
BRANCH="feat/global-readme-cli-v0.10.0"
for cmd in git python3 node; do command -v "$cmd" >/dev/null || { echo "Missing $cmd" >&2; exit 1; }; done
python3 "$ROOT/scripts/sync-agent-skills.py" --check
python3 "$ROOT/taste-engine/scripts/validate-pack.py"
node --test "$ROOT/tests/cli.test.mjs" >/dev/null
TMP="$(mktemp -d -t taste-engine-publish-XXXXXXXX)"
trap 'rm -rf -- "$TMP"' EXIT
echo "Cloning https://github.com/$REPO.git ..."
git clone "https://github.com/$REPO.git" "$TMP/repo"
if git -C "$TMP/repo" show-ref --verify --quiet "refs/heads/$BRANCH"; then
  echo "Local branch $BRANCH already exists. Choose a new branch or delete the local clone." >&2; exit 1
fi
git -C "$TMP/repo" switch -c "$BRANCH"
python3 - "$ROOT" "$TMP/repo" <<'PY'
from pathlib import Path
import shutil,sys
source=Path(sys.argv[1]); dest=Path(sys.argv[2]);
for p in source.iterdir():
    if p.name in {'.git','dist','__pycache__','build'}:continue
    if p.is_symlink(): raise SystemExit('Refusing to publish symlink: '+str(p))
    target=dest/p.name
    if p.is_dir():
        if target.exists():shutil.rmtree(target)
        shutil.copytree(p,target,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    elif p.is_file(): shutil.copy2(p,target)
PY
git -C "$TMP/repo" add -A
if git -C "$TMP/repo" diff --cached --quiet; then
 echo 'No changes to publish';exit 0
fi
git -C "$TMP/repo" commit -m 'feat: English docs and multi-agent CLI installer v0.10.0'
echo "Prepared branch $BRANCH for $REPO"
read -r -p 'Type PUBLISH to push this new branch (never main): ' answer
[[ "$answer" == PUBLISH ]] || { echo 'Cancelled without pushing.'; exit 0; }
git -C "$TMP/repo" push -u origin "$BRANCH"
echo "Changes pushed. Open a pull request: https://github.com/$REPO/compare/main...$BRANCH?expand=1"
if command -v gh >/dev/null && gh auth status >/dev/null 2>&1; then
  gh pr create --repo "$REPO" --base main --head "$BRANCH" --title 'feat: global English documentation and multi-agent CLI installer' --body 'Adds global-English README and docs, standard Agent Skills installation, native Antigravity/Claude/Codex installer, versioned release packaging, and CI validation.' || true
fi
