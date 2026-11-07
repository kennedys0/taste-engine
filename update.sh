#!/usr/bin/env bash
# Taste Engine updater - portable Bash + Python 3, no third-party Python packages.
# Sources: a trusted local ZIP, or a GitHub Release ZIP from an explicitly selected repo.
set -Eeuo pipefail

DEFAULT_TARGET="${HOME}/.gemini/config/skills/taste-engine"
TARGET="${TASTE_ENGINE_TARGET:-$DEFAULT_TARGET}"
CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/taste-engine"
REPO_FILE="$CONFIG_DIR/repository"
REPO="${TASTE_ENGINE_REPO:-}"
ZIP_PATH=""
TAG=""
EXPECTED_SHA=""
FORCE=0
DRY_RUN=0
WORK=""
STAGE=""
BACKUP=""
BACKUP_MOVED=0
COMMITTED=0

fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
info() { printf '%s\n' "$*"; }
usage() {
  cat <<'HELP'
Taste Engine - safe updater

Usage:
  bash update.sh --zip ~/Downloads/taste-engine-v0.13.1.zip
  bash update.sh --repo OWNER/REPO [--tag v0.13.1]
  bash update.sh --set-repo OWNER/REPO    # store GitHub Releases source for later
  taste-engine update                     # downloads from the official GitHub Release
  taste-engine version

Options:
  --zip FILE          Update from downloaded ZIP (works offline)
  --repo OWNER/REPO   Fetch latest GitHub Release ZIP
  --set-repo OWNER/REPO  Save default repo for future `taste-engine update`
  --tag TAG           Choose release tag rather than latest
  --sha256 HEX        Verify ZIP against expected SHA-256
  --target DIRECTORY  Install location (default: ~/.gemini/config/skills/taste-engine)
  --force             Allow reinstalling same/older version
  --dry-run           Validate candidate but do not replace installed skill
  --help              Show help

Default GitHub source: kennedys0/taste-engine. A published Release is required.
Source archives are treated as trusted software: their pack validator executes.
HELP
}

valid_repo() { [[ "$1" =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]]; }

if [[ "${1:-}" == "update" || "${1:-}" == "-update" || "${1:-}" == "--update" ]]; then shift; fi
if [[ "${1:-}" == "version" || "${1:-}" == "--version" || "${1:-}" == "-v" ]]; then
  shift
  [[ $# -eq 0 ]] || fail 'version takes no arguments'
  if [[ -f "$TARGET/SKILL.md" ]]; then
    python3 - "$TARGET/SKILL.md" <<'PY'
import re, sys
text=open(sys.argv[1],encoding='utf-8').read().split('---',2)
match=re.search(r'^\s*version:\s*["\x27]?([0-9]+\.[0-9]+\.[0-9]+)', text[1] if len(text)>1 else '',re.M)
print('Taste Engine v'+match.group(1) if match else 'Taste Engine (unknown version)')
PY
  else
    info 'Taste Engine is not installed at selected target.'
  fi
  exit 0
fi

SET_REPO=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --zip|--repo|--tag|--sha256|--target|--set-repo)
      [[ $# -ge 2 ]] || fail "Missing value after $1"
      case "$1" in
        --zip) ZIP_PATH="$2";;
        --repo) REPO="$2";;
        --tag) TAG="$2";;
        --sha256) EXPECTED_SHA="$(printf '%s' "$2" | tr '[:upper:]' '[:lower:]')";;
        --target) TARGET="$2";;
        --set-repo) SET_REPO="$2";;
      esac
      shift 2;;
    --force) FORCE=1; shift;;
    --dry-run) DRY_RUN=1; shift;;
    -h|--help|help) usage; exit 0;;
    *) fail "Unknown argument: $1 (see --help)";;
  esac
done

if [[ -n "$SET_REPO" ]]; then
  valid_repo "$SET_REPO" || fail 'Repository must be OWNER/REPO'
  [[ -z "$ZIP_PATH" && -z "$TAG" && -z "$EXPECTED_SHA" ]] || fail '--set-repo cannot be combined with update options'
  mkdir -p "$CONFIG_DIR" && chmod 700 "$CONFIG_DIR"
  printf '%s\n' "$SET_REPO" > "$REPO_FILE" && chmod 600 "$REPO_FILE"
  info "Configured release source: $SET_REPO"
  info 'Next time run: taste-engine update'
  exit 0
fi

