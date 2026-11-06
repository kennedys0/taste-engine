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
6. On reply: map selection or literal freeform answer to a concrete spec, avoiding coercion to the nearest trendy aesthetic. If user says "show more", present `skeuomorphism`, `retro-terminal`, `retro-pixel`, and custom. (Bento is selectable within Brutalism as a native layout variant: Raw or Bento). Do not restart the first menu.

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
| "frutiger aero" / "aero" / "aqua" / "web 2.0" | `frutiger-aero` (variant: `classic`, default) |
| "glassmorphism" / "frosted glass" | `frutiger-aero` (variant: `glass`) |
| "brutalist" / "brutalism" | `brutalism` (variant: `raw`, default) |
| "raw brutalism" | `brutalism` (variant: `raw`) |
| "bento" / "bento grid" / "brutalist bento" | `brutalism` (variant: `bento`) |
| "neubrutalism" / "neo brutalism" | `neo-brutalism` (independent) |
| "minimalist" | `minimalism` |
| "Swiss typography" / "editorial" | `swiss-editorial` |
| "realistic physical controls" / "skeumorphsm" / "skeumorphism" / "skeuomorphic" | `frutiger-aero` (variant: `tactile`) |
| "terminal" / "CLI aesthetic" | `retro-terminal` |
| "retro pixel" / "pixel art" / "8-bit ui" / "retro desktop" | `retro-pixel` (distinct from `retro-terminal`) |
| "art deco" / "art-deco" / "deco ui" / "deco style" | `art-deco` (variant: `modern`, default) |
| "classic deco" / "gatsby style" / "vintage deco" | `art-deco` (variant: `classic`) |
| "minimal deco" / "quiet deco" | `art-deco` (variant: `minimal`) |
| "y2k" / "y2k futurism" / "cyber y2k" / "futurism" | `y2k-futurism` (variant: `chrome`, default) |
| "chrome" / "liquid chrome" / "metallic silver" / "chrome ui" | `y2k-futurism` (variant: `chrome`) |
| "holographic" / "holo" / "iridescent" / "spectral" | `y2k-futurism` (variant: `holographic`) |
| "retro tech" / "retro-tech" / "speculative tech" / "cyber optimism" | `y2k-futurism` (variant: `retro-tech`) |
| "enterprise dashboard" / "dense B2B" | `minimalism` (with high-density data cockpits) |
| "modern" / "beautiful" | Ambiguous; offer choices |
| "I have a screenshot" | Ask which parts matter if unclear; don't equate entire screenshot with approval |
| "your choice" | Explicit delegation permits a reasoned, provisional choice; explain trade-off |
| "no glassmorphism" | Negative constraint only; do **not** select glass |
| "neo-brutalism" | Use longer alias, **not** `brutalism` |

## Frutiger Aero taxonomy & backward compatibility

Glassmorphism and Skeuomorphism are consolidated into Frutiger Aero as native visual expressions:
- **Classic Aero** (`variant: classic`, default): Bright aqua-inspired palette, glossy dimensional controls, nature-tech balance, and optimistic mid-2000s technological vision.
- **Aero Glass** (`variant: glass`): Preserves core Glassmorphism principles—frosted crystalline panels, layered transparency, controlled background blur, and soft luminous borders.
- **Aero Tactile** (`variant: tactile`): Preserves core Skeuomorphism principles—physical material cues, tactile button surfaces, convincing highlights and shadows, and realistic surface depth.

### Backward compatibility
Legacy inputs and configurations specifying `style: glassmorphism` automatically resolve to:
```yaml
style: frutiger-aero
variant: glass
```
Legacy inputs and configurations specifying `style: skeuomorphism` automatically resolve to:
```yaml
style: frutiger-aero
variant: tactile
```

## Brutalism taxonomy & backward compatibility

Bento is consolidated into Brutalism as a native layout variant:
- **Raw Brutalism** (`variant: raw`, default): Linear structural scaffolding, monumental grotesk headlines, flush cellular blueprint compartments, and 0px square corners.
- **Brutalist Bento** (`variant: bento`): Asymmetric modular grid composition (2x2 dominant panel, secondary panels, spec cells) locked inside uncompromising 2px–3px brutalist structural borders with 0px corners and high-voltage operational signal accents.

### Backward compatibility
Existing configurations or user prompts specifying `style: bento` or `primary_style: bento` automatically resolve to:
```yaml
style: brutalism
variant: bento
```
Neo-Brutalism remains 100% independent with its own distinct visual language (vibrant pop palette, 4px unblurred offset shadows, mechanical press collapse, 6px radius).

## Art Deco taxonomy & expressions

Art Deco is a unified architectural visual language with three native expressions:
- **Modern Deco** (`variant: modern`, default): Contemporary architectural refinement, generous intentional whitespace, simplified geometric line frames, forest green and muted brass accents.
- **Classic Deco** (`variant: classic`): Monumental architectural symmetry, stepped ornamental borders, high-contrast typography, obsidian canvas, and antique gold accents.
- **Minimal Deco** (`variant: minimal`): Quiet sophistication, subtle geometric accents, ivory canvas, deep burgundy and warm bronze tones, and high-density readability.

All three expressions resolve under `style: art-deco` with their corresponding `variant`.

## Y2K Futurism taxonomy & expressions

Y2K Futurism is a cyber-optimistic and speculative technological visual language with three native expressions:
- **Chrome** (`variant: chrome`, default): Polished metallic silver surfaces, high-contrast dark and light zones, chrome-beveled geometric framing, bold futuristic typography, and restrained electric violet or ice blue accents.
- **Holographic** (`variant: holographic`): Iridescent accents, controlled spectral gradients, translucent colored layering, soft chromatic reflections, and experimental futuristic layouts without chaotic color clashes.
- **Retro Tech** (`variant: retro-tech`): Early internet cyber-optimism, futuristic industrial typography, modular console panels, segmented status indicators, and speculative hardware references.

All three expressions resolve under `style: y2k-futurism` with their corresponding `variant`.

## Persisted choices

Project choices can be stored in `taste-style.json` at project root **only with user approval**. Read and validate it before asking again. Do not silently write a cross-project profile or assume that old preferences are global. Use the project schema at `assets/project-style.schema.json`.

## Frontend execution boundary

At a minimum, gate: creating app components, changing CSS themes/tokens, building visual landing pages, UI prototypes and visual redesigns. Safe preflight preparation that can occur before a user's answer: inspecting repository structure, package manager, design system and requirements. Do not secretly render/code a default implementation while waiting.
