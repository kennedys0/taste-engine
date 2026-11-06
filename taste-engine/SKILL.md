---
name: taste-engine
description: Automatically routes visual UI work to a user-chosen aesthetic and applies SEO readiness to public-facing websites. Use whenever a user asks to build, create, design, or redesign a website, portfolio, landing page, dashboard, web app, mobile app, UI/UX screen, frontend, or component, or add/refine micro-interactions or full-screen hero sections (including Indonesian prompts such as "build a portfolio website"). Before writing UI code, ask ONE style question and stop if no visual style or approved project design system is specified. If the prompt already names an aesthetic such as claymorphism, frutiger-aero, brutalism, neo-brutalism, minimalism, bento, retro-pixel, art-deco, y2k-futurism, or editorial, load its bundled style pack immediately and proceed WITHOUT asking again. Preserve established styles for minor fixes; for SEO-only tasks, load the SEO module without a visual style question; skip unrelated non-visual work.
license: MIT
metadata:
  version: "0.12.0"
---

# Taste Engine — style router

**One universal process, many independent tastes — with anti-slop, conditional public SEO and optional style-aligned motion.** Taste Engine controls **when to ask, which selected style pack to load, and how to enforce it**. The engine itself has no house aesthetic. Style packs in `styles/*.md` contain the actual design instructions.

## Material fidelity (selected styles) — screenshot-level contract

Selected visual aesthetics must be **recognizable from the rendered interface**, not just stated in headings or CSS variable names. When `frutiger-aero` is selected, load `styles/frutiger-aero.md` and apply its mandatory **Frutiger Aero material fidelity gate**: authentic glossy acrylic specular sheens, aqua/ocean/leaf nature-tech balance, tactile controls, and accessible fallback. A flat navy hero plus a blue CTA is not Frutiger Aero. Use `tests/frutiger-aero-visual.md` for acceptance checks and `examples/frutiger-aero/glossy-surfaces.css` as a starting recipe. When `y2k-futurism` is selected, load `styles/y2k-futurism.md` and apply its mandatory **Y2K Futurism material fidelity gate**: polished chrome finishes, liquid silver surfaces, iridescent spectral highlights, and chamfered geometric framing. Use `tests/y2k-futurism-visual.md` and `examples/y2k-futurism/metallic-surfaces.css`. Do not apply these style-specific checks to other styles; every aesthetic retains its own requirements.

## Frutiger Aero and Y2K Futurism material exceptions — gloss, nature gradients, and metallic chrome are allowed

When Frutiger Aero is selected, **purposeful CSS gradient backdrops, atmospheric nature-tech light fields, and acrylic specular horizon sheens are explicitly permitted** because they define optimistic mid-2000s technological aesthetics. When Y2K Futurism is selected, **multi-stop metallic chrome gradients, liquid silver finishes, and iridescent spectral borders are explicitly permitted** because they define millennium speculative cyber-optimism. Do not remove these to satisfy general anti-slop gradient warnings. Read the style packs and validate that the first viewport visibly reads as an authentic composition. These exemptions apply only to the selected material and never override usability, truthfulness, accessibility or user constraints.

## Automatic invocation: the zero-command contract

- This is a **task-triggered skill**, not a slash-command-only workflow. Installed agents that support autonomous Agent Skills should discover the metadata above on portfolio, website, app, dashboard, landing-page, and UI redesign requests—even when the user never says "taste-engine".

- Once invoked, apply [Automatic Invocation Contract](references/auto-invocation.md) before any UI code. The actual platform decides whether the skill is invoked; this file cannot create an OS-level hook or guarantee compliance on every host.

- **Implicit style selection:** "build me a portfolio website" → ask ONE concise style question, then end turn. Never ask the user about unrelated details in the same turn.

- **Explicit style selection:** "build a portfolio website in skeumorphsm style" → normalize the typo to `skeuomorphism` (resolving to canonical `frutiger-aero` with variant `tactile`), read `styles/frutiger-aero.md`, without asking, and build. Do not run the question menu.

- **Established project:** an approved project config or documented brand/style wins over generic defaults for incremental work; do not interrupt with a menu.

- **No frontend work:** API implementation, debugging business logic, database migration, infrastructure, writing-only tasks → do not launch style selector.

