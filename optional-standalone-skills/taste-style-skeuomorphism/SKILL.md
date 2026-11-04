---
name: taste-style-skeuomorphism
description: Apply Skeuomorphism design style to user-selected frontend and UI work. Use only when the user explicitly chooses this style. Provides typography, color, layout, components, interactions, motion, copy and quality gates. Do not impose on unrelated work.
license: MIT
metadata:
  version: "0.10.6"
---

Use this skill only after a user explicitly chooses  or a confirmed project configuration specifies it. For unexplained new UI requests, use a style selector such as  instead of deciding the user's taste here. Existing brand, accessibility and user overrides outrank all examples below. The following style guide is not permission to start UI coding before style selection.

# Style pack: Skeuomorphism

**ID:** `skeuomorphism`  
**Signature:** Digital controls borrow tangible affordances from physical objects, industrial machinery, and analog hardware.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies. A flat card with a subtle gradient **does not qualify as Skeuomorphism**.

## Good fit / trade-offs

- **Works well for:** Music production and synthesizer software, audio gear tools, specialized simulators, tactile dashboard widgets, creative digital instruments, and playful tactile experiences.
- **Be careful with:** Dense transactional data tables or mobile enterprise forms where ornate physical hardware textures create visual clutter.
- **Reference directions:**
  - *Tactile Molded Surfaces / Dual-Shadow Hardware (as in mobile device widgets and hardware control consoles):* Seamless molded matte panels with dual opposite light physics: extruded controls with soft top-left white glow (-6px -6px 16px rgba(255, 255, 255, 0.95)) and bottom-right soft shadow (6px 6px 16px rgba(163, 177, 198, 0.6)), sunken wells with top-left inner shadow (inset 5px 5px 12px rgba(163, 177, 198, 0.65)) and bottom-right inner highlight (inset -5px -5px 12px rgba(255, 255, 255, 0.95)), vertical pill faders with sunken tracks, and active buttons sinking directly into the surface.
  - *Brushed Industrial Aluminum / Studio Hardware:* Machined silver or gunmetal chassis with radial metallic reflections, knurled dials, recessed indicator wells, and crisp mechanical toggle switches.
  - *Precision Matte Instrument:* Deep graphite / matte composite base with engraved white readout typography, LED jewel status indicators, and physical rocker switches.

## Skeuomorphic material fidelity gate — mandatory

**Before calling a skeuomorphic page complete, the opening viewport must visibly read as a physical, touchable instrument or hardware interface.** If a user chose this style, a flat card with standard rounded corners and a single gradient is a **FAIL**, even if CSS classes contain `skeuo`.

A successful skeuomorphic implementation demonstrates **all** of the following:

1. **Light-Model Direction & Specular Highlights:** Surfaces adhere to a single consistent light source (typically top-down): upper edges catch a crisp 1px specular light highlight (`box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.35)`), while bottom edges cast physical drop shadows.
2. **Multi-Stop Reflective Material Surfaces:** Knobs, faceplates, and rocker switches use multi-stop linear or radial gradients simulating brushed aluminum, matte plastic, or anodized metal. Flat single-color fills fail.
3. **Engraved or Recessed Polarity:** Text displays, sliders, and meter wells are visually sunken into the chassis using deep inset shadows (`box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.6)`), clearly distinguishing controls that move from containers that house them.
4. **Mechanical Travel on Interaction:** Buttons physically depress into the chassis on click (`transform: translateY(1.5px); box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.7);`), mimicking real spring-loaded switch mechanisms.
5. **Legible Analog Affordances:** Physical dials and sliders include clear digital readouts or labeled numeric tick marks, ensuring keyboard accessibility and exact data entry.

**First-viewport test:** In a desktop screenshot, identify the physical chassis, the specular bevel highlights, the recessed wells, and the tactile hardware controls **without reading the page title**. If it appears purely digital and flat, strengthen the gradient reflections and bevel highlights.

## Explicit skeuomorphic material exception — hardware reflections are allowed

**Skeuomorphism-specific override:** The universal anti-slop caution against *decorative gradients, textures, or shadows* MUST NOT be interpreted as a ban on multi-stop material gradients, metallic reflections, beveled rims, or physical travel here. These are **material-enabling properties**, essential to communicating mechanical affordance.

- **Allowed material treatments:** Multi-stop metallic linear/radial gradients, 1px highlight bevels, recessed well channels, knurled knob borders, and jewel LED status lights.
- **Anti-slop boundary:** Every mechanical metaphor must correspond to a real, working action. Do not decorate screens with fake screws, non-turning ornamental knobs, or static meters that display fabricated measurements.
- **Anti-slop interpretation:** Evaluate skeuomorphic details by **tactile affordance, functional utility, and legibility**, not by counting gradient color-stops. Removing physical bevels to satisfy a generic flat heuristic is a **design regression**.

