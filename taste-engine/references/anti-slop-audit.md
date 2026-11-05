# Anti-Slop Audit — evidence-driven UI and code review

Run after style selection + implementation and before claiming a UI or code deliverable is finished. Applies alongside the selected style pack and universal quality gates. For custom styles, use that project's agreed style constraints.

See [quality-tiers.md](quality-tiers.md): `FLOOR` is an integrity defect, `REFLEX` is a rebuttable AI-default heuristic, and `FINISH` is non-blocking polish. The severity scale describes **impact** within those tiers; style differences alone never count as blocking defects. Preserve existing product features using [redesign preservation](redesign-preservation.md) and record actual [browser checks](browser-validation.md).

---

## Vibecoded Red Flags — fast scanner (run before structural tests)

Scan for these patterns immediately on load. Each flag is a trigger for the Three-Layer Review below — not a conviction by itself.

- [ ] **Purple/blue mesh gradient as default background** — flag unless glassmorphism or cyberpunk is the confirmed style
- [ ] **Neon glow exceeding `box-shadow` blur > 20px** on non-terminal, non-retro UI elements
- [ ] **Emoji used as functional icon, bullet point, status indicator, or decorative sticker** — replace with Lucide/Radix SVG
- [ ] **Uniform card spam** — every card identical in size, structure, and visual weight (failed Deletion Test candidate)
- [ ] **Inconsistent spacing units** — mixing `px`, `rem`, and arbitrary Tailwind values without a declared token system
- [ ] **Copy with ≥ 3 exclamation marks, ≥ 2 em-dashes, or ≥ 1 "In today's fast-paced world"** variant
- [ ] **Hero section > 100vh** without explicit product justification in the brief
- [ ] **Font stack not loaded** — fallback renders visibly as system default serif or sans
- [ ] **Rainbow text gradient** (`-webkit-background-clip: text`) on headings outside retro/cyberpunk themes
- [ ] **Fake widgets** — fabricated weather, audio spectrum, simulated live telemetry, or animated counters with no real data

Each flagged item proceeds to Layer 0 / Layer 1 below before it becomes a reported finding.

---

## 9-Pass Audit Order

Run passes sequentially. A pass may surface findings at any severity tier; complete all passes before writing the report.

| Pass | Surface | Key checks |
|------|---------|------------|
| **1 — Spacing** | UI | Token consistency, rhythm, padding scale, 320px baseline, circle geometry |
| **2 — Color** | UI | Contrast (WCAG AA 4.5:1), dark/light mode collision, palette intent vs. selected style |
| **3 — Icons** | UI | Vector SVG only, consistent stroke weight (1.5px–2px), no emoji, meaningful state changes |
| **4 — Copy** | Content | Parataxis, banned vocabulary, claim truthfulness (Inversion + Attribution tests) |
| **5 — Typography** | UI + Content | Scale, burstiness, tabular-nums for data, font loading, mobile clamp values |
| **6 — Layout** | UI | 320px baseline, hamburger nav, hero height, single-line command pills, footer grid |
| **7 — Details** | UI | Border-radius consistency, focus rings, hover/active states, shadow intentionality |
| **8 — Visuals** | UI | Gradient intent (style-authentic vs. default soup), texture authenticity, no fake widgets |
| **9 — Motion** | UI | `prefers-reduced-motion` support, no idle/decorative loops, state-driven transitions only |

---

## Core Audit Axioms

1. **Reports defects, never reports authorship:** Never guess whether an AI or a human generated the output. Audit whether there is a verifiable defect in substance, usability, code integrity, or truthfulness.
2. **A marker is never itself a finding:** Seeing a suspicious word ("pivotal"), an em-dash, or an abstraction wrapper merely selects the span for testing. If the structural test confirms the item is load-bearing and carries genuine substance, **drop the marker hit**. Do not downgrade it to keep a finding alive.
3. **Every finding must produce an artifact:** A test you did not actually run produces no artifact and therefore no finding. No "reads as generic" or "probably unnecessary" without evidence.

