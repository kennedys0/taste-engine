---
name: taste-style-bento
description: Apply Bento Grid design style to user-selected frontend and UI work. Use only when the user explicitly chooses this style. Provides typography, color, layout, components, interactions, motion, copy and quality gates. Do not impose on unrelated work.
license: MIT
metadata:
  version: "0.10.0"
---

Use this skill only after a user explicitly chooses `bento` or a confirmed project configuration specifies it. For unexplained new UI requests, use a style selector such as `taste-engine` instead of deciding the user's taste here. Existing brand, accessibility and user overrides outrank all examples below. The following style guide is not permission to start UI coding before style selection.

# Style pack: Bento Grid

**ID:** `bento`  
**Signature:** Modular card composition with varied, purposeful panel sizes.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies.

## Good fit / trade-offs

- **Works well for:** Product overviews, portfolios, landing pages and feature discovery.
- **Be careful with:** Large transactional tables or workflows requiring one obvious linear task flow.

## Typography and typewriting

Contemporary readable sans: DM Sans, Manrope, or system sans. Headings 20–40px; card titles 17–22px; body 14–16px. Each tile has clear heading and limited text.

## Color direction

Muted background, 1–2 carefully chosen accents, tile backgrounds with sufficient foreground contrast.

## Layout and geometry

4/8px grid, consistently aligned card edges, 12–20px card radius, varied grid spans with logical reading order. On mobile collapse in content-priority order.

## Surfaces, depth, texture

Simple panels with subtle borders or mild shadow; variation comes from composition and content rather than gradients.

## Component anatomy and interaction

Tiles for true distinct features, charts, images, and CTAs; clear clickability. Do not make each tile a mini dashboard with nested cards.

## Motion

130–200ms slight hover elevation or image transitions; no attention competition across all tiles.

## Optional Anime.js v4 recipe

- **Motion decision:** Animate a tile only when its contents or layout genuinely change; ensure stable reading order.
- **Starting duration:** 180ms (0 = immediate); adjust to task and user preference.
- **Avoid:** every tile animating on initial page load.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Strong tile headlines, factual descriptions, clear action labels.

## Starter tokens (suggestions, not a complete theme)

| Token | Starting value |
| --- | --- |
| `--taste-radius-sm` | `10px` |
| `--taste-radius-lg` | `18px` |
| `--taste-border` | `1px solid rgba(0,0,0,.08)` |
| `--taste-shadow` | `0 5px 16px rgba(0,0,0,.06)` |
| `--taste-font-body` | `DM Sans, system-ui, sans-serif` |
| `--taste-motion-duration` | `180ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values. Fall back to installed fonts/system stack; do not silently download font assets.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Use a full-height opening composition where one dominant introduction and a small number of genuinely useful supporting tiles share a grid. The 100svh requirement never licenses extra decorative mini-cards; on mobile, prioritize heading and CTA before lower-priority tiles. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Make each span intentional; test missing content, long titles, and mobile reflow.
- **Don't:** Do not use masonry solely for visual novelty; avoid uneven card heights that imply hierarchy accidentally.
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

**Modular content, not tile stuffing.**

- **Reject:** Reject unnecessary nested cards, empty filler tiles, random cell spans, mismatched peer prominence, and 3-card feature spam disguised as a bento grid.
- **Instead:** Assign each tile a real job; justify span by content priority; use internal separators and preserve reading order on mobile.
- **Copy check:** Write tile headings as distinct jobs or facts, not repeated product adjectives.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `bento`.

## Quality tiers (standalone)

**FLOOR (must pass):** correct and truthful data/state, working critical actions, accessible focus/labels/contrast, usable responsive UI and reduced-motion support. **REFLEX (explain or fix):** generic feature grids, purposeless nested cards, decorative labels/icons, default marketing hype or constant motion. A reflex is allowed when it clearly expresses the chosen style and serves the task. **FINISH:** refinement of alignment, typography rhythm and edge cases. Never treat the selected style itself as a violation. Do not claim browser testing unless actually performed.
