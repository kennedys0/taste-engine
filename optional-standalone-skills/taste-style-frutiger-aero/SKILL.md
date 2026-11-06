---
name: taste-style-frutiger-aero
description: Apply Frutiger Aero design style to user-selected frontend and UI work. Use only when the user explicitly chooses this style. Provides typography, color, layout, components, interactions, motion, copy and quality gates. Do not impose on unrelated work.
license: MIT
metadata:
  version: "0.12.0"
---

Use this skill only after a user explicitly chooses frutiger-aero or a confirmed project configuration specifies it. For unexplained new UI requests, use a style selector such as taste-engine instead of deciding the user's taste here. Existing brand, accessibility and user overrides outrank all examples below. The following style guide is not permission to start UI coding before style selection.

# Style pack: Frutiger Aero

**ID:** `frutiger-aero`  
**Signature:** Optimistic mid-2000s technological vision featuring glossy surfaces, luminous aqua/ocean hues, nature-tech harmony, soft dimensional depth, specular highlights, and physical-looking interactive controls.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. A generic frosted SaaS card with a blue button **does not qualify as Frutiger Aero**.

## Good fit / trade-offs

- **Works well for:** Optimistic technology platforms, creative tools, productivity apps, media suites, environmental and educational platforms, personal portfolios, and tactile web applications.
- **Use with care for:** Austere legal registries, ultra-dense monochrome developer tools, or minimalist black-and-white editorial publications.
- **Reference directions:**
  - *Classic Aero (Default):* Bright aqua-inspired palette, glossy dimensional controls, nature and technology symbolism, smooth rounded surfaces, gentle environmental reflections, and balanced translucent panels.
  - *Aero Glass:* Frosted crystalline panels, layered transparency, controlled background blur, soft luminous borders, and clear visual depth rooted in optimistic Aero aesthetics rather than generic SaaS blur.
  - *Aero Tactile:* Physical material cues, tactile button surfaces, convincing highlights and shadows, material-inspired controls, and simulated surface depth preserving the best affordances of tangible computing.

## Frutiger Aero material fidelity gate — mandatory

**Before calling a Frutiger Aero page complete, the opening viewport must visibly read as an authentic, optimistic Aero composition.** If a user chose this style, a flat card with standard borders or generic dark glass is a **FAIL**, even if CSS classes contain `aero`.

A successful Frutiger Aero implementation demonstrates **all** of the following:

1. **Glossy Specular Surfaces & Horizon Sheens:** Surface planes feature dual-gradient curvature—a bright top-half specular highlight (`linear-gradient(180deg, rgba(255, 255, 255, 0.65) 0%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0) 51%, rgba(255, 255, 255, 0.2) 100%)`) that mimics curved acrylic or glass lens physics without obscuring foreground typography.
2. **Luminous Aqua & Nature-Tech Atmosphere:** An atmospheric backdrop featuring sky blue, fresh leaf green, and radiant ocean cyan gradients (`radial-gradient()` or smooth mesh light fields) that convey energy, openness, and forward-looking optimism.
3. **Dimensional Edge System:** Crisp 1px perimeter highlight borders (`border: 1px solid rgba(255, 255, 255, 0.6)`) paired with soft ambient volumetric drop shadows (`box-shadow: 0 12px 28px rgba(36, 126, 163, 0.18), inset 0 1px 0 rgba(255, 255, 255, 0.8)`).
4. **Physical Tactility & Spring Feedback:** Buttons and interactive controls feature convex dimensional depth, tactile press depression (`transform: translateY(1.5px)`), and gentle mechanical rebound.
5. **Anti-Clash Text Contrast (WCAG AA 4.5:1):** Crisp deep charcoal or navy typography (`#173F61` or `#243642`) over bright aqua and cloud surfaces in light mode; crisp porcelain white (`#F4FAFC`) over deep ocean slate in dark mode.
6. **Graceful Fallbacks:** Glass and translucent panels include solid background color fallbacks for platforms without `backdrop-filter` support.

