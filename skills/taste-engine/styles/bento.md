# Style pack: Bento Grid (Consolidated into Brutalism)

> **Notice:** Bento Grid has been consolidated into the **Brutalism** style pack as a native layout variant: **Brutalist Bento** (`variant: bento`).
> 
> Please refer to [styles/brutalism.md](brutalism.md) for full design rules, tokens, layout structures, and quality gates.

## Migration and Backward Compatibility

- **Configuration:** Existing configurations with `style: bento` or `primary_style: bento` automatically resolve to:
  ```yaml
  style: brutalism
  variant: bento
  ```
- **CLI and Prompts:** Prompts specifying `bento`, `bento grid`, or `bento ui` resolve to `brutalism` with `variant: bento`.
- **Visual Design:** Brutalist Bento preserves asymmetric modular grid composition, multi-span panels, and varied internal tile anatomy, implemented with brutalist structural integrity (2px–3px solid borders, strict 0px square corners, stark monochrome contrast, and operational signal accents).
