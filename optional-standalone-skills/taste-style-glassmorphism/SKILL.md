---
name: taste-style-glassmorphism
description: Apply Glassmorphism design style to user-selected frontend and UI work. Use only when the user explicitly chooses this style. Provides typography, color, layout, components, interactions, motion, copy and quality gates. Do not impose on unrelated work.
license: MIT
metadata:
  version: "0.10.6"
---

Use this skill only after a user explicitly chooses  or a confirmed project configuration specifies it. For unexplained new UI requests, use a style selector such as  instead of deciding the user's taste here. Existing brand, accessibility and user overrides outrank all examples below. The following style guide is not permission to start UI coding before style selection.

# Style pack: Glassmorphism

**ID:** `glassmorphism`  
**Signature:** Visibly frosted, translucent surfaces floating over differentiated light/color layers, with clear content and functional depth.

> This is an **opt-in style**, not the engine default. Activate it only when selected by the user or established project design system. Respect product anatomy, brand direction, accessibility, and existing interactions. A generic dark page with a blue button **does not qualify as Glassmorphism**.

## Good fit / trade-offs

- **Works well for:** Expressive portfolios, product landing pages, navigation overlays, media interfaces, creative dashboards, and bounded UI demos.
- **Use with care for:** Dense data tables, long-form reading, accessibility-critical forms, or unpredictable photos behind text. Place high-density content on appropriately solid or strongly tinted surfaces.
- **Reference directions:** A *light, milky frosted pane* with soft blue atmospheric light and gentle rounded geometry; or a *dark, smoked-glass system* with translucent slate panels, muted violet/cyan illumination and legible controls. Both are valid. Neither forces a fixed brand palette.

## Glass material fidelity gate — mandatory

**Before calling a glassmorphism page complete, the opening viewport must visibly read as a glass composition.** If a user chose this style, a large plain background plus typography and a conventional button is a **FAIL**, even if CSS variables are named `glass`.

A successful prominent glass component demonstrates **all** of the following:

1. **Background depth & textured gradients:** A purposeful, differentiated backdrop *behind* the surface (soft light fields, controlled gradients, subtle noise/dot-matrix micro-textures, or existing app content). Glass needs something to visibly filter. **Purposeful gradients, ambient color shapes, and tactile background textures are explicitly allowed by Taste Engine anti-slop for Glassmorphism** when they establish visible light passing through a pane without jarring color collisions. They are not inherently slop.
2. **Translucency & Refractive Saturation:** The panel lets background chroma and luminance influence its appearance (`rgba(...)` or `color-mix`), enhanced with `backdrop-filter: blur(16px–24px) saturate(140%–180%)`. Avoid completely opaque dark cards marketed as glass.
3. **Beveled Specular Edge System:** Dual-layer edge illumination—a 1px perimeter border with high-transparency specular highlight (`rgba(255, 255, 255, 0.4–0.7)` on light, `rgba(255, 255, 255, 0.16–0.32)` on dark) combined with an inner specular sheen (`inset 0 1px 1px 0 rgba(255, 255, 255, 0.25)`). Glass must have a clean, physically grounded boundary, not look like a flat gray slab.
4. **Anti-Clash Color Safety:** Ambient light sources must use restrained, natural gaussian falloff and non-clashing hues (monochromatic, analogous, or balanced complementary pairs). Primary text ink must never collide with background light pools—crisp deep slate on frosted light glass, and pure luminous porcelain on smoked dark glass (WCAG AA 4.5:1).
5. **Elevated Glass Component Hierarchy:** Controls inside glass (switches, sliders, buttons, inputs) use slightly higher opacity or dedicated specular rims for instant affordance without nesting arbitrary decorative boxes.
6. **Content clarity & fallbacks:** Text, focus rings (`:focus-visible`), and actions remain razor-sharp across the composited backdrop, with `@supports not` fallback to solid surfaces for browsers without `backdrop-filter`.

**First-viewport test:** In a desktop screenshot, identify the prominent pane, the distinct backdrop behind it, the blurred/tinted look *inside* its boundary, and its edge highlight **without reading the page title**. If not possible, revise the material before adding more content.

**Not a card-count rule:** A prominent hero pane or a few component demo surfaces is enough. Do not blanket every section with identical transparent cards. On a component showcase, use honest, functional examples (switch, input, dialog, toast as a **labeled demo**, navigation) to demonstrate the material and its states; do not invent real product status or social proof.