## Engineering companion — conditional and framework-aware

Once the visual style question is resolved (or skipped for existing systems/nonvisual work), apply [Engineering Router](references/engineering-router.md). **Every web UI** gets the universal [Web Interface Quality](references/web-interface-quality.md) gate; React/Next gains [React Performance](references/react-performance.md) and optionally [React Composition](references/react-composition.md) only when the stack and task justify them. React Native/Expo work gains [Native Mobile](references/native-mobile.md), not web SEO. Navigation motion may use [View Transitions](references/view-transitions.md) after compatibility checks, or optional Anime.js when truly useful. Documentation-writing tasks gain [Docs Writing](references/docs-writing.md) without a visual style selector.

These are **local original integrations**, not imported Vercel plugins. They summarize engineering practices learned from [upstream research](references/vercel-research.md). Never assume upstream skills installed, never require React, never deploy without explicit deployment intent, and do not let technical guidance overwrite the user's aesthetic. The core preflight, full-screen hero, SEO, anti-slop, and style-aware motion remain unchanged. See [engineering routing tests](tests/engineering-routing.md).

## Full-screen hero — mandatory when relevant

After style selection, for any **new public portfolio, landing page, or homepage with a hero**, load [Full-screen Hero Contract](references/hero-layout.md). Default to a **one-visible-screen header + hero composition**: use mobile-safe `min-height: 100svh` (with `100vh` fallback) and subtract the actual normal-flow header height, or use a full-height hero when the header overlays it. Do not apply `100vh` blindly: fixed heights can clip text and toolbar-changed mobile viewports. Keep content and CTA usable at narrow/short screens; allow natural growth and scrolling at zoom/large text. Follow the selected style's `## Hero composition (full first viewport)` guidance and the shared anti-slop checks. Do not invent imagery, badge, fake statistics or looped motion just to fill the screen.

This rule does **not** force a marketing hero into private dashboards, forms, app workspaces, or incremental edits that do not create/redesign the hero. An explicit user choice for a compact hero or no hero wins. **No extra style-selection question** is needed when style is already established.

## Anime.js v4 Motion Engine — optional and style-aware

For explicit UI micro-interaction requests, or when building a selected style that genuinely benefits from additional motion, load [Motion Engine Adapter](references/motion-engine.md) and the chosen style's `## Motion` guidance. Motion **never becomes a new aesthetic selector**, and **never requires** a second interview. A request like `Tambahkan micro-interaction di dashboard ini` preserves existing project style and works without a style question. If the project has no selected design language and the user is building new UI, the original one-question preflight remains mandatory.

**No automatic dependency installs.** Inspect the existing stack first. Prefer CSS/native browser capabilities for simple transitions; only consider Anime.js v4 when it meaningfully simplifies coordinated motion or was explicitly requested. For React/Next, use `createScope()` + lifecycle cleanup; for users preferring reduced motion, disable nonessential effects while keeping interactions functional. Do not force bounce, loops, or gratuitous stagger. Style mapping is in `styles/motion-profiles.json`; React recipe in `examples/react/anime-v4-press.jsx`. Non-web/native apps should use their platform motion APIs instead.

## Cross-style SEO: automatic and conditional

**SEO is not a style choice.** For a new or substantially redesigned **public website** (portfolio, landing page, blog, public business website, public docs or public product pages), load [SEO Integration](references/seo.md) and, when needed, [SEO implementation recipes](references/seo-implementation.md) **after visual style selection**. Apply technical SEO + anti-slop content to every chosen style, without asking "do you want SEO?" as a second question. SEO never changes the selected material aesthetic.

- **Explicit style:** `Build a Skeuomorphism portfolio` → read `styles/skeuomorphism.md` + `references/seo.md`, no style question, then implement.

- **Missing style:** `Build a portfolio website` → ask exactly one style question and stop. **After the answer**, load style + SEO and implement. Do not bypass the preflight merely to write metadata.

- **SEO-only:** `Audit SEO on my website` / `fix canonical URLs and the sitemap` → read SEO module immediately, **no visual style interview** and no unsolicited redesign.

- **Private/internal application:** preserve confidentiality and existing indexability; don't generate public sitemap or reveal private routes. Native mobile/backend-only tasks are out of ordinary web SEO scope.

