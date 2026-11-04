---
name: taste-style-bento
description: Apply Bento Grid design style to user-selected frontend and UI work. Use only when the user explicitly chooses this style. Provides typography, color, layout, components, interactions, motion, copy and quality gates. Do not impose on unrelated work.
license: MIT
metadata:
  version: "0.10.6"
---

Use this skill only after a user explicitly chooses  or a confirmed project configuration specifies it. For unexplained new UI requests, use a style selector such as  instead of deciding the user's taste here. Existing brand, accessibility and user overrides outrank all examples below. The following style guide is not permission to start UI coding before style selection.

# Style pack: Bento Grid

**ID:** `bento`  
**Signature:** Asymmetric modular card composition with strict visual weight hierarchy, diverse internal tile anatomy, and unified spatial rhythm.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies. A uniform 3x2 grid of identical feature cards **does not qualify as Bento Grid**.

## Good fit / trade-offs

- **Works well for:** Product overviews, portfolio landing pages, developer feature discovery, dashboard summaries, and hardware/software ecosystem showcases.
- **Be careful with:** High-volume linear tabular data or step-by-step transaction flows where grid asymmetry distracts from sequential progression.
- **Reference directions:**
  - *Modern Matte Dark Bento:* Obsidian/slate background (`#0B0D10`) with subtly elevated graphite cards (`#15191E`), 1px translucent borders (`rgba(255, 255, 255, 0.08)`), and one vibrant accent color.
  - *Clean Architectural Light Bento:* Crisp off-white canvas (`#F8F9FA`) with pure white porcelain tiles, hairline dividers (`rgba(0, 0, 0, 0.06)`), and deep charcoal typography.

## Bento grid fidelity gate — mandatory

**Before calling a bento grid page complete, the opening viewport must visibly read as a curated, asymmetric modular composition.** If a user chose this style, a uniform grid of identical cards (icon + title + paragraph) is a direct **FAIL**, as it represents generic template slop.

A successful bento grid implementation demonstrates **all** of the following:

1. **Clear Asymmetric Visual Weight:** The grid features a distinct focal hierarchy: exactly 1 dominant hero tile (spanning 2x2 or 2x1 columns) that communicates the primary message, 1–2 medium secondary tiles, and 2–3 compact tertiary tiles.
2. **Diverse Internal Tile Anatomy:** Every tile possesses a unique internal layout tailored to its specific content. Tile 1 might feature an interactive code block; Tile 2 an active toggle widget; Tile 3 a visual preview or diagram; Tile 4 a live metric readout. Identical repeating layouts across tiles fail.
3. **Unified Spatial Rhythm & Gutter Alignment:** Tile borders align strictly along a consistent CSS Grid (e.g. 3 or 4 columns) with uniform gutters (16px–24px) and matching corner curvature (20px–28px).
4. **Deliberate Mobile Restructuring:** On mobile viewports, the multi-column bento collapses into a logical, content-prioritized single column without clipping contents or causing awkward horizontal overflows.
5. **Legible Internal Hierarchy:** Each tile has a clear, succinct heading (18px–24px) and high-contrast content, avoiding walls of tiny text compressed into small boxes.
6. **Strictly Horizontal Capsule Strip (No Vertical Pill Stacking):** Any ecosystem, social profile links, or quick-filter capsule strip spanning the grid MUST be laid out horizontally side-by-side (`grid-template-columns: repeat(N, 1fr)` or inline horizontal flex ribbon with horizontal scroll on mobile). Never stack capsule buttons vertically in a column or dropdown list.
7. **Single-Viewport Hero Composition ("1-Page Fit"):** When used as the primary hero section, portfolio overview, or studio landing page, the complete Bento composition must calibrate its padding, aspect ratios, and card heights so that the entire set of complementary tiles fits comfortably within a single desktop viewport (`100svh` / `min-height: calc(100svh - header_height)`). Avoid oversized card padding or excessive vertical gaps that force the user to scroll before seeing the primary compartments.
8. **Anti-Pitch-Black Rule:** Never use pure `#000000` for canvas or cards in dark mode. Pitch black creates harsh visual vibration, destroys depth perception, and accelerates eye fatigue. The canvas base must use refined dark graphite slate (`#13151B`), cards use elevated matte charcoal (`#1E222B`), and elevated pill capsules use deep charcoal (`#262B36`).
9. **Two-Tone Typographic Contrast:** In narrative, profile, or value-statement tiles, never render whole paragraphs in monochromatic text. The primary hook or subject uses high-contrast crisp white (`#F4F4F7`, weight 700), while the sentence continuation or supporting role seamlessly continues in warm muted slate gray (`#8E95A5`, weight 400–500).
10. **High-Impact Action Pill CTA:** The primary conversion action (email link, hire button, start project CTA) must use a warm Tangerine/Coral (`#FF5722`) button with full-pill radius (`border-radius: 9999px`) to create an immediate focal pull against the dark slate surfaces.

