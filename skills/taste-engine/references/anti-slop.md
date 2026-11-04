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
- **No dark/light theme collision slop & pitch-black canvas:** when a user requests dark mode or light mode, background and foreground colors must flip in coordinated pairs. Toggling background color while leaving text or borders in the opposing polarity (creating black text on black background, white text on white background, unreadable placeholders, or illegible status badges) is a direct integrity failure. Every theme adaptation must guarantee WCAG AA 4.5:1 text contrast across all states. In dark mode, avoid harsh pitch-black (`#000000` or raw `#0d0f14`) canvas unless specifically requested; prefer warm neutral dark slate-grey (Codex palette: canvas `#212328`, surfaces `#2b2e36`, elevated `#343842`, recessed wells `#1a1c21`, subtle outlines `rgba(255, 255, 255, 0.12)`) to avoid excessive eye strain, glare, and visual emptiness.
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
| Breaking inline command pills into vertical columns | Stacking `$`, code snippet, and copy button into 3 rows wastes space and looks broken | Keep single-line inline horizontal row (`flex-direction: row; align-items: center; justify-content: center;`) with `line-height: 1; flex-shrink: 0;` and fluid font size | Terminal is a multi-line script editor with deliberate multi-step script blocks |
| Giant oversized mobile headings and inflated components ("UI bengkak") | Desktop font sizes and huge paddings cause mobile UI to feel bloated, crowded, and unreadable | Fluid responsive typography (`clamp()`), scaling headings down proportionally (hero ~1.4rem, sections ~1.25rem, code ~0.75rem) | Deliberate poster typography in Swiss/Brutalism styles when explicitly tested for zero overflow |
| Endless 1-column mobile footer link dump | Stacking 15-20 links vertically in 1 column wastes 1000px+ vertical scroll on mobile | Balanced 2-column link grid (`repeat(2, 1fr)`) with full-width brand header and tactile tap targets | Footer has only 1-3 total links |
| Rainbow text gradients on headings (`background-clip: text`) | Typical AI-slop cliché that hurts legibility and contrast across themes | Solid contrast-compliant headings (`--shell-text`), subtle monochrome/duotone accents | Authentic retro, synthwave, or cyberpunk theme where neon multicolor text is an intentional style trait |
| Cartoon emojis as interface icons | Inconsistent visual weight, platform-dependent rendering, and amateur appearance | Crisp, clean, uniform inline SVGs (Lucide, Feather, Heroicons) with semantic sizing and stroke | Explicit conversational chat UI where user inputs emojis |
| Fabricated dashboard widgets (weather, audio spectrum, fake telemetry) | Misrepresents functionality and fills space with useless decorative clutter | Authentic product cards, real metrics, or purposeful content relevant to the actual task | Real connected audio app or weather service |
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
- Scale typography down proportionally on mobile viewports (< 768px, < 480px) to prevent bloated UI ("UI bengkak"): hero titles clamp to 1.4rem–1.65rem, section titles to 1.25rem–1.5rem, and terminal monospace code to 0.725rem–0.785rem with `word-break: break-all` / `overflow-x: auto` to prevent horizontal layout blowout.
- Keep quick install pills, command snippets, and copy bars strictly inline in a single horizontal row (`display: inline-flex; flex-direction: row; align-items: center; justify-content: center;`) with `line-height: 1; flex-shrink: 0;`. Never break prompt `$`, code, and copy button into vertical stacked rows.
- Organize mobile footer navigation links into a balanced 2-column grid (`repeat(2, 1fr)`) with full-width brand header and tactile thumb-friendly tap targets (pill buttons like 'Back to top').
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
