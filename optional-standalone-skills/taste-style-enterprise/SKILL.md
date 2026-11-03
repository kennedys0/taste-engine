---
name: taste-style-enterprise
description: Apply Enterprise / Data-first design style to user-selected frontend and UI work. Use only when the user explicitly chooses this style. Provides typography, color, layout, components, interactions, motion, copy and quality gates. Do not impose on unrelated work.
license: MIT
metadata:
  version: "0.10.5"
---

Use this skill only after a user explicitly chooses  or a confirmed project configuration specifies it. For unexplained new UI requests, use a style selector such as  instead of deciding the user's taste here. Existing brand, accessibility and user overrides outrank all examples below. The following style guide is not permission to start UI coding before style selection.

# Style pack: Enterprise / Data-first

**ID:** `enterprise`  
**Signature:** Information-dense operational cockpits, tabular data alignment, semantic status tokens, keyboard productivity, and reliable workflow architecture.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies. A consumer card template with 3 fake KPI numbers and a decorative pie chart **does not qualify as Enterprise Data-first**.

## Good fit / trade-offs

- **Works well for:** B2B SaaS platforms, operational admin consoles, cloud infrastructure monitors, fintech and trading portals, logistics and supply-chain backends, and data-intensive productivity tools.
- **Be careful with:** Consumer marketing landing pages where narrative pacing and emotional visual branding take priority over dense tabular scanning.
- **Reference directions:**
  - *Modern Cloud Console (Linear / Stripe / Vercel style):* Crisp slate-neutral foundation (`#0F1117` dark or `#F9FAFB` light), compact 36px table rows, tabular figures (`font-variant-numeric: tabular-nums`), quiet hairline dividers (`#E5E7EB` or `#262933`), and semantic status tokens.
  - *High-Density Operations Desk:* Clean white desk with compact 32px rows, search filter bars with keyboard shortcuts (`⌘K`), sticky table headers, and responsive master-detail panes.

## Enterprise data fidelity gate — mandatory

**Before calling an enterprise page complete, the opening viewport must visibly read as a functional, dense, and professional data cockpit.** If a user chose this style, an oversized consumer template featuring decorative metric cards and zero scannable tabular structure is a direct **FAIL**.

A successful enterprise data-first implementation demonstrates **all** of the following:

1. **Information-Dense Tabular Architecture:** Core records and entities are presented in structured, scannable data tables or compact master-detail lists with consistent row heights (32px–40px) and explicit column headers.
2. **Tabular Numerals & Flush Alignment:** All numbers, financial amounts, metrics, and timestamps enforce `font-variant-numeric: tabular-nums`. Numerical columns align strictly flush-right; text columns align flush-left.
3. **Semantic Status Tokens with Legible Contrast:** Status indicators (Healthy, Degraded, Failed, Pending) use calibrated semantic token pills with dark accessible text on soft tinted backgrounds (e.g. Success: `#ECFDF5` background with `#065F46` text, passing WCAG AA 4.5:1).
4. **Productivity Affordances & Shortcuts:** Search bars feature keyboard trigger hints (`⌘K` or `/`), table headers feature sort indicators (`▲/▼`), and batch action bars appear upon record selection.
5. **Truthful State Completeness:** Tables include real pagination bars (showing `Showing 1–25 of 1,420 items`), responsive horizontal scroll handling, and dedicated empty/loading/error states.

**First-viewport test:** In a desktop screenshot, identify the dense data table, sortable headers, filter bar, and tabular numbers **without reading the page title**. If it looks like a consumer marketing page with large empty cards, rebuild it as a functional operational view.

## Explicit enterprise density exception — data tables are required

**Enterprise-specific override:** The universal anti-slop caution against *dashboard clutter or multiple metric boxes* MUST NOT be interpreted as a mandate to hide data tables, filter toolbars, or status indicators here. In authentic enterprise software (Stripe, Datadog, AWS, Bloomberg), dense scannable data is the primary interface requirement.

- **Allowed enterprise treatments:** Compact data tables (32px–40px rows), multi-column metadata grids, filter toolbars, search bars with keyboard shortcut badges, batch action bars, and semantic status pills.
- **Anti-slop boundary:** Never invent fake revenue metrics, decorative mini-sparklines without axis scales, or animated pie charts that convey zero operational data. Real data fields, empty states, and true status indicators are mandatory.
- **Anti-slop interpretation:** Evaluate enterprise layouts by **scannability, information density, and task efficiency**, not by trying to strip away necessary operational controls. Tabular density that speeds up work is authentic design.

## Typography and typewriting

