# Web Interface Quality — universal UI engineering gate

A framework-neutral acceptance checklist informed by the publicly available Vercel Web Interface Guidelines. This is an independent, paraphrased Taste Engine rulebook; upstream: https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines and https://github.com/vercel-labs/web-interface-guidelines .

## FLOOR: functional, accessible and honest

- Semantic links navigate; semantic buttons act. Keyboard users can reach, trigger and dismiss controls; tab order reflects logical reading order.
- Give every field an actual label and meaningful input type; show errors beside the relevant input with a useful fix. Don't prevent paste. For destructive/irreversible actions offer confirmation or undo.
- Focus indication is visible with keyboard interaction; fixed/sticky UI cannot hide the focused control. Modal keyboard management preserves/returns focus.
- Icon-only controls have accessible names; decorative art is hidden from assistive technology; meaningful images have alternative text; status/error updates are announced appropriately.
- Minimum contrast and tap targets follow accessibility guidance; don't disable browser zoom. Test mobile portrait, landscape, keyboard appearance, 200% zoom where applicable.
- Dark/light mode theme integrity: when dark mode or light mode is activated, all color tokens (canvas, elevated surfaces, headings, body, muted captions, borders, input wells, hover/active states, and semantic status pills) must flip in synchronized pairs. Ensure WCAG AA contrast (minimum 4.5:1 normal text, 3:1 large text and interactive boundaries). Never leave black text on dark backgrounds or white text on light backgrounds. For dark mode, avoid harsh pitch-black (`#000000` or raw `#0d0f14`) canvas unless specifically requested; prefer warm neutral dark slate-grey (Codex palette: canvas `#212328`, surfaces `#2b2e36`, elevated `#343842`, recessed wells `#1a1c21`, subtle borders `rgba(255, 255, 255, 0.12)`) for lower eye strain and rich surface hierarchy.
- Mobile typography and component anti-bloat: scale typography and spacing down proportionally on mobile viewports (< 768px, < 480px) to prevent inflated interfaces ("UI bengkak"). Monospace code blocks must use `word-break: break-all` / `overflow-x: auto` to prevent horizontal layout blowout.
- Single-line inline command alignment ("sejajarin"): quick install pills, command snippets, and copy buttons must remain strictly inline in a single horizontal row (`display: inline-flex; flex-direction: row; align-items: center; justify-content: center;`) with `line-height: 1; flex-shrink: 0;`. Do not break prompt `$`, code, and copy button into vertical stacked rows.
- Mobile footer architecture: avoid endless 1-column link dumps. Organize navigation links into a balanced 2-column grid (`repeat(2, 1fr)`) with full-width brand header and tactile tap targets.
- Motion respects reduced-motion preferences. Decorative animations must never prevent reading/operating content; when needed, provide a pause/stop path.
- Never misrepresent loading, online, verified, successful, or financial states; component interactivity must be backed by actual functionality.

## REFLEX: catch routine implementation slop

- Avoid `transition: all`, unnecessary layout-property animations and perpetual loops. Prefer focused opacity/transform transitions, though the user-selected aesthetic may call for an instant state flip.
- Don't leave images with missing intrinsic dimensions; lazy-load noncritical below-fold images but prioritize true above-fold hero imagery.
- Don't let long labels/values spill out of grids. Check `min-width: 0`, wrapping behavior and empty/huge content variants.
- Native scrolling and navigation should keep expected behavior: proper links (including new-tab behavior), URL/address-bar state when shareable, safe areas on phones, scroll containment for modals.
- Avoid measuring layout in React render; avoid over-rendering long lists and unnecessary DOM read/write churn.
- Dates and currencies should be formatted for the correct user locale; use reliable internationalization APIs, not hardcoded formats.
- Do not create nested cards, tooltips, badges, tabs, artificial status lights, rainbow text gradients (`background-clip: text`), cartoon emojis as functional icons (use crisp inline SVGs), or fabricated dashboard widgets (weather, audio spectrum, fake telemetry) to make a layout seem complete. Every element should solve a real task.

## FINISH: deliberate craft

- Review type wrapping, labels, focus/hover/active/disabled/empty/loading/error states, image resolution, color-scheme, touch hover mismatch, orientation and optical alignment.
- Compare desktop and mobile composition, not just shrinking behavior.
- Run browser and accessibility checks when tools are available. Consider keyboard-only, screen-reader, long-content and reduced-motion passes. Distinguish tested outcomes from planned checks.

## Evidence format

For a code audit, cite actual `path:line`, describe why it matters and propose the smallest fix. For conceptual design guidance, describe patterns without inventing locations or grades. **Never claim WCAG compliance solely from scanning source code**; runtime and manual validation can be required.
