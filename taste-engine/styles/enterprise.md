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

- **Canvas Base:** Soft neutral (`#F9FAFB` light or `#0F1117` dark).
- **Surface / Table:** Pure white (`#FFFFFF` light) or elevated charcoal (`#161922` dark).
- **Hairline Borders:** `#E5E7EB` (light) or `#232733` (dark).
- **Primary Brand:** Deep enterprise blue (`#2563EB`) or slate (`#0F172A`).
- **Semantic Tokens (WCAG AA Calibrated):**
  - Success: `#065F46` on `#ECFDF5` (border `#A7F3D0`)
  - Warning: `#92400E` on `#FEF3C7` (border `#FDE68A`)
  - Error: `#991B1B` on `#FEE2E2` (border `#FECACA`)
  - Neutral / Inactive: `#374151` on `#F3F4F6` (border `#E5E7EB`)

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

| Token | Starting value |
| --- | --- |
| `--taste-ent-bg` | `#f9fafb` |
| `--taste-ent-surface` | `#ffffff` |
| `--taste-ent-ink` | `#111827` |
| `--taste-ent-muted` | `#6b7280` |
| `--taste-ent-border` | `1px solid #e5e7eb` |
| `--taste-ent-radius` | `6px` |
| `--taste-ent-row-height` | `36px` |
| `--taste-ent-accent` | `#2563eb` |
| `--taste-ent-font-body` | `Inter, -apple-system, system-ui, sans-serif` |
| `--taste-ent-motion-duration` | `100ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-ent-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Anchor the opening view with a working cockpit summary: key filter bar, live data overview, and an immediate operational action. Avoid consumer card inflation and empty gaps. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Verify tabular numerals (`tabular-nums`) and right-alignment on numerical data; ensure semantic badges meet WCAG AA contrast; provide complete pagination and search filter bars; test sticky table headers.
- **Don't:** Do not replace data tables with consumer card grids; avoid unscaled decorative sparklines; do not invent fake metric numbers that have no backend counterpart.
- Confirm desktop and mobile consistency; visible keyboard focus (`:focus-visible`); loading, empty, disabled, error and success states; reduced-motion behavior (`prefers-reduced-motion`).
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.
## Anti-slop: style-specific

**Operational density, not dashboard spectacle.**

- **Reject:** Giant consumer KPI cards with 3 fake numbers, decorative mini-charts with no units or axis labels, ornamental progress rings, and non-functional search bars.
- **Instead:** Build high-density scannable data tables, clear sortable headers, accessible semantic status pills, keyboard shortcuts, and robust pagination.
- **Copy check:** Use exact business and system metrics; avoid cheerleading marketing copy.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `enterprise`.