**First-viewport test:** In a desktop screenshot, identify the glossy acrylic sheen, the vibrant aqua/leaf color balance, the dimensional button affordance, and the luminous nature-tech depth **without reading the page title**. If it appears flat, generic SaaS, or drab gray, strengthen the specular curvature and luminous palette.

## Explicit Frutiger Aero material exception — gloss and nature gradients are allowed

**Frutiger Aero-specific override:** The universal anti-slop caution against *decorative gradients, glossy highlights, or atmospheric backdrops* MUST NOT be interpreted as a ban on multi-stop sky/ocean gradients, acrylic horizon sheens, or translucent dock panels here. These are **material-enabling properties**, essential to communicating the optimistic mid-2000s technological vision.

- **Allowed material treatments:** Multi-stop aqua/sky/leaf linear and radial gradients, top-half horizon reflection sheens (`linear-gradient` with 50% split), convex tactile button pills, translucent frosted dock containers, and nature-inspired ambient illumination.
- **Harmonious color rules:** Restrict palettes to optimistic nature-tech harmonies (sky cyan, deep ocean blue, fresh leaf green, cloud white, and sunlit accents). Avoid discordant neon purple/pink cyber clashing.
- **Anti-slop boundary:** Every control must be interactive, accessible, and functional. Do not decorate screens with non-functional floating bubbles, fake animated fish, ornamental meters that display fabricated stats, or unreadable glossy text.
- **Anti-slop interpretation:** Evaluate Aero details by **material authenticity, optimistic clarity, and functional legibility**, not by counting gradient color-stops. Removing glossy horizon sheens to satisfy a generic flat heuristic is a **design regression**.

## Typography and typewriting

Use approachable, highly legible humanist or modern sans-serif typography that communicates clarity, optimism, and warmth:
- **Primary Typefaces:** Segoe UI, Frutiger, Trebuchet MS, Inter, or clean system sans-serif.
- **Display Headings:** Medium to bold humanist sans (600–700 weight) with relaxed tracking (`letter-spacing: -0.01em` to `0em`). Avoid abrasive uppercase monospace fonts for primary narrative headlines.
- **Body Text:** Clean, comfortable reading sizes (15–17px desktop, 14–15px mobile) with generous line-height (`1.5` to `1.6`) and strong contrast against backgrounds.
- **Technical & Microcopy:** Clean sans or tabular numerals (11–13px) for status indicators, metrics, and labels with `font-variant-numeric: tabular-nums`.

## Color direction

Frutiger Aero features an authentic, bright nature-tech color foundation supporting both light and dark modes:

### Light Mode (Sunny Sky & Aqua Lagoon — Default)
- **Canvas / Background:** Cloud white to pale sky gradient (`#F4FAFC` to `#E3F4FA`).
- **Surface Panels:** Translucent glossy acrylic (`rgba(255, 255, 255, 0.72)`) with 16px backdrop blur.
- **Primary Aqua:** Vibrant cyan-blue (`#48BFD3` to `#247EA3`).
- **Nature Accent (Leaf):** Fresh spring green (`#70B981` to `#4E9B60`).
- **Sky Tone:** Luminous atmospheric blue (`#C9EDF8`).
- **Deep Navy Ink:** High-contrast reading ink (`#173F61` or `#1A324B`).
- **Secondary Charcoal:** Muted slate ink (`#243642` or `#4A6070`).
- **Specular Border:** Crisp white highlight (`rgba(255, 255, 255, 0.85)`).

### Dark Mode (Deep Ocean & Bioluminescent Night)
- **Canvas / Background:** Deep oceanic midnight slate (`#0B1926` to `#12263A`).
- **Surface Panels:** Translucent deep ocean glass (`rgba(20, 42, 64, 0.68)`) with 18px backdrop blur.
- **Primary Aqua Glow:** Radiant cyan (`#56D2E8`).
- **Nature Accent (Bioluminescent Leaf):** Luminous mint green (`#82D898`).
- **Foreground Ink:** Crisp porcelain cloud (`#F4FAFC`).
- **Muted Ink:** Soft ocean mist (`#A4C3D8`).
- **Specular Border:** Luminous edge highlight (`rgba(255, 255, 255, 0.22)`).

