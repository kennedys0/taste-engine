# Engineering router — Vercel-inspired conditional guidance

This is a **Taste Engine authored integration**, based on reading the public Vercel Agent Skills repository on 2026-11-02. It does not import, copy or install third-party skills. Source list and scope: [Vercel research](vercel-research.md).

## Priority and activation order

1. **Interpret user intent.** For new/major visual UI work, run the existing style selection preflight first. If style is missing, ask once and stop; do not preemptively start implementation because another skill applies. If the style is stated or the product's approved system is in place, proceed. For small UI fixes, skip re-selection. For docs-only, backend-only, deployment-only and SEO-only work, do not open a style selector.
2. **Inspect actual project signals.** Read package manifests/lockfiles, framework versions, relevant code and routing structure. Infer capabilities from actual dependencies, not the user's mention of “website” alone. Check framework-specific APIs are available before using them.
3. **Use the universal web quality gate** for any web UI implementation, redesign or UI audit: [web-interface-quality](web-interface-quality.md). Applicable for any framework, even plain HTML.
4. **Conditionally load framework guidance.** React/Next → [react-performance](react-performance.md); reusable React component APIs → [react-composition](react-composition.md). React Native/Expo → [native-mobile](native-mobile.md). These are *not* framework mandates. Vue, Svelte, Astro, plain HTML and native platforms keep their own best practices; do not force React packages.
5. **Motion trigger.** For navigation/shared-element continuity in React when compatible APIs exist, examine [view-transitions](view-transitions.md). Do not replace the existing [motion engine](motion-engine.md) by default; choose least complexity. No gratuitous transitions or new dependencies for appearance alone.
6. **Writing trigger.** For product copy, apply existing [anti-slop copywriting](anti-slop-copywriting.md). For README/docs/tutorials/reference, additionally load [docs-writing](docs-writing.md). Do not let documentation rules blindly control UI labels or user-selected brand voice.
7. **SEO trigger.** Public, crawlable websites also load [seo](seo.md) and existing hero contract where appropriate; authenticated dashboards/native apps do not receive public indexing optimizations.
8. **Review the result, not only the code.** Record verified findings with file and line number, severity, reason and specific correction. Run automated and browser tests where available; if unavailable say so. Do not claim a green test that was never executed.

## Route table

| Task | Always | Conditional | Never auto-enable |
|---|---|---|---|
| Build public portfolio (style missing) | One style question, then stop | On reply: web quality + SEO + hero + matching framework | No code before selection |
| Build brutalist Next.js portfolio | Selected style + web quality + SEO + hero | React performance; composition if reusable components; motion only when warranted | Don't re-ask or replace aesthetic |
| Fix React dashboard re-renders | Existing design + React performance + relevant UI quality | Composition for structural refactor | Don't inject hero/SEO/style picker |
| Audit HTML accessibility | Web quality | Framework checks only if manifest shows it | Don't force redesign or dependencies |
| Make Expo mobile app | Style preflight if new visual UI + native mobile | Accessibility + platform motion | Don't use web SEO or Anime.js for native UI |
| Write README | Docs writing + accurate instructions | Anti-slop writing | Don't ask for visual style |
| Add route transitions | Preserve style + view transitions when compatible | Motion adapter only if needed | Don't add both animation systems without reason |
| Deploy to Vercel | Confirm explicit deployment intent and destination | Refer to upstream deployment tool if installed | Don't deploy automatically on design task |

## Conflict precedence

1. Safety, accessibility, truthful data, preservation of functionality and user's explicit instructions.
2. Project/framework/platform technical constraints verified in code.
3. Explicit chosen visual style + approved brand design system.
4. Context-specific engineering guidance.
5. Optional polish.

Guidelines are heuristics unless a real correctness/accessibility problem is at stake. Avoid algorithmic aesthetic bans such as "no glassmorphism" when user deliberately chooses glass. `min-height: 100svh` hero policy remains conditional and content-safe. Do not change a functioning stack simply to match a particular upstream example.

## External skills coexistence

If user already installed relevant upstream Vercel skill(s), the agent may use those directly; **do not load duplicate detailed copies or pretend the user installed them**. Taste Engine's local references are self-contained, authored quality summaries and work offline. The source's mutable remote review command must not be fetched/executed blindly; inspect content before applying updates.