Neutral, highly legible UI sans: Inter, Source Sans 3, SF Pro, or system sans. Monospace for identifiers and hashes: JetBrains Mono or system mono. Body & table cells: 13–14 px (line-height 1.45); column headers: 12 px uppercase (weight 600, tracking 0.05em); metrics: 20–28 px with tabular figures.

## Color direction

- **Light Mode (Modern Cloud Console):**
  - **Canvas Base:** Soft neutral slate (`#F9FAFB`).
  - **Surface / Table:** Pure white (`#FFFFFF`).
  - **Primary Ink / Typography:** Deep slate (`#111827`).
  - **Secondary / Muted Text:** Balanced slate (`#6B7280`).
  - **Hairline Borders:** `#E5E7EB`.
  - **Hover Row Highlight:** `#F8FAFC`.
- **Dark Mode (Cloud Cockpit):**
  - **Canvas Base:** Deep slate (`#0F1117`).
  - **Surface / Table:** Elevated charcoal (`#161922`).
  - **Primary Ink / Typography:** Crisp slate (`#F9FAFB`).
  - **Secondary / Muted Text:** Balanced gray (`#9CA3AF`).
  - **Hairline Borders:** `#232733`.
  - **Hover Row Highlight:** `#1F2430`.
- **Primary Brand:** Deep enterprise blue (`#2563EB` light / `#3B82F6` dark).
- **Semantic Status Tokens (WCAG AA Calibrated for Both Modes):**
  - **Success (Healthy):** Light: `#065F46` on `#ECFDF5` (border `#A7F3D0`); Dark: `#34D399` on `rgba(16, 185, 129, 0.15)` (border `rgba(16, 185, 129, 0.35)`).
  - **Warning (Degraded):** Light: `#92400E` on `#FEF3C7` (border `#FDE68A`); Dark: `#FBBF24` on `rgba(245, 158, 11, 0.15)` (border `rgba(245, 158, 11, 0.35)`).
  - **Error (Failed):** Light: `#991B1B` on `#FEE2E2` (border `#FECACA`); Dark: `#F87171` on `rgba(239, 68, 68, 0.15)` (border `rgba(239, 68, 68, 0.35)`).
  - **Neutral (Pending / Inactive):** Light: `#374151` on `#F3F4F6` (border `#E5E7EB`); Dark: `#9CA3AF` on `rgba(156, 163, 175, 0.12)` (border `rgba(156, 163, 175, 0.25)`).
- **Theme Coupling Rule:** Canvas, tables, text ink, and semantic badges MUST adapt together. Never display dark-mode text on light tables or light-mode dark green text on dark console backgrounds.

## Layout and geometry

4px base rhythm with 8/12/16px density increments; subtle 4px–6px corner radii; consistent table row heights (36px default, 32px compact). Master-detail layouts split flexibly on desktop and stack cleanly on mobile.

## Surfaces, depth, texture

Surfaces are clean, flat, and border-driven. Elevation shadows are reserved strictly for floating menus, tooltips, and modal dialogs (`0 4px 12px rgba(0, 0, 0, 0.08)`). No decorative glass or clay effects on data grids.

## Component anatomy and interaction

- **Data Table:** Sticky header row, zebra or hover row highlighting (`#F8FAFC`), flush-right numerical columns, flush-left text.
- **Filter & Search Bar:** Integrated search input with `⌘K` badge, multi-select filter dropdowns, and date range picker.
- **Semantic Status Badge:** Compact rounded pill with colored indicator dot and accessible text.
- **Pagination Footer:** Current page range, items-per-page selector, and next/prev buttons.

## Motion

Minimal 100–140 ms linear feedback transitions. Prioritize rock-solid stability and zero motion during data refreshing or table filtering.

## Optional Anime.js v4 recipe

- **Motion decision:** Subtle row highlight flash on data update or drawer sliding transition.
- **Starting duration:** 120ms (0 = immediate); adjust to task and user preference.
- **Avoid:** decorative page transitions, bouncy charts, spinning loaders on quick queries.
- **Dependency:** CSS/native by default. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Objective, precise, and audit-friendly. Examples: “1,420 records found”, “Filter by status”, “Export CSV”, “Last updated 2 mins ago”. Avoid vague conversational AI slogans.

## Starter tokens (suggestions, not a complete theme)