[[ "$TARGET" == /* ]] || fail '--target must be an absolute path'
[[ "${TARGET%/}" == */taste-engine ]] || fail 'Target directory must be named taste-engine'
TARGET="${TARGET%/}"
[[ ! -L "$TARGET" ]] || fail 'Target cannot be a symlink'
[[ ! -e "$TARGET" || -d "$TARGET" ]] || fail 'Target exists but is not a directory'
PARENT="$(dirname "$TARGET")"
if [[ -z "$REPO" && -z "$ZIP_PATH" && -f "$REPO_FILE" ]]; then
  REPO="$(cat "$REPO_FILE")"
fi
[[ -n "$REPO" || -n "$ZIP_PATH" ]] || REPO="kennedys0/taste-engine"
[[ -z "$REPO" ]] || valid_repo "$REPO" || fail 'Repository must be OWNER/REPO'
[[ -z "$ZIP_PATH" || -z "$REPO" ]] || fail 'Choose --zip OR --repo, not both'
[[ -z "$TAG" || -n "$REPO" ]] || fail '--tag requires --repo'
[[ -z "$EXPECTED_SHA" || "$EXPECTED_SHA" =~ ^[0-9a-f]{64}$ ]] || fail 'Invalid SHA-256 hex string'
[[ -n "$ZIP_PATH" || -n "$REPO" ]] || { usage; fail 'No update source: pass --zip or configure a GitHub repo with --set-repo'; }
command -v python3 >/dev/null 2>&1 || fail 'Python 3 is required'
if command -v sha256sum >/dev/null 2>&1; then
  sha256_cmd() { sha256sum "$1" | awk '{print $1}'; }
elif command -v shasum >/dev/null 2>&1; then
  sha256_cmd() { shasum -a 256 "$1" | awk '{print $1}'; }
else
  fail 'sha256sum or shasum is required'
fi

