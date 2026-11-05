---
name: taste-style-minimalism
description: Apply Minimalism design style to user-selected frontend and UI work. Use only when the user explicitly chooses this style. Provides typography, color, layout, components, interactions, motion, copy and quality gates. Do not impose on unrelated work.
license: MIT
metadata:
  version: "0.10.11"
---

Use this skill only after a user explicitly chooses  or a confirmed project configuration specifies it. For unexplained new UI requests, use a style selector such as  instead of deciding the user's taste here. Existing brand, accessibility and user overrides outrank all examples below. The following style guide is not permission to start UI coding before style selection.

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
2. **Mathematically Calibrated Typographic Scale:** Clear contrast between display titles (32px–44px, weight 600–700), section anchors (18px–22px, weight 600), body text (15px–16px, weight 400, line-height 1.6), and metadata (12px–13px, weight 500 tabular figures).
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

Pure, neutral UI sans: Inter, Source Sans 3, SF Pro, or system sans paired with JetBrains Mono for code and tabular figures. Headlines: 32–44 px (weight 600–700, `letter-spacing: -0.025em`); section titles: 18–22 px (weight 600); body: 15–16 px (weight 400, line-height 1.6); captions/metadata: 12–13 px (weight 500 monospace, tabular numbers). Calm, scannable type scale with golden-ratio line heights.

## Color direction

- **Light Mode (Clean Studio Light):**
  - **Canvas Base:** Soft paper white (`#FAFAF9` or `#FFFFFF`).
  - **Surface Elevated:** Pure white (`#FFFFFF`).
  - **Typography / Ink:** Deep slate black (`#18181B`).
  - **Secondary Text:** Balanced neutral slate (`#52525B` — passes 4.5:1 WCAG AA).
  - **Hairline Divider:** Translucent gray (`rgba(0, 0, 0, 0.08)` or `#E4E4E7`).
- **Dark Mode (Disciplined Studio Dark):**
  - **Canvas Base:** Muted obsidian canvas (`#121214`).
  - **Surface Elevated:** Dense slate obsidian (`#18181B` / `#1F1F23`).
  - **Typography / Ink:** Crisp porcelain (`#F4F4F5`).
  - **Secondary Text:** Balanced slate (`#A1A1AA` — passes 4.5:1 WCAG AA).
  - **Hairline Divider:** Translucent white (`rgba(255, 255, 255, 0.09)` or `#27272A`).
- **Brand Accent:** Singular functional accent (e.g. high-contrast ink anchor `#18181B` light / `#F4F4F5` dark, or calibrated Cobalt `#2563EB` light / `#3B82F6` dark).
- **Theme Coupling Rule:** Canvas, typography, secondary text, and dividers MUST flip synchronously. When user requests dark mode, text must turn light (`#F4F4F5`); when light mode, text must turn dark (`#18181B`). Never leave dark text on dark canvas.

## Layout and geometry

- **Strict 1:1 circle geometry (anti-oval):** Any circular UI element (status indicator dots, avatars, circular buttons with `border-radius: 50%`) must enforce `aspect-ratio: 1 / 1; flex-shrink: 0;` to prevent them from squishing into distorted ovals when viewport shrinks down to 320px.
- **Responsive baseline:** Adhere to the [responsive baseline](../references/responsive-baseline.md) for 320px minimum viewport safety, fluid mobile typography defaults, and small-viewport navigation patterns.
Consistent 4px/8px spacing grid; gentle, unified corner radii (`6px–8px`); subtle hairline borders where structural separation is necessary. Negative space groups related information naturally.

## Surfaces, depth, texture

Surfaces are quiet, flat, and matte. Minimal or zero box-shadows (`0 1px 3px rgba(0, 0, 0, 0.05)` max for elevated dropdowns). Depth is communicated via contrast, spacing, and typographic weight.

## Component anatomy and interaction

