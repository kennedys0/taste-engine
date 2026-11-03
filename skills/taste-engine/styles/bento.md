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

**First-viewport test:** In a desktop screenshot, identify the dominant hero tile, the varied internal tile presentations, and the unified grid alignment **without reading the page title**. If all tiles look identical, redesign the grid hierarchy.

## Explicit bento layout exception — asymmetric tiles are encouraged

**Bento-specific override:** The universal anti-slop caution against *excessive cards or dashboard clutter* MUST NOT be interpreted as a ban on multi-tile layouts here. An authentic bento grid is fundamentally **modular and compartmentalized**, functioning like a Japanese bento box where each compartment serves a distinct dish.

- **Allowed layout treatments:** Asymmetric grid column/row spans (`grid-column: span 2; grid-row: span 2;`), subtle card hover elevations, embedded interactive mini-controls (toggles, code tabs), and ambient edge glows on active tiles.
- **Anti-slop boundary:** No card-inside-card nesting within a bento tile. A tile is already an information container; use typographic hierarchy, dividers, and spacing for internal structure rather than nesting another card inside it.
- **Anti-slop interpretation:** Evaluate bento layouts by **content variety, information density, and reading hierarchy**, not by counting cards. Uniform feature grids are slop; curated asymmetric bento compositions are authentic design.

## Typography and typewriting

Contemporary, refined sans: DM Sans, Manrope, Inter, or system sans. Primary hero headings: 28–44 px (weight 700); tile titles: 18–22 px (weight 600); body: 14–15 px; captions/tags: 12–13 px. Keep body text brief and scannable.

## Color direction

- **Dark Mode (Default Modern Matte):**
  - **Canvas Base:** Obsidian deep slate (`#0B0D10`).
  - **Tile Background:** Elevated slate (`#15191E`).
  - **Primary Typography:** Crisp porcelain (`#F4F4F6`).
  - **Secondary / Muted Text:** Balanced cool gray (`#9CA3AF` — passes 4.5:1 WCAG AA).
  - **Hairline Border:** Translucent white stroke (`rgba(255, 255, 255, 0.08)`).
- **Light Mode (Clean Architectural):**
  - **Canvas Base:** Crisp off-white (`#F8F9FA`).
  - **Tile Background:** Pure white porcelain (`#FFFFFF`).
  - **Primary Typography:** Deep charcoal ink (`#111827`).
  - **Secondary / Muted Text:** Slate gray (`#6B7280` — passes 4.5:1 WCAG AA).
  - **Hairline Border:** Translucent dark stroke (`rgba(0, 0, 0, 0.08)`).
- **Brand Accent:** High-contrast signature color (e.g. Electric Violet `#8B5CF6`, Cyan `#06B6D4`, or Emerald `#10B981`) meeting minimum 3:1 contrast against both dark and light tile fills.
- **Theme Coupling & Anti-Collision Rule:** Canvas, tile surfaces, typography, and borders MUST adapt in synchronized pairs. When switching to dark mode, text must turn light; when switching to light mode, text must turn dark. Never allow dark text (`#111827`) on dark tiles or white text (`#FFFFFF`) on light tiles.

## Layout and geometry

CSS Grid: `grid-template-columns: repeat(3, 1fr)` or `repeat(4, 1fr)`; gaps: 16px–24px. Card radii: 20px–28px. All tile borders must align flush along horizontal and vertical grid tracks.

## Surfaces, depth, texture

- **Bento Tile:** Solid background with subtle hairline stroke (`1px solid var(--taste-bento-border)`) and soft ambient drop shadow (`0 8px 24px rgba(0, 0, 0, 0.12)`).
- **Hover Interaction:** Subtle elevation (`transform: translateY(-2px); box-shadow: 0 12px 32px rgba(0, 0, 0, 0.18)`).

## Component anatomy and interaction

- **Hero Tile (2x2 or 2x1):** Primary value proposition, rich visual or live code preview, prominent CTA.
- **Interactive Action Tile:** Integrated toggle, quick filter, or copyable command block.
- **Metric / Status Tile:** Clean tabular number with concrete label and real data.
- **Showcase Tile:** High-fidelity screenshot, asset preview, or architectural diagram.

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

| Token | Dark mode default | Light mode default |
| --- | --- | --- |
| `--taste-bento-bg` | `#0b0d10` | `#f8f9fa` |
| `--taste-bento-surface` | `#15191e` | `#ffffff` |
| `--taste-bento-text` | `#f4f4f6` | `#111827` |
| `--taste-bento-text-muted` | `#9ca3af` | `#6b7280` |
| `--taste-bento-border` | `1px solid rgba(255, 255, 255, 0.08)` | `1px solid rgba(0, 0, 0, 0.08)` |
| `--taste-bento-radius` | `24px` | `24px` |
| `--taste-bento-gap` | `20px` | `20px` |
| `--taste-bento-shadow` | `0 8px 24px rgba(0, 0, 0, 0.25)` | `0 8px 24px rgba(0, 0, 0, 0.06)` |
| `--taste-bento-accent` | `#8b5cf6` | `#7c3aed` |
| `--taste-bento-font-body` | `DM Sans, Manrope, system-ui, sans-serif` | `DM Sans, Manrope, system-ui, sans-serif` |
| `--taste-bento-motion-duration` | `180ms` | `180ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-bento-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Arrange the top section as a hero bento grid where the main product story occupies the primary 2x2 tile and supporting proof points surround it. Do not force 8 tiny cards into the first viewport merely to fill height. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Verify clear visual dominance of the hero tile; ensure every tile has a distinct internal layout; check grid collapse on mobile; maintain consistent gap spacing; verify dark/light mode switching contrast: ensure canvas, tile surfaces, typography, and borders switch in coupled pairs and pass WCAG AA (at least 4.5:1).
- **Don't:** Do not generate identical repeating 3-card or 4-card templates; avoid nested cards inside tiles; avoid unreadable miniature charts or fake metric labels; do not allow theme collisions such as dark text on dark tiles, white text on white tiles, or invisible borders.
- Confirm desktop and mobile consistency; visible keyboard focus (`:focus-visible`); loading, empty, disabled, error and success states; reduced-motion behavior (`prefers-reduced-motion`).
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.

## Anti-slop: style-specific

**Curated composition, not auto-generated card grids.**

- **Reject:** Uniform grids of identical cards, nested cards within cards, fake metrics with no units, placeholder icons without clear meaning, empty tiles added solely to balance a CSS grid, and dark/light mode color collisions where text remains unreadable against the tile surface.
- **Instead:** Design each tile around actual distinct features or user actions with asymmetric weights and scannable headings.
- **Copy check:** Every tile heading must communicate real functional utility; avoid generic slogan templates.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `bento`.
