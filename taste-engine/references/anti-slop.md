# Anti-Slop Constitution — universal design and engineering integrity

**Applies to every Taste Engine style, custom style, blend, router run, and standalone pack.** Load this document for visual generation, copywriting, code generation, redesign, and audits after the style has been resolved. These are quality rules, **not a secret aesthetic**. No style is privileged.

## Core Philosophy: Filter, Not a Style Guide

Anti-slop is an **integrity filter, not a style guide**. It eliminates generic AI defaults—vacuous claims, purple gradient soup, decorative card spam, ghost abstractions, dead controls, and robotic sentence formulas—without prescribing or flattening aesthetics.

Three non-negotiable axioms govern this system:

1. **Reports defects, never reports authorship:** The objective is to identify and repair verifiable defects in substance, usability, code integrity, accessibility, and truthfulness. We never guess or litigate whether an AI or human wrote something.
2. **A marker is never itself a finding:** A heuristic signal (an em-dash, a triad, a keyword, a wrapper function) is merely a trigger to run a mechanical structural test. If the structural test reveals genuine substance or load-bearing utility, the marker hit is immediately dropped.
3. **Every element and line of code must earn its place:** Do not decorate uncertainty. Content before decoration. Responsive is redesign rather than shrink. Real data before visual density. Restrained, meaningful motion.

**Ask of every visible element, sentence, and code abstraction:** What information, affordance, invariant, or spatial structure would be lost if this were removed? If the answer is none, simplify. A recognizably styled UI is welcome; arbitrary fashion and code bloat without a reason are not.

## Rule Precedence

1. Functional correctness, accessibility, safety, truthful representations.
2. Explicit user instruction and confirmed project requirements (within those constraints).
3. Approved brand system and selected style pack.
4. These anti-slop heuristics and the existing codebase conventions.

A heuristic must **never** erase a defining feature of the chosen style:
- **Frutiger Aero:** Glossy horizon sheens, aqua/sky/leaf atmospheric light fields, translucent acrylic docks, and tactile convex button pills are explicitly exempt from generic anti-gradient or anti-gloss reflexes, as they define authentic mid-2000s technological optimism.
- **Glassmorphism:** Purposeful radial/mesh gradients and ambient color fields are explicitly exempt from generic anti-gradient reflexes when legible and restrained, as they reveal frosted translucency.
- **Claymorphism:** Authentic dual inner shadows (highlight + form shadow), soft directional outer drop shadows, tactile compression on press, and recessed inset wells with white relief rims are explicitly exempt from generic anti-shadow reflexes.
- **Neo-brutalism:** Hard 0-blur offset shadows (`4px 4px 0 #121212`), solid 2px–3px black borders, and mechanical press displacement are explicitly exempt from generic shadow cautions.
- **Skeuomorphism:** Multi-stop metallic reflection gradients, 1px specular bevel highlights, recessed display wells, and physical travel are explicitly exempt from anti-gradient/texture cautions when tied to real controls.
- **Retro-Terminal:** Subtle raster scanlines, phosphor glow (`0 0 6px`), bracketed ASCII frames, and active command prompt lines are explicitly exempt from texture cautions.
- **Retro-Pixel:** Authentic pixel illustrations, stepped pixel borders, hard-edged 0-blur drop shadows, subtle background grid patterns, classic desktop title bars, window controls, and integer-scaled pixel art are explicitly exempt from texture and ornament cautions when purposeful and usable.
- **Bento Grid:** Asymmetric multi-span tiles (`span 2`) and diverse internal tile compositions are explicitly encouraged over repetitive card templates.
- **Swiss / Editorial:** Dramatic display scale contrast (48px–72px headlines), numbered section markers (`01`), structural hairline rules, and active negative space are explicitly permitted.
- **Brutalism:** Exposed 2px–3px structural scaffolding borders, raw monochrome contrast, and immediate state flips are celebrated as honest architecture.
- **Minimalism:** Active intentional negative space, mathematical type calibration, and hairline dividers are prioritized over decorative fillers.
- **Enterprise:** High-density data tables, tabular figures (`tabular-nums`), filter toolbars, keyboard shortcuts, and semantic status pills are essential operational tools.
- **Art Deco:** Geometric ornamental borders, stepped corner brackets, architectural hairline rules, fan/sunburst chevron accents, and flat/layered metallic finishes (antique gold `#B89B5E`, muted brass `#B69A68`, bronze `#A98462`) are explicitly exempt from generic anti-ornament reflexes when purposeful, symmetrical, and structurally aligned.