---

## Severity vs. Confidence (Two Separate Axes)

Never collapse impact and certainty into a single arbitrary score:

### Axis 1: Severity (Impact)
- **Critical (Must fix):** Deceptive fabricated metrics/status, unsafe misleading actions, broken primary flows, accessibility blockers, package hallucination (non-existent dependency).
- **High (Must fix):** Clipped or obstructed controls, confusing interaction, unusable mobile layout (< 320px), heavy gratuitous nested surfaces, unverified success claims, assertion-free tests (coverage padding).
- **Medium (Fix when feasible):** Redundant cards/labels/chips, vacuous copy (failed Inversion Test), padding (failed Deletion Test), passthrough wrappers, defensive error swallowing, purposeless animations.
- **Polish (Stylistic suggestion):** Spacing finesse, subtle surface refinement, optional copy cadence adjustments without usability harm.

### Axis 2: Confidence (Certainty)
- **High:** Verified with a mechanical experiment (deletion broke a test, negation is nonsense, package 404s in npm/PyPI registry, contrast math fails WCAG AA).
- **Medium:** Strong contextual evidence, but runtime or screenshot verification was partially constrained.
- **Low:** Manual heuristic assessment where tests/build could not be executed. Disclose as Low confidence rather than asserting harder.

---

## The Three-Layer Review Procedure

1. **Layer 0 (Decidable Scanners):** Check binary facts.
   - Do all imported packages exist in npm/PyPI?
   - Do called methods match pinned library versions?
   - Does text contrast meet WCAG AA (4.5:1 for normal, 3:1 for large)?
   - Does the build and test suite pass?
2. **Layer 1 (Structural Procedures):** Run the 5 structural tests on suspicious spans and produce artifacts:
   - **Deletion Test (Prose/UI):** Cut the span. What was lost? (Artifact: cut span + named loss).
   - **Inversion Test (Copy):** Negate the claim. Would anyone assert it? (Artifact: written negation).
   - **Stranger Test (Grounding):** Could an outsider write this from a generic prompt? (Artifact: insider ground truth).
   - **Attribution Test (Evidence):** Does the citation/claim resolve? (Artifact: verified source or noted absence).
   - **Load-Bearing Test (Code):** Delete the wrapper/comment/handler/test. Did anything break? (Artifact: test failure log or caller audit).
3. **Layer 2 (Heuristic Markers):** Vocabulary lists, em-dash counts, burstiness, card nesting. Route each marker hit to Layer 1.

---

## Acceptance Checklist

### UI & Layout Surface
- [ ] **Style fidelity:** UI matches the *selected* style (Glass, Clay, Neo-Brutalism, etc.); style-defining features are not penalized by generic anti-gradient or anti-shadow reflexes.
- [ ] **Composition & nesting:** Groups reflect task relationships; nested surfaces have distinct semantic ownership; equal peer cards have equal visual weight.
- [ ] **Strict 320px responsive baseline:** Fully functional down to 320px viewport with zero horizontal scroll blowout.
- [ ] **Strict 1:1 circle geometry (anti-oval):** All circular elements (avatars, status dots, icon badges, action buttons with `border-radius: 50%`) enforce `aspect-ratio: 1 / 1;` and `flex-shrink: 0;`.
- [ ] **Mobile header navigation:** On narrow viewports (< 768px), navigation links collapse behind an accessible Hamburger Menu (Lucide `Menu` SVG) with 44px+ tap targets.
- [ ] **Single-line command pills:** Quick install bars keep `$`, snippet, and copy button strictly inline in one horizontal row.
- [ ] **Zero emojis in UI:** Vector SVGs only (Lucide, Radix, Feather).
- [ ] **Theme contrast integrity:** Coordinated light/dark mode color flips; no dark text on dark canvas; dark mode uses slate-grey canvas (`#212328`) over pitch-black.
- [ ] **Hero layout:** 1-viewport hero composition respects mobile toolbars without manufactured empty fillers.

