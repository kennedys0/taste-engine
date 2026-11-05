# Tailwind CSS & shadcn/ui Integration Guide

This guide describes how to apply Taste Engine design archetypes to **Tailwind CSS (v3 & v4)** and **shadcn/ui** projects.

---

## 1. Quick Setup

Taste Engine includes pre-built presets inside `presets/`:
- `presets/tailwind/tailwind.preset.js`: Extends theme colors, box shadows, borders, and radii for all 10 styles.
- `presets/tailwind/taste-components.css`: Pre-composed `@layer components` (`.taste-clay-card`, `.taste-neo-btn`, etc.).
- `presets/shadcn/shadcn-themes.css`: HSL color variables and radius overrides for shadcn/ui primitives.

### Option A: Install Preset in `tailwind.config.js` (Tailwind v3)

```javascript
// tailwind.config.js
module.exports = {
  presets: [
    require('@kennedys0/taste-engine/presets/tailwind/tailwind.preset.js'),
    // or relative path if copied into your repo:
    // require('./taste-engine/presets/tailwind/tailwind.preset.js'),
  ],
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  plugins: [],
};
```

In your main CSS file (`globals.css` or `index.css`):
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Import Taste Engine component layers & shadcn theme overrides */
@import '@kennedys0/taste-engine/presets/tailwind/taste-components.css';
@import '@kennedys0/taste-engine/presets/shadcn/shadcn-themes.css';
```

### Option B: Tailwind v4 (`@theme`)

In Tailwind v4, import the CSS presets directly:
```css
@import "tailwindcss";
@import "@kennedys0/taste-engine/presets/tailwind/taste-components.css";
@import "@kennedys0/taste-engine/presets/shadcn/shadcn-themes.css";
```

---

## 2. Using with shadcn/ui

shadcn/ui components read CSS variables (`--background`, `--primary`, `--radius`, etc.) defined in `:root` and `.dark`.

To switch the entire application or a specific section to an archetype, set the `data-theme` attribute on `<html>`, `<body>`, or any wrapper element:

```html
<!-- Whole app in Claymorphism -->
<html lang="en" data-theme="claymorphism">
  ...
</html>

<!-- Whole app in Neo-brutalism -->
<html lang="en" data-theme="neo-brutalism">
  ...
</html>

<!-- Whole app in Retro-terminal -->
<html lang="en" data-theme="retro-terminal">
  ...
</html>
```

Supported `data-theme` values:
- `claymorphism` (Light & Dark)
- `neo-brutalism`
- `glassmorphism` (Light & Dark)
- `retro-terminal`
- `bento`
- `swiss-editorial`
- `brutalism`
- `minimalism` (Light & Dark, incorporates Enterprise data cockpits)
- `skeuomorphism`
- `retro-pixel` (Light & Dark)

---

## 3. Adapting shadcn/ui Component Primitives

When building components with shadcn/ui, standard utilities (`rounded-md`, `bg-primary`, `border`) automatically inherit the theme tokens. To achieve **screenshot-level fidelity**, apply style-specific companion classes:

### Claymorphism (Button & Card)

```tsx
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";

export function ClayCardDemo() {
  return (
    <Card className="taste-clay-card border-none">
      <CardHeader>
        <CardTitle className="text-xl font-bold text-slate-800">
          Sculpted Surface
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* Sunken well input */}
        <input
          type="text"
          placeholder="Enter username"
          className="taste-clay-well w-full text-slate-800 placeholder-slate-400"
        />

        {/* Tactile volumetric button */}
        <Button className="taste-clay-btn w-full">
          Confirm Action
        </Button>
      </CardContent>
    </Card>
  );
}
```

### Neo-Brutalism (Button & Card)

```tsx
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";

export function NeoCardDemo() {
  return (
    <Card className="taste-neo-card">
      <CardHeader>
        <CardTitle className="text-2xl font-black uppercase text-taste-neo-ink">
          Pop Surface
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <p className="text-sm font-medium text-taste-neo-ink">
          Bold unblurred shadows with mechanical active press travel.
        </p>
        <Button className="taste-neo-btn w-full">
          Execute Order
        </Button>
      </CardContent>
    </Card>
  );
}
```

### Glassmorphism (Frosted Pane)

```tsx
export function GlassPaneDemo() {
  return (
    <div className="taste-glass-pane dark:taste-glass-pane-dark max-w-md">
      <h3 className="text-lg font-semibold mb-2">Frosted Glass Pane</h3>
      <p className="text-sm text-slate-600 dark:text-slate-300">
        Requires a purposeful color background (radial gradient or mesh) to visibly demonstrate light refraction.
      </p>
    </div>
  );
}
```

---

## 4. Anti-Slop Discipline for Tailwind

When AI coding agents write Tailwind CSS, they frequently introduce **AI-slop** by inventing giant strings of arbitrary values (e.g., `shadow-[0_20px_50px_rgba(8,_112,_184,_0.7)]`).

### Forbidden Practices
- ❌ **Arbitrary shadow strings in HTML**: Do not dump arbitrary hex/rgba strings into inline utility classes like `shadow-[12px_16px_32px_rgba(...)]`.
- ❌ **Arbitrary border colors**: Do not mix `border-[#121212]` with `border-black` randomly.
- ❌ **Stacked card-in-card nesting**: Do not wrap a shadcn `Card` inside another `Card` without functional grouping.

### Mandated Practices
- ✅ **Use preset classes or theme tokens**: Use `taste-clay-btn`, `taste-neo-card`, or extended utility tokens like `shadow-clay-card` and `shadow-neo`.
- ✅ **Preserve tactile active feedback**: Buttons must specify active press displacement (`active:translate-x-1 active:translate-y-1` for neo-brutalism, or `scale-98` for claymorphism).
- ✅ **Respect dark mode contrast**: Never assume white text on dark surfaces without checking the theme's WCAG AA ratio.
