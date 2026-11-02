# Style pack: Claymorphism

**ID:** `claymorphism`  
**Signature:** Soft, tactile, sculpted surfaces with friendly depth.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies.

## Good fit / trade-offs

- **Works well for:** Playful consumer experiences, creative tools, personal dashboards.
- **Be careful with:** Extremely dense operational tables or low-power devices if decoration obstructs scanning.

## Typography and typewriting

Friendly humanist/geometric sans: Nunito Sans, Manrope, or system sans. Weights 400/600/700. Scale 13/14/16/20/26/34 px; calm line height 1.45–1.6. Prefer sentence case and short, human labels. Avoid bubbly decorative display faces by default.

## Color direction

1 softly tinted canvas + 1 primary pastel hue + 1 secondary accent + neutrals. Low saturation; contrast must be measured for real foreground text.

## Layout and geometry

Radius 16–24 px cards, 10–14 px controls; layered but consistent geometry. 8 px rhythm, moderate gutters, no random circles.

## Surfaces, depth, texture

Soft long directional shadow + small ambient shadow + subtle upper-inner highlight; surfaces should feel molded, not flat cards with blur. Inputs can be shallow inset, with visible focus.

## Component anatomy and interaction

Tactile buttons with subtle pressed state; consistently sized cards; soft segmented tabs; labeled form fields; mobile bottom nav if appropriate; do not nest endless rounded cards.

## Motion

140–240 ms smooth ease-out; tiny translation or opacity transition; never bounce, overshoot, or perpetual floating.

## Optional Anime.js v4 recipe

- **Motion decision:** Pressed button with 1–2% compression and a brief return; keep existing sculpted shading.
- **Starting duration:** 180ms (0 = immediate); adjust to task and user preference.
- **Avoid:** bounce, overshoot, floating loops.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Warm and concrete. Examples: “Create report”, “Saved to drafts”. Avoid sugary slogans.

## Starter tokens (suggestions, not a complete theme)

| Token | Starting value |
| --- | --- |
| `--taste-radius-sm` | `12px` |
| `--taste-radius-lg` | `20px` |
| `--taste-border` | `1px solid rgba(70,65,80,.10)` |
| `--taste-shadow` | `8px 12px 22px rgba(48,36,65,.12), inset 1px 1px 1px rgba(255,255,255,.65)` |
| `--taste-font-body` | `Manrope, system-ui, sans-serif` |
| `--taste-motion-duration` | `180ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values. Fall back to installed fonts/system stack; do not silently download font assets.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Use one sculpted hero surface or a carefully balanced soft-material environment; place the true portfolio introduction and CTA in the first-screen composition. Do not nest puffy cards to fill 100svh. Clay depth should remain subtle and directional, with substantial flat space. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Make the tactile material readable in both light and dark modes; maintain consistent light direction; use real disabled, hover, and focus states.
- **Don't:** Do not treat rounded corners alone as clay; avoid balloon shadows, excessive glow, unreadable light-on-light labels, and ornamental badges.
- Confirm desktop and mobile consistency; visible keyboard focus; light/dark adaptation only if requested; loading, empty, disabled, error and success states; reduced-motion behavior.
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.
## Anti-slop: style-specific

**Soft material, not toy inflation.**

- **Reject:** Reject puffy balloon cards, donut shadow halos, glow borders, nested elevated shells, and repeating decorative status pills; make flat/raised/inset states distinct and consistent with one light direction.
- **Instead:** Use one owning sculpted panel with spacing/dividers for internal content; reserve inset wells for real controls or containment.
- **Copy check:** Keep copy calm and concrete rather than cutesy AI encouragement.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `claymorphism`.