### Copy & Content Surface
- [ ] **Truthfulness:** No fabricated metrics, testimonials, customer logos, fake counts, or unearned live statuses.
- [ ] **Structural tests passed:** No padding (Deletion Test passed); no vacuous claims (Inversion Test passed); grounded in product facts (Stranger Test passed).
- [ ] **Cadence & syntax:** No parataxis (ideas connected with real syntax); rule-of-three broken; sentence length rhythm varied (burstiness).
- [ ] **Punctuation discipline:** Max 1 em-dash per 500 words; max 1 exclamation mark per 1,000 words.
- [ ] **Banned patterns eliminated:** No formulaic openers (*"In today's fast-paced world"*, *"It's worth noting that"*); no negative parallelism (*"Not just X, but Y"*); no AI cheerleading.

### Code Surface
- [ ] **Comment hygiene:** Zero decorative ASCII separators (`// ============`); zero comments that merely restate the code line beneath; zero step narration comments.
- [ ] **Load-bearing code:** No passthrough wrappers without logic; no ghost abstractions (interfaces/factories with only 1 implementation).
- [ ] **Error handling:** No defensive bare `except:` or `catch (e) {}` blocks that swallow bugs.
- [ ] **Test suite integrity:** No assertion-free tests; mutations in tested behavior cause test failures.
- [ ] **Decidable dependencies:** All npm/PyPI packages exist; API signatures match pinned versions.

---

## Review Reporting Format

For each observed issue, format the finding as:

```
[Severity] • [Confidence] • [Surface: UI | Copy | Code] • [Location] • [Test Used]
  Artifact: <Verbatim cut span, written negation, resolved source, or failing command>
  Problem:  <Observed defect and why it degrades substance/usability>
  Fix:      <Concrete, actionable correction>
```

### Worked Case Examples

**Case 1: Copy Padding (Prose Surface)**
```
[Medium] • [High] • [Copy] • LandingPage / HeroDescription • [Deletion Test]
  Artifact: Cut span: "marking a pivotal step in the evolution of modern workflows" | Lost: Nothing.
  Problem:  The phrase adds generic praise without naming any mechanism, metric, or workflow task.
  Fix:      Replace with: "Export CSV reports directly from completed work orders."
```

**Case 2: Vacuous Marketing Claim (Copy Surface)**
```
[Medium] • [High] • [Copy] • FeatureList / Item 3 • [Inversion Test]
  Artifact: Written negation: "Our platform is engineered to be fragile and unreliable."
  Problem:  Nobody would assert the negation; the claim "Engineered for maximum reliability" states no checkable fact.
  Fix:      State the concrete guarantee: "99.95% uptime SLA with automated multi-region failover."
```

**Case 3: Ghost Wrapper (Code Surface)**
```
[Medium] • [High] • [Code] • src/services/user_service.py:42 • [Load-Bearing Test]
  Artifact: Deleted `retry_fetch_user`. Rewired single caller `handlers.py:88` directly to `fetch_user`. Ran test suite: all 42 tests passed.
  Problem:  The wrapper passed arguments through unchanged with zero retry or backoff logic.
  Fix:      Remove wrapper and call `fetch_user` directly.
```

**Case 4: Assertion-Free Test (Code Surface)**
```
[High] • [High] • [Code] • tests/test_auth.py:15 • [Load-Bearing Test]
  Artifact: Mutated `login_user()` to `return None`. Test `test_login()` still passed because it only asserted `login_user is not None`.
  Problem:  The test creates false confidence while testing zero authentication behavior.
  Fix:      Assert session token generation, cookie headers, and database session record.
```

---

## Exit Gate

- **Fail:** If any Critical or High findings remain unresolved.
- **Review:** When only Medium/Polish findings remain; resolve where feasible without overriding user taste.
- **Pass:** When all applicable checks have verifiable evidence and no blocking defects remain.
