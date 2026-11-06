# Routing behavior acceptance scenarios

Each case must be tested in an agent that can pause between turns; a pure file validator cannot guarantee this behavior.

| Input | Expected before UI code | Loaded pack | Anti-regression |
| --- | --- | --- | --- |
| "Build a landing page" | One style selection question, then stop | None yet | No inferred clay default |
| "Create brutalist portfolio" | No redundant question | brutalism | No neo-brutalism offset shadow |
| "Glass signup page" | No redundant question | glassmorphism | Opaque fallback and contrast checks |
| "Make mobile layout work on existing app" | Maintain existing style | Existing project | No style reselect |
| "Write API unit tests" | No question | None | No unnecessary UI work |
| "Show other styles" (after menu) | Show remaining styles + custom | None yet | No repeated first menu |
| "Choose neo-brutalism" | Resolve and implement | neo-brutalism | 2–3px borders, intentional offset shadows |
| "Brutalism with editorial type" | Primary brutalism, secondary type-specific editorial | 2 relevant packs | No accidental glass/card blend |
| "I like this screenshot's typography" | Preserve named preference, ask only if style still undecided | Relevant/custom | Don't treat whole screenshot as full taste profile |
| "Surprise me / your choice" | May choose provisional style and disclose | Chosen pack | No claim of user preference |
| Project config `primary_style: minimalism` and `user_confirmed: true` | No question | minimalism | User can override with current request |
| Existing config brutalism; user explicitly requests glassmorphism redesign | No question; override config for this request | glassmorphism | Do not silently overwrite config |
| "Build a Retro Pixel portfolio" | No redundant question | retro-pixel | No retro-terminal CRT scanlines |
| "Create a pixel art landing page" | No redundant question | retro-pixel | Pixel artwork, desktop window chrome |
| "I want neo-brutalism, not pixel art" | Resolve neo-brutalism; exclude pixel art | neo-brutalism | High-contrast black borders, hard offset shadows |
| "Do not use retro pixel design" | Negative constraint only; exclude retro-pixel | None yet | Ask style question without retro-pixel |
| "Design an art deco portfolio" | No redundant question | art-deco | Geometric lines, stepped corners, zero golden gradient slop |
| "Create a classic deco luxury landing page" | No redundant question | art-deco (variant: classic) | Monumental obsidian, antique gold, bilateral symmetry |
| "Build a minimal deco architectural website" | No redundant question | art-deco (variant: minimal) | Burgundy and bronze, quiet refinement, high readability |
| "I want art deco, not brutalism" | Resolve art-deco; exclude brutalism | art-deco | Architectural symmetry, refined typography |
| "Do not use art deco" | Negative constraint only; exclude art-deco | None yet | Ask style question without art-deco |

## Style pack cross-acceptance

- Every registered ID has one matching file and consistent name, descriptions, sections and token values.
- Fonts are recommendations with fallbacks, never required remote downloads.
- Body text contrast, focus state, responsive layout, empty/error/disabled states and reduced-motion rules are present.
- `brutalism` and `neo-brutalism` never collapse into the same style. The former uses raw flat grid and no decorative offset comic shadow; the latter allows playful palette and hard offset shadow.
- `retro-terminal` and `retro-pixel` never collapse into the same style. The former uses CRT scanlines, phosphor luminescence, and CLI consoles; the latter uses 8-bit/16-bit pixel illustrations, desktop window chrome, and stepped pixel borders.
- `art-deco` never degenerates into generic AI gold-gradient slop. It enforces geometric line framing, stepped silhouettes, multi-tiered typography, and disciplined flat metallic finishes.
- Style is applied across all pages and components in scope; avoid unrequested style leaking across projects.
- Project overrides win over style pack guidance, after non-negotiable usability/accessibility requirements.
