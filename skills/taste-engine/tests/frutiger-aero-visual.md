# Frutiger Aero visual acceptance tests

These are **manual visual and behavior tests**, not claims of executed browser tests.

## Explicit Frutiger Aero exception

- [ ] Reviewers do **not** reject glossy horizon sheens, aqua/sky/leaf multi-stop atmospheric gradients, rounded acrylic docks, or tactile convex button depth: they are essential design grammar defining the Frutiger Aero aesthetic.
- [ ] Surface planes feature dual-gradient curvature—a bright top-half specular highlight that mimics curved acrylic or glass lens physics without obscuring foreground typography.
- [ ] Atmospheric light fields feature nature-tech harmonies (sky cyan `#48BFD3`, ocean blue `#247EA3`, fresh leaf green `#70B981`, and cloud white `#F4FAFC`).
- [ ] The style is unmistakably distinct from generic frosted SaaS UI and flat dark cyber aesthetics.

## Fail the style when

- [ ] The interface relies on flat solid cards with `#000000` pitch black background and a single blue button claiming to be Aero.
- [ ] Generic gray SaaS cards use arbitrary background blur with no visible light or color passing through.
- [ ] Random non-functional floating bubbles, animated fish, or decorative spinning dials are added merely as layout filler.
- [ ] Text contrast fails WCAG AA standards (e.g. pale white text on cloud white panels or dark charcoal text on deep ocean glass).
- [ ] Horizontal layout overflow occurs on narrow mobile viewports down to 320px.
- [ ] Circular UI elements (avatars, status indicators) deform into squished ovals on mobile screens.
- [ ] Emojis are used as primary interface icons, buttons, or status badges.

## Pass the material when

- [ ] The opening desktop hero visibly reads as an authentic, optimistic Aero nature-tech composition before reading the page title.
- [ ] Glossy acrylic specular sheens, balanced translucency, and convex button dimensionality are visibly rendered.
- [ ] The three native expressions (Classic Aero, Aero Glass, Aero Tactile) resolve with distinct material cues and appropriate depth density.
- [ ] High-contrast focus indicators (`:focus-visible`) are prominent across all interactive elements (`0 0 0 3px rgba(72, 191, 211, 0.65)`).
- [ ] Paired light (Sky Lagoon) and dark (Ocean Midnight) modes flip background and text in tandem with zero color collisions.
- [ ] `prefers-reduced-motion` is fully honored, disabling all non-essential transforms.
- [ ] Solid surface fallbacks function cleanly when `backdrop-filter` is unsupported.

## Functional checks

1. **First-viewport recognition test:** Capture the opening viewport at desktop width. Can a reviewer recognize authentic Frutiger Aero optimism, gloss, and nature-tech balance without reading the title? If no, strengthen specular highlights and vibrant aqua balance.
2. **Responsive resizing:** Resize across 320, 390, 768, 1024, 1440, and 1920px. Content flows without horizontal scrollbars, and mobile header collapses into an accessible hamburger drawer.
3. **200% text zoom:** Enlarge typography to 200%; verify content wraps cleanly without breaking header buttons or clipping copy.
4. **Theme coupling & anti-collision:** Toggle between Dark (Ocean Midnight) and Light (Sky Lagoon) modes. Ensure text, borders, and buttons flip in synchronized pairs with no black-on-black or white-on-white collisions.
5. **Interactive expression switching:** Test switching between Classic Aero, Aero Glass, and Aero Tactile variants; verify tokens and surfaces update live.
6. **Keyboard navigation:** Tab through all controls in the component gallery and studio preview; verify visible `:focus-visible` outlines.
7. **Reduced motion:** Enable `prefers-reduced-motion`; verify all transitions disable cleanly while functionality remains intact.
