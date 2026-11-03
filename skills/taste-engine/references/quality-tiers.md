# Three-tier anti-slop decision gates

All styles must run the same **integrity floor**. Above the floor, style-specific expression may intentionally override a reflex. A polish finding is never a reason to withhold useful work.

## FLOOR — blocking defects (cannot be waived by aesthetics)

- Invented or misleading factual content, states, people, statistics, reviews, logos, authorizations, payment/success confirmations or live indicators.
- A primary action that appears functional but does nothing; essential controls with no label, keyboard route or visible focus; misrepresented destructive actions.
- Important text or primary actions hidden, clipped, obstructed or unreadable on supported viewports; insufficient contrast and inaccessible motion with no usable reduction.
- **Theme and mode contrast collisions:** when switching or requesting dark mode or light mode, background and foreground/text MUST adapt together as coupled tokens. Background and text colliding with the same or unreadable polarity (e.g. black text on black background, white text on white background, unreadable low-contrast placeholders or borders) is a blocking defect. Both modes must meet WCAG AA contrast (minimum 4.5:1 for body/normal text, 3:1 for large headlines and interactive boundaries).
- Data chart distortion that materially misleads viewers (e.g. truncated bar baselines without explicit justified encoding); inaccessible data with no text/accessible alternative.
- Security/privacy or user-consent regressions during a visual redesign.

Action: fix or clearly disclose as unresolved blocker. A source-only scan cannot certify passing this tier.

## REFLEX — suspicious defaults (challenge; can be justified)

- Gratuitous cards inside cards; auto 3-feature grids; generic four-metric strip; badge → headline → subtitle → CTA conveyor; unused decorative gradients, blobs or glows.
- Repeated identical component framing, unbalanced peers, accidental whitespace, mismatched density, generic font/theme defaults, icons on every label.
- Fancy punctuation or stock UI marketing without content; overlong helper text; vague CTAs; passive voice obscuring the actor.
- Perpetual animation without information; needless UI libraries; scroll reveal applied to everything.

Action: **remove, adapt, or document** a product/style-grounded exception. Example: 'Nested panel = a separately editable bill section with its own focus and validation state.' The words 'modern', 'premium' and 'trendy' are not exceptions.

## FINISH — nonblocking craft improvements

- Optical alignment, typographic rhythm, spacing finesse, fine-grained content density, small copy refinements, border/shadow consistency, responsive edge cases beyond supported device requirements.
- Assess against chosen style. Neutral calm UI isn't inherently polished; expressive layouts aren't inherently unpolished.

Action: improve if feasible, but do not block truthful, usable work just to chase subjective aesthetics.

## Audit record

Use structured observations (written or JSON) with fields:

- `tier`: `FLOOR` / `REFLEX` / `FINISH`
- `location`: exact route/component
- `observation`: what exists, not what you assume
- `impact`: how user experience or style fidelity is harmed
- `evidence`: screenshot, code path, test or 'not verified'
- `resolution`: fix, justified exception, unresolved
- `exception_reason`: required if a REFLEX is kept

Critical check: if a claim of 'tests passed' has no recorded test, the claim itself is misleading. Report static lint as static lint, not browser proof.

## Context-specific exceptions

Glass blur, hard offset shadows, clay depth, paper texture, uneven magazine columns, retro monospace and Bento tiles are **not** automatic findings. Judge whether they serve the selected material, content, accessibility and device. Do not import another repository's universal ban list as the project's law.

## SEO integrity addendum (public web only)

Apply `references/seo.md` for search-facing pages. **FLOOR:** revealing private paths, mismatched indexability vs intended publish state, fabricated JSON-LD/reviews/author claims, conflicting canonicals and false audit assertions. **REFLEX:** duplicate boilerplate titles, keyword-stuffed headings, redundant schema, low-value SEO filler. **FINISH:** refined snippet descriptions, real sharing image, sitemap maintenance and optional rich result validation. These gates are independent of visual style; do not force the same design across aesthetics.