## Typography and typewriting

Utilitarian technical sans or display mono: IBM Plex Sans, DIN Next, Roboto Mono, or system sans. Control labels: 11–13px uppercase with tracking (`letter-spacing: 0.08em`); display meters: high-contrast LCD/LED mono (16–24px). High contrast against dark faceplates (at least 4.5:1).

## Color direction

- **Dark Mode (Anodized Gunmetal Dark Chassis):**
  - **Chassis Base:** Machined slate / anodized gunmetal gradient (`linear-gradient(180deg, #323741 0%, #262A32 100%)`).
  - **Surface Highlights:** Specular white hairline (`rgba(255, 255, 255, 0.40)`).
  - **Recessed Inset Wells:** Deep cavity black (`#141619` to `#181A1E`).
  - **Control Labels:** Crisp engraved white/silver typography (`#F3F4F6`).
- **Light Mode (Brushed Aluminum / Silver Chassis):**
  - **Chassis Base:** Machined aluminum / silver gradient (`linear-gradient(180deg, #F5F7FA 0%, #E4E7EB 100%)`).
  - **Surface Highlights:** Specular white hairline (`rgba(255, 255, 255, 0.85)`).
  - **Recessed Inset Wells:** Soft recessed slate cavity (`#D1D5DB` with inset shadow).
  - **Control Labels:** Deep engraved charcoal ink (`#1F2937` or `#111827`).
- **Physical Accents:** Signal amber (`#FFAE00`), aviation green (`#10B981`), or studio cobalt (`#2563EB`).
- **LED Indicators:** Crisp jewel colors with distinct active glow vs dark inactive state.
- **Theme Coupling & Anti-Collision Rule:** In light skeuomorphic chassis mode, engraved labels and control text MUST flip to deep charcoal (`#1F2937`). Leaving white labels on a brushed silver/aluminum chassis produces invisible text and is strictly prohibited.

## Layout and geometry

- **Strict 1:1 circle geometry (anti-oval):** Any circular UI element (status indicator dots, avatars, circular buttons with `border-radius: 50%`) must enforce `aspect-ratio: 1 / 1; flex-shrink: 0;` to prevent them from squishing into distorted ovals when viewport shrinks down to 320px.
- **Responsive 320px baseline & fluid typography:** All layouts must scale gracefully down to 320px width without horizontal blowout. Typography and paddings must scale down proportionally (hero titles clamp to 1.35rem–1.65rem, section headings to 1.2rem–1.45rem, code to 0.725rem–0.785rem) to prevent bloated interfaces ("UI bengkak"). Top navigation headers must collapse links behind an accessible hamburger menu on narrow mobile screens (< 768px) rather than crowding the header.
Component shapes strictly map to their physical metaphors: rotary dials, tactile push-buttons, rocker switches, and segmented meters. 4–12px corner radii on panels; circular radii for knobs. Avoid applying hardware skins to generic text paragraphs.

## Surfaces, depth, texture

- **Chassis Panel:** Multi-stop linear gradient (`linear-gradient(180deg, #323741 0%, #262A32 100%)`) with 1px top highlight and bottom drop shadow.
- **Physical Push-Button:** Beveled rim with top highlight, radial button surface, and crisp active depression.
- **Sunken Well / Display:** `box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.65), 0 1px 0 rgba(255, 255, 255, 0.15);`
- **Nested Sub-Panels / Recessed Instrument Wells (Card-in-Card):** Permissible when encapsulating physical hardware sub-chassis, modular rack-mount bays, or recessed display wells sunken into the main chassis faceplate (e.g. `background: var(--taste-skeuo-well-bg, #141619); box-shadow: var(--taste-skeuo-well-inset); border: var(--taste-skeuo-chassis-border);`). Mindless decorative box-in-box nesting without mechanical or enclosure logic remains disallowed.

## Component anatomy and interaction

- **Iconography — zero emojis:** Emojis are strictly banned as interface icons, status indicators, or button prefixes across all UI elements. Use Lucide or clean vector SVGs (16px–24px) with consistent stroke weight (1.5px–2px) and currentColor.
- **Tactile Push-Button:** Machined aluminum finish, white engraved label, mechanical spring-back on release.
- **Rocker / Toggle Switch:** Dual-state physical toggle with visible cast shadow on active side.
- **Recessed LCD / Data Readout:** Sunken screen with monospace value, subtle raster grid, and high contrast.
- **Rotary Dial / Slider:** Tactile position indicator with ARIA slider semantics and keyboard arrow-key support.
- **LED Status Light:** Small circular jewel lens with radiant glow when active (`box-shadow: 0 0 8px currentColor`).

## Motion

140–200 ms mechanical response. Direct 1–2px physical depression on click. No bouncy cartoon overshoot; movement must feel weighted and damped.

