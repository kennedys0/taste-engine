#!/usr/bin/env python3
"""Update taste-engine rules in SKILL.md and references/."""
from pathlib import Path

skill_path = Path("taste-engine/SKILL.md")
skill_text = skill_path.read_text(encoding="utf-8")

old_dna = """3. **Build project Design DNA:** type families + fallback, type scale, font weights, writing tone, palette roles, density, spacing, radius, border, elevation, layout grid, component anatomy, states, navigation, motion and reduced-motion rules. See [translation](references/translation.md). **Dark & light mode pair coupling:** when dark or light mode is requested, ensure paired design tokens for canvas, cards, text, borders, inputs, and semantic status pills flip in tandem so background and foreground colors never collide (e.g. zero black-on-black or white-on-white text).
4. **Resolve precedence:** technical/safety/accessibility constraints → explicit current request → confirmed project brand → selected pack → contextual conventions. User overrides are allowed; record which dimensions differ from the pack.
5. **Implement in existing stack**; no automatic requirement for React, MUI, Tailwind, a font provider, or animation library. If meaningful motion is required, consult `references/motion-engine.md` without assuming Anime.js is installed. Prefer semantic design tokens, maintain working functionality and responsive behavior.
6. **Hero geometry when applicable:** for a public-facing opening hero, load `references/hero-layout.md` and use the selected style pack’s hero composition cues; keep the full first viewport inclusive of navigation and test short/mobile screens. Never add a hero to screens that do not need one.
7. **Mandatory Anti-Slop Gate**: read [Anti-Slop Constitution](references/anti-slop.md) and [Anti-Slop Writing](references/anti-slop-copywriting.md); apply the **Anti-slop: style-specific** section in the chosen pack. Reject decorative card nesting, generic templates, meaningless badges/charts/icons, dishonest states, marketing filler, and gratuitous motion. Preserve deliberate style-specific expression."""

new_dna = """3. **Build project Design DNA:** type families + fallback, type scale, font weights, writing tone, palette roles, density, spacing, radius, border, elevation, layout grid, component anatomy, states, navigation, motion and reduced-motion rules. See [translation](references/translation.md).
   - **Dark & light mode pair coupling:** when dark or light mode is requested, ensure paired design tokens for canvas, cards, text, borders, inputs, and semantic status pills flip in tandem so background and foreground colors never collide (zero black-on-black or white-on-white text). In dark mode, avoid harsh pitch-black (`#000000` or raw `#0d0f14`) canvas unless specifically requested; prefer warm neutral dark slate-grey (Codex / OpenAI aesthetic: canvas `#212328`, surfaces `#2b2e36`, elevated `#343842`, recessed wells `#1a1c21`, borders `rgba(255, 255, 255, 0.12)`) for lower eye strain, balanced contrast, and rich surface hierarchy.
   - **Mobile UI anti-bloat & fluid typography:** scale typography, paddings, and card geometry down proportionally on mobile viewports (< 768px, < 480px) using `clamp()` or adaptive breakpoints to prevent oversized, inflated interfaces ("UI bengkak"). Hero titles clamp to `1.4rem`–`1.65rem`, section titles to `1.25rem`–`1.5rem`, and code snippets to `0.725rem`–`0.785rem` with `word-break: break-all` / `overflow-x: auto` to prevent horizontal blowout.
   - **Single-line inline alignment:** keep quick install pills, command-line snippets, and search/copy bars strictly inline in a single horizontal row (`display: inline-flex; flex-direction: row; align-items: center; justify-content: center;`) with `line-height: 1; flex-shrink: 0;` across mobile and desktop. Never break prompt `$`, command text, and copy button into vertical stacked rows.
   - **Mobile footer architecture:** avoid endless 1-column link dumps that inflate vertical scroll on mobile. Organize navigation links into a balanced 2-column grid (`repeat(2, 1fr)`), span brand identity across full-width with a subtle border divider, and provide tactile, thumb-friendly tap targets (pill buttons like 'Back to top').
4. **Resolve precedence:** technical/safety/accessibility constraints → explicit current request → confirmed project brand → selected pack → contextual conventions. User overrides are allowed; record which dimensions differ from the pack.
5. **Implement in existing stack**; no automatic requirement for React, MUI, Tailwind, a font provider, or animation library. If meaningful motion is required, consult `references/motion-engine.md` without assuming Anime.js is installed. Prefer semantic design tokens, maintain working functionality and responsive behavior.
6. **Hero geometry when applicable:** for a public-facing opening hero, load `references/hero-layout.md` and use the selected style pack’s hero composition cues; keep the full first viewport inclusive of navigation and test short/mobile screens. Never add a hero to screens that do not need one.
7. **Mandatory Anti-Slop Gate**: read [Anti-Slop Constitution](references/anti-slop.md) and [Anti-Slop Writing](references/anti-slop-copywriting.md); apply the **Anti-slop: style-specific** section in the chosen pack. Reject decorative card nesting, generic templates, meaningless badges/charts/icons, dishonest states, marketing filler, and gratuitous motion. Specifically enforce:
   - **Zero rainbow text gradients** (`-webkit-background-clip: text` on headings) unless explicitly mandated by authentic retro/cyberpunk themes.
   - **Zero cartoon emojis as functional icons**; always use crisp, semantic inline SVGs (e.g. Lucide/Feather).
   - **Zero fake widgets** (fabricated weather displays, audio spectrum equalizers, simulated live telemetry, or fake counters) invented merely to fill empty space.
   Preserve deliberate style-specific expression."""

norm_text = skill_text.replace("\r\n", "\n")
norm_old = old_dna.replace("\r\n", "\n")
norm_new = new_dna.replace("\r\n", "\n")

if norm_old in norm_text:
    updated = norm_text.replace(norm_old, norm_new, 1)
    if "\r\n" in skill_text:
        updated = updated.replace("\n", "\r\n")
    skill_path.write_text(updated, encoding="utf-8")
    print("SUCCESS: updated taste-engine/SKILL.md")
else:
    print("ERROR: old_dna not found in taste-engine/SKILL.md")