Audit whether each style expression is *intentional, truthful, and usable*, not whether it matches a generic minimal UI.

---

## Vibecoded Red Flags — immediate fast scanner

Before running structural tests, scan for these AI-default visual and copy patterns. A flag is a **trigger**, not a verdict — each proceeds to the Three-Layer Verification below.

| # | Signal | Action |
|---|--------|--------|
| 1 | Purple/blue mesh gradient as background default | Flag unless glassmorphism or confirmed cyberpunk/retro style |
| 2 | Neon `box-shadow` blur > 20px on non-terminal elements | Flag for Deletion Test |
| 3 | Emoji as functional icon, bullet, status indicator, or decorative sticker | Replace with Lucide/Radix SVG — no structural test needed, direct fix |
| 4 | Every card identical in size, structure, and visual weight (uniform card spam) | Flag for Deletion Test |
| 5 | Spacing units inconsistent (mixed `px`, `rem`, arbitrary Tailwind values) | Flag; check for declared token system |
| 6 | Copy contains ≥ 3 exclamation marks, ≥ 2 em-dashes, or any "In today's fast-paced world" variant | Direct fix — no structural test needed |
| 7 | Hero section > 100vh without documented product justification | Flag for Deletion Test |
| 8 | Font stack not loaded; fallback renders visibly as system serif/sans | Direct fix |
| 9 | Rainbow text gradient (`-webkit-background-clip: text`) outside retro/cyberpunk themes | Flag for style-authentic check |
| 10 | Fake widgets (fabricated weather, audio spectrum, simulated telemetry, animated fake counters) | Direct removal — FLOOR violation |
| 11 | Unbalanced multi-column card stacks (dead empty space below shorter column) or 3+1 orphan wrapped cards/controls | Direct layout fix — enforce `align-items: stretch`, `flex: 1` on stacked cards, and matched `2×2` / `3×2` grid multiples |

---

## The Three-Layer Verification Architecture

```
Layer 0: Decidable Scanners   → Package hallucination, API mismatch, WCAG AA contrast math, syntax
Layer 1: Structural Tests     → Deletion, Inversion, Stranger, Attribution, Load-Bearing (Must emit artifacts)
Layer 2: Heuristic Markers    → Banned vocab, em-dashes, tricolons, card nesting (Never convicts alone)
```

1. **Layer 0 (Decidable):** Can fail a build directly. Claims here are binary facts: does the npm/PyPI package exist in the registry? Does the called method exist in the pinned library version? Does the text meet WCAG AA 4.5:1 contrast? Does the test suite compile and pass?
2. **Layer 1 (Structural Procedures):** Can convict and fail a build when an artifact proves a defect. The 5 mechanical procedures below produce tangible evidence.
3. **Layer 2 (Heuristic Markers):** Corpus-validated signals of AI repetition. **They never convict alone.** They route directly to Layer 1 procedures.

---

## The Five Structural Tests (Universal Procedures)

Every structural check is mechanical and produces a named artifact you can inspect.

### 1. The Deletion Test (Prose & UI)
- **Procedure:** Cut the span, element, or visual wrapper. Read/view what remains. Name what was lost.
- **Artifact:** The cut span + the named loss. If the loss is "nothing", the element/span was padding/slop.
- **Finding:** MEDIUM (Padding). If what was lost is an essential context, invariant, or affordance, drop the finding.

### 2. The Inversion Test (Claims & Marketing)
- **Procedure:** Negate the claim. Write the negation out in full as a sentence someone might publish. Ask whether anyone would assert it.
- **Artifact:** The negation, written out.
- **Finding:** If nobody would ever assert the negation (e.g., *"We build unreliable software"* or *"The feature plays no role"*), the original states nothing, excludes no state of the world, and is a vacuous claim / empty puffery (MEDIUM).