- **Unknown domain:** do not fabricate live URLs, authorship, structured data, reviews or page content; safely implement semantics/title and report what remains pending.

SEO and style share **FLOOR / REFLEX / FINISH** gates; privacy, truthful content, accessibility and functional behavior outrank aesthetic and search preferences. See [SEO acceptance scenarios](tests/seo-routing.md). The optional standalone `taste-seo` skill is for SEO-only installations; **router users do not need to install it separately**.

## Proof-of-Work (PoW) showcase architecture — canonical preset contract

When building, generating, or modifying style showcase pages, Proof-of-Work demos, or interactive design studios (such as `docs/*.html`), load [PoW Showcase Structure](references/pow-showcase-structure.md) and reuse the canonical preset template in `presets/templates/pow-showcase.template.html`.

Every showcase must strictly preserve the **7 canonical sections**:
1. **Sticky Header:** uniform `36px` action button heights, theme toggle, and `< 768px` mobile hamburger drawer.
2. **Full-Screen Hero:** fluid typography `clamp()`, pill strip, and overflow-protected copy command box.
3. **Interactive Studio Cockpit:** responsive workspace with title bar, touch containment, and zero horizontal clipping.
4. **Component Anatomy & Quality Gates:** authentic specimen cards and explicit style-specific failure tests.
5. **Tabbed Terminal Installation:** 3-tab terminal (`Standalone`, `Full Engine`, `Presets`), window dots, dedicated top-right header copy button (zero overlapping text), and agent support matrix strip.
6. **Core Architectural Principles:** 3 key design pillars.
7. **Canonical 10-Style Footer:** responsive auto-fit grid linking all 10 canonical styles.

Arbitrary deviations—such as cramped 3-card installation layouts, copy buttons occluding text, mismatched header button heights, or stretched single-column footers—are strictly forbidden.

## Hard requirement: preflight before new visual implementation

For tasks that introduce or substantially redesign visual UI, **do not write UI code, generate interface mockups, or change design tokens until the visual direction is resolved**.

1. Examine the current user request, existing product brand/design system, and an explicitly approved project style configuration.

2. **If a style is already explicitly selected** (for example, “brutalist dashboard”), **do not ask again**. Confirm it in one short line if useful and load that style pack.

3. **If the existing project has a clearly established style and the user requests incremental changes**, preserve it; do not interrupt with a new choice. A redesign request can override the established style.

4. **Otherwise, ask exactly one concise style-selection question and stop.** Offer **6 contrasting choices** and “More styles / Custom / Send reference”. Do not silently select a style, begin coding while awaiting a reply, or ask a multi-question interview.

5. When the user answers, resolve style ID via the registry, read **only the selected pack(s)**, derive project-specific tokens/decisions, and then execute. A user-provided adjective or reference may require interpreting style characteristics instead of forcing a preset.

6. If a tool-runner cannot pause for user input, report the unresolved selection and do **not** fabricate consent. An explicit instruction to use an autonomous best-effort default may authorize a provisional style; mark it provisional and reversible.

### Mandatory first question (example in Indonesian)

> Before I start designing, which visual style would you like?

> 1. **Claymorphism** — lembut, tactile, kedalaman halus

> 2. **Glassmorphism** — transparan, berlapis, modern

> 3. **Brutalism** — tipografi tegas, grid mentah, kontras tinggi (tersedia varian: **Raw** & **Bento**)

> 4. **Neo-brutalism** — warna berani, border dan hard shadow

> 5. **Minimalism** — bersih, sederhana, fokus konten

> 6. **Swiss / Editorial** — grid presisi, tipografi dominan

> Atau ketik **lainnya**, **custom**, atau kirim referensi.

Adapt to the user's language. Keep it a **single question**; describe distinctions without declaring one “best”. For long menus, first present the six plus a way to see the remaining options. If the user wants examples, show options before selecting. If user requests an interactive selector and the agent supports it, present the same choices as UI controls.

## Available style packs

Read `styles/registry.json` when matching IDs, **aliases, common misspellings**, and descriptions. Normalize punctuation, hyphens, and casing; respect negated style mentions ("not glassmorphism") and context. Where available, `python3 scripts/style_probe.py --prompt "..."` can supply a deterministic style hint; semantic interpretation and project context still win. **Do not call a standalone style skill by name**: read the selected local `styles/<id>.md` file, which is part of this installed router. Built-in packs:

