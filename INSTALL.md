# Installation and updates

Taste Engine is a portable Agent Skill with one entry point (`SKILL.md`) and local reference files. It does not require a particular JavaScript UI framework.

## Agent Skills CLI (recommended)

Use the open [`skills` CLI](https://github.com/vercel-labs/skills) to install the skill from this repository:

```bash
npx skills add kennedys0/taste-engine --skill taste-engine
```

The CLI supports selecting an agent, copying or linking the skill, choosing project/global scope, and managed updates.

```bash
npx skills add kennedys0/taste-engine --skill taste-engine -a claude-code -g -y
npx skills add kennedys0/taste-engine --skill taste-engine -a codex -g -y
npx skills add kennedys0/taste-engine --skill taste-engine -a antigravity -g -y
npx skills add kennedys0/taste-engine --skill taste-engine -a antigravity-cli -g -y
```

**Important:** these commands become usable only when the repository contains `skills/taste-engine/SKILL.md` on its default branch. An empty GitHub repository cannot install a skill.

## Built-in Node.js installer

Use the included installer if you need Antigravity IDE's current global path rather than the `skills` CLI's compatibility path.

Prerequisites: Git and Node.js 20 or later. No npm dependencies.

```bash
git clone https://github.com/kennedys0/taste-engine.git
cd taste-engine
node bin/taste-engine.mjs install --agent antigravity --global
```

To preview all 10 styles interactively in your browser with synchronized Dark & Light mode contrast:

```bash
node bin/taste-engine.mjs gallery
```

Supported agent selectors:

| `--agent` | Global install location | Project install location |
| --- | --- | --- |
| `antigravity` or `antigravity-ide` | `~/.gemini/config/skills/taste-engine` | `.agents/skills/taste-engine` |
| `antigravity-cli` or `agy` | `~/.gemini/antigravity-cli/skills/taste-engine` | `.agents/skills/taste-engine` |
| `claude-code` or `claude` | `~/.claude/skills/taste-engine` | `.claude/skills/taste-engine` |
| `codex` | `~/.agents/skills/taste-engine` | `.agents/skills/taste-engine` |
| `cursor` or `cursor-ai` | `~/.cursor/skills/taste-engine` | `.cursor/skills/taste-engine` |
| `cline` | `~/.cline/skills/taste-engine` | `.cline/skills/taste-engine` |
| `roo-code` or `roo` | `~/.roo/skills/taste-engine` | `.roo/skills/taste-engine` |
| `windsurf` | `~/.windsurf/skills/taste-engine` | `.windsurf/skills/taste-engine` |
| `copilot` | `~/.github/skills/taste-engine` | `.github/skills/taste-engine` |
| `all` | All global locations (shared paths deduplicated) | All applicable project locations |

The installer defaults to `--project` in your current directory. Specify `--global` for use across all projects or `--cwd /path/to/project` to target another project. Existing Taste Engine installations are backed up to `<parent-of-skills-dir>/.taste-engine-backups/taste-engine-<timestamp>` before replacement (kept outside the skills directory so agents do not discover duplicate skills). Other installed skills are never overwritten.

```bash
node bin/taste-engine.mjs install --agent all --project
node bin/taste-engine.mjs doctor --agent all --project
node bin/taste-engine.mjs uninstall --agent all --project
node bin/taste-engine.mjs version
```

## Updating

**Using the global `taste-engine` shortcut:**

```bash
taste-engine -v        # Check version
taste-engine -update   # Download and apply latest GitHub Release
```

**If installed with `npx skills add`:** use its managed update commands:

```bash
npx skills check
npx skills update -g
```

**If installed manually in Antigravity IDE:** use the bundled Bash updater and a published Release. For an offline ZIP update, pass `--zip PATH`.

```bash
bash ~/.gemini/config/skills/taste-engine/scripts/update.sh

# Or from an already downloaded release asset:
bash ~/.gemini/config/skills/taste-engine/scripts/update.sh --zip ./taste-engine-v0.10.10.zip
```

The Bash updater requires Bash, Python 3, curl (for GitHub downloads), and standard Linux command-line tools. It checks archive contents, validates a staged installation, backs up the previous version, and restores it if activation fails. Never run arbitrary installer scripts from untrusted forks.

## Validate the installed skill

```bash
python3 ~/.gemini/config/skills/taste-engine/scripts/validate-pack.py
```

Test the expected agent behavior by starting a fresh session and asking:

- `Build a portfolio website.` → the agent asks which visual style you prefer.
- `Build a skeuomorphic portfolio website.` → the agent loads the matching style without repeating the question.
- `Fix the mobile navigation in my existing dashboard.` → the agent preserves your existing design.
- `Audit the SEO on my live portfolio.` → the agent does not trigger the visual style picker.

The agent, not the skill files, ultimately decides which skills to invoke. A filesystem installation alone cannot guarantee zero-command activation.

## GitHub Releases

A tag such as `v0.10.0` triggers the release workflow after code is pushed to the repository. The workflow validates the skill, builds `taste-engine-v0.10.0.zip`, and attaches it to the release. The ZIP is compatible with the Bash updater.

See [README.md](README.md) and [GITHUB_SETUP.md](GITHUB_SETUP.md) for maintainer instructions.
