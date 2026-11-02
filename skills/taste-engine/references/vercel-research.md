# Vercel Agent Skills research, adoption and attribution

Research date: 2026-11-02. Public GitHub repository: https://github.com/vercel-labs/agent-skills/tree/main/skills . Repository README says MIT; some individual skill frontmatters also declare MIT. **Taste Engine has not copied their text or code** and does not bundle the original upstream skills; it adapts general engineering concepts in independently written language. If future contributors import upstream files, inspect individual file/repository licensing at that commit and preserve required attribution and notices.

| Upstream skill | We adopt as independent guidance | Why not bundle wholesale |
|---|---|---|
| web-design-guidelines | Semantic controls, accessibility, forms, focus, reduced motion, responsive audit | Full upstream checklist is fetched dynamically from another repo, changes over time; source-specific formatting and voice preferences are not universal |
| react-best-practices | No waterfalls, smaller client bundle, render profiling | React-only; version-aware; some tactics require evidence and code context |
| composition-patterns | Compound components, explicit variants, state ownership | React-only; don't create abstraction for single-use UI |
| react-view-transitions | Continuity and least-complexity motion selection | React/browser support evolves; Anime.js v4 already available as optional adapter |
| writing-guidelines | Task-oriented docs, honest examples, clear instructions | Vercel house style is not universal copy style; UI writing already covered |
| react-native-skills | Native navigation, list, image, safe-area and performance practices | Native-only; not web or generic mobile wireframes |
| deploy-to-vercel | Treat as optional separately installable deployment skill | Deployment changes live state; must not execute without explicit deployment intent |
| vercel-optimize | Metrics-first performance/cost investigations when user asks | Vercel-specific telemetry, authentication and permissions, not portable UI design |
| vercel-cli-with-tokens | Do not integrate into Taste Engine by default | Token workflows carry secret handling and scope risks; not part of visual skill |

## Important upstream caveats

- `web-design-guidelines/SKILL.md` and `writing-guidelines/SKILL.md` instruct agents to fetch living `command.md` files from separate repositories. Taste Engine does not silently fetch/execute mutable remote material; its local guidance stays usable offline.
- `react-best-practices` source file states 70 rules across eight categories, while repository root README describes 40+; avoid asserting a universal fixed count without checking a source revision.
- The source `react-view-transitions` documentation mentions specific React/browser versions. Treat those as claims tied to a particular revision, not permanent compatibility guarantees.
- Stack preferences and vendor-specific recommendations are not universal defaults. Taste Engine must remain framework-agnostic and taste-directed.

## Provenance

Sources read through GitHub repository content:
- https://github.com/vercel-labs/agent-skills/blob/main/README.md
- https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices
- https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines
- https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns
- https://github.com/vercel-labs/agent-skills/tree/main/skills/react-view-transitions
- https://github.com/vercel-labs/agent-skills/tree/main/skills/writing-guidelines
- https://github.com/vercel-labs/agent-skills/tree/main/skills/react-native-skills
- https://github.com/vercel-labs/agent-skills/tree/main/skills/deploy-to-vercel
- https://github.com/vercel-labs/agent-skills/tree/main/skills/vercel-optimize
