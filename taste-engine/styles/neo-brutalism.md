# Style pack: Neo-brutalism

**ID:** `neo-brutalism`  
**Signature:** Playful bold colors, hard borders and offset shadows.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies.

## Good fit / trade-offs

- **Works well for:** Creator tools, playful SaaS, event or indie product websites.
- **Be careful with:** Serious regulated workflows unless the brand specifically calls for a playful treatment.

## Typography and typewriting

Expressive but legible sans: Space Grotesk, Archivo, or system sans. Headlines 32–52 px, weight 700–800; body 15–17 px, weight 400–600. Punchy, confident sentence-case labels. Contrast via weight and type scale.

## Color direction

Light flat background with black outlines and 2–3 purposeful vivid accent colors; limit simultaneous saturated panels.

## Layout and geometry

Square to lightly rounded corners (0–10px); 2–3px high-contrast strokes; 4–8px hard offset shadows; strong modular grid.

## Surfaces, depth, texture

Flat fills, crisp borders, offset shadows with no blur. Small rotated or illustrated accents only when they help meaning.

## Component anatomy and interaction

Bold filled CTAs, outlined badges with real meaning, clearly separated form controls; shadow offset decreases on press without shifting layout.

## Motion

100–180ms crisp transitions; 1–3px press movement acceptable; never jarring shake or long bouncing.

## Optional Anime.js v4 recipe

- **Motion decision:** Short direct 1–2px button shift with a matching hard-shadow response; never animate giant shadows.
- **Starting duration:** 130ms (0 = immediate); adjust to task and user preference.
- **Avoid:** bounce and endlessly moving stickers.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Energetic and plainspoken. Avoid faux rebellious copy in professional contexts.

## Starter tokens (suggestions, not a complete theme)

| Token | Starting value |
| --- | --- |
| `--taste-radius-sm` | `6px` |
| `--taste-radius-lg` | `8px` |
| `--taste-border` | `2px solid #151515` |
| `--taste-shadow` | `5px 5px 0 #151515` |
| `--taste-font-body` | `Space Grotesk, system-ui, sans-serif` |
| `--taste-motion-duration` | `150ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values. Fall back to installed fonts/system stack; do not silently download font assets.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Make the full viewport energetic through asymmetry, well-grounded display typography and one high-contrast primary action. Thick borders and offset shadows remain intentional; do not stack stickers, extra outlined boxes or spinning ornaments to fill the screen. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Differentiate static card borders from button affordances; maintain hierarchy within colorful layouts.
- **Don't:** Do not copy brutalism guidelines verbatim: offset shadows and playful palette belong here, not in classic brutalism.
- Confirm desktop and mobile consistency; visible keyboard focus; light/dark adaptation only if requested; loading, empty, disabled, error and success states; reduced-motion behavior.
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.
## Anti-slop: style-specific

**Expressive, not chaotic.**

- **Reject:** Reject rainbow-everywhere palettes, offset shadows on every nested tile, rotated stickers without task value, novelty-only badges, and hard shadows that obscure touch boundaries.
- **Instead:** Apply thick border/hard shadow to chosen hierarchy levels; use a controlled expressive palette and stable spacing.
- **Copy check:** Playfulness must clarify the task; avoid fabricated hype, excessive exclamation marks and meme text unrelated to brand.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `neo-brutalism`.
