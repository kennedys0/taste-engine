# Responsive Baseline & Universal Mobile Defaults

**Scope:** Cross-aesthetic foundation for responsive layouts, mobile viewport safety, circular geometry, navigation collapse, and fallback palettes. These baseline defaults apply across all styles unless an explicit style pack, brand guideline, or user instruction intentionally overrides them.

## 1. 320px Viewport Baseline (Zero Overflow)

- **FLOOR:** Every interface must function down to a 320px minimum viewport width (`min-width: 320px`) with zero unexpected horizontal scroll blowout.
- Ensure all containers use `box-sizing: border-box`, `max-width: 100%`, and appropriate `overflow-x: hidden` on viewport roots or clipping wrappers.
- Long strings, URLs, and code tokens must wrap gracefully (`overflow-wrap: anywhere;` or `word-break: break-word;` for text, `overflow-x: auto;` for preformatted code blocks).
- Minimum touch target sizing on mobile viewports must meet or exceed 44×44px for primary interactive elements.

## 2. Fluid Typography Baseline (Mobile Defaults)

- **REFLEX:** On narrow viewports (<= 480px), typography scales down smoothly to prevent oversized elements from crowding mobile screens, while strictly respecting readability minimums:
  - **Body text:** Default minimum >= 1rem (16px) with line-height >= 1.5. Never drop body font below 16px on mobile viewports to prevent iOS browser auto-zoom.
  - **Secondary / metadata text:** Default minimum >= 0.875rem (14px) with line-height >= 1.4.
  - **Monospace code snippets:** Default minimum >= 0.8125rem (13px) with `line-height: 1.4` and horizontal scroll containment.
  - **Headings & hero titles:** May use fluid `clamp()` formulas, but style packs may freely override heading scales (e.g., Swiss Editorial's dramatic headline scale `clamp(2rem, 6vw, 4.5rem)` or Neo-Brutalism's bold display titles).

## 3. Responsive Navigation & Mobile Menus

- **REFLEX:** Top navigation headers should collapse multi-link desktop rows behind an accessible disclosure or mobile drawer / sheet on viewports < 768px:
  - Use an accessible trigger button with `aria-expanded` and an SVG menu icon (such as Lucide `Menu`).
  - Mobile sheets or dropdown panels must provide comfortable tap targets (>= 44px) and clear dismiss options.
  - **Override:** Style packs and application designs may choose tabbed bottom bars, persistent icon rails, or compact inline headers when appropriate for the product pattern.

## 4. Strict Circular Geometry (Anti-Oval)

- **FLOOR:** All circular UI elements (avatars, status indicator dots, circular icon buttons, badges with `border-radius: 50%`) must declare:
  ```css
  aspect-ratio: 1 / 1;
  flex-shrink: 0;
  ```
  This prevents flexbox or grid compression from flattening circular indicators into distorted ovals on narrow mobile screens.

## 5. Inline Command Pills

- **REFLEX:** Quick install pills, monospace terminal snippets, and search/copy bars should keep the command line and copy action aligned horizontally in a single row (`display: inline-flex; align-items: center;`) when viewport space permits.
- Monospace command text should truncate gracefully (`text-overflow: ellipsis; white-space: nowrap; overflow: hidden;`) or scroll horizontally on narrow viewports rather than breaking into disorganized multi-line fragments.

## 6. Iconography: Scalable Vector Icons Over Emojis

- **REFLEX:** Prefer crisp, scalable SVG vector icons (Lucide, Radix, Feather, Heroicons) with consistent stroke weight (1.5px–2px) and `currentColor` inheritance as primary interface icons, status indicators, and button prefixes.
- **Override:** Emojis are permitted when intentionally selected as user content, expressive badges, or playful genre markers in specific aesthetics (e.g. Retro-Arcade or Neo-Brutalism ironic stickers).

## 7. Dark-Mode Slate Fallback Palette

- **REFLEX:** When dark mode is active and neither the chosen style pack nor the project brand specifies a dark palette, use this warm dark slate neutral baseline (Codex / OpenAI aesthetic) for balanced contrast and minimal eye strain:
  - **Canvas Base:** `#212328`
  - **Surfaces / Cards:** `#2b2e36`
  - **Elevated Surfaces:** `#343842`
  - **Recessed Wells:** `#1a1c21`
  - **Borders & Dividers:** `rgba(255, 255, 255, 0.12)`
- **Override:** Style packs with signature dark palettes (e.g., Brutalism `#000000`, Swiss Editorial `#0D0D0D`, Retro-Terminal CRT dark, or OLED pure black) take precedence.
