# Retro Pixel visual acceptance tests

These are **manual visual and behavior tests**, not claims of executed browser tests.

## Explicit retro pixel exception

- [ ] Reviewers do **not** reject pixel illustrations, stepped borders, classic desktop title bars, window controls, background grids, or 0-blur drop shadows: they are the essential material properties that define the Retro Pixel aesthetic.
- [ ] Stepped bevels appear on window panels and buttons: an upper-left light highlight and lower-right dark shadow simulating physical 3D elevation.
- [ ] Inset panels and wells (input fields, command viewports) use inverted inset bevels and deep well grounds.
- [ ] Pixel graphics and sprite assets use `image-rendering: pixelated` to guarantee hard pixel edges without interpolation blur.
- [ ] The style is unmistakably distinct from Retro Terminal (no CRT scanline phosphor glow requirement, features graphical desktop windows and pixel art) and Neo-brutalism (pixel rendering, classic GUI metaphors).

## Fail the style when

- [ ] The opening viewport uses modern flat cards with standard border-radius and a pixel font, falsely labeling it "retro pixel".
- [ ] Raster pixel art illustrations are blurry or anti-aliased due to missing `image-rendering: pixelated`.
- [ ] Text contrast fails WCAG AA standards (e.g. pale cream text on beige window panels in light mode, or dark navy text on midnight canvas).
- [ ] Desktop operating system metaphors (title bars, minimize/close buttons) are entirely decorative nonfunctional dummies disguised as controls.
- [ ] Long body paragraphs are rendered in tiny, illegible 8px pixel fonts instead of readable humanist sans-serif or clean monospace.
- [ ] The layout breaks or causes horizontal scroll blowout on narrow screens down to 320px viewport width.
- [ ] Circular elements (status badges, avatars) distort into ovals when compressed on mobile viewports.

## Pass the material when

- [ ] Prominent raised desktop windows visibly read as classic personal computer interfaces (Windows 95 / Amiga / Macintosh System 7 era).
- [ ] Title bars feature clear window titles, icons, and functional interactive controls (close, minimize, or toggle).
- [ ] Buttons physically depress along the integer grid on press (`transform: translate(2px, 2px)`) with instant or snappy stepped feedback.
- [ ] The reference palette (midnight canvas `#10102B`, retro teal `#2CA7A3`, arcade orange `#F27D36`, desktop purple `#5B438E`, vintage cream `#F2DFB5`) is calibrated across both dark and light modes with WCAG AA compliance.
- [ ] Pixel art illustrations (vintage computer, floppy disk, folder icons, game cartridges) are integer-scaled and purposeful.
- [ ] High-contrast focus indicators (`:focus-visible`) are prominent and visible across all controls.
- [ ] Accessible fallback and `prefers-reduced-motion` are supported cleanly.

## Functional checks

1. **First-viewport recognition test:** Capture the opening viewport at desktop width. Can a reviewer recognize an authentic Retro Pixel interface without reading the title? If no, strengthen desktop window chrome and stepped border treatments.
2. **Responsive resizing:** Resize across 320, 390, 768, 1024, 1440, and 1920px. Windows flex smoothly into single-column modules on mobile with zero horizontal blowout. Touch targets remain comfortable (minimum 44x44px).
3. **200% text zoom:** Enlarge typography to 200%; verify content wraps cleanly without breaking window headers or truncating essential buttons.
4. **Theme coupling & anti-collision:** Toggle between Dark (Midnight Arcade Grid) and Light (Vintage Parchment Workstation) modes. Ensure text, title bars, and borders flip in synchronized pairs with no black-on-black or white-on-white collisions.
5. **Interactive window actions:** Test interactive windows. Close button hides or dismisses the window; reopening restores it cleanly.
6. **Form validation & states:** Input text in fields; check active focus ring, placeholder readability, and error/success states.
7. **Keyboard navigation:** Tab through all controls in the component lab and authentication form; verify visible `:focus-visible` outlines and Enter/Space activation.
8. **Reduced motion:** Enable `prefers-reduced-motion`; verify all translations and transforms disable cleanly while interactions remain functional.

## Example target character (not pixel copying)

- **Desktop Window Reference:** Midnight indigo panel with desktop purple title bar (`#5B438E`), white title text, miniature close button, and stepped bevel border.
- **Arcade Primary Button Reference:** Vibrant arcade orange rectangular button (`#F27D36`) with stepped 3D shadow and 2px press displacement.
- **Vintage Computer Illustration:** Pixel-art vintage beige monitor with teal screen and blinking prompt.
- **Reject:** A generic dark landing page with monospace font and orange buttons that lacks retro window geometry and pixel precision.

If no actual browser/screenshots were reviewed, report these as acceptance criteria **to be validated**, not passed tests.

