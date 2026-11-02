# Style pack: Minimalism

**ID:** `minimalism`  
**Signature:** Purposeful restraint with high information clarity.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies.

## Good fit / trade-offs

- **Works well for:** Productivity tools, storefronts, portfolios, form-centric products.
- **Be careful with:** When minimal styling becomes removal of necessary labels, metadata, or actions.

## Typography and typewriting

Neutral legible sans: Inter, Source Sans 3, or system sans. Body 15–16px; compact display 28–40px; weights 400/500/650. Use whitespace and hierarchy instead of extra decorative typography.

## Color direction

Neutral surfaces, one brand accent, restrained semantic colors. Avoid everything being faint gray.

## Layout and geometry

Measured 4/8px spacing scale, consistent 4–12px radii; clear vertical rhythm; avoid oversized empty regions.

## Surfaces, depth, texture

Mostly flat, subtle borders and rare elevation. Use grouping by alignment before adding cards.

## Component anatomy and interaction

Compact forms with labels, simple tabs, crisp tables, clear CTA priority. Low visual chrome but discoverable controls.

## Motion

120–180ms functional fade or color transitions, none by default when not useful.

## Optional Anime.js v4 recipe

- **Motion decision:** Short opacity or translation feedback only on a meaningful state change.
- **Starting duration:** 140ms (0 = immediate); adjust to task and user preference.
- **Avoid:** reveal-everything choreography.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Concise and concrete. Never replace descriptive labels with ambiguous icons only.

## Starter tokens (suggestions, not a complete theme)

| Token | Starting value |
| --- | --- |
| `--taste-radius-sm` | `6px` |
| `--taste-radius-lg` | `10px` |
| `--taste-border` | `1px solid rgba(0,0,0,.12)` |
| `--taste-shadow` | `0 2px 8px rgba(0,0,0,.05)` |
| `--taste-font-body` | `Inter, system-ui, sans-serif` |
| `--taste-motion-duration` | `150ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values. Fall back to installed fonts/system stack; do not silently download font assets.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Compose a calm full-screen introduction from precise typography, a restrained content width, and one clear next step. Negative space may dominate but must still feel balanced; avoid a tiny content island lost in an empty 100svh page. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Keep focus rings, labels and error messages visible even when they break visual silence.
- **Don't:** Do not equate minimalism with low contrast, giant whitespace, or hiding options.
- Confirm desktop and mobile consistency; visible keyboard focus; light/dark adaptation only if requested; loading, empty, disabled, error and success states; reduced-motion behavior.
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.
## Anti-slop: style-specific

**Reduction without removal of clarity.**

- **Reject:** Reject giant empty whitespace as substitute for composition, invisible borders/focus, ultra-light text, icon-only ambiguous navigation, and hidden essential labels.
- **Instead:** Let typography and proximity do grouping; preserve meaningful whitespace, visible focus and helpful data density.
- **Copy check:** Prefer precise functional copy; do not replace useful instructions with vague one-word poetry.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `minimalism`.
