# Glassmorphism visual acceptance tests

These are **manual visual and behavior tests**, not claims of executed browser tests.

## Explicit gradient exception

- [ ] Reviewers do **not** reject restrained radial, linear or mesh gradients simply for being decorative: they are valid light-field backdrops behind glass.
- [ ] At least one gradient/light-field transition appears behind and partly outside a primary glass pane, allowing comparison between frosted and exposed material.
- [ ] Backdrop remains coherent with the brand, static unless motion has a clear purpose, and never overpowers the content.
- [ ] A light or dark gradient is **not** sufficient by itself; the actual glass surface must still visibly filter that backdrop.

## Fail the style when

- [ ] The opening viewport is a flat navy/white background plus ordinary text/CTA with no prominent frosted surface.
- [ ] A panel is almost fully opaque, so its “glass” quality comes only from its rounded shape, glow or CSS class name.
- [ ] The only blurred element is the **background image**; no pane filters what is behind it.
- [ ] Backdrop filtering exists in CSS but visually cannot be perceived because the backdrop behind the pane is completely uniform.
- [ ] The page relies on dark cards and purple glows as a stand-in for actual translucency.
- [ ] Text or buttons become unreadable when ambient colors/background content change.

## Pass the material when

- [ ] There is a meaningful differentiated background at or near a visible foreground pane.
- [ ] The pane visibly **tints and frosts** the background while uncovered areas stay clearer.
- [ ] Edges/highlights show material separation without excessive glow or fake 3D decoration.
- [ ] Text, icons, actions and focus remain clear through the real composited colors.
- [ ] Both light/milky and dark/smoked interpretations are permitted; actual user reference directs which one to implement.
- [ ] The design doesn't force glass on long-form text, forms or tables that need solid contrast.

## Functional checks

1. Capture the first viewport at desktop width. Can you recognize *glass* without reading a label? If no, revise design.
2. Resize to 320, 390, 768, 1440px. At zoom/text enlargement, header + hero can grow, CTAs remain reachable and no panel clips.
3. Toggle keyboard focus and interactive states; verify focus/labels/error handling.
4. Disable `backdrop-filter` in DevTools or test unsupported browser: panel remains legible with opaque fallback.
5. Apply `prefers-reduced-motion`, forced colors, and `prefers-reduced-transparency` where available; visual effects must not block content.
6. On showcase demos, controls should actually work; demo toasts/statuses must not impersonate live production state.

## Example target character (not pixel copying)

- **Milky reference:** pale background, blue diffused light behind a generously frosted translucent white plane, soft rounded corners and bright edge.
- **Smoked reference:** deep ink ground with violet/cyan light, legible translucent dark-slate component containers, glass nav, controls and layered reflections.
- **Reject:** a plain dark page with centered heading and two opaque buttons, even if named “Glassmorphism.”

If no actual browser/screenshots were reviewed, report these as acceptance criteria **to be validated**, not passed tests.