### 3. The Stranger Test (Context & Grounding)
- **Procedure:** Ask whether someone who never saw the product, codebase, or data could have written this exact UI/text given only a generic prompt.
- **Artifact:** The specific fact, metric, architecture detail, or user task that only an authentic insider knows.
- **Finding:** If the copy/UI lacks any grounded fact and consists solely of generic platitudes (*"Unlock your productivity with our seamless platform"*), rewrite with actual product operations or remove.

### 4. The Attribution Test (Evidence & Sources)
- **Procedure:** Resolve the citation, metric, or endorsement to its concrete source.
- **Artifact:** The resolved reference, or the explicit finding that the claim does not resolve.
- **Finding:** HIGH if a fabricated source/metric/user count is presented as real; MEDIUM if decorative. Fabricated reality is a direct integrity breach.

### 5. The Load-Bearing Test (Code & Architecture)
- **Procedure:** Delete the comment, passthrough wrapper, handler, abstraction, or assertion-free test. Run the test suite / build.
- **Artifact:** What broke, named specifically (with compiler errors or test failure logs), or the evidence that *nothing broke*.
- **Finding:** HIGH for assertion-free tests (false claims of test coverage); MEDIUM for ghost abstractions, passthrough wrappers, and error-swallowing handlers; LOW for redundant comments.

---

## A. Non-negotiable: Truthful, Usable, and Implementable

- **No fabricated reality:** no invented metrics, transactions, users, totals, testimonials, customer logos, audit events, approvals, ratings, waitlists, social proof, or fake live/online/verified status. When real data is absent, use truthful empty/loading/error states or explicit, clearly labeled fixture/demo data only when authorized.
- **No false affordances:** no dead primary buttons, fake search, ornamental filters, nonfunctional dropdowns, or a success notification before the corresponding operation truly succeeds. Distinguish prototype-only elements clearly if a working implementation is out of scope.
- **No inaccessible style theater:** visible focus, text contrast, semantic controls, readable content, error recovery, responsive resizing, and reduced-motion handling are required. Never shrink fonts to hide overflow.
- **No dark/light theme collision slop & pitch-black canvas:** when a user requests dark mode or light mode, background and foreground colors must flip in coordinated pairs. Toggling background color while leaving text or borders in the opposing polarity (creating black text on black background, white text on white background, unreadable placeholders, or illegible status badges) is a direct integrity failure. Every theme adaptation must guarantee WCAG AA 4.5:1 text contrast across all states. In dark mode, avoid harsh pitch-black (`#000000` or raw `#0d0f14`) canvas unless specifically requested; prefer warm neutral dark slate-grey (Codex palette: canvas `#212328`, surfaces `#2b2e36`, elevated `#343842`, recessed wells `#1a1c21`, subtle outlines `rgba(255, 255, 255, 0.12)`) to avoid excessive eye strain, glare, and visual emptiness.
- **No invented product claims or irrelevant decoration:** content must reflect the product, audience, tasks, and data actually known. Do not fill screens with fabricated details to look finished.
- **No unrequested architecture churn:** inspect the existing stack, design tokens and components before adding libraries, fonts, animation dependencies or another styling system.

---

## B. Layout and Composition: Common Slop and Better Alternatives

