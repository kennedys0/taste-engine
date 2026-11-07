# Y2K Futurism visual acceptance tests

These are **manual visual and behavior tests**, not claims of executed browser tests.

## Explicit Y2K Futurism exception

- [ ] Reviewers do **not** reject multi-stop liquid-chrome horizon gradients, iridescent spectral highlights, molded translucent colored plastic surfaces, or bespoke sculptural SVG centerpieces: they are essential material-enabling properties defining the Y2K Futurism ("The Millennium Future") aesthetic.
- [ ] Primary metallic surfaces use multi-band horizon chrome sequences (`linear-gradient(180deg, #ffffff 0%, #e5e9f1 22%, #a4adbf 47%, #424b60 50%, #7e889d 54%, #e5e9f1 82%, #ffffff 100%)`) with sharp specular transitions simulating liquid metal and polished consumer-electronics hardware.
- [ ] Iridescent spectral accents (`#90dcff`, `#5276ff`, `#a78aff`, `#f2a9dc`, `#f3eafd`, `#8fcfe9`, `#8865dd`, `#e6abd8`) and molded translucent colored plastic panels (`backdrop-filter: blur(12px) saturate(145%)`) provide authentic millennium materiality without washing out foreground typography.
- [ ] The style is unmistakably distinct from Frutiger Aero (no nature/aqua/leaf imagery), generic dark Vaporwave, neon Cyberpunk, and flat dark SaaS dashboards.

## Fail the style when

- [ ] The interface relies on a conventional dark SaaS landing page with centered headline typography, 4 generic telemetry stat cards, and thin grey outlines.
- [ ] Split-column card stacks are unbalanced (e.g., a tall left card next to shorter stacked right cards leaving dead empty space below), or 4 buttons/checkboxes wrap into a `3 + 1` orphan row.
- [ ] The opening hero is cluttered with self-congratulatory quality badges (*"WCAG AA Contrast 4.5:1"*, *"New 10th Style"*, *"Zero AI-Slop"*, *"100% WCAG AA Gated"*).
- [ ] Chrome surfaces are flattened into dull 2-stop grey gradients without a horizon reflection band.
- [ ] Switching between `Chrome`, `Holographic`, and `Retro Tech` only swaps a single accent color without changing material treatment, centerpiece geometry, or panel framing.
- [ ] Rainbow text gradients (`-webkit-background-clip: text`) are applied to multi-line body copy or form labels, destroying legibility.
- [ ] Unreadable wide display typography is applied to multi-line body paragraphs.
- [ ] Text contrast fails WCAG AA standards (e.g. muted graphite text on dark obsidian backgrounds or pale white text on bright chrome or pearl panels).
- [ ] Horizontal layout overflow occurs on narrow mobile viewports down to 320px.
- [ ] Circular UI elements (orbs, rotary controls, status indicators, icon buttons) deform into squished ovals on mobile screens.
- [ ] Emojis are used as primary interface icons, buttons, or status badges.

## Pass the material when

- [ ] The opening desktop hero visibly reads as an authentic Y2K Futurism composition (asymmetric expressive display typography, sculptural liquid-metal orb & orbital chrome rings centerpiece, and integrated hardware command console) before reading the page title.
- [ ] All four synthetic materials — Liquid Chrome, Iridescent Spectral Material, Translucent Colored Plastic, and Synthetic Metallic Hardware Panels — are visibly convincing and distinct.
- [ ] All multi-column card grids and split-column card stacks (`.y2k-balanced-stack` / `.taste-y2k-balanced-stack`) stretch to equal height (`flex: 1 1 0%`) so top and bottom edges align flush with zero empty voids.
- [ ] Three-tier typography hierarchy (extended futuristic display with chrome/outline lockups, geometric technical interface labels, and clean sans-serif body copy) is clear and legible.
- [ ] The three native expressions (`Chrome`, `Holographic`, `Retro Tech`) resolve with distinct material finishes, sculptural centerpieces, and hardware/polymer framing.
- [ ] High-contrast focus indicators (`:focus-visible`) are prominent across all interactive elements.
- [ ] Paired Light Mode (Pearl Silver & Brushed Aluminum) and Dark Mode (Deep Titanium & Liquid Chrome) environments feel intentionally designed around reflective materiality with zero color collisions.
- [ ] `prefers-reduced-motion` is fully honored, disabling all non-essential transforms and orbital animations.
- [ ] Pure CSS and SVG styling are utilized without requiring heavy WebGL or unoptimized 3D libraries.

## Functional checks

1. **First-viewport recognition test:** Capture the opening viewport at desktop width. Can a reviewer recognize authentic Y2K Futurism liquid chrome, sculptural orbital geometry, and expressive millennium typography without reading the title? If no, strengthen multi-band chrome reflections, asymmetric composition, and centerpiece presence.
2. **Responsive resizing:** Resize across 320, 390, 768, 1024, 1440, and 1920px (as well as 375px mobile). Hero recomposes cleanly on mobile, content flows without horizontal scrollbars, and mobile header collapses into an accessible hamburger drawer.
3. **200% text zoom:** Enlarge typography to 200%; verify content wraps cleanly without breaking header buttons or clipping copy.
4. **Theme coupling & anti-collision:** Toggle between Light (Pearl Silver & Chrome) and Dark (Deep Graphite & Liquid Mercury) modes. Ensure text, bevels, and specular highlights flip in synchronized pairs with no black-on-black or white-on-white collisions.
5. **Deep variant switching:** Test switching between `Chrome`, `Holographic`, and `Retro Tech` variants; verify material surfaces, centerpiece sculpture, typography accents, and panel framing update live.
6. **Keyboard navigation:** Tab through all controls in the material laboratory, component gallery, and studio preview; verify visible `:focus-visible` outlines.
7. **Reduced motion:** Enable `prefers-reduced-motion`; verify all transitions and orbital rotations disable cleanly while functionality remains intact.