## Optional Anime.js v4 recipe

- **Motion decision:** Damped spring or linear mechanical depression on press; precise rotation for dials.
- **Starting duration:** 160ms (0 = immediate); adjust to task and user preference.
- **Avoid:** perpetual oscillation, unprompted needle shaking, floating elements.
- **Dependency:** CSS/native by default. Use Anime.js v4 only if the requested interaction justifies it. Follow Taste Engine `references/motion-engine.md` when available; standalone skill follows the reduced-motion and no-decorative-loop principles above.

## UI writing and microcopy

Technical, precise, and concise. Examples: “Master Output”, “Bypass”, “Channel 01”, “Gain: +3.5 dB”. Avoid chatty marketing fluff on instrument panels.

## Starter tokens (suggestions, not a complete theme)

| Token | Dark chassis default | Light chassis default |
| --- | --- | --- |
| `--taste-skeuo-chassis-bg` | `linear-gradient(180deg, #323741 0%, #262a32 100%)` | `linear-gradient(180deg, #f5f7fa 0%, #e4e7eb 100%)` |
| `--taste-skeuo-chassis-border` | `1px solid rgba(0, 0, 0, 0.8)` | `1px solid rgba(0, 0, 0, 0.15)` |
| `--taste-skeuo-chassis-highlight` | `inset 0 1px 0 rgba(255, 255, 255, 0.25)` | `inset 0 1px 0 rgba(255, 255, 255, 0.90)` |
| `--taste-skeuo-chassis-shadow` | `0 2px 4px rgba(0, 0, 0, 0.7), 0 8px 24px rgba(0, 0, 0, 0.65), 0 24px 56px -8px rgba(0, 0, 0, 0.8)` | `0 1px 2px rgba(0, 0, 0, 0.08), 0 4px 12px rgba(0, 0, 0, 0.10), 0 16px 36px -6px rgba(0, 0, 0, 0.16)` |
| `--taste-skeuo-well-bg` | `#141619` | `#d1d5db` |
| `--taste-skeuo-text` | `#f3f4f6` | `#1f2937` |
| `--taste-skeuo-text-muted` | `#9ca3af` | `#4b5563` |
| `--taste-skeuo-btn-bg` | `linear-gradient(180deg, #3c424f 0%, #2a2e37 100%)` | `linear-gradient(180deg, #ffffff 0%, #e2e8f0 100%)` |
| `--taste-skeuo-btn-bevel` | `inset 0 1.5px 0 rgba(255, 255, 255, 0.42), inset 0 -1.5px 0 rgba(0, 0, 0, 0.75)` | `inset 0 1.5px 0 rgba(255, 255, 255, 1), inset 0 -1.5px 0 rgba(0, 0, 0, 0.28)` |
| `--taste-skeuo-btn-shadow` | `0 1px 2px rgba(0, 0, 0, 0.8), 0 4px 9px rgba(0, 0, 0, 0.6), 0 10px 22px rgba(0, 0, 0, 0.45)` | `0 1px 2px rgba(0, 0, 0, 0.16), 0 3px 7px rgba(0, 0, 0, 0.12), 0 8px 18px rgba(0, 0, 0, 0.08)` |
| `--taste-skeuo-well-inset` | `inset 0 5px 14px rgba(0, 0, 0, 0.92), inset 0 2px 4px rgba(0, 0, 0, 0.98), 0 1px 0 rgba(255, 255, 255, 0.16)` | `inset 0 4px 10px rgba(0, 0, 0, 0.24), inset 0 1.5px 3px rgba(0, 0, 0, 0.35), 0 1.5px 0 rgba(255, 255, 255, 0.95)` |
| `--taste-skeuo-led-active` | `#10b981` | `#059669` |
| `--taste-skeuo-led-glow` | `0 0 10px rgba(16, 185, 129, 0.75)` | `0 0 8px rgba(5, 150, 105, 0.45)` |
| `--taste-skeuo-radius-panel` | `12px` | `12px` |
| `--taste-skeuo-font-mono` | `IBM Plex Mono, ui-monospace, monospace` | `IBM Plex Mono, ui-monospace, monospace` |
| `--taste-skeuo-motion-duration` | `160ms` | `160ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-skeuo-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Treat the first viewport as an authentic master control console or signature instrument faceplate; provide working controls and an unmistakable primary CTA. Do not litter the canvas with non-functional screws, decorative cables, or disconnected analog meters. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** ensure circular elements (status dots, icon badges, round buttons) maintain strict 1:1 aspect ratio with `aspect-ratio: 1 / 1; flex-shrink: 0;` without squishing into ovals; verify responsive fidelity down to 320px viewport with zero horizontal scroll blowout; ensure mobile typography scales down proportionally to prevent bloated UI; verify header navigation collapses into an accessible hamburger menu on narrow screens (< 768px); Verify consistent top-down specular highlight across all controls; ensure mechanical press states depress smoothly; provide numerical readouts alongside dials/sliders; test keyboard focus; verify dark/light mode switching so chassis, bevel highlights, wells, and label typography adapt in coupled pairs.
- **Don't:** never let circular elements deform into ovals under flexbox compression; never force crowded horizontal navigation links on mobile headers (always use a hamburger menu); avoid bloated mobile font sizes that crowd small screens; never use emojis as UI icons or button prefixes (always use Lucide or clean vector SVGs with currentColor); Do not treat a plain dark theme as skeuomorphic; do not add non-functional decorative screws or fake analog needles that don't connect to real data; avoid unreadable low-contrast text on dark faceplates or white labels on silver light faceplates.
- Confirm desktop and mobile consistency; visible keyboard focus (`:focus-visible`); loading, empty, disabled, error and success states; reduced-motion behavior (`prefers-reduced-motion`).
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.

## Universal anti-slop gate (self-contained)

Every element must earn its place. **Content before decoration. Do not decorate uncertainty.** Do not invent balances, metrics, testimonials, users, logos, approval, verified/live/online status, fake activity, or success confirmations; use honest empty/loading/error states instead. Demo data is acceptable only if requested and visibly labeled.

Do not add decorative **card-inside-card** layers: a nested surface must represent a distinct interaction or information boundary. Avoid auto-generated 3-feature grids, 4-stat dashboards, fake hero claims, purposeless charts, badge/chip/icon spam, unrelated decorative art, and random loops merely to fill the viewport. Prefer grouping with typography, spacing, alignment and dividers. Equal peers need intentional visual balance.

**Anti-slop copywriting & zero emojis:** no generic "Unlock your potential", "Experience the future", "Supercharge your workflow", "seamless" claims, or translated equivalents. Headings must communicate actual content, CTAs must name the action, and empty/error/success text must describe real states and next steps. Avoid fake urgency, made-up counts, vague AI hype, and inaccessible all-caps walls. Emojis are strictly forbidden as UI icons, button prefixes, or badges across all styles; interface elements must exclusively use clean vector SVGs from Lucide, Radix, Feather, or Heroicons with currentColor inheritance. Adapt the wording to this style and the user's language without changing the truth.

**Theme and mode contrast integrity:** When a user requests dark mode or light mode (or builds a theme switcher), background and foreground colors MUST flip in synchronized pairs across all surfaces, text, borders, inputs, and semantic badges. Never leave black text on dark background, white text on white background, or unreadable low-contrast status pills. All states must meet WCAG AA contrast (minimum 4.5:1 for body/normal text, 3:1 for large headlines and interactive boundaries).

**Responsive 320px baseline and fluid typography:** compose mobile deliberately down to 320px minimum viewport width with zero horizontal blowout. Typography and paddings must scale down proportionally (hero ~1.35rem, section headings ~1.2rem) to avoid bloated interfaces ("UI bengkak"). In top navigation bars, never force crowded horizontal links on mobile (< 768px); collapse navigation behind an accessible hamburger menu with comfortable tap targets. Static by default; use motion for meaningful interactions, respect reduced-motion preferences, avoid bounce/floating/pulsing decoration without a real state.

**Critical/High findings block completion:** fabricated status/data, broken actions, inaccessible/clipped controls, misleading copy, theme contrast collisions or significant mobile failure must be fixed. Report what was actually verified; do not claim tests that did not run.

**Not an aesthetics veto:** expressive colors, shadows, gradients, card layouts or decorative treatments are legitimate when they are intentional parts of the selected aesthetic and pass usability checks. Do not silently force minimalism.

## Anti-slop: style-specific

**Physical precision, not decorative skeuo-noise.**

- **Reject:** emojis used as UI icons or button stickers, Disconnected dials that control nothing, decorative screw heads with no enclosure context, unreadable white text on brushed aluminum, and fake needles stuck at arbitrary angles.
- **Instead:** Apply tactile depth to interactive controls that map directly to state, volume, balance, or user parameters.
- **Copy check:** Labels should mimic industrial equipment (engraved, brief, functional).
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `skeuomorphism`.

## Quality tiers (standalone)

**FLOOR (must pass):** correct and truthful data/state, working critical actions, accessible focus/labels/contrast, usable responsive UI and reduced-motion support. **REFLEX (explain or fix):** generic feature grids, purposeless nested cards, decorative labels/icons, default marketing hype or constant motion. A reflex is allowed when it clearly expresses the chosen style and serves the task. **FINISH:** refinement of alignment, typography rhythm and edge cases. Never treat the selected style itself as a violation. Do not claim browser testing unless actually performed.
