# Changelog

All notable changes to Taste Engine are documented here. Release tags use semantic versioning.

## [Unreleased]

### Fixed

- **CLI Install Backups:** Moved installation backups outside the agent's skills directory into `<parent-of-skills-dir>/.taste-engine-backups/` to prevent agents from discovering duplicate skills with the same name.
- **Gallery Command & npm Packaging:** Included `docs/` in `package.json` `files` so `taste-engine gallery` is available in npm-installed packages, and replaced shell-interpolated `exec()` with argument-array `spawn()` with detached option and error handling.
- **CLI Update & Doctor Parity:** Added `--agent`, `--global|--project`, and `--cwd` options to `taste-engine update` to route updates to specific agent installations (or all existing installations via `--agent all`). Enhanced `taste-engine doctor` to report installed skill versions, corrected README/INSTALL guidance to reference the Node CLI rather than `update.sh` for global shortcuts, and clarified CLI version vs installed version reporting.
- **Bash 3.2 Compatibility in Updater:** Replaced Bash 4-specific lowercase expansions (`${var,,}`) with portable `tr` and guarded empty array expansion `${AUTH_HEADER[@]+"${AUTH_HEADER[@]}"}` under `set -u` in `update.sh`, ensuring compatibility with macOS default Bash 3.2. Added `shasum -a 256` fallback for `sha256sum`, resolved ShellCheck warnings, and documented real system prerequisites.
- **Markdown Table & Frontmatter Formatting:** Removed abnormal blank lines separating table rows in `README.md` and `SKILL.md`, cleaned up YAML frontmatter and code fence padding, and added automated validation checks in `validate-pack.py`.
- **Style Probe Negation & Clause Boundaries:** Updated `style_probe.py` to respect clause boundaries (punctuation `,;.:!?` and conjunctions `but`, `and`, `tapi`, `namun`, `melainkan`), prevent cross-clause negation leakage, treat `not only` as non-negating, and support expanded negation/aversion vocabularies (`hate`, `dislike`, `don't want`, `do not want`, `benci`, `gak mau`, `nggak mau`, `ga mau`, `tidak mau`).
- **Package & CLI Hygiene:** Removed root `"."` export from `package.json` `exports` and added main-module execution guard in `bin/taste-engine.mjs` to prevent CLI execution when imported. Added overwrite guard and `--force` flag to `taste-engine init`. Updated `assertSource(dir)` to validate the staged directory in `install()`.
- **Responsive Baseline & De-duplicated Style Rules:** Extracted shared mobile and responsive layout guidance into `references/responsive-baseline.md`, establishing 320px minimum viewport safety, mobile fluid typography defaults, navigation collapse patterns, circular geometry preservation, inline command pills, and dark-mode slate fallback. Removed contradictory and copy-pasted `1.35rem` clamp rules from all 10 style packs, aligned Swiss Editorial headline scales to `clamp(2rem, 6vw, 4.5rem)`, removed out-of-context slang from `styles/minimalism.md`, shortened `SKILL.md` description to eliminate typos, and added validation in `validate-pack.py`.
- **CSS Recipe Accessibility:** Added `prefers-reduced-motion` to `examples/swiss-editorial/grid-typography.css` and `examples/enterprise/data-cockpit.css`, added `:focus-visible` states to `examples/bento/modular-grid.css` and `examples/enterprise/data-cockpit.css`, and extended `validate-pack.py` to enforce `prefers-reduced-motion` on animated/transitioned recipes and `:focus-visible` on interactive element recipes across all examples.
- **CI & Release Hardening:** Pinned GitHub Actions to immutable full commit SHAs, expanded CI test matrix across Ubuntu, macOS, and Windows runners, added ShellCheck and npm package contents validation steps, dropped release `--clobber` in favor of strict non-destructive release asset creation, generated `SHA256SUMS` alongside release archives, and updated `update.sh` to fetch release checksums and warn visibly when download digests cannot be verified.

## [0.10.10] - 2026-11-05

### Fixed

- **CLI ESM Syntax Fix:** Encapsulated CLI dispatcher execution inside a `main()` function to eliminate illegal top-level `return` statements in ECMAScript modules.
- **CI Release Automation:** Added `workflow_dispatch` trigger to the release workflow.