**First-viewport test:** In a desktop screenshot, identify the dominant hero tile, the varied internal tile presentations, and the unified grid alignment **without reading the page title**. If all tiles look identical, redesign the grid hierarchy.

## Explicit bento layout exception — asymmetric tiles are encouraged

**Bento-specific override:** The universal anti-slop caution against *excessive cards or dashboard clutter* MUST NOT be interpreted as a ban on multi-tile layouts here. An authentic bento grid is fundamentally **modular and compartmentalized**, functioning like a Japanese bento box where each compartment serves a distinct dish.

- **Allowed layout treatments:** Asymmetric grid column/row spans (`grid-column: span 2; grid-row: span 2;`), subtle card hover elevations, embedded interactive mini-controls (toggles, code tabs), and ambient edge glows on active tiles.
- **Anti-slop boundary:** No card-inside-card nesting within a bento tile. A tile is already an information container; use typographic hierarchy, dividers, and spacing for internal structure rather than nesting another card inside it.
- **Anti-slop interpretation:** Evaluate bento layouts by **content variety, information density, and reading hierarchy**, not by counting cards. Uniform feature grids are slop; curated asymmetric bento compositions are authentic design.

## Typography and typewriting

Contemporary, refined sans: Space Grotesk, DM Sans, Manrope, Inter, or system sans. Primary hero headings: 28–44 px (weight 700); tile titles: 18–22 px (weight 600); body: 14–15 px; captions/tags: 12–13 px. Keep body text brief and scannable.

**Two-Tone Typographic Contrast (Signature Pattern):**
In narrative, profile, or value-statement tiles, do not render whole paragraphs in uniform white or uniform gray. Use two-tone contrast: the primary message hook or subject is rendered in crisp high-contrast white (`#F4F4F7`, weight 700), while the sentence continuation, role modifier, or supporting explanation seamlessly continues in warm muted slate gray (`#8E95A5`, weight 400–500).

## Color direction

- **Dark Mode (Default Refined Matte Slate — Non-Pitch-Black):**
  - **No Pitch Black Rule:** Never use `#000000` or raw black for canvas or card surfaces. Pitch black creates harsh unnatural contrast and flattens depth. Use refined dark graphite/charcoal slate.
  - **Canvas Base:** Soft dark graphite slate (`#13151B`).
  - **Tile Background:** Elevated matte charcoal (`#1E222B`).
  - **Elevated Sub-elements / Pill Capsules:** Slightly lighter charcoal (`#262B36`).
  - **Primary Typography:** Crisp porcelain (`#F4F4F7`).
  - **Secondary / Muted Text:** Warm slate gray (`#8E95A5` — passes 4.8:1 WCAG AA).
  - **Hairline Border:** Translucent white stroke (`1px solid rgba(255, 255, 255, 0.08)` or `#2A2F3B`).
  - **High-Impact CTA Accent:** Warm Tangerine / Coral (`#FF5722`), providing instant visual pull for action pills (`hey@...`, `Start Project →`).
  - **Brand Accent:** Electric Violet (`#8B5CF6`) or Neon Lime (`#C7F265`).
