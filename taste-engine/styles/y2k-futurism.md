# Style pack: Y2K Futurism

**ID:** `y2k-futurism`  
**Signature:** Late-1990s and early-2000s cyber-optimism and speculative technology aesthetic featuring polished chrome finishes, iridescent reflections, experimental geometric framing, bold futuristic typography, and metallic neutrality.

> This is a **style pack, not a mandatory default**. Load it only after explicit selection or confirmed applicable project style. Project instructions can override individual choices. Preserve accessibility, utility, and brand constraints. A generic purple gradient page **does not qualify as Y2K Futurism**.

## Good fit / trade-offs

- **Works well for:** Creative studios, electronic music platforms, cutting-edge fashion and lifestyle labels, experimental portfolios, web3/fintech products, gaming ecosystems, and forward-looking digital culture apps.
- **Use with care for:** Traditional corporate banking portals, clinical medical records, or conservative legal documentation where speculative metallic ornamentation may distract.
- **Reference directions:**
  - *Chrome (Default):* Polished metallic silver surfaces, high-contrast dark and light zones, chrome-beveled geometric framing, bold futuristic typography, and restrained electric violet or ice blue accents.
  - *Holographic:* Iridescent accents, controlled spectral sheens, translucent colored layering, soft chromatic reflections, and experimental futuristic layouts without chaotic color clashes.
  - *Retro Tech:* Early internet cyber-optimism, futuristic industrial typography, modular console panels, segmented status indicators, and speculative hardware references.

## Y2K Futurism material fidelity gate — mandatory

**Before calling a Y2K Futurism page complete, the opening viewport must visibly read as an authentic speculative metallic composition.** If a user chose this style, a flat dark box with a rainbow border or generic cyberpunk neon is a **FAIL**, even if CSS classes contain `y2k`.

A successful Y2K Futurism implementation demonstrates **all** of the following:

1. **Polished Chrome & Metallic Sheen:** Structural panels and interactive controls feature multi-stop silver-to-chrome gradients (`linear-gradient(135deg, #F1F3F6 0%, #C5CBD3 50%, #9DA5B2 100%)`) with distinct specular light bands simulating liquid mercury or extruded aluminum.
2. **Controlled Iridescent / Holographic Accents:** Spectral gradients (ice blue `#8FCFE9`, electric violet `#8865DD`, soft cyber pink `#E6ABD8`) applied strategically to active states, badges, and framing lines, avoiding uncontrolled rainbow noise across the entire layout.
3. **Reflective Geometric Silhouettes:** Panels use geometric chamfered corners, angled borders (`clip-path` or beveled 4px–8px corners), and segmented framing that evoke futuristic console hardware.
4. **Futuristic Typographic Discipline:** Expressive wide display headings (extended geometric sans or tracked futuristic typography) paired with highly legible monospace or clean modern sans for body text and data readouts.
5. **Anti-Clash Text Contrast (WCAG AA 4.5:1):** Deep graphite ink (`#181821` or `#252833`) on bright chrome and silver surfaces; crisp chrome-white (`#F1F3F6`) on deep space obsidian backgrounds.
6. **Hardware-Accelerated Lightweight Styling:** Pure CSS gradients, clip-paths, and SVG filters without heavy WebGL dependencies or unoptimized 3D libraries.

**First-viewport test:** In a desktop screenshot, identify the polished metallic chrome framing, the iridescent spectral highlights, the bold futuristic geometry, and the speculative tech authority **without reading the page title**. If it looks like generic Vaporwave, dark Cyberpunk neon, or flat gray SaaS, strengthen the chrome reflections and geometric chamfering.

## Explicit Y2K Futurism material exception — chrome and iridescence are allowed

**Y2K Futurism-specific override:** The universal anti-slop caution against *metallic gradients, iridescent highlights, or futuristic ornamentation* MUST NOT be interpreted as a ban on multi-stop chrome gradients, holographic light fields, or geometric framing here. These are **material-enabling properties**, essential to communicating the authentic millennium digital vision.

- **Allowed material treatments:** Multi-stop metallic linear gradients, iridescent linear and conic accent borders, chamfered corner framing, specular button sheens, and subtle scanline/grid micro-textures.
- **Harmonious color rules:** Restrict palettes to metallic silver, chrome light, deep space graphite, ice blue, and electric violet. Avoid harsh unharmonized neon rainbow clashes.
- **Anti-slop boundary:** Every control must be interactive, accessible, and functional. Do not decorate screens with fake spinning 3D globes, animated tribal flames, ornamental counters displaying fabricated numbers, or unreadable sci-fi fonts for body paragraphs.
- **Anti-slop interpretation:** Evaluate Y2K details by **metallic precision, speculative authenticity, and functional legibility**, not by counting gradient color-stops. Removing chrome surfaces to satisfy a generic flat heuristic is a **design regression**.

## Typography and typewriting

