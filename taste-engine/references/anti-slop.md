# Anti-Slop Constitution — universal design integrity

**Applies to every Taste Engine style, custom style, blend, router run, and standalone pack.** Load this document for visual generation, redesign, and UI audit after the style has been resolved. These are quality rules, **not a secret aesthetic**. No style is privileged.

## Source and principle

The foundation was generalized from the user's Human Clay UI v1.1 anti-AI-slop discipline: every element must earn its place; do not decorate uncertainty; content before decoration; responsive is redesign rather than shrink; useful density; honest data; coherent systems; restrained, meaningful motion. This version extends that discipline across aesthetics and adds explicit writing, evidence, exceptions, and verification.

**Ask of every visible element:** What information, affordance, brand character, or spatial structure would be lost if this element were removed? If the answer is none, simplify. A recognizably styled UI is welcome; arbitrary fashion without a reason is not.

## Rule precedence

1. Functional correctness, accessibility, safety, truthful representations.
2. Explicit user instruction and confirmed project requirements (within those constraints).
3. Approved brand system and selected style pack.
4. These anti-slop heuristics and the existing codebase conventions.

A heuristic must **never** erase a defining feature of the chosen style:
- **Glassmorphism:** Purposeful radial/mesh gradients and ambient color fields are explicitly exempt from generic anti-gradient reflexes when legible and restrained, as they reveal frosted translucency.
- **Claymorphism:** Authentic dual inner shadows (highlight + form shadow), soft directional outer drop shadows, tactile compression on press, and recessed inset wells with white relief rims are explicitly exempt from generic anti-shadow reflexes.
- **Neo-brutalism:** Hard 0-blur offset shadows (`4px 4px 0 #121212`), solid 2px–3px black borders, and mechanical press displacement are explicitly exempt from generic shadow cautions.
- **Skeuomorphism:** Multi-stop metallic reflection gradients, 1px specular bevel highlights, recessed display wells, and physical travel are explicitly exempt from anti-gradient/texture cautions when tied to real controls.
- **Retro-Terminal:** Subtle raster scanlines, phosphor glow (`0 0 6px`), bracketed ASCII frames, and active command prompt lines are explicitly exempt from texture cautions.
- **Bento Grid:** Asymmetric multi-span tiles (`span 2`) and diverse internal tile compositions are explicitly encouraged over repetitive card templates.
- **Swiss / Editorial:** Dramatic display scale contrast (48px–72px headlines), numbered section markers (`01`), structural hairline rules, and active negative space are explicitly permitted.
- **Brutalism:** Exposed 2px–3px structural scaffolding borders, raw monochrome contrast, and immediate state flips are celebrated as honest architecture.
- **Minimalism:** Active intentional negative space, mathematical type calibration, and hairline dividers are prioritized over decorative fillers.
- **Enterprise:** High-density data tables, tabular figures (`tabular-nums`), filter toolbars, keyboard shortcuts, and semantic status pills are essential operational tools.

Audit whether each style expression is *intentional, truthful, and usable*, not whether it matches a generic minimal UI.

See [quality-tiers.md](quality-tiers.md) for what actually blocks a release versus what merely suggests a redesign. Use [decision-system.md](decision-system.md) to preserve user taste and separate material from page anatomy.

## A. Non-negotiable: truthful, usable, and implementable

- **No fabricated reality:** no invented metrics, transactions, users, totals, testimonials, customer logos, audit events, approvals, ratings, waitlists, social proof, or fake live/online/verified status. When real data is absent, use truthful empty/loading/error states or explicit, clearly labeled fixture/demo data only when authorized.
- **No false affordances:** no dead primary buttons, fake search, ornamental filters, nonfunctional dropdowns, or a success notification before the corresponding operation truly succeeds. Distinguish prototype-only elements clearly if a working implementation is out of scope.
- **No inaccessible style theater:** visible focus, text contrast, semantic controls, readable content, error recovery, responsive resizing, and reduced-motion handling are required. Never shrink fonts to hide overflow.
- **No invented product claims or irrelevant decoration:** content must reflect the product, audience, tasks, and data actually known. Do not fill screens with fabricated details to look finished.
- **No unrequested architecture churn:** inspect the existing stack, design tokens and components before adding libraries, fonts, animation dependencies or another styling system.

## B. Layout and composition: common slop and better alternatives

