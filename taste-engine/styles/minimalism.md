# Style pack: Minimalism

**ID:** `minimalism`  
**Signature:** Purposeful restraint, active intentional negative space, mathematical typographic calibration, and effortless information clarity.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies. An empty page with low-contrast gray text **does not qualify as Minimalism**.

## Good fit / trade-offs

- **Works well for:** High-focus productivity tools, developer utilities, focused e-commerce storefronts, personal portfolios, documentation hubs, and form-intensive applications.
- **Be careful with:** Highly branded expressive campaign sites where ornamental spectacle and playful visual noise are the primary objective.
- **Reference directions:**
  - *Calm Industrial White:* Warm neutral paper base (`#FAFAF9` or `#FFFFFF`), deep slate typography (`#18181B`), hairline dividers (`rgba(0, 0, 0, 0.08)`), and a single purposeful primary action.
  - *Disciplined Studio Dark:* Muted obsidian canvas (`#121214`) with crisp porcelain typography (`#F4F4F5`), quiet borders (`rgba(255, 255, 255, 0.10)`), and amber or cobalt accent focus.

## Minimalist material fidelity gate — mandatory

**Before calling a minimalist page complete, the opening viewport must visibly read as a masterclass in purposeful restraint, alignment, and information clarity.** If a user chose this style, "lazy minimalism" (faint gray text, missing labels, hidden controls, or an empty screen with one centered sentence) is a direct **FAIL**.

A successful minimalist implementation demonstrates **all** of the following:

1. **Active Proportional Negative Space:** Whitespace is deliberate and calibrated, not accidental empty voids. It frames content purposefully and directs the user's eye directly to key tasks without needing boxes, badges, or arrows.
2. **Mathematically Calibrated Typographic Scale:** Clear contrast between display titles (32px–44px, weight 600), section anchors (18px–22px, weight 600), body text (15px–16px, weight 400, line-height 1.6), and metadata (12px–13px, weight 500).
3. **Razor-Sharp Spatial Alignment:** Grouping is achieved through alignment, proximity, and subtle hairline dividers (`1px solid rgba(0, 0, 0, 0.08)` or `rgba(255, 255, 255, 0.10)`), completely eliminating unnecessary nested cards.
4. **Accessible High Contrast (WCAG AA/AAA):** Text, icons, and interactive elements maintain strong contrast against neutral surfaces. Faint unreadable `#999999` text on white is strictly prohibited.
5. **Clear Action Affordances:** Primary interactive controls are immediately discoverable, featuring high-contrast fills, distinct hover states, and visible keyboard focus indicators (`:focus-visible`).

**First-viewport test:** In a desktop screenshot, identify the calm typographic rhythm, effortless reading flow, and unambiguous primary action **without reading the page title**. If essential labels are hidden or text is washed out, restore contrast and structural hierarchy immediately.

## Explicit minimalist restraint exception — negative space is an active tool

**Minimalism-specific override:** The universal anti-slop caution against *empty canvases or under-designed viewports* MUST NOT be interpreted as a mandate to inject decorative badges, cards, or illustrations here. In authentic minimalist design (Dieter Rams, Massimo Vignelli), removing non-essential decoration elevates clarity and reduces cognitive load.

- **Allowed minimalist treatments:** Generous active negative space, subtle hairline dividers, unembellished typography, single-accent links, and quiet hover transitions.
- **Anti-slop boundary:** Never hide core navigation, delete labels, or sacrifice accessibility in the name of "clean aesthetics". Every control must remain discoverable and usable.
- **Anti-slop interpretation:** Evaluate minimalist layouts by **clarity of task, ease of reading, and information density**, not by demanding ornamental fills. Purposeful white space is authentic design.

## Typography and typewriting

Pure, neutral UI sans: Inter, Source Sans 3, SF Pro, or system sans. Headlines: 32–44 px (weight 600–700, `letter-spacing: -0.02em`); body: 15–16 px (weight 400, line-height 1.6); captions/metadata: 12–13 px (weight 500). Calm, scannable type scale.

## Color direction

- **Light Mode (Clean Studio Light):**
  - **Canvas Base:** Soft paper white (`#FAFAF9` or `#FFFFFF`).
  - **Typography / Ink:** Deep slate black (`#18181B`).
  - **Secondary Text:** Balanced neutral slate (`#52525B` — passes 4.5:1 WCAG AA).
  - **Hairline Divider:** Translucent gray (`rgba(0, 0, 0, 0.08)` or `#E4E4E7`).
