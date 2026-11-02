# Native view transitions and Anime.js selection

Relevant upstream: https://github.com/vercel-labs/agent-skills/tree/main/skills/react-view-transitions . This Taste Engine document is a compatibility-aware policy, not a copied API guide.

Use when the user asks to animate route changes, list→detail continuity, component entry/exit or shared elements. **First inspect the installed framework and its available transition APIs**. Do not assume a future/stable React API is present just because a guide mentions it.

## Choose the smallest tool

1. Instant state update: when motion is not informative or style is strict Brutalism, no animation is valid.
2. Basic hover/press/fade: use CSS. Keep durations brief; ensure reduced-motion behavior.
3. Shared element or route continuity: prefer platform-native View Transitions or framework-supported APIs if compatible and stable in this project. Check support/fallback and navigation behavior.
4. Sequenced/timeline micro-interaction: use optional Anime.js v4 if it materially simplifies the interaction and was approved/needed.
5. React Native/Expo: use native navigation/animation patterns; do not add web Anime.js to native view components.

## Semantics

- Use directional slide only if navigation has meaningful forward/back depth; tabs should not imply false spatial hierarchy.
- Maintain interactive focus and URL/navigation state during transitions. Preserve DOM visibility when animation disabled or unsupported.
- Never duplicate animations (React ViewTransition plus Anime.js on the same state change) unless explicitly coordinated and tested.
- No artificial delay of content, mandatory reveal sequences, scroll hijacking or hover-only controls.
- Test rapid back/forward navigation, concurrent updates, interrupted transitions, no-JS/reduced-motion fallback if relevant, and low-end mobile responsiveness.

Keep style-specific motion from `styles/<id>.md`. It determines aesthetic behavior, not the dependency choice.
