---
name: taste-style-glassmorphism
description: Apply Glassmorphism design style to user-selected frontend and UI work. Use only when the user explicitly chooses this style. Provides typography, color, layout, components, interactions, motion, copy and quality gates. Do not impose on unrelated work.
license: MIT
metadata:
  version: "0.10.0"
---

Use this skill only after a user explicitly chooses `glassmorphism` or a confirmed project configuration specifies it. For unexplained new UI requests, use a style selector such as `taste-engine` instead of deciding the user's taste here. Existing brand, accessibility and user overrides outrank all examples below. The following style guide is not permission to start UI coding before style selection.

# Style pack: Glassmorphism

**ID:** `glassmorphism`  
**Signature:** Translucent layered planes with crisp content.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies.

## Good fit / trade-offs

- **Works well for:** Marketing microsites, media interfaces, hero sections and light dashboards.
- **Be careful with:** Dense tables, accessibility-critical controls, or contexts with uncontrollable imagery behind text.

## Typography and typewriting

Clear, restrained sans: Inter, SF Pro/system sans, or DM Sans. Body 15–16 px, headings 24–40 px; 400–650 weight. Strong hierarchy and generous line-height. Avoid thin white text over photography.

## Color direction

Muted base, one accent, controlled translucent panels; foreground colors chosen against every actual composite background, not just the panel color.

## Layout and geometry

Radius 16–24 px; intentional layer overlap; 8 px spacing rhythm. Keep clear planes and consistent z-order.

## Surfaces, depth, texture

Use backdrop-filter blur(12–24px) only on selected surfaces, 1px translucent border, subtle depth shadow. Provide opaque fallback when blur is unsupported or reduced transparency is preferred.

## Component anatomy and interaction

Navigation, modal, or hero panels may be glass; data-entry fields and long content regions should usually use solid readable backgrounds; account for image changes.

## Motion

Fade or slide 120–220 ms. Avoid perpetual parallax and moving light gradients.

## Optional Anime.js v4 recipe

- **Motion decision:** Short surface opacity/translate transitions for revealing real layers; keep content contrast stable.
- **Starting duration:** 180ms (0 = immediate); adjust to task and user preference.
- **Avoid:** animating blur radius or continuous glow.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Direct and precise; glass is presentation, not a reason for vague microcopy.

## Starter tokens (suggestions, not a complete theme)

| Token | Starting value |
| --- | --- |
| `--taste-radius-sm` | `12px` |
| `--taste-radius-lg` | `20px` |
| `--taste-border` | `1px solid rgba(255,255,255,.28)` |
| `--taste-shadow` | `0 10px 30px rgba(16,24,40,.12)` |
| `--taste-font-body` | `Inter, system-ui, sans-serif` |
| `--taste-motion-duration` | `180ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values. Fall back to installed fonts/system stack; do not silently download font assets.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Let a meaningful photograph, illustration supplied by the project, or brand color field provide depth; one readable glass content plane is usually enough. Keep text contrast and focus visible as imagery changes; a blur overlay must not dominate the full viewport. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Check contrast after compositing; define fallback background and reduced-transparency mode; keep focus indicators explicit.
- **Don't:** Do not place every component on glass; do not rely on blur to communicate semantic grouping; avoid transparent tables over busy imagery.
- Confirm desktop and mobile consistency; visible keyboard focus; light/dark adaptation only if requested; loading, empty, disabled, error and success states; reduced-motion behavior.
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.
## Universal anti-slop gate (self-contained)

Every element must earn its place. **Content before decoration. Do not decorate uncertainty.** Do not invent balances, metrics, testimonials, users, logos, approval, verified/live/online status, fake activity, or success confirmations; use honest empty/loading/error states instead. Demo data is acceptable only if requested and visibly labeled.

Do not add decorative **card-inside-card** layers: a nested surface must represent a distinct interaction or information boundary. Avoid auto-generated 3-feature grids, 4-stat dashboards, fake hero claims, purposeless charts, badge/chip/icon spam, unrelated decorative art, and random loops merely to fill the viewport. Prefer grouping with typography, spacing, alignment and dividers. Equal peers need intentional visual balance.

**Anti-slop copywriting:** no generic "Unlock your potential", "Experience the future", "Supercharge your workflow", "seamless" claims, or translated equivalents. Headings must communicate actual content, CTAs must name the action, and empty/error/success text must describe real states and next steps. Avoid fake urgency, made-up counts, vague AI hype, gratuitous emoji, and inaccessible all-caps walls. Adapt the wording to this style and the user's language without changing the truth.

**Responsive and motion:** compose mobile deliberately, check long labels, focus states and accessible contrast; no text clipping to fit a trendy layout. Static by default; use motion for meaningful interactions, respect reduced-motion preferences, avoid bounce/floating/pulsing decoration without a real state.

**Critical/High findings block completion:** fabricated status/data, broken actions, inaccessible/clipped controls, misleading copy or significant mobile failure must be fixed. Report what was actually verified; do not claim tests that did not run.

**Not an aesthetics veto:** expressive colors, shadows, gradients, card layouts or decorative treatments are legitimate when they are intentional parts of the selected aesthetic and pass usability checks. Do not silently force minimalism.

## Anti-slop: style-specific

**Glass with a job.**

- **Reject:** Reject glass-on-glass-on-glass, full-page blur, noisy backdrops behind body copy, glowing borders on every control, and blur used to hide weak hierarchy.
- **Instead:** Use glass selectively for a meaningful overlay or layer; retain solid fallback surfaces and test contrast over actual composite backgrounds.
- **Copy check:** Use crisp, functional language; avoid "transcend", "immersive future" and similar generic gloss.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `glassmorphism`.

## Quality tiers (standalone)

**FLOOR (must pass):** correct and truthful data/state, working critical actions, accessible focus/labels/contrast, usable responsive UI and reduced-motion support. **REFLEX (explain or fix):** generic feature grids, purposeless nested cards, decorative labels/icons, default marketing hype or constant motion. A reflex is allowed when it clearly expresses the chosen style and serves the task. **FINISH:** refinement of alignment, typography rhythm and edge cases. Never treat the selected style itself as a violation. Do not claim browser testing unless actually performed.
