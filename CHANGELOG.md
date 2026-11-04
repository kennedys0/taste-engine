# Changelog

All notable changes to Taste Engine are documented here. Release tags use semantic versioning.

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

# Changelog

## v0.8.0 — Full-screen hero, style-aware, responsive-safe

- New contextual full-screen hero contract for public portfolios, landing pages, and homepages that have a hero. First-screen geometry includes the nav.
- Stable `100svh` + `100vh` fallback, `min-height` content growth, overlay-vs-normal-flow header recipes and short-mobile/zoom safety.
- Style-specific hero direction in all ten bundled packs and optional standalone skills; anti-slop prevents filler content and decorative card nesting.
- Browser QA checklist, 15 acceptance scenarios and static policy tests; no hero introduced into private dashboards or explicit compact/no-hero requests.


## v0.7.0 — Optional Anime.js v4 motion engine adapter

- Added a cross-style, on-demand motion guidance module that does not automatically install dependencies.
- Added 10 style-specific micro-interaction recipes and machine-readable motion profiles.
- Added scoped React/Next client example with reduced-motion handling and cleanup.
- Added optional standalone `taste-motion` skill and motion acceptance tests.
- Preserved no-style-question policy for existing-design refinements, SEO routing, and anti-slop gates.

## v0.6.0 — Automatic SEO companion, cross-style

- Bundled `references/seo.md` and framework recipes. Public websites load SEO after visual style resolution; SEO-only asks skip style picker. Private sites are not indexed by implication.
- Added optional independent `taste-seo` Agent Skill, SEO routing agent scenarios and static HTML audit script/tests.
- Added anti-slop SEO safeguards: original content, no keyword stuffing, fabricated reviews/schema, made-up canonical origins or unverified scores.
- Verified policies against current Google Search Central documentation; no ranking/index guarantees.
- Preserved all existing ten aesthetics, auto-invocation and standalone style packs.


## v0.5.0 — Automatic skill discovery + explicit-style fast path

- Improved `SKILL.md` discovery description with natural frontend prompts in Indonesian and English.
- Defined mandatory branch: missing style → ask once and stop; explicit style → directly load pack; established design → preserve; nonvisual → skip.
- Added registry aliases and common typos (`skeumorphsm` → `skeuomorphism`, `NeoBrutalism` → `neo-brutalism`).
- Added `references/auto-invocation.md`, runnable `style_probe.py`, unit tests and agent acceptance scenarios.
- Improved `assets/AGENTS.snippet.md` and documented verified Antigravity IDE install paths.
- No change to anti-slop constitution, per-style visual defaults, or the 10 style packs.


## 0.4.0 — 2026-11-02

- Researched four GitHub repositories: Ferousco-dev/anti-slop-design, Nutlope/hallmark, jalaalrd/anti-ai-slop-writing and tasteskill/tasteskill.
- Added design decision system distinguishing selected aesthetics/material from page information architecture.
- Added non-waivable FLOOR, explainable REFLEX, and nonblocking FINISH gates, plus audit evidence rules.
- Added optional project-specific variance/motion/density controls (1–10; no global hard-coded aesthetics).
- Added writing-calibration with rhythm and copy checks **without rigid punctuation bans**.
- Added redesign parity and browser-validation procedures (no fake test claims).
- Updated all 10 self-contained standalone style skills with quality-tier guidance.
- Added research attribution/rejection notes and acceptance scenarios.
- Preserved v0.3 router's mandatory style selection before new UI implementation.

## 0.3.0

- Universal anti-slop constitution, copywriting and style-specific audits.
