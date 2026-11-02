# Style pack: Brutalism

**ID:** `brutalism`  
**Signature:** Raw structure, unapologetic hierarchy, minimal decoration.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies.

## Good fit / trade-offs

- **Works well for:** Experimental portfolios, art/culture, activist/editorial sites, distinctive landing pages.
- **Be careful with:** Where enterprise familiarity or very low cognitive load is the primary goal unless softened.

## Typography and typewriting

Bold grotesk/system sans or purposeful monospace: Arial/Helvetica, IBM Plex Sans, IBM Plex Mono. Large decisive headings 44–72px desktop, 30–44px mobile; body 16–18px; weight 400/700/800. Strong contrast in scale, strict alignment. Uppercase only for short labels, not paragraphs.

## Color direction

Near-white or near-black base, hard black/white contrast and at most one sharp signal color. Color carries meaning rather than decoration.

## Layout and geometry

Rectangular blocks, 0–2px radius, strong 2–3px borders, exposed grid, visible section dividers; deliberate asymmetric composition.

## Surfaces, depth, texture

Flat surfaces. No decorative gradient, glass blur or elevated soft shadows. Layout and type do the visual work.

## Component anatomy and interaction

Blocky high-contrast buttons, outlined controls, visible label text, oversized menu numbering, strong separators; provide clearly distinct interactive and static regions.

## Motion

Prefer immediate state changes or 100–160ms linear transitions. Avoid elastic effects, parallax and embellished entry animation.

## Optional Anime.js v4 recipe

- **Motion decision:** Use immediate state flips by default; Anime.js generally unnecessary.
- **Starting duration:** 0ms (0 = immediate); adjust to task and user preference.
- **Avoid:** springs, sliding reveals, theatrical scroll animations.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Short, blunt, specific. Strong verbs and informative labels; no aggressive or inaccessible all-caps walls of text.

## Starter tokens (suggestions, not a complete theme)

| Token | Starting value |
| --- | --- |
| `--taste-radius-sm` | `0px` |
| `--taste-radius-lg` | `0px` |
| `--taste-border` | `2px solid currentColor` |
| `--taste-shadow` | `none` |
| `--taste-font-body` | `Arial, Helvetica, sans-serif` |
| `--taste-motion-duration` | `120ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values. Fall back to installed fonts/system stack; do not silently download font assets.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Use the screen as a deliberate typographic poster: massive but readable display type, ruled grid, one actionable next step. Treat negative space as structure, not an excuse for fake oversized numbers; no comic offset shadows or random collage noise. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Expose a clear grid, maintain meaningful hierarchy, and make focus / active states as assertive as static borders.
- **Don't:** Do not confuse brutalism with playful neo-brutalism; avoid candy palettes, thick offset comic shadows, random rotated stickers, or deliberately broken usability.
- Confirm desktop and mobile consistency; visible keyboard focus; light/dark adaptation only if requested; loading, empty, disabled, error and success states; reduced-motion behavior.
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.
## Anti-slop: style-specific

**Raw hierarchy, not random aggression.**

- **Reject:** Reject arbitrary broken grids, unreadable oversized headings, fake provocative slogans, random rotation, comic offset shadows, and uppercase walls of text.
- **Instead:** Use repeatable alignment and deliberate contrast; make actions self-evident and retain readable body copy.
- **Copy check:** Write direct, specific labels; short uppercase may be expressive, but not an excuse for shouty filler.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `brutalism`.