| Signal to investigate | Why it fails | Prefer | Allowed when |
|---|---|---|---|
| Card inside card inside card | Duplicated grouping and border noise | One owning surface; internal spacing, headings, dividers, rows | Nested layer models a distinct interaction, scope, hierarchy, or elevation state |
| Every metric has its own card | Creates fake dashboard density | Unified metric group, table, compact row, or genuine summary | Each metric is independently actionable or deserves separate emphasis |
| Repeated 3-feature cards / 4-stat header / hero-CTA template | Layout chosen before content | Compose around actual user tasks and information | Real content and audience benefit from that pattern |
| One small control floating in giant empty canvas | Viewport not intentionally composed | Rebalance width, groups, priority, density | Calm negative space is an intentional expressive choice |
| Unequal peer card heights / unbalanced split-column stacks / inconsistent controls | Leaves dead vertical holes under shorter side stacks, misaligns card footers, or wraps 4 controls into 3+1 orphans | Enforce `align-items: stretch` on grids, `height: 100%; display: flex; flex-direction: column; justify-content: space-between;` on peer cards, `flex: 1 1 0%` on cards inside vertical side stacks, uniform button heights per cluster, and `2×2` or `3×2` grid multiples | Deliberate editorial asymmetry that does not leave unintentional dead holes inside a bounded container |
| Pills, badges and chips everywhere | Noise and false importance | Plain labels, sections, simple metadata | Status/category/filter has real data and useful interaction |
| Icons for each heading or action | Visual repetition and ambiguous meaning | Semantic icons only where recognition improves | Brand-specific iconography has clear purpose |
| Decorative charts, mini-sparklines, timelines | Makes meaningless data look authoritative | Real charts only, or explanatory text/empty state | Data exists and visual encoding aids a decision |
| Glossy effects, blobs, gradients, glow by default | Covers weak hierarchy with trend styling | Design purposeful material, spacing and type first | **Frutiger Aero explicitly permits glossy horizon sheens, aqua/sky/leaf atmospheric light fields, and tactile convex pills; Glassmorphism explicitly permits ambient/mesh/radial gradients to reveal frosted material; Y2K Futurism explicitly permits multi-stop chrome gradients, liquid silver finishes, iridescent spectral borders, and chamfered framing; Claymorphism explicitly permits dual inner-shadow volumetric depth and recessed wells; other styles may use them when integral and readable (Neo-brutalism hard offset shadows, Retro-Terminal scanlines/glow, Retro-Pixel stepped borders/pixel art/grid, Bento asymmetric tiles, Swiss scale contrast, Brutalism scaffolding, Enterprise tabular density, Art Deco stepped geometry and antique gold)** |
| Fake terminals, fake code, status LEDs | Implies features/state that do not exist | Genuine console behavior or honest static illustration | Clearly labeled decorative art that cannot be mistaken for live UI |
| Breaking inline command pills into vertical columns | Stacking `$`, code snippet, and copy button into 3 rows wastes space and looks broken | Keep single-line inline horizontal row (`flex-direction: row; align-items: center; justify-content: center;`) with `line-height: 1; flex-shrink: 0;` and fluid font size | Terminal is a multi-line script editor with deliberate multi-step script blocks |
| Giant oversized mobile headings and inflated components ("UI bengkak") | Desktop font sizes and huge paddings cause mobile UI to feel bloated, crowded, and unreadable down to 320px | Fluid responsive typography (`clamp()`) scaling headings down proportionally (hero ~1.35rem, sections ~1.2rem, code ~0.725rem) | Deliberate poster typography in Swiss/Brutalism styles when explicitly tested for zero overflow |
| Crowding horizontal navigation links on narrow mobile headers | Text wrapping, clipped links, layout blowout, and broken header tap targets | Collapse navigation links behind an accessible Hamburger Menu on mobile (< 768px) with a dedicated slide-out drawer or modal dropdown | Desktop viewports (>= 768px) where links fit with ample whitespace |
| Circular elements squished into ovals/ellipses under mobile compression | Missing `aspect-ratio: 1 / 1;` and missing `flex-shrink: 0;` cause avatars, status dots, icon badges, and round buttons to distort into ovals when flex containers shrink | Enforce `aspect-ratio: 1 / 1; flex-shrink: 0;` on all circular (`border-radius: 50%`) and 1:1 elements | Deliberate pill / stadium shapes (`border-radius: 9999px`) intended for text labels |
| Endless 1-column mobile footer link dump | Stacking 15-20 links vertically in 1 column wastes 1000px+ vertical scroll on mobile | Balanced 2-column link grid (`repeat(2, 1fr)`) with full-width brand header and tactile tap targets | Footer has only 1-3 total links |
| Rainbow text gradients on headings (`background-clip: text`) | Typical AI-slop cliché that hurts legibility and contrast across themes | Solid contrast-compliant headings (`--shell-text`), subtle monochrome/duotone accents | Authentic retro, synthwave, or cyberpunk theme where neon multicolor text is an intentional style trait |
| Emojis as interface icons, buttons, or badges | Platform-dependent rendering, inconsistent visual weight, amateur appearance, and hallmark AI-slop | Zero emojis in UI: exclusively use crisp vector SVGs from Lucide, Radix, Feather, or Heroicons with currentColor | Explicit conversational chat content where a human user inputs emojis |
| Fabricated dashboard widgets (weather, audio spectrum, fake telemetry) | Misrepresents functionality and fills space with useless decorative clutter | Authentic product cards, real metrics, or purposeful content relevant to the actual task | Real connected audio app or weather service |
| Sticky UI chrome, modal/drawer abuse, tab spam | More navigation than task | Minimal interaction model for the task | Complexity genuinely warrants distinct view or overlay |