- **Light Mode (Clean Architectural Ceramic):**
  - **Canvas Base:** Soft warm off-white (`#F3F4F6`).
  - **Tile Background:** Pure white ceramic (`#FFFFFF`).
  - **Elevated Sub-elements / Pill Capsules:** Soft light gray (`#E5E7EB`).
  - **Primary Typography:** Deep charcoal ink (`#111827`).
  - **Secondary / Muted Text:** Slate gray (`#6B7280` — passes 4.5:1 WCAG AA).
  - **Hairline Border:** Translucent dark stroke (`1px solid rgba(0, 0, 0, 0.08)`).
  - **High-Impact CTA Accent:** Warm Tangerine / Coral (`#FF5722`).
- **Theme Coupling & Anti-Collision Rule:** Canvas, tile surfaces, typography, and borders MUST adapt in synchronized pairs. When switching to dark mode, text must turn light; when switching to light mode, text must turn dark. Never allow dark text (`#111827`) on dark tiles or white text (`#FFFFFF`) on light tiles.

## Layout and geometry

CSS Grid: `grid-template-columns: repeat(3, 1fr)` or `repeat(4, 1fr)`; gaps: 16px–24px. Card radii: 24px–28px. All tile borders must align flush along horizontal and vertical grid tracks. Generous corner rounding (`24px–28px`) is essential for the soft, tactile bento compartmentalization.

## Surfaces, depth, texture

- **Bento Tile:** Solid background with subtle hairline stroke (`1px solid var(--taste-bento-border)`) and soft ambient drop shadow (`0 8px 24px rgba(0, 0, 0, 0.16)`).
- **Hover Interaction:** Subtle elevation (`transform: translateY(-2px); box-shadow: 0 12px 32px rgba(0, 0, 0, 0.24)`).
- **Sub-capsules / Pill Bars:** Inline horizontal rows of pill buttons (`border-radius: 9999px; background: var(--taste-bento-surface-elevated); padding: 0.45rem 1rem;`).

## Component anatomy and interaction

1. **Hero Profile / Value Tile (2x2 or 2x1):** Avatar portrait with subtle border ring, bold two-tone headline ("Name is a Role currently doing Activity"), and status indicator.
2. **Contact / CTA Tile (1x1 or 2x1):** Abstract wireframe vector icon (spring, wave, geometric), direct question ("Have a project in mind?"), and high-contrast full-pill button (`#FF5722`, `border-radius: 9999px`).
3. **Capsule Links Strip (Full Width Row):** A continuous horizontal sequence of capsule pills (`[ github. ] [ dribbble. ] [ figma. ] [ x.com. ] [ linkedin. ]`) with clean hover feedback.
4. **Location & Timezone Tile (1x1):** Wireframe globe SVG icon, city/region heading ("Based in Brooklyn, New York"), and muted real-time timezone tag ("GMT-5 / 14:30 EST").
5. **Product / Capability Showcase Tile (2x1 or 2x2):** High-fidelity mobile screen frame or card mockup with status pill (`● ONLINE`), interactive tag chips (`[ 3D Modeling ] [ Design Tokens ] [ Micro-interactions ]`), and social proof metric (`★ ★ ★ ★ ★ +1,456 reviews`).
6. **Craft & Philosophy Tile:** Two-tone manifesto paragraph conveying core design principles.

## Motion

140–220 ms smooth ease-out. Restrained tile lift on hover. No distracting competing animations across multiple tiles simultaneously.

## Optional Anime.js v4 recipe

