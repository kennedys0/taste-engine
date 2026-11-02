# Style pack: Retro Terminal

**ID:** `retro-terminal`  
**Signature:** Developer-console visual language with modern usability.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies.

## Good fit / trade-offs

- **Works well for:** Developer portfolios, CLI dashboards, cyberculture experiences and coding tools.
- **Be careful with:** Mainstream audiences if console familiarity cannot be assumed.

## Typography and typewriting

Readable monospace: IBM Plex Mono, JetBrains Mono, or ui-monospace. Text 14–16px; headings 22–36px; use true text hierarchy rather than all monospace at one size. No excessively thin pixel fonts for important copy.

## Color direction

Dark charcoal / near-black canvas, calm high-contrast foreground, one restrained console accent (green, amber, or cyan); semantic error colors stay distinct.

## Layout and geometry

Tight aligned grid, 0–6px radius, 1px terminal-panel borders; windows/chrome only where it conveys structure.

## Surfaces, depth, texture

Flat dark panels, very subtle scanline texture only if optional and not behind body text. Cursor blink optional, not required.

## Component anatomy and interaction

Command-palette interactions, log lists, code blocks, keyboard shortcuts with clear pointer/mobile fallbacks. Do not turn every action into a faux command.

## Motion

Prefer immediate updates; optional typing animation only for intro demonstrations, skippable and disabled with reduced motion.

## Optional Anime.js v4 recipe

- **Motion decision:** Immediate state changes; optional skippable typing demo only when user asks.
- **Starting duration:** 0ms (0 = immediate); adjust to task and user preference.
- **Avoid:** typing essential instructions and never-ending blinking gimmicks.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Developer-fluent but clear; explain jargon in public-facing projects.

## Starter tokens (suggestions, not a complete theme)

| Token | Starting value |
| --- | --- |
| `--taste-radius-sm` | `2px` |
| `--taste-radius-lg` | `4px` |
| `--taste-border` | `1px solid rgba(180,225,190,.20)` |
| `--taste-shadow` | `none` |
| `--taste-font-body` | `IBM Plex Mono, ui-monospace, monospace` |
| `--taste-motion-duration` | `120ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values. Fall back to installed fonts/system stack; do not silently download font assets.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Treat the opening viewport as a legible console workbench with real navigation and project introduction. A cursor/typing motif is optional and skippable, never blocks the primary action or invents system activity to fill the screen. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Use semantic status symbols plus text, make all functionality keyboard and touch accessible, preserve selectable/copyable text.
- **Don't:** Avoid flashing cursors, green-only status signals, illegible low-contrast text and fake commands that cannot be executed.
- Confirm desktop and mobile consistency; visible keyboard focus; light/dark adaptation only if requested; loading, empty, disabled, error and success states; reduced-motion behavior.
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.
## Anti-slop: style-specific

**Operational feel, not fake hacking theater.**

- **Reject:** Reject fake green-on-black code rain, dead prompt lines, fabricated uptime, fake log feeds, blinking cursors everywhere and horizontal overflow on phones.
- **Instead:** Use honest console conventions where the interface really behaves like a tool; support keyboard, touch, text selection and wrapping.
- **Copy check:** Console-style copy should reflect actual operations and errors; no counterfeit security or "ACCESS GRANTED" theatrics.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `retro-terminal`.
