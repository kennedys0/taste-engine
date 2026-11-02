# React Composition — maintainable component architecture

Use only when the project uses React and the task requires a component system or refactor. Inspired by the concepts in https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns ; this guidance is newly written, not copied.

- Avoid a component API with dozens of mutually interacting `isX`, `showY`, `compact`, `premium`, `mobileOnly` booleans. Prefer a small number of explicit variants for genuinely different behaviors.
- Compose complex UI via meaningful slots or compound parts (`Dialog.Header`, `Dialog.Body`, `Dialog.Actions`) when shared state and reuse warrant it. Don't introduce a compound API for a one-off card.
- Lift state only as high as needed. Keep rendering details separate from state ownership, and avoid deeply threading props when composition or contextual state is clearer.
- Keep accessibility semantics/roles at the primitive level. Don't build `div`-based buttons or clickable cards without keyboard interaction.
- Prefer existing component library primitives and project conventions; maintain one coherent design token system. Never rewrite component architecture simply to show off a pattern.
- Check React version before React-19-specific idioms. Do not assume `use()`, ref behavior, or ViewTransition availability without verifying.

**Taste Engine anti-slop crossover:** architecture composition is not visual card nesting. Compound components can help code organization; they do **not** justify putting card backgrounds inside every card on screen.

Audit prompts: Is this prop necessary? Are states impossible/conflicting? Does each component represent an actual interface responsibility? Can consumers customize intent without exposing internal wiring? Are peer components balanced, accessible and responsive?
