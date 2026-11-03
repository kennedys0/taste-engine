# Web Interface Quality — universal UI engineering gate

A framework-neutral acceptance checklist informed by the publicly available Vercel Web Interface Guidelines. This is an independent, paraphrased Taste Engine rulebook; upstream: https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines and https://github.com/vercel-labs/web-interface-guidelines .

## FLOOR: functional, accessible and honest

- Semantic links navigate; semantic buttons act. Keyboard users can reach, trigger and dismiss controls; tab order reflects logical reading order.
- Give every field an actual label and meaningful input type; show errors beside the relevant input with a useful fix. Don't prevent paste. For destructive/irreversible actions offer confirmation or undo.
- Focus indication is visible with keyboard interaction; fixed/sticky UI cannot hide the focused control. Modal keyboard management preserves/returns focus.
- Icon-only controls have accessible names; decorative art is hidden from assistive technology; meaningful images have alternative text; status/error updates are announced appropriately.
- Minimum contrast and tap targets follow accessibility guidance; don't disable browser zoom. Test mobile portrait, landscape, keyboard appearance, 200% zoom where applicable.
- Dark/light mode theme integrity: when dark mode or light mode is activated, all color tokens (canvas, elevated surfaces, headings, body, muted captions, borders, input wells, hover/active states, and semantic status pills) must flip in synchronized pairs. Ensure WCAG AA contrast (minimum 4.5:1 normal text, 3:1 large text and interactive boundaries). Never leave black text on dark backgrounds or white text on light backgrounds.
- Motion respects reduced-motion preferences. Decorative animations must never prevent reading/operating content; when needed, provide a pause/stop path.
- Never misrepresent loading, online, verified, successful, or financial states; component interactivity must be backed by actual functionality.

## REFLEX: catch routine implementation slop

- Avoid `transition: all`, unnecessary layout-property animations and perpetual loops. Prefer focused opacity/transform transitions, though the user-selected aesthetic may call for an instant state flip.
- Don't leave images with missing intrinsic dimensions; lazy-load noncritical below-fold images but prioritize true above-fold hero imagery.
- Don't let long labels/values spill out of grids. Check `min-width: 0`, wrapping behavior and empty/huge content variants.
- Native scrolling and navigation should keep expected behavior: proper links (including new-tab behavior), URL/address-bar state when shareable, safe areas on phones, scroll containment for modals.
- Avoid measuring layout in React render; avoid over-rendering long lists and unnecessary DOM read/write churn.
- Dates and currencies should be formatted for the correct user locale; use reliable internationalization APIs, not hardcoded formats.
- Do not create nested cards, tooltips, badges, tabs or artificial status lights to make a layout seem complete. Every element should solve a real task.

## FINISH: deliberate craft

- Review type wrapping, labels, focus/hover/active/disabled/empty/loading/error states, image resolution, color-scheme, touch hover mismatch, orientation and optical alignment.
- Compare desktop and mobile composition, not just shrinking behavior.
- Run browser and accessibility checks when tools are available. Consider keyboard-only, screen-reader, long-content and reduced-motion passes. Distinguish tested outcomes from planned checks.

## Evidence format

For a code audit, cite actual `path:line`, describe why it matters and propose the smallest fix. For conceptual design guidance, describe patterns without inventing locations or grades. **Never claim WCAG compliance solely from scanning source code**; runtime and manual validation can be required.
