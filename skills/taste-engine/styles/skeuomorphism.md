# Style pack: Skeuomorphism

**ID:** `skeuomorphism`  
**Signature:** Digital controls borrow useful affordances from physical objects.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies.

## Good fit / trade-offs

- **Works well for:** Music tools, specialized controls, educational simulations and playful product interfaces.
- **Be careful with:** Critical high-density workflows where realistic textures distract or reduce accessibility.

## Typography and typewriting

Utilitarian sans with product-specific display treatment: IBM Plex Sans, system sans; optional mono for device readouts. Body at least 14–16px; control labels must stay legible.

## Color direction

Material-derived colors (metal, paper, leather, plastic) only where justified; strong contrast for actual labels and state indications.

## Layout and geometry

Component shapes map to their physical metaphors: rotary knobs, switches, sliders; avoid applying random material skins to everything.

## Surfaces, depth, texture

Subtle realistic lighting, inset channels and raised control shadows; visually distinguish up/down/disabled states; include texture only if it reinforces affordance.

## Component anatomy and interaction

Knobs, switches, sliders with accessible keyboard/pointer semantics and numerical alternatives. Native mobile touch targets and clear focus indicators.

## Motion

160–220ms believable but restrained pressed/rotated states; honor reduced motion and no sound without user consent.

## Optional Anime.js v4 recipe

- **Motion decision:** Believable short travel of a physical control with strong immediate feedback.
- **Starting duration:** 190ms (0 = immediate); adjust to task and user preference.
- **Avoid:** slow springs, idle knob movement, decorative sounds.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Clear labels and units. Keep task text separate from decorative device labeling.

## Starter tokens (suggestions, not a complete theme)

| Token | Starting value |
| --- | --- |
| `--taste-radius-sm` | `8px` |
| `--taste-radius-lg` | `14px` |
| `--taste-border` | `1px solid rgba(0,0,0,.18)` |
| `--taste-shadow` | `inset 0 1px 2px rgba(255,255,255,.55), 0 4px 10px rgba(0,0,0,.18)` |
| `--taste-font-body` | `IBM Plex Sans, system-ui, sans-serif` |
| `--taste-motion-duration` | `190ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values. Fall back to installed fonts/system stack; do not silently download font assets.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Make the first viewport feel like one coherent physical environment where actual controls are recognizable and functional. Reserve depth for meaningful affordances, not a frame-inside-frame mock device simply to occupy height; tactile motion stays restrained. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Provide non-visual alternatives and check that tactile affordances map to actual interactive behavior.
- **Don't:** Do not let texture obscure content; avoid decorative faux knobs that do not work.
- Confirm desktop and mobile consistency; visible keyboard focus; light/dark adaptation only if requested; loading, empty, disabled, error and success states; reduced-motion behavior.
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.
## Anti-slop: style-specific

**Metaphors with useful affordance.**

- **Reject:** Reject fake knobs/switches, ornamental controls that do nothing, heavy texture covering text, uncontrolled realism and endless nested physical containers.
- **Instead:** Use physical metaphors where they make manipulation and feedback clearer, with actual interactive states and keyboard support.
- **Copy check:** Use familiar real-world control labels only when they map to real actions; no pretend hardware status.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `skeuomorphism`.
