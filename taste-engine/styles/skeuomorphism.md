# Style pack: Skeuomorphism

**ID:** `skeuomorphism`  
**Signature:** Digital controls borrow tangible affordances from physical objects, industrial machinery, and analog hardware.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. Fonts are suggestions, not required dependencies. A flat card with a subtle gradient **does not qualify as Skeuomorphism**.

## Good fit / trade-offs

- **Works well for:** Music production and synthesizer software, audio gear tools, specialized simulators, tactile dashboard widgets, creative digital instruments, and playful tactile experiences.
- **Be careful with:** Dense transactional data tables or mobile enterprise forms where ornate physical hardware textures create visual clutter.
- **Reference directions:**
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

Component shapes strictly map to their physical metaphors: rotary dials, tactile push-buttons, rocker switches, and segmented meters. 4–12px corner radii on panels; circular radii for knobs. Avoid applying hardware skins to generic text paragraphs.

## Surfaces, depth, texture

- **Chassis Panel:** Multi-stop linear gradient (`linear-gradient(180deg, #323741 0%, #262A32 100%)`) with 1px top highlight and bottom drop shadow.
- **Physical Push-Button:** Beveled rim with top highlight, radial button surface, and crisp active depression.
- **Sunken Well / Display:** `box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.65), 0 1px 0 rgba(255, 255, 255, 0.15);`

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
| `--taste-skeuo-text` | `#f3f4f6` | `#1f2937` |
| `--taste-skeuo-btn-bg` | `linear-gradient(180deg, #3c424f 0%, #2a2e37 100%)` | `linear-gradient(180deg, #ffffff 0%, #e2e8f0 100%)` |
| `--taste-skeuo-btn-bevel` | `inset 0 1px 0 rgba(255, 255, 255, 0.40), inset 0 -1px 0 rgba(0, 0, 0, 0.50)` | `inset 0 1px 0 rgba(255, 255, 255, 0.80), inset 0 -1px 0 rgba(0, 0, 0, 0.20)` |
| `--taste-skeuo-btn-shadow` | `0 4px 8px rgba(0, 0, 0, 0.50), 0 1px 2px rgba(0, 0, 0, 0.40)` | `0 4px 8px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.08)` |
| `--taste-skeuo-well-inset` | `inset 0 3px 6px rgba(0, 0, 0, 0.70), 0 1px 0 rgba(255, 255, 255, 0.12)` | `inset 0 3px 6px rgba(0, 0, 0, 0.18), 0 1px 0 rgba(255, 255, 255, 0.80)` |
| `--taste-skeuo-led-active` | `#10b981` | `#059669` |
| `--taste-skeuo-led-glow` | `0 0 10px rgba(16, 185, 129, 0.75)` | `0 0 8px rgba(5, 150, 105, 0.45)` |
| `--taste-skeuo-radius-panel` | `12px` | `12px` |
| `--taste-skeuo-font-mono` | `IBM Plex Mono, ui-monospace, monospace` | `IBM Plex Mono, ui-monospace, monospace` |
| `--taste-skeuo-motion-duration` | `160ms` | `160ms` |

Tokens represent a **direction** and are not copy-paste guaranteed for every palette/platform. Define `--taste-skeuo-*` at project level, ensure color contrast, and adapt via theme tokens rather than scattering literal values.

## Hero composition (full first viewport)

**When a public-facing portfolio/landing/homepage has a hero:** use a one-visible-screen header+hero composition. Base height on `min-height: 100svh` with `100vh` fallback, subtracting the **real** header only when it is in normal flow; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win. **Style-specific direction:** Treat the first viewport as an authentic master control console or signature instrument faceplate; provide working controls and an unmistakable primary CTA. Do not litter the canvas with non-functional screws, decorative cables, or disconnected analog meters. See the router `references/hero-layout.md` when present. Standalone use follows the same responsive and anti-slop principles.


## Style-specific quality gate

- **Do:** Verify consistent top-down specular highlight across all controls; ensure mechanical press states depress smoothly; provide numerical readouts alongside dials/sliders; test keyboard focus; verify dark/light mode switching so chassis, bevel highlights, wells, and label typography adapt in coupled pairs.
- **Don't:** never use emojis as UI icons or button prefixes (always use Lucide or clean vector SVGs with currentColor); Do not treat a plain dark theme as skeuomorphic; do not add non-functional decorative screws or fake analog needles that don't connect to real data; avoid unreadable low-contrast text on dark faceplates or white labels on silver light faceplates.
- Confirm desktop and mobile consistency; visible keyboard focus (`:focus-visible`); loading, empty, disabled, error and success states; reduced-motion behavior (`prefers-reduced-motion`).
- Do not inject style-specific assumptions into unrelated projects. When combining styles, explicitly name the primary style and the borrowed features.

## Anti-slop: style-specific

**Physical precision, not decorative skeuo-noise.**

- **Reject:** emojis used as UI icons or button stickers, Disconnected dials that control nothing, decorative screw heads with no enclosure context, unreadable white text on brushed aluminum, and fake needles stuck at arbitrary angles.
- **Instead:** Apply tactile depth to interactive controls that map directly to state, volume, balance, or user parameters.
- **Copy check:** Labels should mimic industrial equipment (engraved, brief, functional).
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `skeuomorphism`.
