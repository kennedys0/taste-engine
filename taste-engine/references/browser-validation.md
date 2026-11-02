# UI evidence and browser validation (host/tool permitting)

This is a repeatable **procedure**, not a claim that a browser was run. A frontend screenshot is necessary for many visual claims; static source review cannot prove visual balance or interaction usability.

## Full-screen hero evidence (when applicable)

Use [hero-layout.md](hero-layout.md) to verify header+hero really form one opening viewport. Check both overlay and normal-flow navbar arrangements, viewport toolbars on mobile, short-height landscape, 200% zoom, long translated headings and primary CTA visibility. Prefer `100svh` stable minimum for mobile hero; ensure content can grow. Source code cannot prove visual correctness.

## Suggested coverage

1. Capture desktop 1440px, tablet 768px, mobile 390px and narrow 320px; add intermediate widths for content-driven breakpoints. On native mobile test actual safe areas and font scaling.
2. Inspect top viewport **and** long-page overflow; verify no horizontal scrolling in ordinary reading state, long button labels, form error text, long user names, empty data.
3. Keyboard-only navigation: tab/focus order, inputs, dialogs, menus, drawers, primary action, Escape and return focus.
4. Functional conditions: empty, loading, partial results, success from real acknowledgment, error/retry, disabled and offline where relevant.
5. If motion exists, test `prefers-reduced-motion`; check touch-only devices don't depend on hover.
6. Check contrast and meaningful alt/accessible names with appropriate tools if available; annotate manual checks separately from automated findings.
7. Compare intended style to rendered output. Does the selected material genuinely appear? Do not call a white card + soft shadow 'clay' or blurry overlay 'glass' if material logic is inconsistent.
8. Report exact environments and widths actually tested. Any missing check is **untested**, not passed.

Optional external tooling (Playwright, axe-core, device emulators) may help if present in a project; this skill does not install them silently. For an audit-only request, do not modify code.