- **Motion decision:** Staggered subtle tile entrance or smooth hover elevation.
- **Starting duration:** 180ms (0 = immediate); adjust to task and user preference.
- **Avoid:** tile flipping, erratic scaling, floating loop distractions.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Direct, punchy, and informative. Examples: “Instant deployment”, “Zero configuration”, “48ms latency”. Avoid vague buzzwords like “Next-gen synergy”.

## Starter tokens (suggestions, not a complete theme)

| Token | Dark mode default (Refined Slate / Non-Pitch-Black) | Light mode default |
| --- | --- | --- |
| `--taste-bento-bg` | `#13151b` | `#f3f4f6` |
| `--taste-bento-surface` | `#1e222b` | `#ffffff` |
| `--taste-bento-surface-elevated` | `#262b36` | `#e5e7eb` |
| `--taste-bento-text` | `#f4f4f7` | `#111827` |
| `--taste-bento-text-muted` | `#8e95a5` | `#6b7280` |
| `--taste-bento-border` | `1px solid rgba(255, 255, 255, 0.08)` | `1px solid rgba(0, 0, 0, 0.08)` |
| `--taste-bento-radius` | `28px` | `28px` |
| `--taste-bento-gap` | `20px` | `20px` |
| `--taste-bento-shadow` | `0 8px 24px rgba(0, 0, 0, 0.20)` | `0 8px 24px rgba(0, 0, 0, 0.06)` |
| `--taste-bento-accent-cta` | `#ff5722` | `#ff5722` |
| `--taste-bento-accent-brand` | `#8b5cf6` | `#7c3aed` |
| `--taste-bento-font-display` | `Space Grotesk, DM Sans, sans-serif` | `Space Grotesk, DM Sans, sans-serif` |
| `--taste-bento-font-body` | `DM Sans, Manrope, system-ui, sans-serif` | `DM Sans, Manrope, system-ui, sans-serif` |
| `--taste-bento-motion-duration` | `180ms` | `180ms` |

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Arrange the top section as a hero bento grid where the main product story occupies the primary 2x2 tile and supporting proof points surround it. Do not force 8 tiny cards into the first viewport merely to fill height. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Verify clear visual dominance of the hero tile; ensure every tile has a distinct internal layout; confirm single-viewport first-screen fit on desktop; ensure horizontal side-by-side capsule link alignment; verify non-pitch-black graphite slate (#13151b / #1e222b); check grid collapse on mobile; maintain consistent gap spacing; verify dark/light mode switching contrast: ensure canvas, tile surfaces, typography, and borders switch in coupled pairs and pass WCAG AA (at least 4.5:1).
- **Don't:** Do not generate identical repeating 3-card or 4-card templates; avoid nested cards inside tiles; never stack capsule links vertically in a column; avoid oversized padding that breaks the 1-page viewport fit; do not use raw pitch black (#000000); avoid unreadable miniature charts or fake metric labels; do not allow theme collisions such as dark text on dark tiles, white text on white tiles, or invisible borders.
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

**Curated composition, not auto-generated card grids.**

- **Reject:** Uniform grids of identical cards, nested cards within cards, vertically stacked capsule pills, raw pitch black (#000000) surfaces, fake metrics with no units, placeholder icons without clear meaning, empty tiles added solely to balance a CSS grid, and dark/light mode color collisions where text remains unreadable against the tile surface.
- **Instead:** Design each tile around actual distinct features or user actions with asymmetric weights and scannable headings.
- **Copy check:** Every tile heading must communicate real functional utility; avoid generic slogan templates.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `bento`.

## Quality tiers (standalone)

**FLOOR (must pass):** correct and truthful data/state, working critical actions, accessible focus/labels/contrast, usable responsive UI and reduced-motion support. **REFLEX (explain or fix):** generic feature grids, purposeless nested cards, decorative labels/icons, default marketing hype or constant motion. A reflex is allowed when it clearly expresses the chosen style and serves the task. **FINISH:** refinement of alignment, typography rhythm and edge cases. Never treat the selected style itself as a violation. Do not claim browser testing unless actually performed.
