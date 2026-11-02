# React Native / Expo — conditional mobile engineering

Activate for confirmed React Native or Expo projects, not for responsive websites. Conceptual source: https://github.com/vercel-labs/agent-skills/tree/main/skills/react-native-skills . Use the app's current supported versions and existing libraries rather than importing the upstream examples indiscriminately.

## Mobile FLOOR

- Navigation is reachable and correct for iOS/Android; account for system bars, notches, home indicators, software keyboard, font scaling and orientation.
- Touch targets, focus/accessibility labels and text contrast must remain usable. Don't rely on hover or web-only CSS/DOM interactions.
- Preserve data state, permissions and platform conventions. Request device permission at the point of need, with fallback for denial.
- Prefer actual platform-native animation/gesture systems and interruptible interactions; honor user motion accessibility settings.

## Technical opportunities

- Large lists: virtualize with the project's established list primitive; optimize expensive rows, stable keys, and image handling. Do not force a specific vendor library if current versions or needs differ.
- Image views: use correct caching/sizing primitives for the project. Avoid loading huge images for tiny thumbnails.
- Use existing native navigators and safe-area management. Prefer platform-native menus/modals where behavior aligns with the app.
- Avoid broad state subscriptions and expensive per-frame React updates. Use native animation/gesture handling where appropriate.
- Preserve native dependency consistency in monorepos; inspect Expo config, lockfiles and SDK versions before imports.

SEO/canonical/sitemap and Anime.js-on-DOM do not apply to native screens. If the product also has a public marketing site, run web SEO on the web portion only.
