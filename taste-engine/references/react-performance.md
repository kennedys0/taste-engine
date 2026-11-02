# React / Next.js Performance — conditional layer

Activate only after confirming React or Next.js through user instructions, `package.json`, or code. This is a compact original interpretation of Vercel's React Best Practices: https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices . Version-sensitive APIs require project compatibility checks.

## Priority 1 — avoid network waterfalls

- Identify dependent vs independent requests; launch independent fetches concurrently when safe. Don't move every fetch to the client by reflex.
- For Next.js, prefer appropriate server-side data fetching and streaming boundaries when the installed version supports them. Preserve authorization and cache correctness across users.
- Avoid sequential requests caused by avoidable component nesting. Never cache user-private data across request boundaries without correct scoping.

## Priority 2 — ship less JavaScript

- Audit expensive packages, large icons/visualization libraries, unnecessary barrel imports and client-only subtrees.
- Keep static layout on the server if using compatible Next.js Server Components; isolate interactive islands. Lazy-load heavy functionality when needed, without hiding the primary action.
- Anime.js v4 is optional, not a prerequisite for micro-interactions. Don't bundle it to animate a single hover when CSS is sufficient.

## Priority 3 — optimize rendering and interaction

- Avoid unnecessary subscriptions and expensive recomputation in render. Derive simple state from props/state rather than syncing with effects.
- Memoize *measurably expensive* calculations/components, not every value; use stable references only when doing so solves an actual issue.
- Keep form input updates responsive, prevent duplicate submissions, cleanup listeners and animation scopes.
- For large feeds/tables, consider virtualization with keyboard and screen-reader behavior tested; avoid virtualizing short lists.

## Priority 4 — visuals, motion and web vitals

- Preserve image dimensions and reserve layout space. Avoid content jumping during asynchronous data or animated transitions.
- Prefer GPU-friendly animated properties, honor reduced-motion, and don't use `transition: all`.
- Measure initial load, responsiveness and layout stability in a real environment; don't claim Core Web Vitals improvements before profiling.

## Agent protocol

1. Inspect framework/runtime versions and existing dependencies.
2. Check network/devtools/React profiler evidence when available; otherwise label findings as hypotheses.
3. Prioritize correctness and authorization, then network waterfall/bundle weight, then render work, then micro-optimizations.
4. Prefer small scoped changes and preserve behavior. Run project tests/build, audit the resulting UI across widths if feasible.
5. Explain impact as expected unless measured. Never force a Next-specific optimization into Vue, Svelte or plain HTML.
