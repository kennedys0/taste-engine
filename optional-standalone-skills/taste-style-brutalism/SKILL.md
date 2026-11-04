---
name: taste-style-brutalism
description: Apply Brutalism design style to user-selected frontend and UI work. Use only when the user explicitly chooses this style. Provides typography, color, layout, components, interactions, motion, copy and quality gates. Do not impose on unrelated work.
license: MIT
metadata:
  version: "0.10.6"
---

Use this skill only after a user explicitly chooses  or a confirmed project configuration specifies it. For unexplained new UI requests, use a style selector such as  instead of deciding the user's taste here. Existing brand, accessibility and user overrides outrank all examples below. The following style guide is not permission to start UI coding before style selection.

# Style pack: Brutalism

**ID:** `brutalism`  
**Signature:** Raw structural honesty, exposed layout scaffolding, uncompromising monochrome contrast, and zero decorative camouflage.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies. A chaotic, broken layout with arbitrary font sizes **does not qualify as architectural Brutalism**.

## Good fit / trade-offs

- **Works well for:** Avant-garde portfolios, activist platforms, architectural archives, independent publishing, art/culture institutions, and developer tools seeking uncompromised structural authenticity.
- **Be careful with:** Conventional mass-market consumer applications where decorative familiarity and gentle aesthetics reduce initial user hesitation.
- **Reference directions:**
  - *Architectural Béton Brut:* Raw concrete gray (`#E8E8E8` to `#DCDCDC`), pure stark black lines (`#000000`), exposed structural grid divisions, and monospaced architectural metadata.
  - *Stark Monochrome Scaffolding:* Pure white background (`#FFFFFF`) with heavy black borders (`2.5px solid #000000`), stark black block actions, and zero cosmetic ornamentation.

## Brutalist material fidelity gate — mandatory

**Before calling a brutalist page complete, the opening viewport must visibly read as a raw, honest structural composition.** If a user chose this style, a generic site that merely applies unstyled defaults or chaotic overlapping text is a **FAIL**.

A successful brutalist implementation demonstrates **all** of the following:

1. **Exposed Structural Scaffolding:** Grid lines, section dividers, and content containers are formed by visible solid black borders (`2px–3px solid #000000`), celebrating the structural skeleton of the webpage.
2. **Zero Cosmetic Camouflage:** Absolutely no soft blurred drop shadows, no glossy reflections, no rounded bubble corners, and no translucent glass blurs. Surfaces are flat, opaque, and unapologetically direct.
3. **Hyper-Disciplined Alignment:** Despite its raw material honesty, alignment is razor-sharp. Columns, borders, and rows lock together seamlessly with zero erratic wandering.
4. **Stark High-Contrast Palette:** Uncompromising black-on-white or black-on-concrete monochrome contrast meeting WCAG AAA (7:1+). Color is used only as an operational alert signal (pure red `#FF0000` or raw warning yellow `#FFD700`).
5. **Immediate Interactive State Transitions:** Buttons and interactive elements flip instantly on `:hover` and `:active` (e.g. immediate color inversion from black-on-white to white-on-black) without delayed easing or artificial spring physics.
6. **Exposed Blueprint Gridlines & Cellular Enclosure:** Every section, compartment, and functional module must be enclosed in solid structural borders (`2px–3px solid`), aligning flush without awkward gaps like an architectural blueprint or constructivist formwork.
7. **Strict 0px Border Radii Mandate:** Absolute square corners everywhere (`border-radius: 0px`). Bubble corners, rounded buttons, and pill badges are strictly forbidden in architectural brutalism.
8. **Monumental Heavyweight Condensed Typography:** Primary hero headlines must use heavyweight condensed grotesk typography (`Anton`, `Space Grotesk 900`, `Impact`, or heavy bold sans) with tight leading (0.88–1.05) and uppercase treatment.
9. **Controlled Operational Signal Colors:** The foundation is uncompromising black and white / concrete paper. Saturated color is strictly limited to high-voltage Warning Yellow (`#FFDE00`) and Signal Red (`#FF3B30`), used for operational status cells, active project rows, and primary conversion CTAs.
10. **Structured Architectural Indexing:** Compartments must feature explicit structural numbering (`01`, `02`, `03`, `04`), directional arrows (`↗`, `→`, `↓`), and technical metadata brackets.
11. **Single-Viewport Hero Composition ("1-Page Fit"):** The opening desktop hero must assemble the brand headline, architectural coordinate cell, status ticker, and primary action within a single view (`100svh`) before expanding into the project matrix and documentation.
12. **Cellular Blueprint Navigation Architecture:** Navigation bars must be composed of discrete, bounded rectangular cells divided by continuous vertical lines (`2px–3px solid`). Keep the main navigation track uncluttered by avoiding long code snippets or oversized command strings directly inside menu cells; place CLI installation pills or utility commands in the hero action group or a dedicated sub-bar. The brand cell features monumental condensed type, auxiliary role/taglines use compact uppercase stacked text (e.g. 2–3 vertical lines), navigation links sit in distinct rectangular bays, and the primary conversion CTA occupies the far right cell highlighted in a high-voltage operational color (such as Caution Yellow `#FFDE00`) with a directional corner arrow (`↗`).
13. **Hero Void Elimination & Architectural Spec Grid:** A brutalist hero composition avoids hollow, unpurposed whitespace between the primary headline and action row. When vertical space exists, structure it with dense, authentic architectural data relevant to the project: such as a multi-compartment numbered technical spec grid (`01`, `02`, `03` with prominent monospace index numbers and truthful functional specifications), an authentic circular stamp seal with running perimeter text, or technical metadata callouts.
14. **Monumental Headline Architecture:** Primary hero headlines must use monumental, tightly stacked condensed heavyweight grotesk typography (`Anton`, `Space Grotesk 900`, `Impact`, or heavy bold sans) with tight leading (`0.88–1.05`) and uppercase treatment, paired with a high-contrast bulleted micro-statement establishing the site's authentic purpose. The copy must directly reflect the user's specific product or project without generic template filler.

