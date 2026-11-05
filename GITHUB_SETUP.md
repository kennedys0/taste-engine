# Maintainer publishing checklist

Repository: [kennedys0/taste-engine](https://github.com/kennedys0/taste-engine).

## Verification pre-flight

Before tagging or publishing a release, ensure all checks pass locally:

```bash
python3 scripts/sync-agent-skills.py --check
python3 taste-engine/scripts/validate-pack.py
python3 -m unittest discover -s taste-engine/tests -p 'test_*.py'
node --test tests/cli.test.mjs
python3 scripts/build-release.py
```

Note: Canonical edits must always be made in `taste-engine/`. Run `python3 scripts/sync-agent-skills.py` to keep `skills/taste-engine/` and root `update.sh` in sync.

## Release workflow

Releases are published using the automated GitHub Actions workflow (`.github/workflows/release.yml`):

### 1. Triggering a release

- **Automatic:** Push a semantic version tag:
  ```bash
  git tag v<version>
  git push origin v<version>
  ```
- **Manual:** Navigate to **Actions** -> **Publish release** and click **Run workflow** (`workflow_dispatch`), specifying the target branch or tag.

### 2. What the workflow does

1. Validates version parity across `package.json`, `SKILL.md`, and `bin/taste-engine.mjs`.
2. Runs the full test suite (`sync-agent-skills.py --check`, `validate-pack.py`, Python unittests, and Node CLI tests).
3. Builds the release archive `dist/taste-engine-v<version>.zip`.
4. Computes cryptographic checksums into `dist/SHA256SUMS`.
5. Checks if the release tag already exists (fails safely to prevent silent clobbering).
6. Publishes the GitHub Release with generated release notes, attaching both the ZIP archive and `SHA256SUMS`.

### 3. Workflow permissions

The release workflow requires `contents: write` permissions (configured in the workflow YAML) to publish releases and upload assets. Ensure the default `GITHUB_TOKEN` has read/write permissions enabled under **Settings** -> **Actions** -> **General** -> **Workflow permissions**.

## Repository settings

Add a concise description and topics such as `agent-skills`, `frontend`, `ui-ux`, `anti-slop`, `seo`, `antigravity`, `claude-code`, and `codex`. Enable Issues and Discussions if you plan to accept community proposals, and consider branch protection on `main` requiring green CI before merges.
