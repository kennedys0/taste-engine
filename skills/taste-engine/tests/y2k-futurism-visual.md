# Y2K Futurism visual acceptance tests

These are **manual visual and behavior tests**, not claims of executed browser tests.

## Explicit Y2K Futurism exception

- [ ] Reviewers do **not** reject multi-stop metallic gradients, polished chrome finishes, iridescent/holographic spectral accent borders, or chamfered hardware framing: they are essential design grammar defining the Y2K Futurism aesthetic.
- [ ] Structural panels feature polished chrome and liquid silver surfaces (`linear-gradient(135deg, #F1F3F6 0%, #C5CBD3 50%, #9DA5B2 100%)`) with distinct specular light bands simulating liquid mercury or extruded aluminum.
- [ ] Spectral highlights and iridescent borders use controlled light fields (ice blue `#8FCFE9`, electric violet `#8865DD`, soft cyber pink `#E6ABD8`) without washing out foreground typography.
- [ ] The style is unmistakably distinct from generic dark Vaporwave, neon Cyberpunk, and flat gray SaaS.

## Fail the style when

- [ ] The interface relies on flat solid dark boxes with a generic purple gradient and claims to be Y2K.
- [ ] Random non-functional floating 3D chrome globes, spinning ASCII skulls, or decorative tribal flames are added merely as layout filler.
- [ ] Rainbow text gradients (`-webkit-background-clip: text`) are applied to body copy or interactive labels, destroying legibility.
- [ ] Unreadable narrow sci-fi display typography is applied to multi-line body paragraphs.
- [ ] Text contrast fails WCAG AA standards (e.g. muted graphite text on dark obsidian backgrounds or pale white text on chrome light panels).
- [ ] Horizontal layout overflow occurs on narrow mobile viewports down to 320px.
- [ ] Circular UI elements (avatars, status indicators) deform into squished ovals on mobile screens.
- [ ] Emojis are used as primary interface icons, buttons, or status badges.

## Pass the material when

- [ ] The opening desktop hero visibly reads as an authentic, speculative Y2K metallic composition before reading the page title.
- [ ] Polished chrome reflections, liquid silver surfaces, and chamfered geometric framing are visibly rendered.
- [ ] The three native expressions (Chrome, Holographic, Retro Tech) resolve with distinct material cues and appropriate depth density.
- [ ] High-contrast focus indicators (`:focus-visible`) are prominent across all interactive elements (`0 0 0 3px rgba(136, 101, 221, 0.65)`).
- [ ] Paired dark (Deep Space & Liquid Chrome) and light (Liquid Silver & Iridescent Cloud) modes flip background and text in tandem with zero color collisions.
- [ ] `prefers-reduced-motion` is fully honored, disabling all non-essential transforms.
- [ ] Pure CSS and SVG styling are utilized without requiring heavy WebGL or unoptimized 3D libraries.

## Functional checks

1. **First-viewport recognition test:** Capture the opening viewport at desktop width. Can a reviewer recognize authentic Y2K Futurism chrome precision, iridescent accents, and speculative tech geometry without reading the title? If no, strengthen chrome reflections and chamfered framing.
2. **Responsive resizing:** Resize across 320, 390, 768, 1024, 1440, and 1920px. Content flows without horizontal scrollbars, and mobile header collapses into an accessible hamburger drawer.
3. **200% text zoom:** Enlarge typography to 200%; verify content wraps cleanly without breaking header buttons or clipping copy.
4. **Theme coupling & anti-collision:** Toggle between Dark (Deep Space) and Light (Liquid Silver) modes. Ensure text, borders, and buttons flip in synchronized pairs with no black-on-black or white-on-white collisions.
5. **Interactive expression switching:** Test switching between Chrome, Holographic, and Retro Tech variants; verify tokens and surfaces update live.
6. **Keyboard navigation:** Tab through all controls in the component gallery and studio preview; verify visible `:focus-visible` outlines.
7. **Reduced motion:** Enable `prefers-reduced-motion`; verify all transitions disable cleanly while functionality remains intact.