**First-viewport test:** In a desktop screenshot, identify the exposed structural border grid, the flat unornamented planes, and the stark monochrome authority **without reading the page title**. If it contains rounded cards or soft shadows, strip away the decorative camouflage immediately.

## Explicit brutalist structural exception — exposed grid borders are required

**Brutalism-specific override:** The universal anti-slop caution against *excessive borders or harsh contrast* MUST NOT be interpreted as a ban on thick black dividing lines (2px–3px solid) or exposed structural scaffolding here. In architectural brutalism, structural joints and honest materials are celebrated, not hidden behind cosmetic paint.

- **Allowed structural treatments:** Visible 2px–3px structural borders, raw rectangular containers, high-contrast monospace metadata, and immediate color inversion states.
- **Anti-slop boundary:** Do not deliberately break accessibility by overlapping body paragraphs, using unreadable neon clash colors, or making buttons impossible to locate. Authentic brutalism is hyper-functional, not randomly broken.
- **Anti-slop interpretation:** Evaluate brutalist layouts by **structural integrity, functional utility, and legibility**, not by trying to soften hard edges. Removing structural borders to satisfy a generic soft heuristic is a **design regression**.

## Typography and typewriting

Unyielding, heavyweight grotesk sans or technical monospace: Arial, Helvetica, IBM Plex Sans, IBM Plex Mono, or system sans. Headlines: 44–72 px desktop / 30–44 px mobile (weight 800–900, tight line-height 1.05–1.15). Body text: 16–18 px (weight 400, line-height 1.5). Monospace for metadata, timestamps, and section indexes.

## Color direction

- **Light Mode (Stark Paper):**
  - **Canvas Base:** Stark paper white (`#FFFFFF`) or architectural concrete (`#E5E5E5`).
  - **Structural Ink / Borders:** Pure black (`#000000`).
  - **Surface Blocks:** High-contrast solid fills (`#000000` or `#FFFFFF`).
- **Dark Mode (Pitch Inverted):**
  - **Canvas Base:** Stark pitch black (`#000000`).
  - **Structural Ink / Borders:** Pure stark white (`#FFFFFF`).
  - **Surface Blocks:** High-contrast solid dark fills (`#000000` or `#121212`).
