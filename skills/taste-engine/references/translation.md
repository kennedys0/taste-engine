# Translate a person's taste into a coherent interface

## From language to implementation

| User signal | Potential design levers | Avoid assuming |
| --- | --- | --- |
| Clean | Reduced competing emphasis, consistent alignment, focused content | Everything must be white or flat |
| Premium | Typography, composition, material quality, restraint, content credibility | Black-and-gold, thin unreadable type |
| Playful | Softer geometry, expressive illustration, approachable language, intentional motion | Random bouncing or childlike UI |
| Serious | Predictable hierarchy, stable interactions, disciplined color and copy | Dense, sterile, or colorless UI |
| Futuristic | Functional visualization, distinctive layout, clear technology cues | Neon gradients or illegible HUDs |
| Compact | Tight but accessible controls, scannable tables, deliberate grouping | Tiny tap targets or crammed whitespace |
| Soft | Gentle edges, layered surfaces, subtle contrast, comfortable rhythm | Mandatory claymorphism |
| Bold | Deliberate scale contrast, standout accent, confident structure | Maximum saturation everywhere |

These are starting hypotheses, not style presets. Confirm by concrete feedback.

## Design token protocol

Prefer project-local tokens that are based on *selected* decisions, not this skill's opinion. Relevant categories:

- `color.background`, `color.surface`, `color.text`, `color.accent`, semantic colors.
- `type.family`, `type.scale`, `type.weight`, `type.lineHeight`.
- `space.scale`, `layout.container`, `layout.columns`, `layout.gutters`.
- `shape.radius`, `shape.border`, `surface.shadow`.
- `motion.duration`, `motion.easing`, `motion.reduced`.
- `interaction.focus`, `interaction.hover`, `interaction.pressed`, `interaction.disabled`.

Keep names semantic and implementation-agnostic. Avoid accidental token proliferation; apply a consistent spatial scale and visual grammar.

## Project-sensitive implementation

- **Mobile:** navigation reflects app information architecture and platform conventions. Never force bottom navigation in all products. Ensure touch ergonomics and safe areas.
- **Data-heavy UI:** optimize scanning, loading/empty/error states, data semantics, pagination/filter clarity.
- **Marketing page:** emphasize content narrative, call-to-action visibility, imagery relevance, performance.
- **Forms:** consistency, labels, validation, focus order, error recovery.
- **Existing products:** preserve design tokens, recognizable patterns, and user workflows unless explicitly asked to change them.

## Variant strategy

When experimentation is warranted, present 2–3 alternatives that differ on meaningful axes. Explain what each optimizes and identify tradeoffs. Avoid declaring one universal winner; choose the direction grounded in the user's feedback and product goals.