Y2K Futurism pairs expressive speculative display headers with disciplined functional body type:
- **Display Headings:** Extended geometric sans or futuristic wide display (e.g., Space Grotesk, Syne, Orbitron, or clean tracked extended sans) with bold weights (700–800) and generous letter spacing (`letter-spacing: 0.04em` to `0.08em`).
- **Body Text:** Highly readable modern geometric sans (Inter, Plus Jakarta Sans, system sans) at 15–17px desktop, 14–15px mobile, with `1.55` line-height for effortless reading.
- **Microcopy & Readouts:** High-contrast monospace (JetBrains Mono, Roboto Mono) at 11–13px with `font-variant-numeric: tabular-nums` for coordinates, status telemetry, and version metrics.

## Color direction

Y2K Futurism is anchored in a refined metallic foundation supporting both light and dark modes:

### Dark Mode (Deep Space & Liquid Chrome — Default)
- **Canvas / Background:** Deep space graphite (`#181821` to `#252833`).
- **Surface Panels:** Metallic dark graphite (`linear-gradient(145deg, #2A2E3D 0%, #1E202B 100%)`).
- **Primary Chrome Light:** Polished mirror highlight (`#F1F3F6`).
- **Metallic Neutral:** Brushed silver (`#C5CBD3`).
- **Holographic Accent:** Electric violet (`#8865DD`) and ice blue (`#8FCFE9`).
- **Secondary Accent:** Soft iridescent pink (`#E6ABD8`).
- **Reading Ink:** Crisp chrome-white (`#F1F3F6`) with muted silver (`#9AA2B1`).
- **Specular Border:** 1px liquid chrome edge (`rgba(241, 243, 246, 0.35)`).

### Light Mode (Liquid Silver & Iridescent Cloud)
- **Canvas / Background:** Chrome light mist (`#F1F3F6` to `#E4E7ED`).
- **Surface Panels:** Polished brushed silver (`#FFFFFF` to `#E8ECF2`).
- **Primary Metallic:** Liquid silver (`#C5CBD3`).
- **Deep Contrast Base:** Deep space graphite (`#181821`).
- **Holographic Accent:** Vibrant electric violet (`#734BC7`) and deep cyan (`#2E96BF`).
- **Reading Ink:** High-contrast deep graphite (`#181821` or `#252833`).
- **Specular Border:** 1px crisp silver highlight (`rgba(255, 255, 255, 0.95)`).

### Theme Coupling & Anti-Collision Rule
When switching between light and dark modes, text, borders, and metallic finishes MUST flip in synchronized pairs. Foreground text must maintain at least 4.5:1 contrast against both the panel surface and the metallic background. Never leave deep graphite text on deep space surfaces or white text on chrome light panels.

## Layout and geometry

- **Strict 1:1 circle geometry (anti-oval):** Any circular UI element (status indicator dots, avatars, circular buttons with `border-radius: 50%`) must enforce `aspect-ratio: 1 / 1; flex-shrink: 0;` to prevent deformation on narrow mobile viewports.
- **Responsive baseline:** Adhere to the [responsive baseline](../references/responsive-baseline.md) for 320px minimum viewport safety, fluid mobile typography defaults, and small-viewport navigation patterns.
- **Chamfered & Beveled Geometry:** Use angled 4px–8px chamfers (`clip-path: polygon(...)`) or crisp 4px–6px radii on cards, panels, and input frames to evoke futuristic hardware modules.
- **Segmented Console Grids:** Layouts feature modular technological framing with clear visual hierarchy, thin metallic dividers, and data-dense status telemetry strips.

## Surfaces, depth, texture

Y2K Futurism surfaces balance metallic reflection with crisp functional clarity:

- **1. Liquid Chrome Surface (Default):**
  ```css
  background: linear-gradient(135deg, #2E3344 0%, #1E202B 100%);
  border: 1px solid rgba(197, 203, 211, 0.35);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(241, 243, 246, 0.4);
  border-radius: 8px;
  ```

- **2. Holographic Spectral Surface (Variant: Holographic):**
  ```css
  background: linear-gradient(145deg, rgba(37, 40, 51, 0.85) 0%, rgba(24, 24, 33, 0.9) 100%);
  border: 1px solid rgba(136, 101, 221, 0.45);
  box-shadow: 0 10px 32px rgba(136, 101, 221, 0.15), inset 0 1px 1px rgba(143, 207, 233, 0.5);
  position: relative;
  ```

- **3. Retro Tech Console Surface (Variant: Retro Tech):**
  ```css
  background: #1C1E26;
  border: 1px solid #3B4052;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5), inset 0 1px 0 #4E556D;
  border-radius: 4px;
  ```

- **Chrome Action Button:**
  ```css
  background: linear-gradient(180deg, #F1F3F6 0%, #C5CBD3 50%, #9DA5B2 100%);
  color: #181821;
  font-weight: 800;
  border: 1px solid #FFFFFF;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35), inset 0 1px 0 #FFFFFF;
  border-radius: 6px;
  ```

## Component anatomy and interaction