- **Operational Signal Accent (Single Color Only):** Signal Red (`#FF0000` / `#FF3333`) or Warning Amber (`#FFCC00`).
- **Theme Inversion Rule:** In brutalism, dark/light mode is an authoritative polarity flip. In dark mode, canvas is `#000000` and text/borders are `#FFFFFF`. Buttons invert cleanly on hover (light: white button flips to black fill + white text; dark: black button flips to white fill + black text). Black text on black background or white text on white background is strictly forbidden.

## Layout and geometry

Corners are strictly square (`border-radius: 0px`). Structural borders: `2px–3px solid #000000`. Content blocks lock flush against each other or maintain firm 16px/24px modular gaps.

## Surfaces, depth, texture

Surfaces are 100% flat, opaque, and structural. Zero shadows. Zero gradients. Depth is established purely by layering black blocks over white frames and immediate inversion of foreground and background colors.

## Component anatomy and interaction

- **Brutalist Button:** Heavy black border (`2px solid #000000`), white background, bold uppercase text; on hover/active, immediately inverts to solid black background and white text.
- **Structural Panel:** Rectangular container with heavy top/bottom borders; dividers between internal sections.
- **Metadata Tag:** Monospace tag enclosed in square brackets: `[DOC_REF: 4092]`.
- **Form Controls:** Unadorned input fields with thick black border and high-contrast solid black focus ring (`outline: 3px solid #000000; outline-offset: 2px;`).
- **Architectural Spec Cell:** A rectangular compartment bounded by 2px solid lines featuring a prominent 2rem+ monospace index number (`01`, `02`, `03`), an uppercase technical label, and brief, truthful functional specifications.
- **Circular Stamp Seal:** An authentic vector circular stamp badge with running perimeter text along an SVG circular textPath and a solid central graphic mark (such as an asterisk `*` or star `★`), celebrating verified structural fidelity without relying on soft decorative badges. Copy is user-defined.
- **Cellular Navigation Bar:** A full-width header divided into discrete architectural bays (brand cell, stacked multi-line role/tagline cell, individual link cells, theme polarity invert button, and high-visibility corner action cell).

## Motion

Immediate state flips by default (0 ms) or very brief linear transitions (60–100 ms). No bounce, no easing curves, no parallax, no decorative transitions.

## Optional Anime.js v4 recipe

- **Motion decision:** Immediate state flips by default; Anime.js generally unnecessary for authentic brutalism.
- **Starting duration:** 0ms (immediate); adjust only if a specific functional mechanical sliding shutter is requested.
- **Avoid:** springs, sliding reveals, theatrical scroll animations.
- **Dependency:** CSS/native by default. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Direct, unapologetic, and factual. Examples: “INDEX”, “DOWNLOAD SPECIFICATION”, “TERMINAL ERROR: CONNECTION LOST”, “CONFIRM”. Avoid chatty conversational copy or persuasive marketing fluff.

## Starter tokens (suggestions, not a complete theme)