- **Dark Mode (Disciplined Studio Dark):**
  - **Canvas Base:** Muted obsidian canvas (`#121214`).
  - **Typography / Ink:** Crisp porcelain (`#F4F4F5`).
  - **Secondary Text:** Balanced slate (`#A1A1AA` — passes 4.5:1 WCAG AA).
  - **Hairline Divider:** Translucent white (`rgba(255, 255, 255, 0.10)` or `#27272A`).
- **Brand Accent:** Singular functional accent (e.g. Cobalt `#2563EB` light / `#3B82F6` dark, or Deep Forest `#059669`).
- **Theme Coupling Rule:** Canvas, typography, secondary text, and dividers MUST flip synchronously. When user requests dark mode, text must turn light (`#F4F4F5`); when light mode, text must turn dark (`#18181B`). Never leave dark text on dark canvas.

## Layout and geometry

Consistent 4px/8px spacing grid; gentle, unified corner radii (`6px–12px`); subtle hairline borders where structural separation is necessary. Negative space groups related information naturally.

## Surfaces, depth, texture

Surfaces are quiet, flat, and matte. Minimal or zero box-shadows (`0 1px 3px rgba(0, 0, 0, 0.05)` max for elevated dropdowns). Depth is communicated via contrast, spacing, and typographic weight.

## Component anatomy and interaction

- **Primary Action (CTA):** Solid dark pill or rounded rectangle with white text, high contrast, and smooth hover transition.
- **Secondary Action:** Unadorned text link or subtle outline button with hairline border.
- **Form Input:** Clean input field with visible border, clear placeholder, and high-contrast focus ring (`outline: 2px solid #18181B; outline-offset: 2px;`).
- **Content Row / List:** Clean horizontal rows separated by hairline dividers with aligned tabular data.

## Motion

120–180 ms quiet ease-out transitions for opacity, background color, or subtle border color. Zero gratuitous movement; animations should be felt, not watched.

## Optional Anime.js v4 recipe

- **Motion decision:** Subtle opacity fade or gentle micro-transition on active state; keep motion minimal.
- **Starting duration:** 140ms (0 = immediate); adjust to task and user preference.
- **Avoid:** bouncing, sliding reveals, floating loops.
- **Dependency:** CSS/native by default. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Calm, concise, and helpful. Examples: “Save changes”, “Account settings”, “3 files selected”. Avoid marketing superlatives or enthusiastic exclamation marks.

## Starter tokens (suggestions, not a complete theme)

| Token | Light mode default | Dark mode default |
| --- | --- | --- |
| `--taste-mini-bg` | `#fafaf9` | `#121214` |
| `--taste-mini-ink` | `#18181b` | `#f4f4f5` |
| `--taste-mini-muted` | `#52525b` | `#a1a1aa` |
| `--taste-mini-border` | `1px solid rgba(0, 0, 0, 0.08)` | `1px solid rgba(255, 255, 255, 0.10)` |
| `--taste-mini-radius` | `8px` | `8px` |
| `--taste-mini-accent` | `#2563eb` | `#3b82f6` |
| `--taste-mini-font-body` | `Inter, -apple-system, system-ui, sans-serif` | `Inter, -apple-system, system-ui, sans-serif` |
| `--taste-mini-motion-duration` | `140ms` | `140ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-mini-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Compose the first viewport around a crystal-clear headline, one primary action, and generous, intentional white space. Do not invent filler cards, fake testimonials, or decorative badges to clutter the canvas. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Verify high text contrast (WCAG AA 4.5:1) in both light and dark modes; ensure interactive controls have clear hit targets and visible focus indicators; group content through spacing and hairline dividers; verify that mode switching flips canvas, ink, muted text, and borders in paired synchronization.
- **Don't:** Do not treat washed-out gray text or missing labels as minimalism; avoid hiding core actions behind obscure icons; do not create vast empty voids that confuse navigation; avoid dark/light theme collisions where text remains dark on dark canvas.
- Confirm desktop and mobile consistency; visible keyboard focus (`:focus-visible`); loading, empty, disabled, error and success states; reduced-motion behavior (`prefers-reduced-motion`).
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.

## Anti-slop: style-specific

**Clarity through restraint, not lazy emptiness.**

- **Reject:** Faint low-contrast gray text, unlabelled icon-only controls, ghost buttons that look disabled, empty viewports that communicate zero product information, and theme collisions where text is unreadable against the canvas.
- **Instead:** Combine ample breathing room with high-contrast type hierarchy, clear semantic actions, and robust dark/light theme support.
- **Copy check:** Every word must serve a clear purpose; remove filler and hype copy.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `minimalism`.