| Signal to investigate | Why it fails | Prefer | Allowed when |
|---|---|---|---|
| Card inside card inside card | Duplicated grouping and border noise | One owning surface; internal spacing, headings, dividers, rows | Nested layer models a distinct interaction, scope, hierarchy, or elevation state |
| Every metric has its own card | Creates fake dashboard density | Unified metric group, table, compact row, or genuine summary | Each metric is independently actionable or deserves separate emphasis |
| Repeated 3-feature cards / 4-stat header / hero-CTA template | Layout chosen before content | Compose around actual user tasks and information | Real content and audience benefit from that pattern |
| One small control floating in giant empty canvas | Viewport not intentionally composed | Rebalance width, groups, priority, density | Calm negative space is an intentional expressive choice |
| Unequal peer card heights / inconsistent controls | Implies hierarchy accidentally | Equal relationship = equal visual weight and aligned structure | Deliberate hierarchy justifies asymmetry |
| Pills, badges and chips everywhere | Noise and false importance | Plain labels, sections, simple metadata | Status/category/filter has real data and useful interaction |
| Icons for each heading or action | Visual repetition and ambiguous meaning | Semantic icons only where recognition improves | Brand-specific iconography has clear purpose |
| Decorative charts, mini-sparklines, timelines | Makes meaningless data look authoritative | Real charts only, or explanatory text/empty state | Data exists and visual encoding aids a decision |
| Glossy effects, blobs, gradients, glow by default | Covers weak hierarchy with trend styling | Design purposeful material, spacing and type first | **Glassmorphism explicitly permits ambient/mesh/radial gradients to reveal frosted material; Claymorphism explicitly permits dual inner-shadow volumetric depth and recessed wells; other styles may use them when integral and readable (Neo-brutalism hard offset shadows, Skeuomorphism metallic reflections/bevels, Retro-Terminal scanlines/glow, Bento asymmetric tiles, Swiss scale contrast, Brutalism scaffolding, Enterprise tabular density)** |
| Fake terminals, fake code, status LEDs | Implies features/state that do not exist | Genuine console behavior or honest static illustration | Clearly labeled decorative art that cannot be mistaken for live UI |
| Sticky UI chrome, modal/drawer abuse, tab spam | More navigation than task | Minimal interaction model for the task | Complexity genuinely warrants distinct view or overlay |

**No blanket ban on cards or decorative expression.** A Bento design can rightly use many tiles; a Skeuomorphic design can use layered surfaces. Count *semantic ownership* and interaction boundaries, not raw component tags.

### Hero-height anti-slop

For new portfolio/marketing pages *with* an opening hero, build one intentional viewport-height first-screen composition (navigation included) using [hero-layout.md](hero-layout.md). Never make the hero shallow by accident, but do **not** manufacture oversized empty gaps, fake trust badges, nested cards, decorative UI or animations to force a 100svh canvas to look busy. No forced hero on internal workflows. Content must be allowed to exceed the viewport when needed for accessibility.

## C. Typography and visual rhythm

- Define purpose-driven font roles, sizes, weight, line height, wrapping, tracking, and hierarchy from the selected pack. Do not mix unrelated typefaces to achieve accidental novelty.
- Headings should explain the section or express a real brand message, not just be huge for impact. Body and control text must survive narrow screens, zoom, localization, and long labels.
- Keep consistent spacing, baseline, paddings, button height, input states, border logic, and icon alignment; do not mix visual systems in the same screen without reason.
- For styles that embrace deliberate irregularity, preserve *repeatable rules* for asymmetry or varied sizing. Accidental inconsistency is not a style.

## D. Motion and effects

- Static by default; use motion to signal a state transition, continuity, reveal, or affordance.
- No idle bouncing/floating/pulsing hero decoration or perpetual animation merely for attention. Avoid giant hover scaling and scroll hijacking.
- A chosen style may define its own transition speed/easing; still support reduced motion. Motion should never delay the core action.

## E. Content and language

- Run [anti-slop-copywriting.md](anti-slop-copywriting.md) on headings, descriptions, buttons, onboarding, empty/error/success states, toasts, navigation, and marketing copy.
- Do not create attractive-but-empty claims, vague headings, formulaic hype, repetitive exclamation points, irrelevant emojis, or fake urgency.
- Choose vocabulary suited to the user's language, brand voice, domain, and selected style. A playful style permits playful *specific* copy; a brutalist style permits blunt, useful copy.

## F. Responsive and real-world checks

- Recompose mobile rather than shrinking desktop. Check 320–430 px narrow mobile, intermediate widths, and actual desktop viewport when those are relevant. Also check long translated text and browser zoom.
- Test form labels, button wrapping, headers, navigation, table overflow, keyboard focus, empty/loading/error states, and touch use. On native apps, account for safe areas and system text scaling.
- Do not add a mobile bottom nav automatically to every project; choose navigation based on information architecture and user workflows.

## Decision test for suspicious patterns

1. **Purpose:** Can we articulate why it exists? If not, remove.
2. **Evidence:** Is content/data/state authentic? If not, replace with an honest state.
3. **Style:** Is it intentionally part of the selected design language, or a generic trend? Preserve legitimate style expression.
4. **Cost:** Does it harm comprehension, performance, accessibility, or responsiveness? Refine or remove.
5. **Simpler path:** Can alignment, type, or spacing do the job without another element?
6. **User intent:** Does this express the user's stated taste and project context rather than an agent's preference?

A single exception must explain *what it serves*, not just claim that the result is "modern" or "premium".

## Required audit

Before presenting completed UI, apply [anti-slop-audit.md](anti-slop-audit.md), the selected style's **Anti-slop: style-specific** section, and [universal quality gates](quality-gates.md). Fix Critical/High issues before treating the deliverable as complete. Note unverified claims or tests accurately. For pure backend tasks, do not force a visual audit.