### Theme Coupling & Anti-Collision Rule
When switching between light and dark Aero modes, foreground text, borders, and ambient light sources MUST switch in tandem. Foreground text must maintain at least 4.5:1 contrast against both the glossy surface and the atmospheric background behind it. Never leave dark text on dark ocean glass or white text on cloud white panels.

## Layout and geometry

- **Strict 1:1 circle geometry (anti-oval):** Any circular UI element (status indicator dots, avatars, circular buttons with `border-radius: 50%`) must enforce `aspect-ratio: 1 / 1; flex-shrink: 0;` to prevent deformation on narrow mobile viewports.
- **Responsive baseline:** Adhere to the [responsive baseline](../references/responsive-baseline.md) for 320px minimum viewport safety, fluid mobile typography defaults, and small-viewport navigation patterns.
- **Fluid Corner Radii:** Friendly, approachable curves—typically 12px–20px for content cards, 24px–32px for floating dock bars, and full pill (`9999px`) for primary buttons and status badges.
- **Dock & Island Navigation:** Floating navigation bars inspired by macOS Aqua docks and Windows Aero taskbars, featuring glossy acrylic backdrops, rounded corners, and elevated depth.
- **Modular Fluid Grids:** Clear content flow with generous whitespace that lets atmospheric light breathe through the interface without horizontal scroll blowout.

## Surfaces, depth, texture

Frutiger Aero uses physical, light-accurate surface formulas across three expressions:

- **1. Classic Aero Surface (Glossy Acrylic):**
  ```css
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.85) 0%, rgba(240, 248, 252, 0.65) 100%);
  backdrop-filter: blur(14px) saturate(130%);
  -webkit-backdrop-filter: blur(14px) saturate(130%);
  border: 1px solid rgba(255, 255, 255, 0.75);
  box-shadow: 0 8px 24px rgba(36, 126, 163, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.9);
  border-radius: 16px;
  ```

- **2. Aero Glass Surface (Crystalline Translucency):**
  ```css
  background: rgba(255, 255, 255, 0.45);
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  border: 1px solid rgba(255, 255, 255, 0.65);
  box-shadow: 0 12px 32px rgba(23, 63, 97, 0.12), inset 0 1px 1px rgba(255, 255, 255, 0.8);
  border-radius: 16px;
  ```

- **3. Aero Tactile Surface (Physical Dimensionality):**
  ```css
  background: linear-gradient(180deg, #FFFFFF 0%, #E8F4F8 100%);
  border: 1px solid #B8D8E6;
  box-shadow: 0 4px 12px rgba(23, 63, 97, 0.15),
              inset 0 1px 0 #FFFFFF,
              inset 0 -2px 0 rgba(36, 126, 163, 0.2);
  border-radius: 12px;
  ```

- **Glossy Push-Button:**
  ```css
  background: linear-gradient(180deg, #48BFD3 0%, #247EA3 100%);
  color: #FFFFFF;
  border: 1px solid rgba(255, 255, 255, 0.4);
  box-shadow: 0 4px 12px rgba(36, 126, 163, 0.35),
              inset 0 1px 0 rgba(255, 255, 255, 0.6),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
  border-radius: 9999px;
  ```

## Component anatomy and interaction

- **Vector Iconography (Anti-Slop):** Emojis are strictly banned as interface icons, buttons, or status badges. Use crisp vector icons (Lucide, Radix, Feather) with consistent stroke weight (1.5px–2px) inheriting `currentColor`.
- **Glossy Action Buttons:** Pill-shaped or rounded-rectangle controls with subtle top-half specular sheen, vibrant gradient fill, and crisp white typography with subtle drop-shadow for legibility.
- **Sunken Input Fields:** Inset text boxes with soft inner shadow (`box-shadow: inset 0 2px 4px rgba(23, 63, 97, 0.12)`), clean focus rings (`:focus-visible` with 2px cyan glow), and high text contrast.
- **Translucent Segmented Controls:** Pill tabs housed within an inset well, where the active pill slides with a glossy specular highlight.
- **Dimensional Stat Cards:** Acrylic cards displaying bold tabular numbers, nature/tech trend indicators, and soft specular borders.
- **Accessible Accordions & Dialogs:** Smoothly animated disclosures with clean borders, clear keyboard focus, and solid fallbacks.

