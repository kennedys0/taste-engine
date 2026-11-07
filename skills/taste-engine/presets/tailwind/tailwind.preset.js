/**
 * Taste Engine — Tailwind CSS Preset (v0.12.0)
 * Comprehensive theme extension for 10 curated frontend aesthetic archetypes.
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

          // Frutiger Aero: luminous aqua, sky, seafoam, deep ocean, spring leaf, and cloud white
          'aero-aqua': 'var(--taste-aero-aqua, #48BFD3)',
          'aero-aqua-bright': 'var(--aero-aqua, #6CD1E8)',
          'aero-ocean': 'var(--taste-aero-ocean, #247EA3)',
          'aero-ocean-bright': 'var(--aero-ocean, #2C90B8)',
          'aero-seafoam': 'var(--aero-seafoam, #A7E6D5)',
          'aero-leaf': 'var(--taste-aero-leaf, #70B981)',
          'aero-leaf-bright': 'var(--aero-leaf, #79C67A)',
          'aero-sky': 'var(--taste-aero-sky, #C9EDF8)',
          'aero-sky-soft': 'var(--aero-sky, #DCEFF8)',
          'aero-cloud': 'var(--taste-aero-cloud, #F4FAFC)',
          'aero-cloud-pure': 'var(--aero-cloud, #F7FBFD)',
          'aero-deep-blue': 'var(--taste-aero-deep-blue, #173F61)',
          'aero-deep-ocean': 'var(--aero-deep-blue, #1F5D87)',
          'aero-charcoal': 'var(--taste-aero-charcoal, #243642)',
          'aero-surface': 'var(--taste-aero-surface, rgba(255, 255, 255, 0.78))',
          'aero-surface-dark': 'var(--taste-aero-surface-dark, rgba(20, 42, 64, 0.76))',
          'aero-border': 'var(--taste-aero-border, rgba(255, 255, 255, 0.92))',

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

          // Brutalism: raw unembellished mono (Raw & Bento layout variants)
          'brutal-bg': 'var(--taste-brutal-bg, #f4f4f4)',
          'brutal-ink': 'var(--taste-brutal-ink, #000000)',
          'brutal-canvas': 'var(--taste-brutal-canvas, #ffffff)',
          'brutal-yellow': 'var(--taste-brutal-signal-yellow, #ffde00)',
          'brutal-red': 'var(--taste-brutal-signal-red, #ff3b30)',

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

          // Art Deco: architectural geometric elegance and metallic accents
          'deco-bg': 'var(--taste-deco-bg, #f5f0e6)',
          'deco-surface': 'var(--taste-deco-surface, #ffffff)',
          'deco-surface-elevated': 'var(--taste-deco-surface-elevated, #ece5d6)',
          'deco-ink': 'var(--taste-deco-ink, #292b29)',
          'deco-ink-muted': 'var(--taste-deco-ink-muted, #636662)',
          'deco-brass': 'var(--taste-deco-accent, #b69a68)',
          'deco-gold': '#b89b5e',
          'deco-bronze': '#a98462',
          'deco-emerald': '#183d36',
          'deco-forest': '#24453d',
          'deco-burgundy': '#693b43',
          'deco-border': 'var(--taste-deco-border, #d4c7b0)',

          // Y2K Futurism: liquid chrome, iridescent spectral tones, and synthetic hardware
          'y2k-silver': 'var(--taste-y2k-silver, #C5CBD3)',
          'y2k-chrome-highlight': 'var(--y2k-chrome-highlight, #FFFFFF)',
          'y2k-chrome-light': 'var(--taste-y2k-chrome-light, #F1F3F6)',
          'y2k-chrome-mid': 'var(--y2k-chrome-mid, #A4ADBF)',
          'y2k-chrome-shadow': 'var(--y2k-chrome-shadow, #424B60)',
          'y2k-chrome-deep': 'var(--y2k-chrome-deep, #1D2331)',
          'y2k-graphite': 'var(--taste-y2k-graphite, #252833)',
          'y2k-violet': 'var(--taste-y2k-violet, #8865DD)',
          'y2k-orchid': 'var(--y2k-orchid, #A78AFF)',
          'y2k-electric-blue': 'var(--y2k-electric-blue, #5276FF)',
          'y2k-ice-blue': 'var(--taste-y2k-ice-blue, #90DCFF)',
          'y2k-pink': 'var(--taste-y2k-pink, #F2A9DC)',
          'y2k-pearl': 'var(--y2k-pearl, #F3EAFD)',
          'y2k-deep-space': 'var(--taste-y2k-deep-space, #181821)',
          'y2k-surface': 'var(--taste-y2k-surface, #2A2E3D)',
          'y2k-border': 'var(--taste-y2k-border, rgba(197, 203, 211, 0.35))',
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

        // Art Deco: crisp architectural framing
        'deco-card': '0 4px 20px rgba(0, 0, 0, 0.06)',
        'deco-elevated': '0 12px 36px rgba(0, 0, 0, 0.12)',

        // Frutiger Aero: glossy horizon sheens, tactile molded buttons, and translucent dock elevation
        'aero-card': '0 14px 32px rgba(58, 105, 141, 0.18), 0 2px 6px rgba(31, 93, 135, 0.08), inset 0 1.5px 0 #FFFFFF, inset 0 0 0 1px rgba(108, 209, 232, 0.24), inset 0 -2px 4px rgba(44, 144, 184, 0.12)',
        'aero-card-dark': '0 16px 38px rgba(0, 0, 0, 0.48), inset 0 1.5px 0 rgba(255, 255, 255, 0.32), inset 0 0 0 1px rgba(108, 209, 232, 0.16), inset 0 -2px 5px rgba(0, 0, 0, 0.45)',
        'aero-btn': '0 6px 16px rgba(31, 93, 135, 0.34), 0 2px 4px rgba(23, 63, 97, 0.2), inset 0 1.5px 0 rgba(255, 255, 255, 0.92), inset 0 -2px 3px rgba(11, 38, 59, 0.45), inset 0 -1px 6px rgba(108, 209, 232, 0.55)',
        'aero-btn-active': '0 1px 3px rgba(31, 93, 135, 0.25), inset 0 3px 6px rgba(11, 35, 54, 0.5), inset 0 1px 2px rgba(0, 0, 0, 0.35), inset 0 -1px 2px rgba(108, 209, 232, 0.35)',
        'aero-btn-secondary': '0 5px 14px rgba(58, 105, 141, 0.18), 0 1px 3px rgba(31, 93, 135, 0.12), inset 0 1.5px 0 #FFFFFF, inset 0 -2px 3px rgba(44, 144, 184, 0.22)',
        'aero-dock': '0 14px 34px rgba(44, 144, 184, 0.22), inset 0 1.5px 0 #FFFFFF, inset 0 -2px 4px rgba(44, 144, 184, 0.16)',
        'aero-well': 'inset 0 2px 5px rgba(31, 93, 135, 0.18), inset 0 1px 2px rgba(23, 63, 97, 0.12), 0 1px 0 rgba(255, 255, 255, 0.95)',

        // Y2K Futurism: metallic chrome, holographic glow, and specular framing
        'y2k-card': '0 8px 32px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(241, 243, 246, 0.4)',
        'y2k-card-light': '0 8px 24px rgba(37, 40, 51, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.9)',
        'y2k-btn': '0 4px 14px rgba(0, 0, 0, 0.35), inset 0 1px 0 #FFFFFF',
        'y2k-btn-violet': '0 4px 16px rgba(136, 101, 221, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.4)',
      },
      borderRadius: {
        'clay-sm': '1rem',
        'clay-md': '1.5rem',
        'clay-lg': '2rem',
        'clay-full': '9999px',
        'aero-sm': '0.625rem',
        'aero-md': '1rem',
        'aero-lg': '1.25rem',
        'aero-full': '9999px',
        'y2k-sm': '0.25rem',
        'y2k': '0.375rem',
        'y2k-lg': '0.5rem',
        'neo': '0.375rem',
        'brutal': '0px',
        'bento': '1.75rem',
        'pixel': '0px',
        'deco': '2px',
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
        deco: ['"Cinzel"', '"Playfair Display"', 'Georgia', 'serif'],
        aero: ['"Segoe UI"', 'Frutiger', '"Trebuchet MS"', 'Inter', 'sans-serif'],
        y2k: ['"Space Grotesk"', '"Syne"', '"Orbitron"', 'Inter', 'sans-serif'],
      },
    },
  },
};

export default tastePreset;

if (typeof module !== 'undefined' && module.exports) {
  module.exports = tastePreset;
}
