# Claymorphism visual acceptance tests

These are **manual visual and behavior tests**, not claims of executed browser tests.

## Explicit clay depth exception

- [ ] Reviewers do **not** reject dual inner shadows or ambient drop shadows simply for being decorative: they are the essential material properties that define molded, touchable clay.
- [ ] Opposing dual inner shadows appear on raised surfaces: an upper-left inner highlight (incident light) and a lower-right inner form shadow (volumetric curve).
- [ ] Sunken wells (input fields, inactive tracks) use inverted inset depth and an optional crisp white relief rim (`3px solid rgba(255, 255, 255, 0.85)`).
- [ ] Material styling remains coherent with brand color and typography, never relying on cartoonish floating blobs or unreadable low contrast.

## Fail the style when

- [ ] The opening viewport uses flat rectangular cards with simple border-radius and standard single box-shadow, falsely labeling it "clay".
- [ ] Surfaces have only an outer drop shadow with no inner volumetric highlights, looking flat rather than molded.
- [ ] Hard black drop shadows or harsh outline borders replace soft tinted ambient shadows.
- [ ] Input fields are flat white boxes with standard borders instead of sunken tactile wells with relief rims.
- [ ] Interactive buttons have no tactile compression, displacement, or shadow response on hover/press.
- [ ] Text contrast fails WCAG AA standards (e.g. low-contrast light purple text on pale lavender backgrounds).
- [ ] Giant puffy cards are nested 3–4 layers deep, starving the page of information hierarchy.

## Pass the material when

- [ ] Prominent raised controls (buttons, badges, toggle thumbs) visibly read as physical, soft, tactile clay pieces.
- [ ] Dual inner shadows give objects noticeable 3D curvature and volumetric thickness without gloss or glare.
- [ ] Saturated clay (e.g. vibrant purple `#813FFC`) and neutral porcelain clay (e.g. soft off-white `#ECEBF5`) exist harmoniously with calibrated text contrast.
- [ ] Sunken wells provide clear, recessed polarity for inputs and form controls.
- [ ] Controls respond physically on click/tap with subtle scale down (`scale(0.97)`) and tightened shadows.
- [ ] High-contrast focus indicators (`:focus-visible`) are prominent and unobstructed by shadows.
- [ ] Accessible fallback and `prefers-reduced-motion` are supported cleanly.

## Functional checks

1. Capture the first viewport at desktop width. Can you recognize *molded tactile clay* without reading a label? If no, revise shadows.
2. Resize across 320, 390, 768, and 1440px. Buttons, inputs, and toggle controls remain comfortably clickable (minimum 44x44px touch targets).
3. Toggle keyboard focus across primary and secondary controls; verify visible focus rings.
4. Click and hold buttons: verify the tactile compression press state (`translateY(2px)`, tightened shadow).
5. Apply `prefers-reduced-motion`: verify animated translations and transforms disable cleanly.
6. Verify form fields: text remains legible with clear placeholder contrast and focused relief border.

## Example target character (not pixel copying)

- **Primary Saturated Clay Reference:** Vibrant violet/purple pill button ("Submit >") with white text, top-left bright white inner highlight, bottom-right deep purple inner shadow, and soft tinted drop shadow.
- **Light Porcelain Clay Reference:** Soft off-white pill button ("Go Back ↶") with dark slate-purple text, crisp upper-left inner highlight, soft gray-lavender lower-right inner shadow, and ambient depth.
- **Circular Action Reference:** Round purple clay button (50% radius) with centered pause icon (`❚❚`).
- **Interactive Controls Reference:** Dual-state toggle switch with smooth tactile thumb and squircle checkbox with vibrant checkmark.
- **Sunken Input Field Reference:** Recessed lavender well container with white relief border rim (`3px solid rgba(255, 255, 255, 0.85)`), muted lavender placeholder and icon.
- **Reject:** A flat minimal layout with CSS variables named `--clay` that possesses no volumetric dual inner shadows.

If no actual browser/screenshots were reviewed, report these as acceptance criteria **to be validated**, not passed tests.