**No blanket ban on cards or decorative expression.** A Bento design can rightly use many tiles; a Skeuomorphic design can use layered surfaces. Count *semantic ownership* and interaction boundaries, not raw component tags.

### Hero-height Anti-Slop
For new portfolio/marketing pages *with* an opening hero, build one intentional viewport-height first-screen composition (navigation included) using [hero-layout.md](hero-layout.md). Never make the hero shallow by accident, but do **not** manufacture oversized empty gaps, fake trust badges, nested cards, decorative UI or animations to force a 100svh canvas to look busy. No forced hero on internal workflows. Content must be allowed to exceed the viewport when needed for accessibility.

---

## C. Code Surface Integrity: Anti-Slop Code Standards

AI agents frequently generate code bloat that looks productive but degrades maintainability. Apply the **Load-Bearing Test** to code.

### 1. Code Comment Hygiene
- **No decorative separators:** Remove ASCII banners (`// ====================`, `/* ---- ROUTES ---- */`, `// -------- WORKFLOW --------`). A single clean empty line or clear function name is superior.
- **No restating the obvious (echo comments):** Delete comments that merely translate the line of code into English:
  ```python
  # BAD:
  # Increment the counter
  counter += 1

  # GOOD (preserves the non-obvious invariant or WHY):
  # API returns 200 with an empty body when rate-limited; check JSON explicitly.
  if resp.status_code == 200 and resp.json():
  ```
- **No step-narration comments:** Delete `// Step 1: Initialize variables`, `// Step 2: Make request`, `// Step 3: Return result`. Write expressive, self-explanatory code structure instead.

### 2. Architecture & Abstraction Hygiene
- **No passthrough wrappers:** Do not create wrapper functions that take arguments and immediately pass them unchanged to another function without adding caching, transformation, validation, or policy.
- **No ghost over-abstractions:** Do not create abstract classes, interfaces, and factory providers for a service that has exactly one implementation and no planned second caller. Implement directly.
- **No defensive error-swallowing:** Never write bare exception handlers that conceal bugs:
  ```typescript
  // BAD:
  try {
    processPayment(order);
  } catch (e) {
    console.log(e); // swallows real error, order appears hung
  }

  // GOOD: Handle specific expected failures, or let unexpected errors propagate to boundary
  ```

### 3. Test Suite Integrity
- **No assertion-free tests (coverage padding):** Every test must verify an actual invariant. If replacing the function body with `return True` or `return object()` still passes the test suite, the test is vacuous slop.
- **Decidable Registry Scanners (Package & API Hallucination):**
  - Verify every imported library exists in the official registry (`npm`, `PyPI`).
  - Verify that methods and options called exist in the pinned library version. Do not invent options that "sound logical" for an API.

---

## D. Motion and Effects

- Static by default; use motion to signal a state transition, continuity, reveal, or affordance.
- No idle bouncing/floating/pulsing hero decoration or perpetual animation merely for attention. Avoid giant hover scaling and scroll hijacking.
- A chosen style may define its own transition speed/easing; still support reduced motion (`prefers-reduced-motion`). Motion should never delay the core action.