| Token | Light mode default | Dark mode default |
| --- | --- | --- |
| `--taste-brutal-bg` | `#ffffff` | `#000000` |
| `--taste-brutal-ink` | `#000000` | `#ffffff` |
| `--taste-brutal-surface` | `#ffffff` | `#121212` |
| `--taste-brutal-border` | `2.5px solid #000000` | `2.5px solid #ffffff` |
| `--taste-brutal-radius` | `0px` | `0px` |
| `--taste-brutal-signal-yellow` | `#ffde00` | `#ffde00` |
| `--taste-brutal-signal-red` | `#ff3b30` | `#ff3b30` |
| `--taste-brutal-font-heading` | `'Arial Black', Arial, Helvetica, sans-serif` | `'Arial Black', Arial, Helvetica, sans-serif` |
| `--taste-brutal-font-body` | `Arial, Helvetica, sans-serif` | `Arial, Helvetica, sans-serif` |
| `--taste-brutal-font-mono` | `'IBM Plex Mono', monospace` | `'IBM Plex Mono', monospace` |
| `--taste-brutal-motion-duration` | `0ms` | `0ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-brutal-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Construct the first viewport as an unapologetic architectural monolith: massive display title locked inside structural scaffolding, stark black call-to-action blocks, and zero cosmetic filler. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Verify stark monochrome contrast; ensure 2–3px structural borders are solid; verify sharp 0px square corners; confirm single-viewport hero fit on desktop; enforce monumental condensed typography; verify controlled caution yellow (#ffde00) and signal red (#ff3b30) operational roles; verify dark/light mode polarity inversion so text and background never clash (no black-on-black or white-on-white text); verify cellular navigation without long code clutter; ensure hero voids are structured with 3-cell architectural spec grids; confirm circular stamp seal or technical metadata.
- **Don't:** Do not add rounded corners, soft drop shadows, or smooth color gradients (strictly 0px radius); avoid arbitrary font size chaos; never use pill buttons; avoid oversized padding that breaks the single-viewport hero fit; avoid decorative filler badges or chatty marketing copy; do not leave black ink or borders when switching to dark canvas; never leave cavernous empty whitespace between hero headlines and buttons; do not place long command code strings inside the main navigation bar.
- Confirm desktop and mobile consistency; visible keyboard focus (`:focus-visible`); loading, empty, disabled, error and success states; reduced-motion behavior (`prefers-reduced-motion`).
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.

## Universal anti-slop gate (self-contained)

Every element must earn its place. **Content before decoration. Do not decorate uncertainty.** Do not invent balances, metrics, testimonials, users, logos, approval, verified/live/online status, fake activity, or success confirmations; use honest empty/loading/error states instead. Demo data is acceptable only if requested and visibly labeled.

Do not add decorative **card-inside-card** layers: a nested surface must represent a distinct interaction or information boundary. Avoid auto-generated 3-feature grids, 4-stat dashboards, fake hero claims, purposeless charts, badge/chip/icon spam, unrelated decorative art, and random loops merely to fill the viewport. Prefer grouping with typography, spacing, alignment and dividers. Equal peers need intentional visual balance.

**Anti-slop copywriting:** no generic "Unlock your potential", "Experience the future", "Supercharge your workflow", "seamless" claims, or translated equivalents. Headings must communicate actual content, CTAs must name the action, and empty/error/success text must describe real states and next steps. Avoid fake urgency, made-up counts, vague AI hype, gratuitous emoji, and inaccessible all-caps walls. Adapt the wording to this style and the user's language without changing the truth.

**Theme and mode contrast integrity:** When a user requests dark mode or light mode (or builds a theme switcher), background and foreground colors MUST flip in synchronized pairs across all surfaces, text, borders, inputs, and semantic badges. Never leave black text on dark background, white text on white background, or unreadable low-contrast status pills. All states must meet WCAG AA contrast (minimum 4.5:1 for body/normal text, 3:1 for large headlines and interactive boundaries).

**Responsive and motion:** compose mobile deliberately, check long labels, focus states and accessible contrast; no text clipping to fit a trendy layout. Static by default; use motion for meaningful interactions, respect reduced-motion preferences, avoid bounce/floating/pulsing decoration without a real state.

**Critical/High findings block completion:** fabricated status/data, broken actions, inaccessible/clipped controls, misleading copy, theme contrast collisions or significant mobile failure must be fixed. Report what was actually verified; do not claim tests that did not run.

**Not an aesthetics veto:** expressive colors, shadows, gradients, card layouts or decorative treatments are legitimate when they are intentional parts of the selected aesthetic and pass usability checks. Do not silently force minimalism.

## Anti-slop: style-specific

**Structural honesty, not aesthetic playfulness.**

- **Reject:** Rounded pill shapes, pastel accents, decorative shadow blurs, arbitrary font chaos, playful sticker illustrations, generic template cards, and theme collisions (such as black text remaining on a dark brutalist canvas).
- **Instead:** Expose layout grids with heavy structural borders, stark type hierarchy, immediate state flips, and unambiguous contrast.
- **Copy check:** UI writing must be brief, direct, and functional without marketing jargon.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `brutalism`.

## Quality tiers (standalone)

**FLOOR (must pass):** correct and truthful data/state, working critical actions, accessible focus/labels/contrast, usable responsive UI and reduced-motion support. **REFLEX (explain or fix):** generic feature grids, purposeless nested cards, decorative labels/icons, default marketing hype or constant motion. A reflex is allowed when it clearly expresses the chosen style and serves the task. **FINISH:** refinement of alignment, typography rhythm and edge cases. Never treat the selected style itself as a violation. Do not claim browser testing unless actually performed.