# The swap and backups reside on the same filesystem as the installed skill.
mkdir -p "$PARENT"
WORK="$(mktemp -d "$PARENT/.taste-engine-update.XXXXXXXX")"
cleanup() {
  code=$?
  trap - EXIT
  if [[ $BACKUP_MOVED -eq 1 && $COMMITTED -eq 0 && ! -d "$TARGET" && -d "$BACKUP" ]]; then
    mv "$BACKUP" "$TARGET" || printf 'CRITICAL: restore backup manually: %s\n' "$BACKUP" >&2
  fi
  [[ -z "$STAGE" || ! -e "$STAGE" ]] || rm -rf -- "$STAGE"
  [[ -z "$WORK" || ! -d "$WORK" ]] || rm -rf -- "$WORK"
  exit "$code"
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

if [[ -n "$REPO" && -z "$ZIP_PATH" ]]; then
  command -v curl >/dev/null 2>&1 || fail 'curl required for GitHub Releases updates'
  info "Checking GitHub releases for $REPO ..."
  API="https://api.github.com/repos/$REPO/releases"
  if [[ -n "$TAG" ]]; then
    [[ "$TAG" =~ ^[A-Za-z0-9_.-]+$ ]] || fail 'Invalid release tag'
    API="$API/tags/$TAG"
  else
    API="$API/latest"
  fi
  AUTH_HEADER=()
  if [[ -n "${GITHUB_TOKEN:-}" ]]; then
    AUTH_HEADER=(-H "Authorization: Bearer $GITHUB_TOKEN")
  fi

  API_SUCCESS=0
  if curl -fsSL ${AUTH_HEADER[@]+"${AUTH_HEADER[@]}"} --connect-timeout 12 --max-time 45 \
    -H 'Accept: application/vnd.github+json' \
    -H 'User-Agent: taste-engine-updater' "$API" -o "$WORK/release.json" 2>/dev/null; then
    API_SUCCESS=1
  fi

  if [[ $API_SUCCESS -eq 1 ]]; then
    python3 - "$WORK/release.json" "$WORK/download-url" "$WORK/release-digest" <<'PY'
import json,re,sys
r=json.load(open(sys.argv[1],encoding='utf-8'))
assets=[a for a in r.get('assets',[]) if re.fullmatch(r'taste-engine-v\d+\.\d+\.\d+\.zip',a.get('name',''))]
if len(assets)!=1:
    raise SystemExit('ERROR: Expected exactly one Release asset named taste-engine-vX.Y.Z.zip')
a=assets[0]; url=a.get('browser_download_url','')
if not re.fullmatch(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/releases/download/[^/]+/[^/]+\.zip',url):
    raise SystemExit('ERROR: unexpected GitHub asset URL')
open(sys.argv[2],'w').write(url)
open(sys.argv[3],'w').write(a.get('digest') or '')
PY
    DOWNLOAD_URL="$(cat "$WORK/download-url")"
    [[ ! -f "$WORK/release-digest" ]] || RELEASE_SHA="$(cat "$WORK/release-digest")"
  else
    # Fallback when GitHub API is rate-limited (HTTP 403) or unauthenticated
    info "GitHub API rate limit or auth constraint detected; resolving release directly via web redirect..."
    if [[ -z "$TAG" ]]; then
      TAG_URL="$(curl -fsSIL --connect-timeout 12 --max-time 30 -o /dev/null -w "%{url_effective}" "https://github.com/$REPO/releases/latest" 2>/dev/null || true)"
      TAG_NAME="${TAG_URL##*/}"
    else
      TAG_NAME="$TAG"
    fi
    [[ -n "$TAG_NAME" && "$TAG_NAME" =~ ^v?[0-9]+\.[0-9]+\.[0-9]+ ]] || fail 'Could not resolve latest release tag from GitHub'
    DOWNLOAD_URL="https://github.com/$REPO/releases/download/$TAG_NAME/taste-engine-$TAG_NAME.zip"
    RELEASE_SHA=""
  fi
  if [[ -z "$RELEASE_SHA" ]]; then
    RELEASE_TAG="${TAG:-}"
    if [[ -z "$RELEASE_TAG" && -f "$WORK/release.json" ]]; then
      RELEASE_TAG="$(python3 -c "import json,sys; print(json.load(open(sys.argv[1],encoding='utf-8')).get('tag_name',''))" "$WORK/release.json" 2>/dev/null || true)"
    fi
    if [[ -z "$RELEASE_TAG" && -n "${TAG_NAME:-}" ]]; then
      RELEASE_TAG="$TAG_NAME"
    fi
    if [[ -n "$RELEASE_TAG" ]]; then
      SHA256_URL="https://github.com/$REPO/releases/download/$RELEASE_TAG/SHA256SUMS"
      if curl -fsSL --connect-timeout 12 --max-time 30 -H 'User-Agent: taste-engine-updater' "$SHA256_URL" -o "$WORK/SHA256SUMS" 2>/dev/null; then
        while read -r sha filename || [[ -n "$sha" ]]; do
          if [[ "$filename" == "taste-engine-$RELEASE_TAG.zip" || "$filename" == *"taste-engine-$RELEASE_TAG.zip"* ]]; then
            if [[ "$sha" =~ ^[0-9a-fA-F]{64}$ ]]; then
              RELEASE_SHA="sha256:$sha"
              break
            fi
          fi
        done < "$WORK/SHA256SUMS"
      fi
    fi
  fi
  ZIP_PATH="$WORK/release.zip"
  curl -fsSL --retry 2 --connect-timeout 12 --max-time 180 \
    -H 'User-Agent: taste-engine-updater' "$DOWNLOAD_URL" -o "$ZIP_PATH" \
    || fail 'Failed to download release ZIP'
  if [[ -z "$EXPECTED_SHA" && "$RELEASE_SHA" =~ ^sha256:[0-9a-fA-F]{64}$ ]]; then
    EXPECTED_SHA="${RELEASE_SHA#sha256:}"
    EXPECTED_SHA="$(printf '%s' "$EXPECTED_SHA" | tr '[:upper:]' '[:lower:]')"
  fi
  [[ -n "$EXPECTED_SHA" ]] || info 'WARNING: Download could not be verified against an expected SHA256 digest.'
fi
[[ -f "$ZIP_PATH" ]] || fail "ZIP not found: $ZIP_PATH"
if [[ -n "$EXPECTED_SHA" ]]; then
  ACTUAL_SHA="$(sha256_cmd "$ZIP_PATH")"
  [[ "$ACTUAL_SHA" == "$EXPECTED_SHA" ]] || fail 'SHA-256 mismatch; refusing update'
  info 'SHA-256 verification passed.'
fi

# Strict ZIP safety: reject traversal, absolute paths, symlinks, oversized archives,
# encrypted entries and multiple ambiguous router candidates.
mkdir -p "$WORK/extract"
python3 - "$ZIP_PATH" "$WORK/extract" <<'PY'
from pathlib import Path, PurePosixPath
import os, shutil, stat, sys, zipfile
src=Path(sys.argv[1]); out=Path(sys.argv[2]); total=0
with zipfile.ZipFile(src) as z:
    infos=z.infolist()
    if len(infos)>1000: raise SystemExit('ERROR: ZIP has too many entries')
    for i in infos:
        p=PurePosixPath(i.filename)
        if not i.filename or '\\' in i.filename or p.is_absolute() or '..' in p.parts or '.' in p.parts:
            raise SystemExit(f'ERROR: unsafe ZIP path: {i.filename!r}')
        if i.flag_bits & 0x1: raise SystemExit('ERROR: encrypted ZIP not supported')
        mode=(i.external_attr >> 16)
        if stat.S_ISLNK(mode) or (stat.S_IFMT(mode) and not (stat.S_ISREG(mode) or stat.S_ISDIR(mode))):
            raise SystemExit('ERROR: links/devices are not allowed inside ZIP')
        total+=i.file_size
        if total>75*1024*1024: raise SystemExit('ERROR: ZIP exceeds 75 MB unpacked')
    for i in infos:
        p=out.joinpath(*PurePosixPath(i.filename).parts)
        if i.is_dir(): p.mkdir(parents=True,exist_ok=True)
        else:
            p.parent.mkdir(parents=True,exist_ok=True)
            with z.open(i) as source, p.open('wb') as dest: shutil.copyfileobj(source,dest)
routers=[p.parent for p in out.rglob('SKILL.md') if p.parent.name=='taste-engine' and (p.parent/'styles/registry.json').is_file()]
if len(routers)!=1: raise SystemExit('ERROR: Archive must contain exactly one taste-engine/SKILL.md + styles/registry.json')
(out.parent/'router-path').write_text(str(routers[0]))
PY
ROUTER="$(cat "$WORK/router-path")"
[[ -f "$ROUTER/scripts/validate-pack.py" ]] || fail 'Archive does not contain pack validator'

info 'Running source-pack validation ...'
python3 "$ROUTER/scripts/validate-pack.py" || fail 'Source pack validation failed; installation unchanged'
OLD_VERSION="$(python3 - "$TARGET/SKILL.md" <<'PY'
import pathlib,re,sys
p=pathlib.Path(sys.argv[1]); s=p.read_text() if p.is_file() else ''
m=re.search(r'(?m)^\s*version:\s*["\x27]?(\d+\.\d+\.\d+)',s)
print(m.group(1) if m else '')
PY
)"
NEW_VERSION="$(python3 - "$ROUTER/SKILL.md" <<'PY'
import pathlib,re,sys
s=pathlib.Path(sys.argv[1]).read_text()
m=re.search(r'(?m)^\s*version:\s*["\x27]?(\d+\.\d+\.\d+)',s)
print(m.group(1) if m else '')
PY
)"
[[ "$NEW_VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || fail 'Source SKILL.md has no valid semantic version'
if [[ -n "$OLD_VERSION" && $FORCE -eq 0 ]]; then
  CMP="$(python3 - "$OLD_VERSION" "$NEW_VERSION" <<'PY'
import sys
old=tuple(map(int,sys.argv[1].split('.')))
new=tuple(map(int,sys.argv[2].split('.')))
print((new>old)-(new<old))
PY
)"
  if [[ "$CMP" != 1 ]]; then
    info "Already at v$OLD_VERSION; candidate v$NEW_VERSION is not newer. (Use --force to override.)"
    exit 0
  fi
fi
info "Candidate v$NEW_VERSION; installed v${OLD_VERSION:-none}; target: $TARGET"
if [[ $DRY_RUN -eq 1 ]]; then
  info 'Dry run passed. No files were changed.'
  exit 0
fi

# Stage completely before touching the existing installation.
STAGE="$(mktemp -d "$PARENT/.taste-engine-stage.XXXXXXXX")"
cp -a "$ROUTER/." "$STAGE/"
# The validator now supports both a complete distribution and an installed router.
python3 "$STAGE/scripts/validate-pack.py" || fail 'Staged pack validation failed; installation unchanged'

if [[ -e "$TARGET" ]]; then
  BACKUP_DIR="$(dirname "$PARENT")/.taste-engine-backups"
  mkdir -p "$BACKUP_DIR"
  BACKUP="$BACKUP_DIR/taste-engine-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  mv -- "$TARGET" "$BACKUP" || fail 'Could not back up existing installation'
  BACKUP_MOVED=1
fi
mv -- "$STAGE" "$TARGET" || fail 'Could not activate new installation'
STAGE=""
if ! python3 "$TARGET/scripts/validate-pack.py"; then
  info 'Installed pack validation failed. Restoring backup ...' >&2
  rm -rf -- "$TARGET"
  fail 'Update failed; previous skill will be restored'
fi
COMMITTED=1
info "SUCCESS: Taste Engine v$NEW_VERSION installed at $TARGET"
[[ $BACKUP_MOVED -eq 0 ]] || info "Backup retained at $BACKUP"
info 'Restart the agent conversation or reload skill discovery in your IDE.'
