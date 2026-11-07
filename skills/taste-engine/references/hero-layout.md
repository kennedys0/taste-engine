# Full-screen Hero Contract — all aesthetics

**Scope:** Any public-facing portfolio, landing page, campaign page or homepage where a hero/intro section exists. For new work in those categories, design a purposeful first-screen introduction. When an established page is being refined, preserve its information and behavior; do not add a new hero without a request to create/redesign it. Internal dashboards, task screens, forms, articles, private apps and SEO-only edits do **not** gain a hero automatically.

## Default geometry: one full visible opening screen (100% first viewport)

- The **first-screen composition** (header/navigation + hero where both appear) MUST occupy **one full visible viewport (`100vh` / `100svh`)** and fit as one intentional, self-contained 1-screen composition at typical desktop and mobile sizes (`1440×900`, `1440×950`, `1024×768`, `390×844`). Never leave the hero at 70vh–80vh where the heading of the next section bleeds into the bottom of the first desktop viewport.
- Prefer `min-height` over a fixed `height` or `max-height`. One full screen is a **mandatory minimum design intent, not a license to clip real content**. If the visitor uses large text, localization, landscape mode, a short screen or long honest content, the hero must expand and scroll naturally.
- On desktop, give the hero a full 1-screen composition (`display: flex; flex-direction: column; justify-content: center;`) that uses both axes thoughtfully: focal content, meaningful material or interactive centerpiece (`align-items: center` between left copy and right visual so columns keep natural content proportions), aligned CTAs, and balanced negative space. Do **not** fill the viewport with fake metrics, decorative cards, or purposeless floating shapes.
- On mobile, change the composition: prioritize the actual title, explanation and primary action, keep CLI/install command boxes compact on a single scrollable row (`flex-wrap: nowrap; height: 42px–44px;` with a pinned copy button—never wrapping into a tall multi-line capsule), keep tap targets visible (`44px`), respect safe areas and let overflow scroll instead of shrinking text to fit.
- This is a **layout policy** for every style, not an aesthetic. Only the selected style pack determines colors, fonts, materials, borders, surface treatment, and motion. No requirement to add a hero to every screen or to stack every page section at 100vh.

## CSS: header is part of the height budget (always provide a fallback value)

Choose **one** of these header patterns after checking the real project. Do not combine both offsets. Always define `--site-header-height` / `--pow-header-h` in `:root` **and** provide a fallback value inside `var(--site-header-height, 60px)` so an undefined variable never invalidates `calc()` and collapses the hero below 1 full screen.

**A. Header in normal flow** — navbar is a sibling *before* the hero; subtract its occupied height (measure it; do not hard-code an imagined size):

```css
:root { --site-header-height: 60px; } /* Must match actual header; update per breakpoint. */
.site-hero,
.pow-hero {
  box-sizing: border-box;
  min-height: calc(100vh - var(--site-header-height, 60px)); /* fallback */
  min-height: calc(100svh - var(--site-header-height, 60px));
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: clamp(24px, 4.5vh, 64px) 0;
}
```

**B. Header overlays/is positioned inside the hero** — hero occupies the entire viewport; add clear top room for the actual navbar and any top safe area:

```css
.site-hero {
  box-sizing: border-box;
  min-height: 100vh; /* fallback */
  min-height: 100svh;
  display: grid;
  align-content: center;
  padding:
    calc(var(--site-header-height) + env(safe-area-inset-top, 0px) + 20px)
    clamp(16px, 5vw, 80px)
    max(24px, env(safe-area-inset-bottom, 0px));
}
```

If the header grows/wraps, `--site-header-height` must track its real occupied height, or use a shared grid wrapper instead of manual subtraction. If the site uses a fixed/sticky overlay, verify it does not obscure heading or CTA and that focus targets are not hidden behind it.

### Viewport choice

- `100svh` is the **stable mobile-safe default** for promotional heroes; it keeps the opening content clear when mobile browser toolbars are expanded.
- `100dvh` follows changing browser toolbar height and can be deliberately chosen for experiences that must continuously fill the current visible area. It can resize during scroll, so test carefully. Do not use `100lvh` to size critical mobile content where toolbars can cover it.
- `100vh` may behave like the large viewport on mobile. Treat it as a fallback, not the sole modern mobile solution.
- Prefer CSS layout over resize listeners, scroll-jacking, `overflow:hidden` on the body, custom fullpage wheel capture, or an animation-library dependency just to make the hero full height.

## Content and anti-slop

A full-screen hero needs an idea, not more decoration:

- One product-grounded, clear `h1` or equivalent primary page heading and useful next step (CTA/link if applicable); no invented social proof, fake user counts, hype copy, decorative live status, unrelated huge icon, or giant orb.
- Typography, media scale, crop, positioning and whitespace express the selected style. A Brutalism hero may be a typographic poster; a Glassmorphism hero may layer legible content over real imagery; a portfolio can show actual work rather than a fake dashboard.
- Avoid autoplaying decorative animation; never hide title or button until Anime.js initializes. Respect `prefers-reduced-motion`. No forced smooth-scroll takeover.
- Full-screen **does not** mean full-bleed photo is mandatory. Do not fetch or invent assets just to fill space.
- Semantic heading structure, relevant visible copy, image sizing and adequate first-screen loading remain required for SEO and performance; never promise rankings or invent measurements.

## Acceptance checks (browser/device when available)

1. First viewport contains the intended complete header+hero composition at 1440×900 and 1024×768; no accidental blank strip or 120vh double-height from forgetting the header.
2. At 390×844, 360×640 and 320×568, the actual heading, CTA and navigation remain usable, with no horizontal overflow, clipping, or browser-toolbar occlusion.
3. At short landscape heights, 200% zoom and increased text sizes, content can grow beyond one viewport and scroll normally. **Do not mark an expanded hero as a failure:** clipping is the failure.
4. Fixed/sticky nav, notches/safe areas, reduced motion, keyboard focus and skip links still work.
5. Review content hierarchy. Remove any invented metrics, nested decorative cards, floating ornaments or idle loops added solely to fill the full-height canvas.
6. Record actual viewport tests only when executed. A code-level checklist is not proof of browser behavior.

## Overrides

A direct request for a compact/half-screen hero, no hero, or an existing locked design system **overrides this default**, subject to functionality/accessibility. Do not ask an extra question merely to apply this rule; it runs after the style-selection preflight. When overriding, retain the user's specified height or structure and do not silently reintroduce 100svh.
