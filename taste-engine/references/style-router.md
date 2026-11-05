# Style router: selection, resolution, blending

See [automatic invocation](auto-invocation.md) for host discovery and the authoritative stop/skip rules.

## Trigger boundaries

Apply style preflight to requests that create or substantially redesign visible interfaces. Do not trigger on backend, infrastructure, purely written copy, data, or logic-only tests. Do not require re-selection for routine maintenance of established UI.

## Resolution sequence

1. Detect explicit current-task style: "brutalism", "glass", "no rounded corners", screenshots + user-identified features, or concrete brand guidelines.
2. Normalize spelling using `styles/registry.json` aliases, reject negative-only mentions, and prefer the longer matching style (neo-brutalism over brutalism). If explicit style is registered, route directly to `styles/<id>.md`; if style is unregistered, use a temporary custom spec based on the same dimensions.
3. If not specified, detect approved project config. If it describes the current project and the user has not overridden it, route directly.
4. If maintaining existing UI, infer its documented or established style *for preservation only*; don't start a redesign.
5. Otherwise ask exactly one choice question and **end that agent turn without UI implementation**.
6. On reply: map selection or literal freeform answer to a concrete spec, avoiding coercion to the nearest trendy aesthetic. If user says "show more", present `bento`, `skeuomorphism`, `retro-terminal`, `enterprise`, and custom. Do not restart the first menu.

## Multiple selections

A user may choose "brutalism + editorial typography". Set:
- **primary** style = brutalism; controls layout, surface treatment and component grammar;
- **secondary** style = swiss-editorial; contributes only explicitly approved properties, such as body copy hierarchy and caption rhythm;
- **overrides** = named exceptions;
- **conflicts** = ask only if it determines a significant irreversible design choice; else follow primary.

Don't merge entire files blindly. Create a component-level decision table, e.g. border = brutalism, type rhythm = editorial, color = user brand.

## Examples of selection normalization

| User writes | Routing |
| --- | --- |
| "clay" or "claymorphism" | `claymorphism` |
| "glassmorphism" / "frosted glass" | `glassmorphism` |
| "brutalist" / "raw brutalism" | `brutalism` |
| "neubrutalism" / "neo brutalism" | `neo-brutalism` |
| "minimalist" | `minimalism` |
| "Swiss typography" / "editorial" | `swiss-editorial` |
| "bento grid" | `bento` |
| "realistic physical controls" / "skeumorphsm" / "skeumorphism" / "skeuomorphic" | `skeuomorphism` |
| "terminal" / "CLI aesthetic" | `retro-terminal` |
| "retro pixel" / "pixel art" / "8-bit ui" / "retro desktop" | `retro-pixel` (distinct from `retro-terminal`) |
| "enterprise dashboard" / "dense B2B" | `enterprise` **only if user intends an aesthetic**, otherwise consider it a product type, not style consent |
| "modern" / "beautiful" | Ambiguous; offer choices |
| "I have a screenshot" | Ask which parts matter if unclear; don't equate entire screenshot with approval |
| "your choice" | Explicit delegation permits a reasoned, provisional choice; explain trade-off |
| "no glassmorphism" | Negative constraint only; do **not** select glass |
| "neo-brutalism" | Use longer alias, **not** `brutalism` |

## Persisted choices

Project choices can be stored in `taste-style.json` at project root **only with user approval**. Read and validate it before asking again. Do not silently write a cross-project profile or assume that old preferences are global. Use the project schema at `assets/project-style.schema.json`.

## Frontend execution boundary

At a minimum, gate: creating app components, changing CSS themes/tokens, building visual landing pages, UI prototypes and visual redesigns. Safe preflight preparation that can occur before a user's answer: inspecting repository structure, package manager, design system and requirements. Do not secretly render/code a default implementation while waiting.
