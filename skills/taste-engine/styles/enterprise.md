# Style pack: Enterprise / Data-first

**ID:** `enterprise`  
**Signature:** Efficient professional interfaces designed for repeated workflows.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies.

## Good fit / trade-offs

- **Works well for:** Admin consoles, B2B SaaS, trading and logistics operations, dashboards.
- **Be careful with:** Brand-first editorial campaigns where distinctive expression has priority over operational density.

## Typography and typewriting

Neutral highly legible UI sans: Inter, Source Sans 3, system sans. Body 13–15px (small only where density requires), headings 20–30px; tabular numerals for data, clear 500–700 weight hierarchy.

## Color direction

Neutral surfaces, one functional primary color plus semantic success/warning/error. Avoid confusing accent colors with statuses.

## Layout and geometry

4px spacing base with 8/12/16 density increments; 4–8px radius; consistent table row heights; flexible master-detail desktop, stacked flows mobile.

## Surfaces, depth, texture

Quiet borders, selected elevation for menus/dialogs only; no visual novelty that obscures workflow.

## Component anatomy and interaction

Sortable/filterable tables, search, pagination, complete empty/loading/error states, responsive navigation, audit-friendly labels and precise input validation.

## Motion

Minimal 100–160ms feedback transitions; prioritize stability and low motion during data refresh.

## Optional Anime.js v4 recipe

- **Motion decision:** Minimal immediate feedback, no distracting animation during repeated data work.
- **Starting duration:** 110ms (0 = immediate); adjust to task and user preference.
- **Avoid:** staggering tables, moving metrics, and loading delays.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Precise, task-based, informative; define units, timestamps and statuses explicitly. Avoid invented demo metrics.

## Starter tokens (suggestions, not a complete theme)

| Token | Starting value |
| --- | --- |
| `--taste-radius-sm` | `4px` |
| `--taste-radius-lg` | `8px` |
| `--taste-border` | `1px solid rgba(0,0,0,.14)` |
| `--taste-shadow` | `0 4px 12px rgba(0,0,0,.08)` |
| `--taste-font-body` | `Inter, system-ui, sans-serif` |
| `--taste-motion-duration` | `130ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values. Fall back to installed fonts/system stack; do not silently download font assets.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** For a public enterprise homepage with a real hero, use the first viewport for concrete proposition, proof only when verified, and a clear next step. Do not force this pattern on signed-in dashboards or operational workspaces; keep first-screen utility above decorative theatrics. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Test dense tables on narrow screens; prioritize keyboard, filtering, empty states and operational error recovery.
- **Don't:** Do not reduce text to illegible sizes or force heavy card views on all tabular data.
- Confirm desktop and mobile consistency; visible keyboard focus; light/dark adaptation only if requested; loading, empty, disabled, error and success states; reduced-motion behavior.
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.
## Anti-slop: style-specific

**Functional density, not dashboard cosplay.**

- **Reject:** Reject automatic 4-KPI headers, redundant status badges, useless mini-charts, modal-on-modal interactions, over-abstract metrics, and tables converted to giant cards for trendiness.
- **Instead:** Use compact aligned controls, appropriate tables, real filtering/search, explicit states, and grouped operational summaries.
- **Copy check:** State counts and outcomes precisely only when sourced from data; errors must support recovery.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `enterprise`.
