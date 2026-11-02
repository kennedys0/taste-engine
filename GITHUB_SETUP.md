# Maintainer publishing checklist

Repository: [kennedys0/taste-engine](https://github.com/kennedys0/taste-engine).

## First source push

The GitHub repository was created before the full source tree. From the **project root on your own computer**, clone the existing repository, copy the package files into it, and commit. Do not force-push over the existing `main` branch.

```bash
# Run after extracting the latest source package, in its root directory.
git clone https://github.com/kennedys0/taste-engine.git ../taste-engine-live
rsync -av --exclude='.git' --exclude='dist/' --exclude='__pycache__/' ./ ../taste-engine-live/
cd ../taste-engine-live
python3 scripts/sync-agent-skills.py --check
python3 taste-engine/scripts/validate-pack.py
git add .
git commit -m "feat: publish Taste Engine v0.10.0"
git push origin main
```

If you prefer pull requests, create a feature branch, push it, and open a PR before merging.

## Release

After the source is on `main` and CI is green:

```bash
git tag v0.10.0
git push origin v0.10.0
```

The release workflow validates the package and creates an updater-compatible ZIP. Verify the release file and GitHub Actions run before advertising automatic updates.

## Repository settings

Add a concise description, topics such as `agent-skills`, `frontend`, `ui-ux`, `anti-slop`, `seo`, `antigravity`, `claude-code`, and `codex`; enable Issues and Discussions if you plan to accept community proposals. Consider branch protection requiring passing CI before merges.
