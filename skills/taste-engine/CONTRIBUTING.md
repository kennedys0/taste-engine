# Contributing to Taste Engine

Thanks for helping make UI design more adaptable to everyone instead of forcing one author's visual taste.

## Ground rules

- Propose actionable behavior rather than purely aesthetic opinions. A style pack must be distinguishable from existing packs in typography, component anatomy, color roles, layout, surface treatment and motion.
- Avoid one creator's branding, proprietary asset dependencies, unlicensed fonts, watermark imagery, and personal data. Include accessible fallbacks.
- All packs should give **typography** (family with system fallbacks, scales, weights, hierarchy), **UI microcopy**, colors, spacing/grid, surfaces, borders, controls/states, responsive rules, motion/reduced-motion, do/don't and starter tokens.
- Accessibility, functioning interactions, accurate content and user preferences override any stylistic signature.
- Do not modify the mandatory ask-before-visual-code logic or silently change defaults. There are no default style IDs.

## Add or revise a pack

1. Add `styles/<id>.md`, following the sections and depth of existing packs.
2. Register the ID, description and file in `styles/registry.json`.
3. Add scenario cases to `tests/style-routing.md`, especially for near-neighbor styles.
4. Run `python3 scripts/validate-pack.py`.
5. To publish an optional standalone variant, copy its complete guidance into `optional-standalone-skills/taste-style-<id>/SKILL.md` in the bundle. The standalone installer is not required for the main router.

Before suggesting a new aesthetic, consider whether it should instead be a **project-specific override** or a blend of existing styles. Styles are optional starting directions, not psychological labels for users.

## Review criteria

Maintainable instructions, real visual differentiation, a clear trade-off story, no one-size-fits-all aesthetic and no regression on responsive/accessibility testing. For agent changes, include transcripts showing that unstyled new visual tasks result in a **question and pause**, while already-styled tasks and backend-only work proceed directly.

## Anti-Slop contribution contract

Every new style pack **must** include `## Anti-slop: style-specific` with concrete failure patterns, preferred corrections, and appropriate copy tone. General rules live in `references/anti-slop.md`, `references/anti-slop-copywriting.md`, and `references/anti-slop-audit.md`. Avoid blanket bans on characteristic features of another style. Add regression scenarios to `tests/anti-slop.md` and mirror updated style packs into their optional standalone skills. Do not invent visual test outcomes.
