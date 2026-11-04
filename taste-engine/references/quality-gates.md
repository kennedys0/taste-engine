# Universal design quality gates

Taste can vary; product quality should not.

## 1. Usability

- Key actions are clear and discoverable.
- Navigation reflects user jobs and structure, not decorative trends.
- Labels communicate real meaning; hierarchy supports scanning.
- Loading, empty, error, success, offline, and disabled states are addressed where applicable.
- Inputs support correction and recovery.

## 2. Accessibility

- Target WCAG 2.2 AA where appropriate for web, including legible text, keyboard access, meaningful semantics, sufficient contrast, and focus visibility.
- Support dark/light mode switching cleanly: verify that background and text colors change in coupled pairs and never collide (e.g. no black text on black background, white text on white background, or low-contrast gray-on-dark). All inputs, placeholders, borders, hover states, and semantic status badges must remain legible and pass contrast in both modes.
- Support reduced motion; do not use motion as the only way to convey meaning.
- Consider touch target size, zoom/text scaling, screen readers, and color-independent status messaging.
- Visual references are not an excuse to copy inaccessible behavior.

## 3. Responsive integrity

- Check narrow screens, tablet/intermediate widths, and desktop as relevant.
- No clipped headings, overflowing actions, unusable tables, or arbitrary blank columns.
- Keep layout rhythm, card/component alignment, and readable density coherent across breakpoints.
- Scale typography and spacing down proportionally on mobile viewports (< 768px, < 480px) using `clamp()` or adaptive breakpoints to prevent bloated UI ("UI bengkak"). Terminal code must use `word-break: break-all` / `overflow-x: auto` without horizontal blowout.
- Keep quick install pills, command-line snippets, and copy buttons inline in a single horizontal row ("sejajarin").
- On mobile, organize footer navigation links into a balanced 2-column grid (`repeat(2, 1fr)`) with tactile thumb-friendly tap targets instead of endless 1-column link dumps.

### Public hero composition

When the product legitimately has a hero, its first-screen header+hero composition must feel full-viewport, use real content, and not clip navigation or primary actions on mobile/short screens. Check [full-screen hero contract](hero-layout.md). Do not force heroes into task-driven internal screens; if the user requests no/compact hero, respect that.

## 4. Visual coherence

- Typography, spacing, color, radii, depth, and motion form a coherent system.
- Repeated components have consistent behavior and sizing.
- Decoration has a purpose; avoid trend-driven UI noise.
- Distinguish an intentional design direction from an accidental mixture of styles.

## 5. Trust and implementation

- No fake metrics, reviews, activity indicators, or misleading status labels.
- Test working interactions when execution/test tools are available.
- Respect the existing stack and avoid unrequested dependencies.
- Report what was checked, what was not checked, and remaining limitations.

## Review result

When auditing an existing UI, separate:

- **Blocking defects** (broken interactions, inaccessible controls, content clipping).
- **Strong UX recommendations** (navigation or clarity improvements).
- **Subjective taste considerations** (color, depth, roundedness, expressive typography).

Do not treat subjective deviations from the agent's taste as objective defects.

## 6. Universal Anti-Slop gate (mandatory)

For every visual project or UI audit, also run:
- [Anti-Slop Constitution](anti-slop.md) — purpose, honest data/states, nested surface restraint, compositional discipline and style-specific exceptions.
- [Anti-Slop Writing](anti-slop-copywriting.md) — product-aware content, exact CTAs, truthful status/error/empty copy.
- [Anti-Slop Audit](anti-slop-audit.md) — evidence-based Critical/High findings that block completion.
- Selected style pack's `## Anti-slop: style-specific` section.

This gate rejects *unjustified* patterns, not whole aesthetics. Distinguish blocking defects from personal taste and document exceptions with a functional/style rationale.