- **Iconography — zero emojis:** Emojis are strictly banned as interface icons, status indicators, or button prefixes across all UI elements. Use Lucide or clean vector SVGs (16px–24px) with consistent stroke weight (1.5px–2px) and currentColor.
- **Hairline Navigation Header:** Fixed or sticky top bar with subtle hairline dividing stroke (`1px solid rgba(0, 0, 0, 0.08)`), brand mark, horizontal link row on desktop, and a dedicated high-contrast installation CTA. On mobile viewports (< 768px), links collapse into an accessible hamburger button with 44px+ tap target drawer.
- **Primary Action (CTA):** Solid dark pill or rounded rectangle (`border-radius: 6px`) with high contrast fill, distinct hover state, and zero visual blur noise.
- **Secondary Action:** Unadorned text link or subtle outline button with hairline border (`1px solid var(--pow-border)`).
- **Restrained Form Input:** Clean input field with visible hairline border, clear placeholder, and high-contrast focus ring (`outline: 2px solid var(--pow-accent); outline-offset: 2px;`).
- **Hairline Data Matrix (Anti-Card-Clutter):** Dense, scannable data list grouped through proximity and 1px hairline dividers without nested card boxes. Includes tabular numbers (`font-variant-numeric: tabular-nums;`), semantic status pills (`Active`, `Verified`), and compact action buttons.
- **Minimalist Toggle Switch:** Pill-shaped track with smooth sliding circular knob enforcing `aspect-ratio: 1 / 1; flex-shrink: 0;` (never deforms into an oval).
- **Segmented Control Tabs:** Flush inline segmented pill bar (`border-radius: 4px`) for density, scale, or view switching.
- **Hairline Accordion:** Flush collapsible section headers with Lucide `ChevronDown` SVG rotating 180° on toggle, revealing clean body copy.
- **Mathematical 4-Metric Grid:** Box grid separated by 1px hairline rules without individual floating card shadows.

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

| Token | Light mode default | Dark mode default | Architectural Role |
| --- | --- | --- | --- |
| `--taste-mini-bg` | `#fafaf9` | `#121214` | Base canvas backdrop base |
| `--taste-mini-surface` | `#ffffff` | `#18181b` | Elevated surface / card fill |
| `--taste-mini-ink` | `#18181b` | `#f4f4f5` | Primary typography & vector icons (WCAG AAA) |
| `--taste-mini-muted` | `#52525b` | `#a1a1aa` | Secondary metadata text (4.5:1+) |
| `--taste-mini-border` | `1px solid rgba(0, 0, 0, 0.08)` | `1px solid rgba(255, 255, 255, 0.09)` | Subtle structural hairline dividing rule |
| `--taste-mini-accent` | `#18181b` | `#f4f4f5` | Primary functional action fill |
| `--taste-mini-radius` | `6px` | `6px` | Gentle unified corner radius |
| `--taste-mini-font-sans` | `Inter, system-ui, sans-serif` | `Inter, system-ui, sans-serif` | Pure unembellished typography stack |
| `--taste-mini-font-mono` | `JetBrains Mono, monospace` | `JetBrains Mono, monospace` | Tabular metadata and monospace code font |
| `--taste-mini-space-unit` | `4px / 8px` | `4px / 8px` | Mathematical grid rhythm base |
| `--taste-mini-motion-duration` | `140ms` | `140ms` | Subtle ease-out micro-transition timing |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-mini-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Compose the first viewport around a crystal-clear headline, one primary action, and generous, intentional white space. Do not invent filler cards, fake testimonials, or decorative badges to clutter the canvas. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.

## Style-specific quality gate

- **Do:** ensure circular elements (status dots, icon badges, round buttons) maintain strict 1:1 aspect ratio with `aspect-ratio: 1 / 1; flex-shrink: 0;` without squishing into ovals; verify responsive fidelity down to 320px viewport with zero horizontal scroll blowout; ensure mobile typography scales down proportionally to prevent bloated UI; verify header navigation collapses into an accessible hamburger menu on narrow screens (< 768px); verify high text contrast (WCAG AA 4.5:1) in both light and dark modes; ensure interactive controls have clear hit targets and visible focus indicators; group content through spacing and hairline dividers; verify that mode switching flips canvas, ink, muted text, and borders in paired synchronization.
- **Don't:** never let circular elements deform into ovals under flexbox compression; never force crowded horizontal navigation links on mobile headers (always use a hamburger menu); avoid bloated mobile font sizes that crowd small screens; never use emojis as UI icons or button prefixes (always use Lucide or clean vector SVGs with currentColor); do not treat washed-out gray text or missing labels as minimalism; avoid hiding core actions behind obscure icons; do not create vast empty voids that confuse navigation; avoid dark/light theme collisions where text remains dark on dark canvas.
- Confirm desktop and mobile consistency; visible keyboard focus (`:focus-visible`); loading, empty, disabled, error and success states; reduced-motion behavior (`prefers-reduced-motion`).
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.

