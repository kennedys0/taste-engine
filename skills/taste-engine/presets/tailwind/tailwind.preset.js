/**
 * Taste Engine — Tailwind CSS Preset (v0.11.0)
 * Comprehensive theme extension for 11 curated frontend aesthetic archetypes.
 *
 * Usage in tailwind.config.js / tailwind.config.mjs:
 *   // ESM (Next.js / Vite / Nuxt):
 *   import tastePreset from '@kennedys0/taste-engine/presets/tailwind/tailwind.preset.js';
 *   export default { presets: [tastePreset], content: ['./src/**/*.{js,ts,jsx,tsx}'] };
 *
 *   // CommonJS:
 *   module.exports = {
 *     presets: [require('@kennedys0/taste-engine/presets/tailwind/tailwind.preset.js')],
 *     content: ['./src/**/*.{js,ts,jsx,tsx}'],
 *   };
 */

const tastePreset = {
  theme: {
    extend: {
      colors: {
        taste: {
          // Claymorphism: soft sculpted tones with vibrant accents
          'clay-bg': 'var(--taste-clay-bg, #e8ecf2)',
          'clay-surface': 'var(--taste-clay-surface, #e8ecf2)',
          'clay-primary': 'var(--taste-clay-primary, #6366f1)',
          'clay-well': 'var(--taste-clay-well, #dfe4ec)',

          // Neo-brutalism: high-contrast pop palette
          'neo-bg': 'var(--taste-neo-bg, #fffdf8)',
          'neo-ink': 'var(--taste-neo-ink, #121212)',
          'neo-yellow': 'var(--taste-neo-yellow, #ffdf00)',
          'neo-pink': 'var(--taste-neo-pink, #ff6b8b)',
          'neo-cyan': 'var(--taste-neo-cyan, #00e5ff)',
          'neo-green': 'var(--taste-neo-green, #00f076)',

          // Glassmorphism: frosted translucent surfaces
          'glass-bg': 'var(--taste-glass-bg, #0b0f19)',
          'glass-surface': 'var(--taste-glass-surface, rgba(255, 255, 255, 0.45))',
          'glass-surface-dark': 'var(--taste-glass-surface-dark, rgba(20, 24, 38, 0.65))',
          'glass-border': 'var(--taste-glass-border, rgba(255, 255, 255, 0.65))',
          'glass-border-dark': 'var(--taste-glass-border-dark, rgba(255, 255, 255, 0.12))',

          // Retro-Terminal: CRT phosphor tones
          'term-bg': 'var(--taste-term-bg, #0c0d0e)',
          'term-amber': 'var(--taste-term-amber, #ffb000)',
          'term-green': 'var(--taste-term-green, #33ff33)',
          'term-cyan': 'var(--taste-term-cyan, #00e5ff)',

          // Bento: deep rich modular slate
          'bento-bg': 'var(--taste-bento-bg, #13151b)',
          'bento-surface': 'var(--taste-bento-surface, #1e222b)',
          'bento-surface-elevated': 'var(--taste-bento-surface-elevated, #262b36)',
          'bento-cta': 'var(--taste-bento-accent-cta, #ff5722)',
          'bento-border': 'var(--taste-bento-border, rgba(255, 255, 255, 0.08))',

          // Swiss / Editorial: stark modernist ink
          'swiss-bg': 'var(--taste-swiss-bg, #ffffff)',
          'swiss-ink': 'var(--taste-swiss-ink, #111111)',
          'swiss-red': 'var(--taste-swiss-red, #e53935)',
          'swiss-muted': 'var(--taste-swiss-muted, #767676)',

          // Brutalism: raw unembellished mono
          'brutal-bg': 'var(--taste-brutal-bg, #f4f4f4)',
          'brutal-ink': 'var(--taste-brutal-ink, #000000)',
          'brutal-canvas': 'var(--taste-brutal-canvas, #ffffff)',

          // Minimalism: deliberate intentional whitespace
          'minimal-bg': 'var(--taste-minimal-bg, #ffffff)',
          'minimal-surface': 'var(--taste-minimal-surface, #fafafa)',
          'minimal-ink': 'var(--taste-minimal-ink, #171717)',
          'minimal-muted': 'var(--taste-minimal-muted, #737373)',

          // Enterprise: high-density cockpit
          'ent-bg': 'var(--taste-ent-bg, #0f172a)',
          'ent-surface': 'var(--taste-ent-surface, #1e293b)',
          'ent-border': 'var(--taste-ent-border, #334155)',
          'ent-blue': 'var(--taste-ent-blue, #2563eb)',
          'ent-emerald': 'var(--taste-ent-emerald, #059669)',

          // Retro Pixel: nostalgic 8-bit / 16-bit personal computing
          'pixel-bg': 'var(--taste-pixel-bg, #10102b)',
          'pixel-surface': 'var(--taste-pixel-surface, #1b1b3a)',
          'pixel-window': 'var(--taste-pixel-window, #22224a)',
          'pixel-header': 'var(--taste-pixel-window-header, #5b438e)',
          'pixel-well': 'var(--taste-pixel-well-bg, #0d0d22)',
          'pixel-teal': 'var(--taste-pixel-teal, #2ca7a3)',
          'pixel-orange': 'var(--taste-pixel-orange, #f27d36)',
          'pixel-purple': 'var(--taste-pixel-purple, #5b438e)',
          'pixel-cream': 'var(--taste-pixel-cream, #f2dfb5)',
        },
      },
      boxShadow: {
        // Claymorphism: volumetric dual inner + ambient drop shadows
        'clay-card': '12px 16px 32px rgba(166, 178, 198, 0.65), -10px -10px 24px rgba(255, 255, 255, 0.95)',
        'clay-card-dark': '12px 16px 32px rgba(0, 0, 0, 0.65), -8px -8px 20px rgba(255, 255, 255, 0.05)',
        'clay-btn': '8px 10px 20px rgba(99, 102, 241, 0.35), inset 3px 4px 6px rgba(255, 255, 255, 0.45), inset -4px -6px 8px rgba(0, 0, 0, 0.28)',
        'clay-btn-active': '4px 6px 12px rgba(99, 102, 241, 0.4), inset 4px 5px 8px rgba(0, 0, 0, 0.35), inset -2px -3px 4px rgba(255, 255, 255, 0.3)',
        'clay-well': 'inset 4px 4px 8px rgba(166, 178, 198, 0.6), inset -4px -4px 8px rgba(255, 255, 255, 0.95)',
        'clay-well-dark': 'inset 4px 4px 8px rgba(0, 0, 0, 0.65), inset -3px -3px 6px rgba(255, 255, 255, 0.04)',

        // Neo-brutalism: unblurred mechanical offset shadows
        'neo-sm': '2px 2px 0px #121212',
        'neo': '4px 4px 0px #121212',
        'neo-lg': '8px 8px 0px #121212',
        'neo-xl': '12px 12px 0px #121212',

        // Skeuomorphism: tactile multi-stop specular bevels
        'skeuo-btn': 'inset 0 1px 0 rgba(255, 255, 255, 0.75), inset 0 -2px 0 rgba(0, 0, 0, 0.35), 0 3px 6px rgba(0, 0, 0, 0.2)',
        'skeuo-pressed': 'inset 0 2px 5px rgba(0, 0, 0, 0.5), inset 0 -1px 0 rgba(255, 255, 255, 0.3), 0 1px 2px rgba(0, 0, 0, 0.1)',
        'skeuo-well': 'inset 0 2px 6px rgba(0, 0, 0, 0.55), inset 0 0 1px rgba(0, 0, 0, 0.8)',

        // Retro-terminal: authentic CRT raster glows
        'crt-amber': '0 0 8px rgba(255, 176, 0, 0.55), 0 0 20px rgba(255, 176, 0, 0.25)',
        'crt-green': '0 0 8px rgba(51, 255, 51, 0.55), 0 0 20px rgba(51, 255, 51, 0.25)',

        // Glassmorphism: ambient diffuse refraction
        'glass-surface': '0 8px 32px 0 rgba(31, 38, 135, 0.15)',
        'glass-surface-dark': '0 8px 32px 0 rgba(0, 0, 0, 0.55)',

        // Bento: subtle layered elevation
        'bento-card': '0 1px 2px rgba(0, 0, 0, 0.3), 0 10px 24px -4px rgba(0, 0, 0, 0.45)',

        // Retro Pixel: stepped bevels and integer offset shadows
        'pixel-btn': 'inset 2px 2px 0px rgba(255, 255, 255, 0.35), inset -2px -2px 0px #000, 2px 2px 0px #000',
        'pixel-btn-active': 'inset 2px 2px 0px #000, inset -2px -2px 0px rgba(255, 255, 255, 0.35)',
        'pixel-window': 'inset 2px 2px 0px rgba(255, 255, 255, 0.35), inset -2px -2px 0px #000, 4px 4px 0px #000',
        'pixel-well': 'inset 2px 2px 0px #000, inset -2px -2px 0px rgba(255, 255, 255, 0.25)',
      },
      borderRadius: {
        'clay-sm': '1rem',
        'clay-md': '1.5rem',
        'clay-lg': '2rem',
        'clay-full': '9999px',
        'neo': '0.375rem',
        'brutal': '0px',
        'bento': '1.75rem',
        'pixel': '0px',
      },
      borderWidth: {
        'neo': '2.5px',
        'brutal': '2.5px',
        'pixel': '2px',
        'hairline': '1px',
      },
      fontFamily: {
        term: ['"JetBrains Mono"', '"Courier New"', 'monospace'],
        swiss: ['"Space Grotesk"', 'Inter', 'Helvetica', 'Arial', 'sans-serif'],
        pixel: ['"Pixelify Sans"', '"Press Start 2P"', 'monospace'],
      },
    },
  },
};

export default tastePreset;

if (typeof module !== 'undefined' && module.exports) {
  module.exports = tastePreset;
}
