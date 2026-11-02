# Motion routing + quality acceptance

These are scenarios for agent/browser smoke tests, **not** claims that real browser testing has already happened.

| Prompt | Expected behavior |
| --- | --- |
| "Build a portfolio" | Ask ONE style question and STOP before UI code; do not preload Anime.js |
| "A Skeuomorphism portfolio with tactile buttons" | Select pack explicitly, add SEO for public portfolio, consider motion; no extra style interview |
| "Tambahkan micro-interaction ke tombol existing" | Preserve project style, no selection menu, CSS first; Anime.js only when justified |
| "Portfolio brutalism animasi minimal" | Use instantaneous/short state changes; no bounce or perpetual transitions |
| "Buat dashboard privat enterprise" | No public SEO injection; restrained functional motion only |
| "Build a glassmorphism landing page with no animations" | Do not animate, even if style recipe mentions motion |
| "Build a React page using Anime.js v4" | Use named ESM imports; useEffect + createScope + revert; avoid V3 API |
| "Build a native iOS UI with Anime.js" | Explain DOM engine mismatch; use native animation approach |
| "Fix animation accessibility" | Honor reduced-motion; focus/touch/keyboard remain functional |
| "Build a loading button showing 99% progress" | Never invent progress; show real pending state only |

## Real browser review (requires tools)

- Confirm normal, focus, keyboard Enter/Space, touch and reduced-motion operation.
- Confirm no navigation/content is blocked while the animation runs.
- Confirm no looping, compositing conflicts or transform buildup in repeated clicks.
- Verify mount/unmount leaves no stray listeners or animation instances.
- Test at mobile and desktop viewport; measure performance where tools exist. Never invent numbers.