## Universal anti-slop gate (self-contained)

Every element must earn its place. **Content before decoration. Do not decorate uncertainty.** Do not invent balances, metrics, testimonials, users, logos, approval, verified/live/online status, fake activity, or success confirmations; use honest empty/loading/error states instead. Demo data is acceptable only if requested and visibly labeled.

Do not add decorative **card-inside-card** layers: a nested surface must represent a distinct interaction or information boundary. Avoid auto-generated 3-feature grids, 4-stat dashboards, fake hero claims, purposeless charts, badge/chip/icon spam, unrelated decorative art, and random loops merely to fill the viewport. Prefer grouping with typography, spacing, alignment and dividers. Equal peers need intentional visual balance.

**Anti-slop copywriting & zero emojis:** no generic "Unlock your potential", "Experience the future", "Supercharge your workflow", "seamless" claims, or translated equivalents. Headings must communicate actual content, CTAs must name the action, and empty/error/success text must describe real states and next steps. Avoid fake urgency, made-up counts, vague AI hype, and inaccessible all-caps walls. Emojis are strictly forbidden as UI icons, button prefixes, or badges across all styles; interface elements must exclusively use clean vector SVGs from Lucide, Radix, Feather, or Heroicons with currentColor inheritance. Adapt the wording to this style and the user's language without changing the truth.

**Theme and mode contrast integrity:** When a user requests dark mode or light mode (or builds a theme switcher), background and foreground colors MUST flip in synchronized pairs across all surfaces, text, borders, inputs, and semantic badges. Never leave black text on dark background, white text on white background, or unreadable low-contrast status pills. All states must meet WCAG AA contrast (minimum 4.5:1 for body/normal text, 3:1 for large headlines and interactive boundaries).

**Responsive 320px baseline and fluid typography:** compose mobile deliberately down to 320px minimum viewport width with zero horizontal blowout. Scale typography down smoothly while respecting readability minimums (body >= 1rem / 16px, secondary >= 0.875rem, code >= 0.8125rem). In top navigation bars, collapse navigation behind an accessible hamburger menu or disclosure with comfortable tap targets on mobile (< 768px). Circular geometry must enforce aspect-ratio: 1 / 1; flex-shrink: 0;. Static by default; use motion for meaningful interactions, respect reduced-motion preferences, avoid bounce/floating/pulsing decoration without a real state.

**Critical/High findings block completion:** fabricated status/data, broken actions, inaccessible/clipped controls, misleading copy, theme contrast collisions or significant mobile failure must be fixed. Report what was actually verified; do not claim tests that did not run.

**Not an aesthetics veto:** expressive colors, shadows, gradients, card layouts or decorative treatments are legitimate when they are intentional parts of the selected aesthetic and pass usability checks. Do not silently force minimalism.

## Anti-slop: style-specific

**Clarity through restraint, not lazy emptiness.**

- **Reject:** emojis used as UI icons or button stickers, faint low-contrast gray text, unlabelled icon-only controls, ghost buttons that look disabled, empty viewports that communicate zero product information, and theme collisions where text is unreadable against the canvas.
- **Instead:** Combine ample breathing room with high-contrast type hierarchy, clear semantic actions, and robust dark/light theme support.
- **Copy check:** Every word must serve a clear purpose; remove filler and hype copy.
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `minimalism`.

## Quality tiers (standalone)

**FLOOR (must pass):** correct and truthful data/state, working critical actions, accessible focus/labels/contrast, usable responsive UI and reduced-motion support. **REFLEX (explain or fix):** generic feature grids, purposeless nested cards, decorative labels/icons, default marketing hype or constant motion. A reflex is allowed when it clearly expresses the chosen style and serves the task. **FINISH:** refinement of alignment, typography rhythm and edge cases. Never treat the selected style itself as a violation. Do not claim browser testing unless actually performed.