| ID | Direction | File to load once selected |
| --- | --- | --- |
| `claymorphism` | Sculpted tactile | [style pack](styles/claymorphism.md) |
| `frutiger-aero` | Optimistic mid-2000s gloss & nature-tech (Classic, Glass, Tactile) | [style pack](styles/frutiger-aero.md) |
| `brutalism` | Raw structural (Raw & Bento variants) | [style pack](styles/brutalism.md) |
| `neo-brutalism` | Playful bold | [style pack](styles/neo-brutalism.md) |
| `minimalism` | Restrained clarity & data cockpits | [style pack](styles/minimalism.md) |
| `swiss-editorial` | Typographic grid | [style pack](styles/swiss-editorial.md) |
| `retro-terminal` | Console aesthetic | [style pack](styles/retro-terminal.md) |
| `retro-pixel` | 8-bit/16-bit arcade desktop | [style pack](styles/retro-pixel.md) |
| `art-deco` | Architectural geometric elegance & luxury (Modern, Classic, Minimal) | [style pack](styles/art-deco.md) |
| `y2k-futurism` | Cyber-optimism, polished chrome & iridescent reflections (Chrome, Holographic, Retro Tech) | [style pack](styles/y2k-futurism.md) |

**Custom is first-class:** if the chosen aesthetic is not in the registry, gather a short reference or constraints, then create a provisional project-specific style definition using the same dimensions. Never mislabel the style as a pack not present. Do not require external internet access to choose.

## Router states

- **`needs-selection`**: New visual work; no chosen/confirmed direction. Ask a style question **and stop**.

- **`ready`**: Style or existing brand explicitly established; load relevant pack and implement.

- **`refine`**: Small change in existing UI; preserve style, modify only necessary tokens/components.

- **`custom`**: User chooses a blend, gives screenshots, or requests an unspecified style; map to the same design dimensions and confirm only consequential ambiguity.

- **`non-visual`**: Backend, tests, docs, bug fixes with no visual decision; skip design selection entirely.

Detailed routing, blends, and conflict rules: [style router](references/style-router.md). For autonomous discovery, style aliases, host limitations, and exact example transcripts, see [auto-invocation](references/auto-invocation.md).

## Applying the style after selection

1. **Extract requirements:** product, audience, device, framework, existing brand, explicit likes/dislikes, accessibility, performance.

   **Domain pre-flight (mandatory before resolving visual direction):** Before selecting or applying a style pack, state the product domain and primary audience in one sentence — e.g., *"A project management tool for indie developers"* or *"A personal finance tracker for non-technical users."* The design direction must follow from this domain statement, not from the agent's default palette. If domain and audience cannot be derived from context, include this in the style question — combine into one question, never a separate interview step.

2. **Load selected pack only** (plus shared references as needed). Do not blend random rules from unselected packs.

   - **Style ≠ anatomy:** derive product flow and page content from real user goals, while the selected pack determines visual material. Before coding, define a one-sentence, product-grounded visual thesis that names domain + audience + aesthetic intention. Follow [Decision System](references/decision-system.md).

3. **Build project Design DNA:** type families + fallback, type scale, font weights, writing tone, palette roles, density, spacing, radius, border, elevation, layout grid, component anatomy, states, navigation, motion and reduced-motion rules. See [translation](references/translation.md).

   - **Dark & light mode pair coupling:** when dark or light mode is requested, ensure paired design tokens for canvas, cards, text, borders, inputs, and semantic status pills flip in tandem so background and foreground colors never collide (zero black-on-black or white-on-white text). In dark mode, unless the chosen style pack specifically dictates otherwise (e.g., Brutalism's intentional `#000000` high-contrast canvas or Retro-Terminal's CRT phosphor dark), use the warm dark slate fallback defined in [Responsive Baseline](references/responsive-baseline.md).

   - **Responsive baseline & layout safety:** follow [Responsive Baseline](references/responsive-baseline.md) for universal 320px viewport safety, fluid mobile typography defaults, small-viewport navigation patterns, circular geometry (`aspect-ratio: 1 / 1; flex-shrink: 0;`), inline command pills, and balanced mobile footers. Style packs may override typography and layout scales to honor their signature aesthetics.

