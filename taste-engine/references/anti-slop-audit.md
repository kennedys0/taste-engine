# Anti-Slop Audit — evidence-driven UI review

Run after style selection + implementation and before claiming a UI is finished. Applies alongside selected style pack and universal quality gates. For custom styles, use that project's agreed style constraints.

See [quality tiers](quality-tiers.md): `FLOOR` is an integrity defect, `REFLEX` is a rebuttable AI-default heuristic, and `FINISH` is non-blocking polish. The severity scale below describes **impact** within those tiers; style differences alone never count as blocking defects. Preserve existing product features using [redesign preservation](redesign-preservation.md) and record actual [browser checks](browser-validation.md).

## Review ordering and severity

1. **Critical — must fix:** deceptive fabricated metrics/status, unsafe misleading action, broken primary flow, accessibility blocker.
2. **High — must fix:** clipped or obstructed controls, confusing interaction, unusable mobile layout, heavy gratuitous nested surfaces, unverified success claims.
3. **Medium — fix when feasible:** redundant cards/labels/chips, inconsistent hierarchy, confusing copy, mismatched peer components, purposeless animation.
4. **Polish — stylistic suggestion:** spacing finesse, subtle surface refinement, optional copy tone adjustment without a usability issue.

Do **not** mark an expressive style feature as defective just because the auditor personally prefers minimalism. Explain impact and a concrete fix. No arbitrary numeric slop score is necessary.

## Acceptance checklist

- [ ] **Style fidelity:** the UI matches the *selected* style and approved project choices, not generic trends or an unrelated preference.
- [ ] **Composition:** groups reflect data/task relationships; nested surfaces have distinct semantic ownership; equal peers feel balanced; intentional asymmetry is clear.
- [ ] **Purpose & zero emojis:** each badge, icon, chart, gradient, hero, motion, and control serves content, interaction, or chosen style; zero emojis used as UI icons, button prefixes, or badges (only Lucide or clean vector SVGs with currentColor).
- [ ] **Full-screen hero (if applicable):** header + hero respect one visible viewport; height uses a mobile-safe min-height strategy; no clipped title, CTA, safe area or keyboard focus; no fake decoration to fill space. See `hero-layout.md`.
- [ ] **Content & truth:** no invented numbers, testimonials, logo strips, realtime statuses, urgency, placeholders masquerading as real users, or false successes.
- [ ] **Copywriting:** headings say something; CTA predicts result; microcopy explains state/recovery; no generic motivational filler; locale is natural.
- [ ] **Typography & controls:** coherent tokens, readable type hierarchy, working focus, labels, button shapes, and consistent component geometry.
- [ ] **Responsive down to 320px & Mobile Header:** verified down to 320px viewport with zero horizontal scroll blowout; mobile typography scales down proportionally to prevent bloated UI; navigation header collapses comfortably into an accessible hamburger menu on narrow screens (< 768px).
- [ ] **Strict circle geometry (anti-oval):** circular elements (avatars, status dots, icon badges, action buttons with `border-radius: 50%`) enforce `aspect-ratio: 1 / 1` and `flex-shrink: 0` so they never squish into ovals/ellipses under mobile flexbox compression.
- [ ] **Motion:** purposeful and respects reduced motion; no idle bounce / glow loops unless explicitly justified as meaningful UI state.
- [ ] **Functional integrity:** key actions work or are explicitly labeled unfinished; state transitions reflect real responses; empty/loading/error handling.
- [ ] **Evidence:** only claim viewport checks, accessibility tests or end-to-end behavior actually performed. Note untested checks.

## Review format (use when reporting audit results)

For each observed issue:

`[Critical | High | Medium | Polish] • [location/component] • [observed problem] • [user impact] • [specific correction] • [evidence/status]`

Example:

`[High] • Overview / ReportsPanel • an empty-state card is placed inside an empty dashboard card • doubled borders make the primary action hard to scan • render text + CTA directly inside ReportsPanel • verified in 375px screenshot`

If a design variant intentionally departs from a heuristic, state: `Exception: [specific style/product purpose]; verified [usability criterion]`. Never justify an exception merely as "modern".

## Exit gate

- **Fail** until all Critical/High findings are resolved or clearly disclosed as unresolved blockers.
- **Review** when only Medium/Polish findings remain; fix them where feasible without overriding the user's taste.
- **Pass** when all applicable checks have evidence and no blocking defects remain.

If screenshots or a runnable environment are unavailable, give an **instruction-level review**, not a claim of a visual/functional test. This document is a human/agent checklist, not a guaranteed enforcement mechanism.