## [0.10.9] - 2026-11-05

### Added

- **CLI Uninstallation & Safety Guard:** Added `taste-engine uninstall [--agent <name|all>] [--global|--project] [--cwd DIR] [--dry-run]` command that safely uninstalls skill instances while verifying folder identity (`SKILL.md` check) to prevent accidental removal of unrelated user directories.
- **CLI Dry-Run Previews:** Added `--dry-run` (`-n`) flag support across `install`, `uninstall`, and `init` commands for non-destructive filesystem previews.
- **Universal `--help` & `-h` Flags:** Added support for `--help` and `-h` across all subcommands (`init`, `preset`, `gallery`, `install`, `uninstall`, `doctor`, and `update`).
- **Flexible `--init` & Flag Parsing:** Added `--init` and `-init` aliases for preset scaffolding with proper flag parsing (`--dry-run`, `--cwd`), eliminating false folder creation.
- **Global Reduced Motion Token:** Added `reduced_motion` accessibility token (`override_duration_ms: 0`) to `styles/motion-profiles.json`.
- **Automated Version Drift Validation:** Added deterministic checks in `taste-engine/scripts/validate-pack.py` verifying version parity across `package.json`, `SKILL.md`, and `bin/taste-engine.mjs`.
- **Comprehensive Showcase SEO Metadata:** Equipped all 11 HTML showcase pages in `docs/` (`index.html` and 10 style Proof-of-Work studios) with complete Open Graph, Twitter Cards, canonical links, and theme color tags.

### Fixed

- **Package.json Packaging:** Removed nonexistent root `assets/` directory and added `skills/` mirror to `files` array, ensuring complete Agent Skills discovery upon package installation.
- **Package.json npm Scripts & Metadata:** Added standard `npm test` script mapped to CLI test runner, and added `author`, `keywords`, `homepage`, and `bugs` fields.
- **CLI Dead Code & Traversal Sanitization:** Removed redundant dynamic import in `gallery` command, and added input validation to `--agent` and `--cwd` arguments.
- **CHANGELOG Formatting:** Removed duplicate mid-file `# Changelog` heading, normalized line endings from CRLF/double-CR to Unix LF (`\n`), and standardized version headers.
- **Updater Duplicate Read:** Removed redundant secondary file read of `release-digest` in `update.sh`.

## [0.10.8] - 2026-11-04

### Added

