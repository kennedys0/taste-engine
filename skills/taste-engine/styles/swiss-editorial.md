# Style pack: Swiss / Editorial

**ID:** `swiss-editorial`  
**Signature:** Rigorous grid-driven typographic hierarchy, stark scale contrast, structural hairline rules, numbered indexes, and intentional negative space.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies. A plain page with black sans-serif text **does not qualify as Swiss Editorial**.

## Good fit / trade-offs

- **Works well for:** High-end design agencies, architectural publications, editorial portfolios, cultural magazines, annual reports, and luxury product narratives.
- **Be careful with:** Fast-paced transactional operational tools where massive display typography slows down repetitive data entry.
- **Reference directions:**
  - *Classic Zurich International Style:* Crisp paper white background (`#FFFFFF` or `#F7F7F7`), stark jet black typography (`#111111`), 1px structural dividing rules, numbered indexes (`01`, `02`), and a single strike of Swiss Red (`#E3000F`).
  - *Modern Editorial Klein Blue:* Ultra-clean monochrome canvas with International Klein Blue (`#002FA7`) as a high-precision focal accent on navigation and primary actions.

## Swiss editorial fidelity gate — mandatory

**Before calling a swiss-editorial page complete, the opening viewport must visibly read as a rigorous, grid-aligned typographic editorial work.** If a user chose this style, a generic minimal page lacking dramatic scale contrast and structural rules is a **FAIL**.

A successful swiss-editorial implementation demonstrates **all** of the following:

1. **Extreme Typographic Scale Contrast:** A decisive, uncompromised contrast between massive grotesk display headlines (48px–72px desktop / 32px–44px mobile, tight tracking) and disciplined body copy (16px, line-height 1.55), with tracked uppercase section labels (`letter-spacing: 0.08em`).
2. **Structural Horizontal Hairline Rules:** Content sections, column boundaries, and metadata headers are demarcated by clean 1px solid rules (`border-top: 1px solid #111111`), establishing clear visual shelves.
3. **Numbered Section Hierarchy:** Distinct editorial index numbering (`01`, `02`, `03`) placed above or beside primary article blocks, creating scannable visual anchors.
4. **Rigorous Multi-Column Grid Alignment:** Layout conforms strictly to a 12-column desktop grid with generous asymmetrical gutters and margins. Content never floats loosely without grid anchoring.
5. **Monochrome Base + 1 High-Impact Signal Accent:** The layout remains strictly monochrome (black, off-white, paper gray) with exactly one deliberate signal accent (Swiss Red `#E3000F` or Klein Blue `#002FA7`) applied sparingly to active links, index tags, or primary CTAs.

**First-viewport test:** In a desktop screenshot, identify the massive headline scale, the 1px structural dividing rules, the numbered section markers, and the deliberate asymmetric grid **without reading the page title**. If it looks like a standard blog template, elevate the typography scale and grid rules.

## Explicit swiss editorial typographic exception — dramatic scale is required

**Swiss-editorial-specific override:** The universal anti-slop caution against *excessive font sizes or empty space* MUST NOT be interpreted as a ban on large display headlines (48px–72px) or generous whitespace here. In Swiss Typography (Josef Müller-Brockmann, Max Bill), active negative space and bold scale contrast are the primary structural materials, replacing decorative graphics or shadows.

- **Allowed typographic treatments:** Massive display scale (up to 72px), numbered index typography, hairline structural borders, uppercase tracked metadata, and high-impact single-accent links.
- **Anti-slop boundary:** Do not paste random floating pull-quotes without editorial context, fake publication issue numbers, or oversized headlines that crowd out actual readable content.
- **Anti-slop interpretation:** Evaluate swiss layouts by **grid discipline, typographic rhythm, and information clarity**, not by trying to fill every square inch with cards. White space that directs focus is authentic design.

## Typography and typewriting

Objective grotesk sans: Helvetica Neue, Neue Haas Grotesk, Arial, Inter, or system sans. Headlines: 48–72 px desktop (weight 700–800, `letter-spacing: -0.03em`); subheadings: 24–32 px; body: 16–18 px (line-height 1.55–1.65); index numerals and captions: 12–14 px uppercase (`letter-spacing: 0.08em`).

