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

1. **Background depth:** a meaningful differentiated backdrop *behind* the surface (soft light fields, controlled gradients, shapes, photography supplied for the project, or existing app content). Glass needs something to visibly filter. **Purposeful gradients and ambient color shapes are explicitly allowed by Taste Engine anti-slop for Glassmorphism** when they establish visible light passing through a pane. They are not inherently slop.
2. **Translucency:** the panel lets some background chroma/luminance influence its appearance. Avoid completely opaque dark cards marketed as glass.
3. **Frosting:** `backdrop-filter: blur(...)` (and `-webkit-backdrop-filter` if required) visibly softens background detail *within the pane*, while nearby exposed background stays clearer. A blurred background image on its own is not frosted glass.
4. **Readable edge and depth:** soft bright hairline/highlight, slight interior sheen, rounded silhouette where appropriate, and restrained shadow or separation. Glass should have a perceptible boundary, not a flat gray slab.
5. **Content clarity:** text, focus indicators, control states and actions remain legible across the real composited background and with fallback effects disabled.

**First-viewport test:** In a desktop screenshot, identify the prominent pane, the distinct backdrop behind it, the blurred/tinted look *inside* its boundary, and its edge highlight **without reading the page title**. If not possible, revise the material before adding more content.

**Not a card-count rule:** A prominent hero pane or a few component demo surfaces is enough. Do not blanket every section with identical transparent cards. On a component showcase, use honest, functional examples (switch, input, dialog, toast as a **labeled demo**, navigation) to demonstrate the material and its states; do not invent real product status or social proof.

## Explicit background gradient exception — glass is allowed to glow

**Glassmorphism-specific override:** The universal anti-slop warning against *generic decorative gradients* MUST NOT be interpreted as a ban on gradients, mesh-like color fields, blurred color shapes, atmospheric lighting, or coherent background imagery here. These are valid **material-enabling backdrop layers**, even when decorative, because they make translucency, frosting, edges, and depth perceptible. This exemption is **not** permission for fabricated content or inaccessible/slow effects.

- **Allowed backdrop treatments:** 1–3 coherent `radial-gradient()` light fields, a restrained multi-stop linear or mesh gradient, blurred colored ambient shapes using pseudo-elements, a brand-aligned illustration/photograph, or existing content behind a pane. Static CSS is often enough and needs no extra images or animation libraries.
- **Light / milky example:** white/ice base with cool blue/lavender soft light fields behind a translucent white card; the pane visibly softens the color boundaries.
- **Dark / smoked example:** dark ink base with controlled purple/cyan/teal light areas behind translucent slate panes; bright gradient fields must not obscure white body text.
- **Composition requirement:** Place at least one light/color transition or recognizable backdrop element **behind and partly beyond the main glass pane** so the filtered-vs-unfiltered difference is visible; a uniform full-screen gradient with no local variation can still fail.
- **Depth control:** Background should be lower emphasis than content; use few light sources with natural falloff and intentional positions, rather than default purple/blue blobs on every page. Use the user's brand palette and supplied references.
- **Performance and accessibility:** Prefer static CSS gradients and restrained surfaces. Avoid full-screen moving gradient animations, excessive full-page backdrop blurs, tiny low-contrast text and hidden focus rings. Honor transparency preferences and test readable opaque fallbacks.
- **Anti-slop interpretation:** Evaluate gradients by **material purpose, restraint and legibility**, not by their mere presence. Removing a useful glass backdrop to satisfy a generic gradient heuristic is a **design regression**.

A strong screenshot should make the frosted material obvious even if all headings and labels are hidden. See `examples/glassmorphism/frosted-surfaces.css` for a starter implementation and `tests/glassmorphism-visual.md` for visual acceptance criteria.

## Typography and typewriting

Use a clean sans suited to the brand (system sans, DM Sans, Inter, etc.). Typical reading size 15–17 px; display type may be larger. Maintain strong type hierarchy and avoid ultra-thin text over variable glass backgrounds. A light frosted panel often benefits from deep foreground text; a dark smoked panel from high-contrast off-white. Never substitute colored glow for typographic hierarchy.

## Color direction

Choose one coherent direction from the context, or use the user's reference:

- **Frosted light / milky glass:** pale ice-white or light gray field, cool blue or other brand-tinted diffuse light *behind* semi-opaque white panes. Use restrained saturated accent. A soft glass highlight is visible along the upper edge.
- **Smoked dark / night glass:** deep navy/ink *base* with violet/blue/teal ambient light fields behind blue-gray translucent panels. Foreground text stays clear; dark panels are **not** nearly opaque rectangles.