- **The Five Structural Tests (Verifiable Artifacts):** Codified mechanical structural procedures across UI, copywriting, and code inspired by [AgriciDaniel/anti-slop](https://github.com/AgriciDaniel/anti-slop):

  - *The Deletion Test:* Cut spans/elements and name what was lost; convict padding if loss is "nothing".

  - *The Inversion Test:* Negate claims; identify vacuous puffery when no rational person would assert the negation.

  - *The Stranger Test:* Ground content in concrete product mechanics that only authentic insiders know.

  - *The Attribution Test:* Verify that claims, metrics, and user counts resolve to real sources or eliminate them.

  - *The Load-Bearing Test:* Delete code abstractions, wrappers, handlers, or tests; verify with test failures and compiler logs.

- **Three-Layer Verification Architecture:** Formalized audit layers:

  - *Layer 0 (Decidable Scanners):* Binary checks (package hallucination check against npm/PyPI registries, API signature verification against pinned versions, WCAG AA contrast calculation).

  - *Layer 1 (Structural Procedures):* The 5 mechanical tests emitting tangible artifacts.

  - *Layer 2 (Heuristic Markers):* Vocabulary frequency, em-dashes, and card nesting (triggers Layer 1; never convicts alone).

- **Code Surface Slop Hygiene:** Codified code integrity rules inspired by [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) and [AgriciDaniel/anti-slop](https://github.com/AgriciDaniel/anti-slop):

  - Zero decorative separator banners (`// =====`, `/* ---- ROUTES ---- */`).

  - Zero echo comments merely restating the code line beneath (`counter += 1 // increment counter`).

  - Zero step narration comments (`// Step 1: Initialize`).

  - Ban on passthrough ghost wrappers and single-implementation over-abstractions.

  - Ban on defensive error-swallowing catch blocks (`catch (e) {}` / `except: pass`).

  - Ban on assertion-free tests and coverage padding.

### Improved

- **Cadence, Syntax, and Punctuation Discipline:** Integrated writing constraints from [jalaalrd/anti-ai-slop-writing](https://github.com/jalaalrd/anti-ai-slop-writing):

  - *Eliminate Parataxis:* Ban choppy staccato declarations ("Short sentence. Then another."); enforce connective syntax (subordinate clauses, conjunctions, semicolons, commas) to express causal and relational meaning.

  - *Break the Rule of Three:* Break habitual triads ("fast, secure, and scalable") into 2, 4, 1, or 5 items.

  - *Burstiness & Sentence Length Rhythm:* Prohibit 3 consecutive sentences of uniform length; mix 4-word punchy sentences with 25-30 word nuanced explanations.

  - *Punctuation Discipline:* Enforce strict ceiling of maximum 1 em-dash per 500 words and 1 exclamation mark per 1,000 words; reintroduce purposeful semicolons and colons.

  - *Banned Openers & Negative Parallelism:* Eliminate formulaic openers (*"In today's fast-paced world"*, *"It's worth noting that"*) and artificial contrast (*"Not just X, but Y"*).

- **Dual-Axis Audit Reporting:** Re-architected `anti-slop-audit.md` to report findings across two independent axes: Severity (Critical / High / Medium / Polish) and Confidence (High / Medium / Low), with mandatory test name and inspected artifact fields.

- **Research Notes Alignment:** Documented external inspiration and originality notes for `jalaalrd/anti-ai-slop-writing`, `miqdadbadjuber/anti-slop`, and `AgriciDaniel/anti-slop` in `references/research-notes.md`.

## [0.10.7] - 2026-11-04

### Added

- **Full Suite Proof-of-Work (PoW) Showcase Gallery:** Shipped dedicated interactive specimen studio labs for all 10 curated style archetypes (`bento.html`, `brutalism.html`, `claymorphism.html`, `enterprise.html`, `glassmorphism.html`, `minimalism.html`, `neo-brutalism.html`, `retro-terminal.html`, `skeuomorphism.html`, `swiss-editorial.html`).

- **Interactive Specimen Studios & Token Synthesizers:** Equipped showcase pages with interactive diagnostic controls: Swiss 12-column typographic scale synthesizer, authentic phosphor CRT raster calibrator, analog hardware gain dial and tactile instrument deck, mechanical 2px offset displacement switches, and live token inspectors.

- **Theme Preference Persistence:** Integrated `localStorage` persistence (`taste-theme-main`) across the central showcase portal and PoW pages, maintaining user Dark/Light theme selection across browser sessions.

- **Accessible Mobile Navigation Drawer:** Implemented responsive overlay drawer navigation (`openMobileNav`, `closeMobileNav`, `Escape` key listeners) across all 10 showcase pages and the root portal.

### Improved

- **Single-Plane Tactile Faceplate Physics:** Codified strict unibody faceplate architecture for Skeuomorphism and Swiss Editorial, eliminating nested card-on-card stacking and aligning dual-shadow neumorphic lighting (-6px -6px 16px white highlight / 6px 6px 16px shadow) with recessed sunken telemetry wells.

- **Showcase Gallery Bugfixes & Token Alignment:** Resolved unclosed Section 5 HTML comment in `docs/index.html` restoring full Design Token cheatsheet visibility, synchronized all 10 style filter chips (`enterprise`, `neo-brutalism`, `minimalism`, `retro-terminal`), and updated standalone skill commands to match verified `optional-standalone-skills/` packages.

- **Responsive 320px Baseline & Anti-Oval Geometry:** Enforced universal responsive scaling down to 320px viewport baseline without horizontal overflow, alongside strict 1:1 circle geometry (`aspect-ratio: 1 / 1; flex-shrink: 0;`).

- **Universal Anti-Slop Iconography Gate:** Codified strict prohibition against cartoon emojis across all skill guides, mandating high-contrast Lucide or inline SVG vectors with consistent stroke metrics.

## [0.10.6] - 2026-11-04

### Added

- **Codex Dark Slate-Grey Palette:** Transitioned showcase gallery and core skill dark mode specifications from pitch-black (`#000000`) to warm neutral dark slate-grey (canvas `#212328`, surfaces `#2b2e36`, elevated `#343842`, recessed wells `#1a1c21`, borders `rgba(255, 255, 255, 0.12)`) inspired by OpenAI Codex and ChatGPT developer interfaces, reducing eye strain and improving surface contrast hierarchy.

- **Mobile Fluid Typography & Anti-Bloat:** Implemented responsive typography clamping and scaling rules across hero titles, section headings, card paddings, and badges on mobile viewports (< 768px and < 480px) to prevent oversized, inflated layouts ("UI bengkak").

- **Single-Line Inline Command Alignment:** Enforced horizontal single-row alignment (`display: inline-flex; flex-direction: row; align-items: center; justify-content: center;`) with `line-height: 1; flex-shrink: 0;` for quick install pills, terminal snippets, and copy buttons across desktop, tablet, and mobile.

- **Balanced Mobile Footer Architecture:** Re-architected mobile footer into a balanced 2-column navigation grid (`repeat(2, 1fr)`), full-width brand identity header, tactile thumb-friendly "Back to top" pill button, and valid HTML copyright entities (`&copy;`).

- **Strict Anti-Slop Protections:** Codified explicit bans in `SKILL.md` and `references/anti-slop.md` against rainbow text gradients (`background-clip: text`), cartoon emojis as functional icons (enforcing crisp inline SVGs), and fabricated space-filling dashboard widgets (weather/spectrum/telemetry).

## [0.10.5] - 2026-11-03

### Added

- **Tailwind CSS & shadcn/ui Presets:** Added official theme presets for Tailwind CSS (v3 & v4) and theme variable overrides for shadcn/ui in `presets/` with companion `taste-components.css` and integration guide (`references/tailwind-shadcn.md`).

- **CLI Preset & Init Commands:** Added `taste-engine preset` and `taste-engine init` commands to inspect and scaffold Tailwind and shadcn themes directly into any web project.

- **Interactive Live Style Gallery & Showcase:** Added comprehensive interactive documentation in `docs/index.html` showcasing all 10 curated frontend aesthetic archetypes with live Light/Dark mode toggling, 1-click token clipboard copying, and responsive preview viewports.

- **CLI Gallery Command:** Added `taste-engine gallery` command in `bin/taste-engine.mjs` to launch and explore the interactive style showcase locally in the browser.

- **Brand Identity & WebP Assets:** Added production-ready WebP branding assets (`assets/logo.webp`, `assets/banner.webp`, and `docs/assets/`) with high-resolution visual headers.

- **Interactive Architecture & Installation Guides:** Integrated multi-agent tabbed installation instructions (Antigravity IDE, CLI, Claude Code, Codex), interactive FAQ accordions, pipeline architecture flows, and token quick-reference cheatsheets into the showcase.

### Improved

- **Tactile Neumorphic Dark Mode Alignment:** Aligned dark mode theme tokens with tactile soft clay and neumorphic specifications: matte charcoal surfaces (`#15171c`), sunken relief wells (`#121317`), specular bevels, and radiant neon violet/cyan gradients.

- **Global Documentation Localization:** Localized all style packs, architecture documentation, guidelines, and showcase copy to standard English.

- **Release Workflow Idempotency:** Hardened GitHub Actions release workflow (`.github/workflows/release.yml`) to automatically inspect existing releases and perform seamless asset re-uploading without tag conflicts.

## [0.10.3] - 2026-11-03

### Improved

- **Full Suite Material & Aesthetic Fidelity Upgrade:** All 10 style packs now enforce mandatory first-viewport fidelity gates, anti-slop material exemptions, complete token architectures, and production-ready CSS recipes:

  - **Claymorphism:** Dual opposing inner shadows, soft tinted ambient drop shadows, tactile active compression, and sunken relief wells with companion recipe (`examples/claymorphism/sculpted-surfaces.css`).

  - **Neo-brutalism:** High-contrast solid black borders (`2.5px solid #121212`), unblurred hard offset shadows (`4px–8px`), mechanical press displacement, and companion recipe (`examples/neo-brutalism/pop-surfaces.css`).

  - **Skeuomorphism:** Top-down specular bevel highlights, multi-stop metallic reflection gradients, recessed display wells, and mechanical physical travel with companion recipe (`examples/skeuomorphism/tactile-controls.css`).

  - **Retro-Terminal:** Authentic CRT phosphor glow, static scanline raster overlays, bracketed ASCII frames, and active command prompt lines with companion recipe (`examples/retro-terminal/crt-console.css`).

  - **Bento Grid:** Strict asymmetric visual weight hierarchy (2x2 hero tile), diverse internal tile anatomy, uniform grid alignment, and responsive collapse with companion recipe (`examples/bento/modular-grid.css`).

  - **Swiss / Editorial:** Dramatic typographic scale contrast (48px–72px display headlines), structural hairline dividing rules (`1px solid #111`), section index numbers (`01`), and singular signal accents with companion recipe (`examples/swiss-editorial/grid-typography.css`).

  - **Brutalism:** Raw architectural structural scaffolding (`2.5px solid #000`), square corners (`0px`), stark monochrome contrast (WCAG AAA), and immediate state flips with companion recipe (`examples/brutalism/raw-surfaces.css`).

  - **Minimalism:** Active intentional negative space, mathematically calibrated type scale, hairline dividers, high contrast, and unambiguous affordances with companion recipe (`examples/minimalism/clean-surfaces.css`).

  - **Enterprise / Data-first:** High-density operational cockpits, 36px table rows, tabular figures (`tabular-nums`), semantic status tokens, and keyboard hints (`⌘K`) with companion recipe (`examples/enterprise/data-cockpit.css`).

- **Anti-Slop Constitution Alignment:** Clarified explicit material exemptions across all styles in `references/anti-slop.md`, ensuring that legitimate style features (hard shadows, metallic bevels, scanlines, asymmetric spans, and tabular density) are never rejected as slop.

- **Synchronized Standalone Skills & Discovery:** Updated all 10 standalone skills in `optional-standalone-skills/` and synced the canonical `taste-engine/` to `skills/taste-engine/`.

- **Validation & Test Suites:** Added automated fidelity unit tests (`test_clay_fidelity.py`, `test_glass_fidelity.py`) and visual acceptance guidelines (`claymorphism-visual.md`, `glassmorphism-visual.md`). All 31 test suites pass cleanly.

## [0.10.2] - 2026-11-03

### Refined

- Explicit Glassmorphism exemption from anti-slop's default gradient caution: purposeful radial, linear, mesh, or ambient color backgrounds are a legitimate part of glass material fidelity.

- Clarified the layered-backdrop composition test: glass panes must visibly filter a local color transition, while the uncovered backdrop stays differentiated.

- Strengthened light/dark static CSS gradient examples and manual visual quality checks without requiring new libraries, continuous motion, or non-glass style changes.

- Updated portable router, standalone Glassmorphism skill, validator and release package.

## [0.10.1] - 2026-11-03

### Improved

- Strengthened Glassmorphism as a **visible frosted material**, not a dark theme or a blur class: mandatory first-viewport material fidelity gate, composited contrast and responsive checks.

- Supported both milky/light and smoked/dark glass, with dedicated CSS recipe and manual screenshot acceptance criteria.

- Updated standalone glass style skill, registry aliases, validator, and router; preserved style-neutral routing and the existing SEO/motion/anti-slop system.

## [0.10.0] - 2026-11-02

### Added

- Portable `skills/taste-engine/` discovery package for the Agent Skills CLI (`npx skills add`).

- Cross-platform native installer for Antigravity IDE, Antigravity CLI, Claude Code, and Codex, with global or project scope, backup, and diagnostic commands.

- CLI test suite and deterministic mirror verification in CI.

- GitHub-centered English README, installation guide, contributor guidance, and maintainer publishing instructions.

### Changed

- Replaced Indonesian user-facing instructions and UI copy examples with English-language equivalents. Multilingual recognition remains supported in alias probing and test fixtures.

- Updated the default Bash updater source to `kennedys0/taste-engine`; a published Release is still required for automatic downloads.

### Notes

- This release is source and packaging work; agent auto-invocation and rendered UI must still be tested in real hosts/browsers.

## [0.9.1] — 2026-11-02

- Added safe standalone `update.sh` for offline ZIP and GitHub Releases updates (only after configuring a real repo).

- Added backup, staged validation, atomic activation, version checks and automatic rollback.

- Added optional `taste-engine update` CLI symlink installation, checksum verification, dry-run, and source-repo configuration.

- Fixed installed-router-only validation; cross-check standalone skill copies when present in full archive.

- Added script updater acceptance tests.

## [0.9.0] — 2026-11-02

- Added a framework-aware engineering router and original universal web quality gate informed by public Vercel Agent Skills.

- Added React/Next performance, composition, React Native/Expo, view transitions and documentation-writing guidance; all conditional.

- Added provenance and explicit non-adoption rationale for deployment, token and billing-related skills.

- Preserved automatic style-question preflight, 10 style packs, anti-slop, SEO, hero and optional Anime.js v4.

- Added engineering routing acceptance scenarios and deterministic validation checks.

## [0.8.0] — Full-screen hero, style-aware, responsive-safe

- New contextual full-screen hero contract for public portfolios, landing pages, and homepages that have a hero. First-screen geometry includes the nav.

- Stable `100svh` + `100vh` fallback, `min-height` content growth, overlay-vs-normal-flow header recipes and short-mobile/zoom safety.

- Style-specific hero direction in all ten bundled packs and optional standalone skills; anti-slop prevents filler content and decorative card nesting.

- Browser QA checklist, 15 acceptance scenarios and static policy tests; no hero introduced into private dashboards or explicit compact/no-hero requests.

## [0.7.0] — Optional Anime.js v4 motion engine adapter

- Added a cross-style, on-demand motion guidance module that does not automatically install dependencies.

- Added 10 style-specific micro-interaction recipes and machine-readable motion profiles.

- Added scoped React/Next client example with reduced-motion handling and cleanup.

- Added optional standalone `taste-motion` skill and motion acceptance tests.

- Preserved no-style-question policy for existing-design refinements, SEO routing, and anti-slop gates.

## [0.6.0] — Automatic SEO companion, cross-style

- Bundled `references/seo.md` and framework recipes. Public websites load SEO after visual style resolution; SEO-only asks skip style picker. Private sites are not indexed by implication.

- Added optional independent `taste-seo` Agent Skill, SEO routing agent scenarios and static HTML audit script/tests.

- Added anti-slop SEO safeguards: original content, no keyword stuffing, fabricated reviews/schema, made-up canonical origins or unverified scores.

- Verified policies against current Google Search Central documentation; no ranking/index guarantees.

- Preserved all existing ten aesthetics, auto-invocation and standalone style packs.

## [0.5.0] — Automatic skill discovery + explicit-style fast path

- Improved `SKILL.md` discovery description with natural frontend prompts in Indonesian and English.

- Defined mandatory branch: missing style → ask once and stop; explicit style → directly load pack; established design → preserve; nonvisual → skip.

- Added registry aliases and common typos (`skeumorphsm` → `skeuomorphism`, `NeoBrutalism` → `neo-brutalism`).

- Added `references/auto-invocation.md`, runnable `style_probe.py`, unit tests and agent acceptance scenarios.

- Improved `assets/AGENTS.snippet.md` and documented verified Antigravity IDE install paths.

- No change to anti-slop constitution, per-style visual defaults, or the 10 style packs.

## [0.4.0] — 2026-11-02

- Researched four GitHub repositories: Ferousco-dev/anti-slop-design, Nutlope/hallmark, jalaalrd/anti-ai-slop-writing and tasteskill/tasteskill.

- Added design decision system distinguishing selected aesthetics/material from page information architecture.

- Added non-waivable FLOOR, explainable REFLEX, and nonblocking FINISH gates, plus audit evidence rules.

- Added optional project-specific variance/motion/density controls (1–10; no global hard-coded aesthetics).

- Added writing-calibration with rhythm and copy checks **without rigid punctuation bans**.

- Added redesign parity and browser-validation procedures (no fake test claims).

- Updated all 10 self-contained standalone style skills with quality-tier guidance.

- Added research attribution/rejection notes and acceptance scenarios.

- Preserved v0.3 router's mandatory style selection before new UI implementation.

## [0.3.0] — 2026-11-01

- Universal anti-slop constitution, copywriting and style-specific audits.