## Explicit background gradient exception — glass is allowed to glow

**Glassmorphism-specific override:** The universal anti-slop warning against *generic decorative gradients* MUST NOT be interpreted as a ban on gradients, mesh-like color fields, blurred color shapes, atmospheric lighting, or coherent background imagery here. These are valid **material-enabling backdrop layers**, even when decorative, because they make translucency, frosting, edges, and depth perceptible. This exemption is **not** permission for fabricated content or inaccessible/slow effects.

- **Allowed backdrop treatments:** 1–3 coherent `radial-gradient()` light fields, a restrained multi-stop linear or mesh gradient, blurred colored ambient shapes using pseudo-elements, paired with subtle tactile micro-textures (SVG grain or fine dot-matrix grids) that prevent flat banding. Static CSS is often enough and needs no extra images or animation libraries.
- **Harmonious, non-clashing color rules:** Strictly avoid discordant rainbow gradients or clashing secondary hues. Restrict palettes to monochromatic or analogous harmonic groups (e.g. cyan/periwinkle/slate, or emerald/teal/obsidian) with gentle gaussian falloff.
- **Light / milky example:** white/ice base with cool blue/lavender soft light fields behind a translucent white card; the pane visibly softens the color boundaries.
- **Dark / smoked example:** dark ink base with controlled purple/cyan/teal light areas behind translucent slate panes; bright gradient fields must not obscure white body text.
- **Composition requirement:** Place at least one light/color transition or recognizable backdrop element **behind and partly beyond the main glass pane** so the filtered-vs-unfiltered difference is visible; a uniform full-screen gradient with no local variation can still fail.
- **Depth control:** Background should be lower emphasis than content; use few light sources with natural falloff and intentional positions, rather than default purple/blue blobs on every page. Use the user's brand palette and supplied references.
- **Performance and accessibility:** Prefer static CSS gradients and restrained surfaces. Avoid full-screen moving gradient animations, excessive full-page backdrop blurs, tiny low-contrast text and hidden focus rings. Honor transparency preferences and test readable opaque fallbacks.
- **Anti-slop interpretation:** Evaluate gradients by **material purpose, restraint and legibility**, not by their mere presence. Removing a useful glass backdrop to satisfy a generic gradient heuristic is a **design regression**.

A strong screenshot should make the frosted material obvious even if all headings and labels are hidden. See `examples/glassmorphism/frosted-surfaces.css` for a starter implementation and `tests/glassmorphism-visual.md` for visual acceptance criteria.

## Explicit nested glass exception — card inside card is permitted

**Glassmorphism-specific override:** The universal anti-slop caution against *card-inside-card nested surfaces* MUST NOT be interpreted as a prohibition on nested translucent glass elements here. In authentic glass design systems (macOS, VisionOS, iOS), layering a child glass card inside a parent frosted window is a primary architectural pattern that establishes physical optical depth.

- **Allowed nested glass treatments:** Placing elevated glass widgets, control pods, media players, filter strips, or telemetry cards inside a primary frosted container.
- **Depth hierarchy rule:** Child glass surfaces must have a distinct optical density from the parent surface (e.g. parent glass at 0.20–0.30 alpha with 24px blur; child cards at 0.40–0.60 alpha with 14px blur and tighter 1px specular borders).
- **Anti-slop boundary:** Do not nest meaningless empty frames merely to add decorative borders. Every nested glass surface must represent an authentic functional boundary (e.g., an audio player, a setting segment, or an interactive tool).

## Typography and typewriting

Use a clean sans suited to the brand (system sans, DM Sans, Inter, etc.). Typical reading size 15–17 px; display type may be larger. Maintain strong type hierarchy and avoid ultra-thin text over variable glass backgrounds. A light frosted panel often benefits from deep foreground text; a dark smoked panel from high-contrast off-white. Never substitute colored glow for typographic hierarchy.

## Color direction

Choose one coherent direction from the context, or use the user's reference:

- **Frosted light / milky glass:** pale ice-white or light gray field (`#F0F4F8`), cool blue or other brand-tinted diffuse light *behind* semi-opaque white panes (`rgba(255, 255, 255, 0.45)`). Typography is deep slate (`#0F172A`) with muted slate (`#475569`). A soft glass highlight is visible along the upper edge (`rgba(255, 255, 255, 0.75)`).
- **Smoked dark / night glass:** deep navy/ink *base* (`#090D16`) with violet/blue/teal ambient light fields behind blue-gray translucent panels (`rgba(22, 28, 45, 0.55)`). Foreground text is crisp porcelain (`#F8FAFC`) with muted slate (`#94A3B8`); dark panels are **not** nearly opaque rectangles.
- **Theme Coupling & Anti-Collision Rule:** When switching between light and dark glass modes, foreground text, borders, and ambient light sources MUST switch in tandem. Foreground text must maintain at least 4.5:1 contrast against both the frosted glass surface and the illuminated backdrop behind it. Never leave dark text on smoked dark glass or white text on frosted light glass.

Color alone is not Glassmorphism. Never default to neon purple/cyan for every brand. Preserve brand and high-contrast requirements. Check actual composited foreground contrast (WCAG AA 4.5:1 normal text, 3:1 large text; relevant non-text controls at least 3:1).

## Layout and geometry

- Use a purposeful foreground/background composition: ambient backdrop → primary glass surfaces → elevated child glass controls and crisp content. Layered glass cards (card inside card) are explicitly encouraged when establishing functional interaction boundaries.
- Use consistent corners (commonly 16–28 px for larger panes) and spacing. Avoid an entirely empty oversized first viewport just to reach 100svh.
- On responsive screens, panes should stack cleanly, preserve readable padding, and avoid clipped blur or overflow. Header, hero content, and controls must fit or expand naturally.

## Surfaces, depth, texture

- **Glass recipe:** semi-transparent tint (`rgba(...)` or `color-mix`), `backdrop-filter: blur(16px) saturate(140%)`, a translucent 1px border, mild inset top highlight, and soft layered shadow. Start around 12–24 px blur, then tune against the real backdrop.
- **Light glass:** use a white tinted surface with approximately 0.24–0.55 alpha *when backdrop allows*; too much opacity removes the frosted effect. Strong text contrast is still mandatory.
- **Dark glass:** use a slate/indigo tint around 0.25–0.56 alpha, visible brighter edge and contrasting ambient light behind it. Avoid both pitch-black slabs and eye-searing neon halos.
- **Depth cues:** soft blurred **backdrop behind** the panel, a restrained inner shine, a subtle edge glow/reflection. No stock generic bubble wallpaper needed.
- Use `@supports` fallback with solid readable surfaces when backdrop filtering is missing. Provide a reduced-transparency/high-contrast alternative. Blur itself must never be necessary to understand content or interact.

See `examples/glassmorphism/frosted-surfaces.css` in the full Taste Engine router (the token recipe above also works in standalone installations) for independent light and dark starting tokens. Adapt tokens to the project; do **not** copy all examples or force a fixed palette.

## Component anatomy and interaction

- **Frosted Glass Pane/Pod:** Master translucent container with 16–24px corner radius, 1px translucent specular border, inset top sheen (`inset 0 1px 1px 0 rgba(255, 255, 255, 0.25)`), and smooth ambient drop shadow.
- **Hero Window:** Opening viewport anchor placing brand headings and primary actions inside a visible, frosted glass composition with light filtering through from behind.
- **Glass Controls & Sliders:** Frosted slider tracks with tactile thumb handles and interactive value tags.
- **Segmented Pill Toggles:** Recessed well container with active frosted pill slider and smooth hover sheen.
- **Telemetry / Audio Gauges:** High-contrast text values paired with soft equalizer bars or micro-gauges visible through the glass pane.
- **Glass Buttons & Action Controls:** Crisp semi-opaque or solid accent surfaces ensuring high tactile affordance and clear `:focus-visible` focus rings.
- **Content Surfaces:** Strongly tinted or solid readable containers for long paragraphs, forms, and data tables to preserve WCAG AA contrast.

## Motion

Use interaction feedback rather than ambient movement. 140–220 ms fade/translate on hover, selection, pane reveal or modal only when user action warrants it. Preserve glass layer continuity. No endless drifting orbs, moving light beams or mandatory 3D spins.

## Optional Anime.js v4 recipe