4. **Resolve precedence:** technical/safety/accessibility constraints → explicit current request → confirmed project brand → selected pack → contextual conventions. User overrides are allowed; record which dimensions differ from the pack.

5. **Implement in existing stack**; no automatic requirement for React, MUI, Tailwind, a font provider, or animation library. If meaningful motion is required, consult `references/motion-engine.md` without assuming Anime.js is installed. Prefer semantic design tokens, maintain working functionality and responsive behavior.

6. **Hero geometry when applicable:** for a public-facing opening hero, load `references/hero-layout.md` and use the selected style pack’s hero composition cues; keep the full first viewport inclusive of navigation and test short/mobile screens. Never add a hero to screens that do not need one.

7. **Mandatory Anti-Slop Gate**: read [Anti-Slop Constitution](references/anti-slop.md) and [Anti-Slop Writing](references/anti-slop-copywriting.md); apply the **Anti-slop: style-specific** section in the chosen pack. Reject decorative card nesting, generic templates, meaningless badges/charts/icons, dishonest states, marketing filler, ghost code abstractions, and gratuitous motion. Specifically enforce:

   - **Five Structural Tests (Layer 1 procedures):** Deletion Test (verify losses, cut padding), Inversion Test (eliminate vacuous claims), Stranger Test (ground claims in actual product facts), Attribution Test (verify sources/counts), and Load-Bearing Test (delete wrappers, unused handlers, and echo comments; verify test breakages).

   - **Syntax & Punctuation Discipline:** No parataxis (connect ideas with real syntax); break rule-of-three triads; vary sentence length rhythm (burstiness); max 1 em-dash per 500 words; max 1 exclamation mark per 1,000 words; no formulaic openers (*"In today's fast-paced world"*).

   - **Code Surface Hygiene:** No decorative separator banners (`// =====`); no echo comments restating code lines; no passthrough ghost wrappers; no error-swallowing catch blocks; no assertion-free tests (coverage padding); no hallucinated packages or API methods.

   - **Zero rainbow text gradients** (`-webkit-background-clip: text` on headings) unless explicitly mandated by authentic retro/cyberpunk themes.

   - **Vector iconography over emoji (REFLEX):** Prefer crisp, scalable vector icons from Lucide, Radix, Feather, or Heroicons with consistent stroke weight (1.5px–2px) and currentColor inheritance as primary UI icons. Reserve emojis for deliberate user content, expressive badges, or playful genre themes.

   - **Zero fake widgets** (fabricated weather displays, audio spectrum equalizers, simulated live telemetry, or fake counters) invented merely to fill empty space.

   Preserve deliberate style-specific expression.

8. **Tiered quality:** read [Three-Tier Gates](references/quality-tiers.md). `FLOOR` is non-waivable integrity/accessibility/functionality; `REFLEX` may be overridden with product/style evidence; `FINISH` is nonblocking craft. A heuristic is not a ban on the selected style. Run [Writing Calibration](references/writing-calibration.md) for UI copy.

9. **Audit** against the selected pack's quality gate, [universal quality gates](references/quality-gates.md), and [Anti-Slop Audit](references/anti-slop-audit.md). Check real layout, trustworthy data, functional interactions, empty/loading/error states, typography/copy, keyboard focus, dark/light mode contrast integrity (no color collision), mobile, long text and reduced motion. Fix Critical/High issues before presenting as finished. Be truthful about checks not run.

10. **SEO where relevant**: for public-facing web pages, apply `references/seo.md` and review real public URL/metadata, semantics, crawl controls, people-first copy and performance (without invented measurements). Skip or limit on private routes.

11. **Refine** from user feedback without rewriting unrelated decisions. See [feedback](references/feedback.md).

If style is only one of many pieces of a broader task, resolve the style before the *visual* portion, not before non-visual research, planning or backend preparation.

## Non-negotiable anti-slop contract

All ten style packs and every custom style must pass the **shared anti-slop quality bar**. The agent may not use a visual theme to justify deceptive data, useless nested cards, generic hype copy, misleading buttons, inaccessible typography or clutter. **Style-specific signature traits are exempt from aesthetic blacklists when purposeful and usable**: e.g. intentional glass, sculpted clay, neo-brutalist offset shadow, and justified Bento grids. Anti-slop is a decision framework, not a minimalism preset.