- **Vector Iconography (Anti-Slop):** Emojis are strictly banned as interface icons, buttons, or status badges. Use crisp vector icons (Lucide, Radix, Feather) with consistent stroke weight (1.5px–2px) inheriting `currentColor`.
- **Chrome Specular Buttons:** Angled or beveled buttons with a bright top specular highlight, crisp metallic text, and positive 1.5px physical travel on depression.
- **Holographic Accent Badges:** Compact pills with iridescent gradients (`linear-gradient(90deg, #8FCFE9 0%, #8865DD 50%, #E6ABD8 100%)`) and high-contrast dark ink.
- **Chamfered Data Modules:** Diagnostic bays with monospace tabular readouts, subtle metallic border sheens, and clean status indicators.
- **Segmented Control Sliders:** Sleek metallic sliders and tabs that shift with a crisp 120ms ease-out metallic glint.

## Motion

Y2K Futurism motion is precise, technological, and restrained:
- **Button Press Feedback:** Immediate 1.5px downward shift (`transform: translateY(1.5px)`) with 110ms timing and shadow contraction.
- **Chrome Hover Glint:** Subtle specular glint reflection sweep across metallic borders over 150ms without distracting bounce.
- **Panel Entrances:** Crisp fade-in with 2px vertical settling over 140ms.
- **Reduced Motion:** When `@media (prefers-reduced-motion: reduce)` is active, set duration to 0ms and disable all physical transforms while preserving immediate state changes.

## Hero composition (full first viewport)

For a public-facing landing page or portfolio, apply [Full-screen Hero Contract](../references/hero-layout.md):
- **First Viewport Equation:** `min-height: 100svh` (with `100vh` fallback). Subtract normal-flow header height or let hero span under an overlay metallic header; let the hero expand for accessibility and short mobile screens. Do not apply this to private dashboards or other task screens; direct user overrides win.
- **Metallic Tech Backdrop:** Deep space obsidian background with subtle metallic horizon lighting and restrained holographic aurora fields.
- **Hero Module:** A prominent chrome-framed showcase bay housing the bold futuristic headline, speculative technological thesis, and paired action buttons.
- **Live Command Pill:** Single-line command box with `$ npm install @kennedys0/taste-engine` and copy button aligned horizontally with `display: inline-flex; align-items: center;`.
- **Responsive Stacking:** On viewports below 768px, gracefully stack elements with comfortable touch targets (44px+) and zero text overflow.

## UI writing and microcopy

- **Tone:** Speculative, technological, forward-looking, and precise. Inspired by millennium cyberculture and advanced engineering.
- **Anti-Slop Voice:** Ground claims in concrete product features. Reject empty techno-babble (*"quantum blockchain synergy"*), fake neural counters, and invented testimonials.
- **Button Labels:** Direct, action-oriented verbs (*"Initialize Engine"*, *"Access Matrix"*, *"Deploy Spec"*).
- **Empty & Loading States:** Honest, technological explanations with clear recovery actions (*"Telemetry feed standby. Click 'Initialize Stream' above to reconnect."*).

## Style-specific quality gate

Before marking a Y2K Futurism page or component complete, verify every gate:

1. **Gate 1 (Chrome & Metallic Precision):** Do structural panels and buttons feature convincing multi-stop metallic reflections rather than flat gray or neon purple slabs?
2. **Gate 2 (Holographic Restraint):** Are iridescent accents applied selectively to highlights and borders rather than washing out body text with rainbow gradients?
3. **Gate 3 (Contrast & Readability):** Does every text element exceed WCAG AA 4.5:1 contrast against both the panel surface and the backdrop behind it?
4. **Gate 4 (Futuristic Typographic Balance):** Are wide display fonts reserved for headlines, while body copy and data readouts remain in highly legible sans or mono?
5. **Gate 5 (320px Mobile Safety):** Does the entire layout adapt down to 320px width without horizontal scrollbars, clipped text, or deformed circular icons?
6. **Gate 6 (Performance):** Are all visual effects achieved with lightweight CSS and SVG rather than heavy 3D rendering engines?

## Anti-slop: style-specific

- **FAIL:** A generic purple/pink Vaporwave gradient background with low-contrast white text claiming to be Y2K Futurism.
- **FAIL:** Random floating 3D chrome globes, spinning ASCII skulls, or decorative visualizers that communicate no real data.
- **FAIL:** Unreadable narrow sci-fi display fonts used for long paragraphs of body copy.
- **FAIL:** Rainbow text gradients (`-webkit-background-clip: text`) applied to body copy or interactive labels.
- **FAIL:** Emojis used as UI button icons, bullet points, or status badges.
- **FAIL:** Dark gray text on deep space obsidian backgrounds causing severe WCAG contrast violations.
- **PASS:** Polished metallic silver surfaces, high-contrast typography, restrained holographic spectral accents, tactile button depression, and robust mobile responsiveness.

## Optional Anime.js v4 recipe

For projects that justify external coordinated motion, use Anime.js v4 with lifecycle cleanup and reduced-motion compliance:

```javascript
import { animate } from 'animejs';

// Respect user motion preferences
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

export function animateY2KPress(element) {
  if (prefersReduced) return;
  
  animate(element, {
    translateY: [0, 1.5, 0],
    duration: 120,
    ease: 'outQuad',
  });
}
```
