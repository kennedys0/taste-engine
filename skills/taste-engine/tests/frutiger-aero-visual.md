# Frutiger Aero visual acceptance tests

These are **manual visual and behavior tests**, not claims of executed browser tests.

## Explicit Frutiger Aero exception

- [ ] Reviewers do **not** reject glossy horizon sheens, aqua/sky/seafoam/leaf multi-stop atmospheric gradients, rounded acrylic docks, or tactile molded button bevels: they are essential design grammar defining the Frutiger Aero aesthetic (Glassmorphism + Skeuomorphism fusion).
- [ ] Surface planes feature dual-gradient curvature—a bright top-half specular highlight that mimics curved acrylic or glass lens physics without obscuring foreground typography.
- [ ] Atmospheric light fields feature nature-tech harmonies (sky `#DCEFF8` / `#C9EDF8`, aqua `#6CD1E8` / `#48BFD3`, ocean `#2C90B8` / `#247EA3`, seafoam `#A7E6D5`, fresh leaf green `#79C67A` / `#70B981`, and cloud white `#F7FBFD` / `#F4FAFC`).
- [ ] The style is unmistakably distinct from generic frosted SaaS UI, plain white stat boxes on a blue page, and flat dark cyber aesthetics.

## Fail the style when

- [ ] The interface looks like a flat soft blue SaaS page with plain white rectangular stat cards and generic gradient pill buttons.
- [ ] The hero relies only on centered text and self-congratulatory QA boast badges (*"WCAG AA Contrast"*, *"Zero AI-Slop"*, *"320px Zero Mobile Overflow"*) instead of visually demonstrating Frutiger Aero through a glossy orb/acrylic/glass centerpiece.
- [ ] Buttons lack physical molding, top specular highlight bands, or a compressed/inset `:active` pressed state.
- [ ] Variant switching only changes text or sets hardcoded inline light backgrounds that break Dark Mode contrast.
- [ ] Generic gray SaaS cards use arbitrary background blur with no visible light or color passing through.
- [ ] Random non-functional noisy wallpaper clutter, animated swimming fish, or fake telemetry boasts are added as filler.
- [ ] Text contrast fails WCAG AA standards (e.g. pale white text on cloud white panels or dark charcoal text on deep ocean glass).
- [ ] Horizontal layout overflow occurs on narrow mobile viewports down to 320px, or split-column card stacks leave dead vertical gaps.
- [ ] Circular UI elements (avatars, status indicators, orbs) deform into squished ovals on mobile screens.
- [ ] Emojis are used as primary interface icons, buttons, or status badges.

## Pass the material when

- [ ] The opening desktop hero visibly reads as an authentic, optimistic Aero composition ("Optimistic computing under a clear blue digital sky") with a material-led focal centerpiece before reading the page title.
- [ ] Three core Aero materials are visibly distinct and fused: Aero Glass (`.taste-aero-glass-surface`), Glossy Acrylic (`.taste-aero-acrylic-surface`), and Tactile Skeuomorphic Depth (`.taste-aero-tactile-surface` + `.taste-aero-inset-well`).
- [ ] Primary and Secondary buttons look touchable, dimensional, and physically responsive across Rest, Hover, and Pressed (`:active`) states.
- [ ] The three native expressions (`Classic Aero`, `Aero Glass`, `Aero Tactile`) resolve with distinct material cues, centerpiece sculptures, button bevels, and panel depth.
- [ ] High-contrast focus indicators (`:focus-visible`) are prominent across all interactive elements.
- [ ] Paired light (Clear Sky Lagoon) and dark (Bioluminescent Deep Ocean) modes flip background, recessed wells, and text in tandem with zero color collisions.
- [ ] `prefers-reduced-motion` is fully honored, disabling all non-essential transforms.
- [ ] Solid surface fallbacks function cleanly when `backdrop-filter` is unsupported.

## Functional checks

1. **First-viewport recognition test:** Capture the opening viewport at desktop width. Can a reviewer recognize authentic Frutiger Aero optimism, Glass + Skeuomorphism fusion, tactile buttons, and the glossy orb/lens centerpiece without reading the title? If no, strengthen specular highlights, molded bevels, and atmospheric aqua depth.
2. **Button press inspection:** Click and hold both Primary (molded aqua acrylic) and Secondary (translucent cloud glass) buttons; verify downward movement, shadow compression, reduced top highlight, and inset pressure bevel.
3. **Responsive resizing:** Resize across 320, 390, 768, 1024, 1440, and 1920px. Content flows without horizontal scrollbars, cards remain dimensional, and mobile header collapses into an accessible hamburger drawer.
4. **200% text zoom:** Enlarge typography to 200%; verify content wraps cleanly without breaking header buttons or clipping copy.
5. **Theme coupling & anti-collision:** Toggle between Dark (Bioluminescent Ocean) and Light (Clear Sky Lagoon) modes across all 3 variants. Ensure text, borders, wells, and buttons flip in synchronized pairs with no black-on-black or white-on-white collisions.
6. **Interactive expression switching:** Test switching between Classic Aero, Aero Glass, and Aero Tactile variants; verify centerpiece sculpture, panel materials, and tokens update live.
7. **Keyboard navigation:** Tab through all controls in the component gallery and studio preview; verify visible `:focus-visible` outlines.
8. **Reduced motion:** Enable `prefers-reduced-motion`; verify all transitions disable cleanly while functionality remains intact.
