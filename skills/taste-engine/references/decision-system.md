# Decision System: user-led aesthetics, not an AI house style

Load this after a user has selected a style and before changing visual code. It is a decision method, **not a style preset**.

## 1. Style and page anatomy are separate

- **Material/style** sets type, contrast, color, surface, geometry, graphic character, interaction treatment and voice.
- **Anatomy** sets what the product needs: task flow, information architecture, content groups, priority, data relationships, forms and navigation.
- Never turn a style pack into a rigid template. A brutalist checkout and brutalist editorial homepage can share a material system without sharing a hero, card count or section order.
- Choose information architecture from **user goals and real content**, not a theme catalog. Do not create evidence, claims or features to populate a composition.

### Full-screen opening composition is an anatomy constraint, not a theme

For a new public-facing landing page/homepage/portfolio *with a hero*, apply [Full-screen Hero Contract](hero-layout.md): the first screen includes the header and hero; the hero should fill its available viewport, not force a 100vh box below navigation. Actual content and user tasks still define what fills it. Small/short screens may require natural scrolling for accessibility. Existing compact heroes and user-requested exceptions win.

## 2. Build a visual thesis

Write one concise sentence privately or in a design log before implementation. Include: selected style, specific typographic character, contrast/palette intent, density, composition strategy, and one product-related reason. Example: 'Brutalist incident dashboard: tightly aligned sans headings, near-monochrome rules, dense tables, and one genuine severity accent for faster scanning.' This is not permission to assume the user likes brutalism; it is created **only after selection**.

If you cannot tie the thesis to audience, brand, or task, it is too generic. Avoid phrases like 'premium, clean, modern'. A selected style is the starting point, not a substitute for designing.

## 3. Calibrated preferences, optional

Never force a questionnaire for these values. Defaults are pack- and context-derived, not globally fixed 8/6/4 values. If user wants further control, accept 1–10 sliders or natural-language overrides:

| Dimension | Lower | Higher | Guard |
|---|---|---|---|
| design_variance | predictable hierarchy | more experiment/asymmetry | never violate comprehension |
| motion_intensity | static feedback | richer purposeful transitions | reduced-motion + performance |
| visual_density | fewer objects per view | more operational information | preserve legibility and touch |

Other useful taste axes (descriptive, **not scored without input**): warmth, formality, expressiveness, contrast, ornament, typographic voice. Learn from user corrections only when expressed; do not infer a persistent preference from one project or quietly save a profile.

## 4. Conflict precedence

1. Functional truth, accessibility and safety.
2. Explicit user request and project requirements.
3. Approved brand, existing patterns and project style config.
4. Selected style pack's distinctive attributes.
5. Contextual anti-slop reflex checks and optional inspiration.

When a request says 'glass but no blur', honor it as a custom glass-influenced style; do not reintroduce blur because the pack recommends it. User's explicit content and labels should not be rewritten during a visual restyle unless requested or a proven correctness/safety issue demands it.

## 5. Decision trace (short)

For meaningful work record: `STYLE`, `REASON`, `TOKEN CHOICES`, `KEY LAYOUT DECISION`, `NON-DEFAULT CHOICES`, `TESTED`, `UNTESTED`. This can live in an optional project `DESIGN.md` or in the handoff. Do not generate a file for tiny changes.

## 6. Deliberate craft, not negative-only design

Passing the anti-slop checklist is necessary but insufficient. A generic gray page can pass if it has no fake data and no purposeless cards. Demand at least one product-grounded **positive** design decision: e.g. an inspection report organized around the actual inspection sequence, or a billing summary whose most important action is positioned near the invoice facts.

Ask: 'If I remove the logo, what about this composition still says THIS product?' If the answer is nothing, improve content hierarchy and the chosen style's expression; do not add decorative noise.