---

## E. Content and Language

- Run [anti-slop-copywriting.md](anti-slop-copywriting.md) on all interface copy, READMEs, documentation, and agent outputs.
- Enforce **parataxis elimination**, **rule-of-three break**, **sentence length rhythm (burstiness)**, and **punctuation discipline** (max 1 em-dash per 500 words, max 1 exclamation mark per 1,000 words).
- Eliminate corporate cheerleading, ungrounded metrics, and formulaic AI openers.

---

## F. Responsive and Real-World Baseline

- **Strict 320px responsive baseline:** Every interface must be tested and fully functional down to 320px minimum viewport width (narrow mobile screens like iPhone SE). Zero horizontal layout blowouts, zero clipped content, and zero inaccessible controls.
- **Strict 1:1 circle preservation (no squishing into ovals / 'tidak menjadi oval'):** Any circular or square UI element—including avatars, status indicator dots, icon containers, circular action buttons (`border-radius: 50%`), logo boxes, and notification badges—must enforce `aspect-ratio: 1 / 1;` (or equal explicit `width` and `height`) AND must include `flex-shrink: 0;` whenever placed inside flex containers or grid rows. Circular images and avatars must use `object-fit: cover;` to prevent aspect distortion. Under responsive compression down to 320px viewport, circular elements must NEVER deform into ellipses or ovals.
- **Fluid proportional font scaling (anti-bloat):** Scale typography down proportionally on small viewports (< 768px, < 480px) so the UI stays compact, balanced, and never feels bloated or oversized ("UI bengkak"). Hero titles clamp to `1.35rem`–`1.65rem`, section titles to `1.2rem`–`1.45rem`, body text to `0.85rem`–`0.95rem`, and code snippets to `0.725rem`–`0.785rem` with `word-break: break-all` / `overflow-x: auto`.
- **Header mobile navigation — use a hamburger menu:** In top navigation headers, never crowd or force horizontal link rows onto narrow screens. On viewports where navigation links cannot breathe comfortably (< 768px), collapse navigation links behind an accessible **Hamburger Menu** (using a Lucide `Menu` SVG icon) that opens a mobile sheet or dropdown drawer with comfortable 44px+ touch tap targets.
- **Single-line inline command pills ("sejajarin"):** Keep quick install pills, command snippets, and copy bars strictly inline in a single horizontal row (`display: inline-flex; flex-direction: row; align-items: center; justify-content: center;`) with `line-height: 1; flex-shrink: 0;`. Never break prompt `$`, code, and copy button into vertical stacked rows.
- **Balanced 2-column mobile footer:** Organize mobile footer navigation links into a balanced 2-column grid (`repeat(2, 1fr)`) with full-width brand header and tactile thumb-friendly tap targets (pill buttons like 'Back to top').
- Test form labels, button wrapping, headers, navigation, table overflow, keyboard focus, empty/loading/error states, and touch use. On native apps, account for safe areas and system text scaling.

---

## Decision Test for Suspicious Patterns

1. **Purpose:** Can we articulate why it exists? If not, remove.
2. **Evidence:** Is content/data/state authentic? If not, replace with an honest state.
3. **Style:** Is it intentionally part of the selected design language, or a generic trend? Preserve legitimate style expression.
4. **Cost:** Does it harm comprehension, performance, accessibility, or responsiveness? Refine or remove.
5. **Simpler path:** Can alignment, type, or spacing do the job without another element?
6. **User intent:** Does this express the user's stated taste and project context rather than an agent's preference?

A single exception must explain *what it serves*, not just claim that the result is "modern" or "premium".

---

## Required Audit

Before presenting completed UI or code, apply [anti-slop-audit.md](anti-slop-audit.md), the selected style's **Anti-slop: style-specific** section, and [universal quality gates](quality-gates.md). Fix Critical/High issues before treating the deliverable as complete. Note unverified claims or tests accurately. For pure backend tasks, do not force a visual audit.