- **Motion decision:** CSS/native transitions for most interactions; Anime.js v4 is optional for coordinated state transitions, not a required visual dependency.
- **Starting duration:** 180 ms, easing without bounce. Animate compositor-friendly `opacity`/`transform` rather than continuously animating blur or box-shadow.
- **Reduce motion:** honor `prefers-reduced-motion` and allow interrupted/short-circuited transitions.
- **Dependency:** follow Taste Engine `references/motion-engine.md` where available; standalone skill applies the same guidance.

## UI writing and microcopy

Direct, product-specific and concise. Glass is a material, not an excuse for vague copy such as “the future is transparent.” Avoid fake badges, verification status, users, productivity scores, or testimonials. Demo data must be explicitly labeled.

## Starter tokens (suggestions, not a complete theme)

| Token | Light glass default | Dark glass default |
| --- | --- | --- |
| `--taste-radius-sm` | `14px` | `14px` |
| `--taste-radius-lg` | `24px` | `24px` |
| `--taste-glass-blur` | `18px` | `18px` |
| `--taste-glass-bg` | `#f0f4f8` | `#090d16` |
| `--taste-glass-surface` | `rgba(255, 255, 255, 0.45)` | `rgba(22, 28, 45, 0.55)` |
| `--taste-glass-text` | `#0f172a` | `#f8fafc` |
| `--taste-glass-text-muted` | `#475569` | `#94a3b8` |
| `--taste-glass-light` | `rgba(255, 255, 255, 0.38)` | `rgba(255, 255, 255, 0.38)` |
| `--taste-glass-dark` | `rgba(36, 45, 72, 0.38)` | `rgba(36, 45, 72, 0.38)` |
| `--taste-glass-edge-light` | `rgba(255, 255, 255, 0.65)` | `rgba(255, 255, 255, 0.18)` |
| `--taste-motion-duration` | `180ms` | `180ms` |

These are starting values only. The result must be checked against real content and backdrop. Do not secretly load fonts, illustrations or motion libraries.

## Hero composition (full first viewport)

For public portfolio/landing/homepages with a hero, use a **header + hero** first-viewport composition (`min-height: 100svh` with `100vh` fallback) rather than a clipped fixed-height hero. Subtract an actual in-flow header as needed, not twice for overlays. Grow naturally on short mobile screens and at zoom. **Material requirement:** the first viewport shows an unmistakable frosted pane filtering a visible, carefully composed backdrop—not 80% empty dark space above ordinary text. Build visual interest from meaningful layered structure and brand-aligned ambient light; do not invent photos, fake statistics or purposeless animated ornaments. An explicit compact/no-hero preference overrides the default.

## Style-specific quality gate

- **Do:** Verify translucent frosted surfaces filtering backdrop light; ensure 1px translucent borders and specular highlights define panel edges; ensure background gradients are non-clashing and paired with subtle tactile micro-textures; test accessibility fallback without `backdrop-filter`; verify dark/light mode switching so foreground text and glass panels flip cleanly without color collisions (WCAG AA 4.5:1).
- **Don't:** Do not treat plain dark/light cards as glassmorphism; avoid whole-screen blur; avoid low-contrast text floating over noisy translucent areas; do not use discordant rainbow gradients that clash or overpower content; do not leave dark text when switching to smoked dark glass.
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

**Translucent depth, not blurry chaos.**

- **Reject:** Completely opaque flat cards described as glass, clashing rainbow gradient blobs with no depth or texture, text placed over high-contrast translucent clutter with no solid underlay, and theme contrast collisions (such as black text on dark smoked glass).
- **Instead:** Filter structured, purposeful, non-clashing ambient light through legible frosted panes with clear hierarchy, distinct nested glass depth planes, and solid readable content containers.
- **Copy check:** Avoid clichés like "crystal clear" or "transparent future."
- **Audit:** Run universal anti-slop purpose, truth, nested-surface, copywriting, responsiveness, accessibility and motion checks **in addition** to this style's quality gate. Do not penalize deliberate, accessible features characteristic of `glassmorphism`.

## Quality tiers (standalone)

**FLOOR (must pass):** correct and truthful data/state, working critical actions, accessible focus/labels/contrast, usable responsive UI and reduced-motion support. **REFLEX (explain or fix):** generic feature grids, purposeless nested cards, decorative labels/icons, default marketing hype or constant motion. A reflex is allowed when it clearly expresses the chosen style and serves the task. **FINISH:** refinement of alignment, typography rhythm and edge cases. Never treat the selected style itself as a violation. Do not claim browser testing unless actually performed.