## Color direction

- **Canvas Base:** Paper white (`#FFFFFF` or warm gallery white `#FBFBFA`).
- **Ink / Typography:** Deep obsidian black (`#111111`).
- **Dividing Rules:** Solid hairline stroke (`#111111` or `#D1D5DB`).
- **Singular Signal Accent:** Swiss Red (`#E3000F`) or International Klein Blue (`#002FA7`).
- **Secondary Gray:** Editorial neutral (`#6B7280`).

## Layout and geometry

Corners are razor-sharp (`0px` border-radius by default, up to `2px` max); generous outer margins; strict 12-column grid alignment. Structural 1px horizontal rules frame content blocks.

## Surfaces, depth, texture

Surfaces are completely flat, unornamented, and ink-sharp. Zero drop shadows, zero background gradients, zero blur. Depth is communicated purely through typographic scale, weight, and spatial juxtaposition.

## Component anatomy and interaction

- **Editorial Primary CTA:** Crisp solid black block with white typography, or clean underlined text link with 2px stroke offset.
- **Numbered Index Tag:** Small uppercase tag: `[ 01 / ARCHITECTURE ]`.
- **Dividing Rule:** `border-top: 1px solid #111111; padding-top: 1.5rem; margin-top: 2rem;`.
- **Tabular Metadata:** Two-column key-value pairs separated by hairline dividers.

## Motion

Minimal, instantaneous, or 120–160 ms clean linear transitions. No spring bounce, no floating parallax. Focus on crisp state changes.

## Optional Anime.js v4 recipe

- **Motion decision:** Clean text opacity fade or horizontal rule expansion on scroll.
- **Starting duration:** 140ms (0 = immediate); adjust to task and user preference.
- **Avoid:** elastic motion, 3D rotations, playful wobbles.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Cultured, concise, and articulate. Examples: “Selected Works 2026”, “Index”, “Read Documentation”, “01 / Overview”. Avoid colloquial slang or enthusiastic sales hype.

## Starter tokens (suggestions, not a complete theme)

| Token | Starting value |
| --- | --- |
| `--taste-swiss-bg` | `#ffffff` |
| `--taste-swiss-ink` | `#111111` |
| `--taste-swiss-accent` | `#e3000f` |
| `--taste-swiss-muted` | `#6b7280` |
| `--taste-swiss-rule` | `1px solid #111111` |
| `--taste-swiss-radius` | `0px` |
| `--taste-swiss-font-heading` | `'Helvetica Neue', Inter, system-ui, sans-serif` |
| `--taste-swiss-font-body` | `'Helvetica Neue', Inter, system-ui, sans-serif` |
| `--taste-swiss-motion-duration` | `120ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-swiss-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Anchor the opening screen with an authoritative, massive display title, clear section numbering, and an asymmetrical grid split between hero narrative and key navigation. Whitespace must feel deliberate and composed, not empty. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Verify strict 12-column grid alignment; maintain dramatic headline-to-body scale ratio; ensure 1px hairline rules cleanly separate sections; keep accent color strictly singular.
- **Don't:** Do not add drop shadows, rounded bubbles, or decorative gradients; do not clutter whitespace with meaningless badge chips; avoid low-contrast gray text on small labels.
- Confirm desktop and mobile consistency; visible keyboard focus (`:focus-visible`); loading, empty, disabled, error and success states; reduced-motion behavior (`prefers-reduced-motion`).
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.
## Anti-slop: style-specific

**Typographic authority, not generic minimalism.**

- **Reject:** Faux editorial layouts that are just centered text on white space, arbitrary italic quotes with no source, fake publication dates, and unanchored floating text blocks.
- **Instead:** Build an unyielding mathematical grid with clear structural dividing rules, numbered section hierarchy, and decisive contrast between display and reading typography.
- **Copy check:** Write articulate, informative copy that respects user intelligence; avoid marketing buzzwords.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `swiss-editorial`.