Color alone is not Glassmorphism. Never default to neon purple/cyan for every brand. Preserve brand and high-contrast requirements. Check actual composited foreground contrast (WCAG AA 4.5:1 normal text, 3:1 large text; relevant non-text controls at least 3:1).

## Layout and geometry

- Use a purposeful foreground/background composition: ambient backdrop → glass surfaces → crisp content and interactive controls. Distinguish 2–3 depth planes without nested-card clutter.
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

- **Hero:** make the selected aesthetic obvious immediately. Place actual Taste Engine/project heading and CTAs *inside or overlapping a visible glass plane*, or present an equally convincing glass window composition. Provide meaningfully lit backdrop behind the pane.
- **Header/nav:** a subtle frosted bar can overlap the backdrop, but keep contrast and focus visible. Avoid a flat opaque top bar visually disconnected from the page when demonstrating glass UI.
- **Functional examples:** switch with real on/off state, selectable option, tab, modal, form, and a toast **only if genuinely triggered** or clearly marked as a static demo. Show focused, hovered, active, disabled and error conditions when applicable. Foreground control surfaces can be more opaque than parent glass for usability.
- **Buttons:** can be solid accent surfaces for affordance; not every control must be transparent. A conventional button does not compensate for missing glass elsewhere.
- **Content:** reserve strongly tinted or solid readable containers for long paragraphs, tables and forms; do not place paragraphs on noisy translucent images.

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

| Token | Starting value |
| --- | --- |
| `--taste-radius-sm` | `14px` |
| `--taste-radius-lg` | `24px` |
| `--taste-glass-blur` | `18px` |
| `--taste-glass-light` | `rgba(255, 255, 255, 0.38)` |
| `--taste-glass-dark` | `rgba(36, 45, 72, 0.38)` |
| `--taste-glass-edge-light` | `rgba(255, 255, 255, 0.65)` |
| `--taste-motion-duration` | `180ms` |

These are starting values only. The result must be checked against real content and backdrop. Do not secretly load fonts, illustrations or motion libraries.

## Hero composition (full first viewport)

For public portfolio/landing/homepages with a hero, use a **header + hero** first-viewport composition (`min-height: 100svh` with `100vh` fallback) rather than a clipped fixed-height hero. Subtract an actual in-flow header as needed, not twice for overlays. Grow naturally on short mobile screens and at zoom. **Material requirement:** the first viewport shows an unmistakable frosted pane filtering a visible, carefully composed backdrop—not 80% empty dark space above ordinary text. Build visual interest from meaningful layered structure and brand-aligned ambient light; do not invent photos, fake statistics or purposeless animated ornaments. An explicit compact/no-hero preference overrides the default.

## Style-specific quality gate

**Required visible material check:** Can a reviewer distinguish frosted/translucent material from solid cards **without reading the description**? Can they see background-filtering through at least one primary pane on the actual screenshot? If not, fail and revise.

- **Do:** Check frosted appearance, layered separation, real composite contrast, border highlights, mobile wrapping, keyboard focus, interactive states, and opaque fallback.
- **Don't:** Mark a flat navy hero with a bright blue CTA as “glass”; count CSS blur on an invisible element as visual fidelity; use fully opaque cards with a decorative outer glow as a substitute.
- **Light and dark both valid:** No global requirement that a glass demo be dark. Choose a reference-aligned look and make the actual material visible.
- **Browser QA:** At ~320, 390, 768 and 1440 CSS pixels, inspect the first viewport and controls. Check blur support/fallback, `prefers-reduced-motion`, and high-contrast/reduced-transparency modes where supported. If no browser was used, report this as a manual check **not yet verified**.
- The full visual acceptance checklist is in the `tests/glassmorphism-visual.md` checks in the full router (and the checklist in this section for standalone use). Preserve existing functions, routes and content when restyling a working site.

## Anti-slop: style-specific

**Glass as a material, not a label. Purposeful gradients are an explicit exception.**

- **Reject:** Flat dark layouts described as glass; fake frosted panes that are really opaque blocks; **arbitrary** gradient/blob spam without depth or hierarchy; border/glow spam; heavy blur across the whole screen; endless parallax; glass-on-glass nesting with no functional separation. **Do not reject functional ambient gradients simply because they are decorative.**
- **Instead:** Give a few important planes believable translucency and visible filtering over purposefully placed gradients or ambient light, subtle lit edges, restrained depth and accessible high-contrast content. Keep other surfaces solid when needed.
- **Copy check:** Avoid “immersive future” or “next-gen experience” filler. Make labels and CTAs describe real features/actions.
- **Audit:** Run universal anti-slop, truthfulness, responsive, keyboard, focus, motion, and semantic checks in addition to the **material fidelity gate**. Do not reject deliberate expressive glass styling merely because it is decorative; it must have a coherent compositional purpose.