## Motion

Frutiger Aero motion feels buoyant, physical, and restrained:
- **Button Press Feedback:** Quick tactile compression (`transform: translateY(1.5px) scale(0.99)`) with 120ms ease-out timing and immediate specular shadow contraction.
- **Dock & Island Hover:** Subtle upward float (`transform: translateY(-2px)`) with mild shadow expansion (`box-shadow` spread +2px) over 160ms.
- **Panel Entrances:** Gentle fade and 4px vertical rise over 180ms without distracting bounce or screen shake.
- **Reduced Motion:** When `@media (prefers-reduced-motion: reduce)` is active, set duration to 0ms and disable all physical transforms while preserving immediate state changes.

## Hero composition (full first viewport)

For a public-facing landing page or portfolio, apply [Full-screen Hero Contract](../references/hero-layout.md):
- **First Viewport Equation:** `min-height: 100svh` (with `100vh` fallback). Subtract normal-flow header height or let hero span under an overlay acrylic header; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win.
- **Nature-Tech Backdrop:** Atmospheric sky-blue to deep-aqua gradient with subtle soft luminous ambient light fields that make foreground acrylic panels visibly refract.
- **Hero Island Card:** A prominent translucent glossy acrylic showcase panel housing the primary headline, product value thesis, and dual call-to-action buttons.
- **Live Command Pill:** Single-line command box with `$ npm install @kennedys0/taste-engine` and copy button aligned horizontally with `display: inline-flex; align-items: center;`.
- **Responsive Stacking:** On viewports below 768px, gracefully stack elements with comfortable touch targets (44px+) and zero text overflow.

## UI writing and microcopy

- **Tone:** Clear, optimistic, human, and encouraging. Focus on progress, creative capability, and genuine utility.
- **Anti-Slop Voice:** Ground claims in concrete product features. Reject hollow buzzwords (*"synergistic next-gen paradigm"*), fake metric counters, and invented user testimonials.
- **Button Labels:** Direct, action-oriented verbs (*"Launch Workspace"*, *"Explore Showcase"*, *"Download Preset"*).
- **Empty & Loading States:** Honest, friendly explanations with clear recovery actions (*"No connected audio feeds. Click 'Connect Input' above to begin."*).

## Style-specific quality gate

Before marking a Frutiger Aero page or component complete, verify every gate:

1. **Gate 1 (Gloss & Specular Quality):** Do interactive buttons and cards feature convincing specular highlights and dimensional curvature rather than flat solid color?
2. **Gate 2 (Aqua & Nature Balance):** Is the palette grounded in vibrant aqua, ocean blue, and fresh leaf green rather than generic gray SaaS or dark neon cyberpunk?
3. **Gate 3 (Contrast & Readability):** Does every text element exceed WCAG AA 4.5:1 contrast against both the panel surface and the backdrop behind it?
4. **Gate 4 (Tactile Spring):** Do buttons depress on click (`:active`) and rebound smoothly with tactile physical travel?
5. **Gate 5 (320px Mobile Safety):** Does the entire layout adapt down to 320px width without horizontal scrollbars, clipped text, or deformed circular icons?
6. **Gate 6 (Fallbacks):** Does the UI remain fully usable when `backdrop-filter` is unsupported or disabled via `prefers-reduced-transparency`?

## Universal anti-slop gate (self-contained)

Every element must earn its place. **Content before decoration. Do not decorate uncertainty.** Do not invent balances, metrics, testimonials, users, logos, approval, verified/live/online status, fake activity, or success confirmations; use honest empty/loading/error states instead. Demo data is acceptable only if requested and visibly labeled.

Do not add decorative **card-inside-card** layers: a nested surface must represent a distinct interaction or information boundary. Avoid auto-generated 3-feature grids, 4-stat dashboards, fake hero claims, purposeless charts, badge/chip/icon spam, unrelated decorative art, and random loops merely to fill the viewport. Prefer grouping with typography, spacing, alignment and dividers. Equal peers need intentional visual balance.