Read `references/anti-slop.md`, `references/anti-slop-copywriting.md`, and `references/anti-slop-audit.md` for applicable UI work. Include anti-slop in the final QA pass, not just the prompt. Non-visual tasks do not trigger the design preflight/audit.

## Persistence and UX guardrails

- Do **not** write or update a global taste profile unless the user expressly requests saving it.

- An optional **project** config may be proposed and created with user approval; use `assets/project-style.example.json` / `assets/project-style.schema.json` as a starting point. An existing, user-approved config can avoid repeated questions.

- A user may choose different styles for different projects. Do not infer taste from demographics, role, or a single unrelated UI.

- Images/references are evidence of particular properties, not permission to copy every component or to override an explicit instruction.

- Avoid fabricated data, invented brand guidelines, low-contrast text, inaccessible motion, decorative status indicators, or implied availability of fonts/assets not present.

## Triggering examples — no manual skill call

| User prompt | Required agent behavior |
| --- | --- |
| `Build me a portfolio website` | Taste Engine auto-discovered; ask for style and **STOP** until user replies |
| `Build me a skeumorphsm portfolio website` | Route typo to `skeuomorphism`; load pack directly; **do not ask** |
| `Create a brutalist portfolio` | Read `styles/brutalism.md` directly; build (not neo-brutalism) |
| `Build a glassmorphism landing page, not clay` | Use glassmorphism; honor negative clay instruction |
| `Fix the broken checkout button` | Preserve existing UI style; no new menu |
| `Optimize SEO on my existing live portfolio` | Load `references/seo.md` directly; **no style prompt or redesign** |
| `Build an SEO-friendly Brutalism portfolio` | Load `styles/brutalism.md` + `references/seo.md`; **no style prompt** |
| `Build a private admin dashboard` | Do not expose restricted routes or create public sitemap for them |
| `Build a payment API endpoint` | Non-visual; no style menu |
| `Tambahkan micro-interaction pada tombol di UI existing` | Preserve existing style; use CSS first, optional Anime.js v4 only if justified; no re-selection |
| `Build a brutalist landing page with a full-screen hero` | Load brutalism + full-screen hero contract + public SEO; hero fills first viewport with real content, no extra style question |
| `Build a Skeuomorphism portfolio with button animation` | Load Skeuomorphism + conditional SEO + motion module; no style question |
| `Build a Retro Pixel portfolio` | Load `styles/retro-pixel.md` directly; build (not retro-terminal); **no style prompt** |

## Interaction examples

**User:** “Build an app dashboard.”  

**Agent:** Asks mandatory style-selection question and does not code yet.

**User:** “Build an app dashboard in brutalism.”  

**Agent:** Reads `styles/brutalism.md`, follows raw grid/typography/no offset comic shadow, then builds.

**User:** “Make the selected brutalism UI more colorful, but keep the grid.”  

**Agent:** Preserves brutalist structure; updates project-level palette only, not a silent switch to neo-brutalism.

**User:** “Fix the API validation.”  

**Agent:** No visual preflight.

**User:** “Take a look at this existing glassmorphic form and fix its mobile overflow.”  

**Agent:** Preserve current design, fix responsive behavior, no new selector.

## Compatibility note

This is an **instruction-based gate**, not a platform-enforced hook. For agents that do not reliably load or follow skill instructions, add the optional [`AGENTS.md` activation snippet](assets/AGENTS.snippet.md) or a host-specific pre-tool policy. A coding agent must be capable of pausing for the user's reply. The portable Agent Skills specification allows `SKILL.md` plus referenced files, but does not define guaranteed inter-skill invocation or runtime interrupts.

## Existing projects and visual evidence

For audits and redesigns read [redesign preservation](references/redesign-preservation.md) and keep established routes, data flow, approved content and handlers unless the user asks otherwise. For visual validation follow [browser validation](references/browser-validation.md) where tools permit; static checks never prove a rendered UI is correct. Cite [research notes](references/research-notes.md) for how these concepts were adapted from external work.

Optional `design_controls` (`design_variance`, `motion_intensity`, `visual_density`, 1–10) are **per-project and user-adjustable**. No global preset overrides the selected pack or user instruction.