| Token | Light mode default | Dark mode default |
| --- | --- | --- |
| `--taste-ent-bg` | `#f9fafb` | `#0f1117` |
| `--taste-ent-surface` | `#ffffff` | `#161922` |
| `--taste-ent-ink` | `#111827` | `#f9fafb` |
| `--taste-ent-muted` | `#6b7280` | `#9ca3af` |
| `--taste-ent-border` | `1px solid #e5e7eb` | `1px solid #232733` |
| `--taste-ent-radius` | `6px` | `6px` |
| `--taste-ent-row-height` | `36px` | `36px` |
| `--taste-ent-accent` | `#2563eb` | `#3b82f6` |
| `--taste-ent-font-body` | `Inter, -apple-system, system-ui, sans-serif` | `Inter, -apple-system, system-ui, sans-serif` |
| `--taste-ent-motion-duration` | `100ms` | `100ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-ent-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Anchor the opening view with a working cockpit summary: key filter bar, live data overview, and an immediate operational action. Avoid consumer card inflation and empty gaps. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Verify tabular numerals (`tabular-nums`) and right-alignment on numerical data; ensure semantic badges meet WCAG AA contrast in both light and dark modes; provide complete pagination and search filter bars; test sticky table headers; verify dark/light mode switching so all rows, borders, and text flip in synchronized pairs.
- **Don't:** Do not replace data tables with consumer card grids; avoid unscaled decorative sparklines; do not invent fake metric numbers that have no backend counterpart; avoid theme contrast collisions such as dark green text on dark backgrounds or dark text on dark table rows.
- Confirm desktop and mobile consistency; visible keyboard focus (`:focus-visible`); loading, empty, disabled, error and success states; reduced-motion behavior (`prefers-reduced-motion`).
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.

## Universal anti-slop gate (self-contained)

Every element must earn its place. **Content before decoration. Do not decorate uncertainty.** Do not invent balances, metrics, testimonials, users, logos, approval, verified/live/online status, fake activity, or success confirmations; use honest empty/loading/error states instead. Demo data is acceptable only if requested and visibly labeled.

Do not add decorative **card-inside-card** layers: a nested surface must represent a distinct interaction or information boundary. Avoid auto-generated 3-feature grids, 4-stat dashboards, fake hero claims, purposeless charts, badge/chip/icon spam, unrelated decorative art, and random loops merely to fill the viewport. Prefer grouping with typography, spacing, alignment and dividers. Equal peers need intentional visual balance.

**Anti-slop copywriting:** no generic "Unlock your potential", "Experience the future", "Supercharge your workflow", "seamless" claims, or translated equivalents. Headings must communicate actual content, CTAs must name the action, and empty/error/success text must describe real states and next steps. Avoid fake urgency, made-up counts, vague AI hype, gratuitous emoji, and inaccessible all-caps walls. Adapt the wording to this style and the user's language without changing the truth.

**Theme and mode contrast integrity:** When a user requests dark mode or light mode (or builds a theme switcher), background and foreground colors MUST flip in synchronized pairs across all surfaces, text, borders, inputs, and semantic badges. Never leave black text on dark background, white text on white background, or unreadable low-contrast status pills. All states must meet WCAG AA contrast (minimum 4.5:1 for body/normal text, 3:1 for large headlines and interactive boundaries).

**Responsive and motion:** compose mobile deliberately, check long labels, focus states and accessible contrast; no text clipping to fit a trendy layout. Static by default; use motion for meaningful interactions, respect reduced-motion preferences, avoid bounce/floating/pulsing decoration without a real state.

**Critical/High findings block completion:** fabricated status/data, broken actions, inaccessible/clipped controls, misleading copy, theme contrast collisions or significant mobile failure must be fixed. Report what was actually verified; do not claim tests that did not run.

**Not an aesthetics veto:** expressive colors, shadows, gradients, card layouts or decorative treatments are legitimate when they are intentional parts of the selected aesthetic and pass usability checks. Do not silently force minimalism.

## Anti-slop: style-specific

**Information density, not consumer card spam.**

- **Reject:** Giant marketing cards replacing tables, decorative sparklines without scales, fake metric deltas (+24% with no time horizon), and half-baked dark mode where tables or badges keep blinding white backgrounds or unreadable dark text.
- **Instead:** Build compact, structured tables with clean column alignment, explicit pagination, real filter controls, and calibrated dark/light theme support.
- **Copy check:** Table headers and status tags must use precise operational terminology.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `enterprise`.

## Quality tiers (standalone)

**FLOOR (must pass):** correct and truthful data/state, working critical actions, accessible focus/labels/contrast, usable responsive UI and reduced-motion support. **REFLEX (explain or fix):** generic feature grids, purposeless nested cards, decorative labels/icons, default marketing hype or constant motion. A reflex is allowed when it clearly expresses the chosen style and serves the task. **FINISH:** refinement of alignment, typography rhythm and edge cases. Never treat the selected style itself as a violation. Do not claim browser testing unless actually performed.
