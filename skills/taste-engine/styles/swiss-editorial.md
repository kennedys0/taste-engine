# Style pack: Swiss / Editorial

**ID:** `swiss-editorial`  
**Signature:** Grid-driven typographic hierarchy and intentional rhythm.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies.

## Good fit / trade-offs

- **Works well for:** Magazines, agencies, portfolios, reports and information-rich marketing sites.
- **Be careful with:** Task-heavy administrative UIs if editorial hierarchy makes frequent operations slower.

## Typography and typewriting

Grotesk sans: Helvetica Neue/system sans, IBM Plex Sans, or Neue Haas-like available family. Headlines 36–72px desktop / 28–42px mobile; body 16–18px; tight heading tracking and comfortable body line-height. Optional contrasting serif for quotes, not as a default.

## Color direction

Mostly monochrome with one sparse accent; photographic color can supply the variety.

## Layout and geometry

Strong 12-column editorial grid desktop, 4-column mobile, consistent baseline and generous edges. Radius 0–4px and hairline rules.

## Surfaces, depth, texture

Flat, border-led; strong use of type and whitespace; photography and captions aligned to grid.

## Component anatomy and interaction

Index numbers, editorial navigation, section rules, media captions, unobtrusive article controls; adapt forms for clear usability.

## Motion

Subtle reveal on scroll only if meaningful and respects reduced motion; otherwise 120–200ms transitions.

## Optional Anime.js v4 recipe

- **Motion decision:** Precise, restrained underlines or sectional changes that preserve reading flow.
- **Starting duration:** 160ms (0 = immediate); adjust to task and user preference.
- **Avoid:** word-by-word autoplay and gratuitous kinetic text.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Editorial, informative, specific. Use accurate captions and real metadata; no fabricated publication dates.

## Starter tokens (suggestions, not a complete theme)

| Token | Starting value |
| --- | --- |
| `--taste-radius-sm` | `0px` |
| `--taste-radius-lg` | `2px` |
| `--taste-border` | `1px solid rgba(0,0,0,.20)` |
| `--taste-shadow` | `none` |
| `--taste-font-body` | `IBM Plex Sans, Helvetica, Arial, sans-serif` |
| `--taste-motion-duration` | `160ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values. Fall back to installed fonts/system stack; do not silently download font assets.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Fill the opening viewport with purposeful editorial scale, consistent columns, baseline alignment and an asymmetrical-but-structured layout. Let typography and real work samples carry impact, not decorative lines or fabricated issue numbers. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Make a coherent typographic scale with precise alignment; prioritize reading flow and caption clarity.
- **Don't:** Do not treat editorial as merely using large fonts and empty space; avoid broken alignment and low-contrast light gray body text.
- Confirm desktop and mobile consistency; visible keyboard focus; light/dark adaptation only if requested; loading, empty, disabled, error and success states; reduced-motion behavior.
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.
## Anti-slop: style-specific

**Editorial order, not typography theater.**

- **Reject:** Reject decorative tiny type, arbitrarily broken grids, multiple fonts without roles, full-width all-caps paragraphs, and editorial headlines that say nothing.
- **Instead:** Use repeatable grid, clear type hierarchy, disciplined measure and purposeful editorial asymmetry.
- **Copy check:** Headlines can be expressive but must communicate a real idea, not "The future starts here" filler.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `swiss-editorial`.
