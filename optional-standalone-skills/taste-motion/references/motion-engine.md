# Motion Engine Adapter — Anime.js v4 (optional)

**Purpose:** add meaningful micro-interactions that match the user's selected aesthetic. **This is a guidance module, not a runtime engine, plugin, or auto-installer.** It never changes the style-selection preflight and never adds Anime.js automatically to every generated project.

## Activation and dependency decision

1. **Only inspect this module for visible UI motion work** (new interactive UI after style resolution, a requested micro-interaction, or a motion audit). No need on backend, copy-only, or SEO-only tasks.
2. If the user asks solely to improve interactions in an established UI, preserve its existing style and skip the style selection menu. A new unnamed visual product still requires the one-question taste preflight before any UI code.
3. First inspect `package.json`, lockfile, existing styling/animation tools, client boundaries, and installed motion dependencies. **If CSS transitions or the existing motion solution meet the requirements, use those and do not add Anime.js.**
4. Only recommend/install `animejs` when a justified interaction needs coordinated keyframes, SVG morph/path control, fine timeline control, or when Anime.js was explicitly requested. Do not mix it with Framer Motion/GSAP for the same DOM properties. Never install dependencies in the generated project without following that project's dependency/change policy.
5. Load exactly one style profile from `styles/motion-profiles.json` plus the selected style pack's `## Motion` section. Those define direction; do not synthesize an unrelated animation aesthetic. User/project instructions override aesthetic defaults, but not accessibility or truthful functionality.
6. **Start static.** Motion must improve confirmation, continuity, orientation, or affordance. If removal does not reduce comprehension, leave it out.

## Anime.js V4 API — no V3 snippets

- NPM package is `animejs`: `npm install animejs` (only after deciding it is needed).
- Use named ESM imports: `import { animate, createScope } from 'animejs'` — **not** `import anime from 'animejs'` or `anime({ targets: ... })` from V3.
- For simple animations with compositor-friendly properties, consider `import { waapi } from 'animejs'` then `waapi.animate(...)`. Full `animate(...)` supports more control when needed; WAAPI has feature limits.
- In React and Next.js client components, create scoped animations inside `useEffect` with `createScope({ root: ref })`, register click methods on scope, then clean up using `scope.revert()` on unmount. Never run browser animations inside server components or render bodies.
- `Scope` supports `mediaQueries`, including `'(prefers-reduced-motion: reduce)'`; short-circuit or zero the nonessential animation, **not** the real state change.
- Use small transform/opacity transitions where possible. Avoid repeatedly animating layout-affecting properties (`top`, `left`, `width`, `height`), expensive blurs, or scroll-linked changes in large lists. No infinite loops for decorative movement, and no loading animation that implies real progress falsely.
- On touch, focus and keyboard, the core feedback and action must remain available. A hover reveal cannot hide essential information.

## Universal motion quality tiers

- **FLOOR (must pass)**: usable without animation; meaningful focus/keyboard/touch states; reduced-motion behavior; no autoplay that obscures content; semantic state and action are real; screen-reader updates do not depend on movement; animation cleanup exists; no hydration/SSR breakage.
- **REFLEX (fix unless defended)**: bounce/elastic default, simultaneous entrance on every card, perpetual floating elements, scroll hijacking, decorative typing, animated blur/glow, staggered transactional information, hidden content until JS runs, unnecessary animation dependency.
- **FINISH (nice to have)**: coherent ease/duration tokens, consistent press direction, no transform conflict with existing CSS, reduced layout/repaint cost, mobile acceptance at low-power settings.

## Practical thresholds (design guidance, not WCAG requirements)

- Button press: roughly 80–200 ms. Small navigation/segment transitions: roughly 120–220 ms. Dialog/region changes only if they improve continuity and do not delay operation.
- 1–3px travel / 1–2% scale is plenty for tactile UI; the exact travel depends on selected style. **Brutalism and Retro Terminal can validly choose zero animation.**
- Never fake loading with an animation; always pair real async state with real progress or neutral pending text.

## React example

Open [`../examples/react/anime-v4-press.jsx`](../examples/react/anime-v4-press.jsx) for a user-triggered, keyboard-accessible press + real details toggle, scoped React lifecycle, and reduced-motion handling. This is an example **not** an imperative for every button. Adapt duration and interaction to the selected style and avoid double-animation if the component already has a CSS transform transition.

## Framework notes

- Vanilla JS: select a local node after DOM ready; stop/revert animations when replacing UI; respect reduced-motion media query.
- Vue/Svelte: initialize in the mounted lifecycle and cleanup on unmount; use element refs rather than global class selectors.
- Next.js App Router: keep static markup/SEO in server components and use small `'use client'` interaction leaf components only where needed.
- Native apps: Anime.js targets web DOM/SVG/JS objects; do **not** apply it as a substitute for native Compose, SwiftUI, or Flutter motion APIs.

## Failure modes / anti-slop

- An installed motion package is not permission to animate. Don't add animation to satisfy a quota.
- Shadows, translucency and texture should be treated as the chosen material; animating those can be expensive. Prefer subtle transform/opacity where a motion effect is justified.
- If the user explicitly requests 'no animation', disable decorative and optional motion even if a style pack has a motion recipe.
- Review the final render at reduced motion, keyboard-only, touch/mobile, and under slower CPU if possible; **do not claim measured fps, Web Vitals or tested devices without actual evidence.**

## Source references (consult for implementation updates)

- Installation / ES modules: https://animejs.com/documentation/getting-started/installation/
- React with Scope cleanup: https://animejs.com/documentation/getting-started/using-with-react/
- Scope media queries: https://animejs.com/documentation/scope/scope-parameters/mediaqueries/
- WAAPI vs JS animate: https://animejs.com/documentation/web-animation-api/when-to-use-waapi/
- Compositor properties: https://animejs.com/documentation/web-animation-api/hardware-accelerated-animations/