**Anti-slop copywriting & zero emojis:** no generic "Unlock your potential", "Experience the future", "Supercharge your workflow", "seamless" claims, or translated equivalents. Headings must communicate actual content, CTAs must name the action, and empty/error/success text must describe real states and next steps. Avoid fake urgency, made-up counts, vague AI hype, and inaccessible all-caps walls. Emojis are strictly forbidden as UI icons, button prefixes, or badges across all styles; interface elements must exclusively use clean vector SVGs from Lucide, Radix, Feather, or Heroicons with currentColor inheritance. Adapt the wording to this style and the user's language without changing the truth.

**Theme and mode contrast integrity:** When a user requests dark mode or light mode (or builds a theme switcher), background and foreground colors MUST flip in synchronized pairs across all surfaces, text, borders, inputs, and semantic badges. Never leave black text on dark background, white text on white background, or unreadable low-contrast status pills. All states must meet WCAG AA contrast (minimum 4.5:1 for body/normal text, 3:1 for large headlines and interactive boundaries).

**Responsive 320px baseline and fluid typography:** compose mobile deliberately down to 320px minimum viewport width with zero horizontal blowout. Scale typography down smoothly while respecting readability minimums (body >= 1rem / 16px, secondary >= 0.875rem, code >= 0.8125rem). In top navigation bars, collapse navigation behind an accessible hamburger menu or disclosure with comfortable tap targets on mobile (< 768px). Circular geometry must enforce aspect-ratio: 1 / 1; flex-shrink: 0;. Static by default; use motion for meaningful interactions, respect reduced-motion preferences, avoid bounce/floating/pulsing decoration without a real state.

**Critical/High findings block completion:** fabricated status/data, broken actions, inaccessible/clipped controls, misleading copy, theme contrast collisions or significant mobile failure must be fixed. Report what was actually verified; do not claim tests that did not run.

**Not an aesthetics veto:** expressive colors, shadows, gradients, card layouts or decorative treatments are legitimate when they are intentional parts of the selected aesthetic and pass usability checks. Do not silently force minimalism.

## Anti-slop: style-specific

- **FAIL:** A flat dark card with `#000000` background and a single blue gradient button claiming to be Frutiger Aero.
- **FAIL:** Generic SaaS dashboard with gray cards and arbitrary blurry circles in the background that filter nothing.
- **FAIL:** Fabricated weather widgets, fake live audio visualizers, or non-functional decorative dials invented solely to fill empty layout space.
- **FAIL:** Rainbow text gradients (`-webkit-background-clip: text`) applied to body text or headings.
- **FAIL:** Emojis used as UI button icons, bullet points, or status badges.
- **FAIL:** Unreadable white text placed over semi-transparent white frosted glass.
- **PASS:** Luminous nature-tech aqua palette, glossy acrylic horizon highlights, honest functional controls, clear tactile feedback, and robust mobile responsiveness.

## Optional Anime.js v4 recipe

For projects that justify external coordinated motion, use Anime.js v4 with lifecycle cleanup and reduced-motion compliance:

```javascript
import { animate, createScope } from 'animejs';

// Respect user motion preferences
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

export function animateAeroPress(element) {
  if (prefersReduced) return;
  
  animate(element, {
    scale: [1, 0.98, 1],
    translateY: [0, 1.5, 0],
    duration: 160,
    ease: 'outQuad',
  });
}
```

## Quality tiers (standalone)

**FLOOR (must pass):** correct and truthful data/state, working critical actions, accessible focus/labels/contrast, usable responsive UI and reduced-motion support. **REFLEX (explain or fix):** generic feature grids, purposeless nested cards, decorative labels/icons, default marketing hype or constant motion. A reflex is allowed when it clearly expresses the chosen style and serves the task. **FINISH:** refinement of alignment, typography rhythm and edge cases. Never treat the selected style itself as a violation. Do not claim browser testing unless actually performed.
