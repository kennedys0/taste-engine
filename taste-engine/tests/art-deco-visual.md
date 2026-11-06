# Art Deco visual acceptance tests

These are **manual visual and behavior tests**, not claims of executed browser tests.

## Explicit art deco exception

- [ ] Reviewers do **not** reject architectural double lines, stepped corner brackets, symmetrical header dividers, or flat metallic finishes: they are essential design grammar defining the Art Deco aesthetic.
- [ ] Stepped geometric corner silhouettes appear on cards, buttons, or frames, replacing rounded bubble corners.
- [ ] Symmetrical dividers feature central diamond or chevron medallions with balanced horizontal hairline wings.
- [ ] Metallic finishes (Antique Gold `#B89B5E`, Muted Brass `#B69A68`, Bronze `#A98462`) are applied as flat tones or crisp line art, never as multi-stop yellow gradients.
- [ ] The style is unmistakably distinct from generic luxury templates (architectural framing, multi-tiered typography, purposeful ornamentation).

## Fail the style when

- [ ] The interface relies on diagonal yellow-to-white gradients simulating "gold shine" or glowing yellow button shadows.
- [ ] Cards use generic rounded SaaS border radii (`1.5rem–2rem`).
- [ ] Random unaligned fan shapes or decorative emojis are plastered across the page as filler.
- [ ] Text contrast fails WCAG AA standards (e.g. pale gold text on white canvas or dark charcoal text on obsidian night).
- [ ] Decorative corner brackets cause horizontal layout overflow on narrow viewports down to 320px.
- [ ] Continuous animation loops (spinning fans, glittering sparkles) run indefinitely and delay user interaction.
- [ ] Circular elements (monograms, status gems) distort into ovals under flexbox compression.

## Pass the material when

- [ ] The opening desktop hero visibly reads as an architecturally composed, geometrically disciplined design system before reading the title.
- [ ] Symmetrical axial alignment and balanced proportions govern the layout.
- [ ] Multi-tiered typography (Display decorative/geometric uppercase, Editorial serif/geometric sans, Functional sans body) is clearly established.
- [ ] The three native expressions (Modern Deco, Classic Deco, Minimal Deco) resolve with distinct palettes and appropriate ornamentation density.
- [ ] High-contrast focus indicators (`:focus-visible`) are prominent across all interactive elements (`outline: 2px solid var(--taste-deco-accent)`).
- [ ] Paired light and dark modes invert background and text cleanly with zero color collisions.
- [ ] `prefers-reduced-motion` is fully honored, disabling all non-essential transforms.

## Functional checks

1. **First-viewport recognition test:** Capture the opening viewport at desktop width. Can a reviewer recognize authentic Art Deco architecture without reading the title? If no, strengthen geometric framing and stepped corner details.
2. **Responsive resizing:** Resize across 320, 390, 768, 1024, 1440, and 1920px. Content flows without horizontal scrollbars, and mobile header collapses into an accessible hamburger drawer.
3. **200% text zoom:** Enlarge typography to 200%; verify content wraps cleanly without breaking headers or clipping buttons.
4. **Theme coupling & anti-collision:** Toggle between Dark (Obsidian Pine / Night) and Light (Warm Cream / Ivory) modes. Ensure text, borders, and buttons flip in synchronized pairs with no black-on-black or white-on-white collisions.
5. **Interactive expression switching:** Test switching between Modern, Classic, and Minimal Deco variants; verify tokens update live.
6. **Keyboard navigation:** Tab through all controls in the component gallery and authentication preview; verify visible `:focus-visible` outlines.
7. **Reduced motion:** Enable `prefers-reduced-motion`; verify all transitions disable cleanly while functionality remains intact.

