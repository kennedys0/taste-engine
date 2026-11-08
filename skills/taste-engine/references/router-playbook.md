# Taste Engine — detailed router playbook

Deep-dive reference for `SKILL.md`. Load the sections you need; the router file stays lean, this file holds the full contracts.

## 1. Material fidelity — screenshot-level contract

Selected visual aesthetics must be **recognizable from the rendered interface**, not just stated in headings or CSS variable names.

- `frutiger-aero` → mandatory **Frutiger Aero material fidelity gate** in `styles/frutiger-aero.md`: authentic glossy acrylic specular sheens, aqua/ocean/leaf nature-tech balance, tactile controls, accessible fallback. A flat navy hero plus a blue CTA is not Frutiger Aero. Acceptance: `tests/frutiger-aero-visual.md`; recipe: `examples/frutiger-aero/glossy-surfaces.css`.
- `y2k-futurism` → mandatory **Y2K Futurism material fidelity gate** in `styles/y2k-futurism.md`: polished chrome, liquid silver, iridescent spectral highlights, chamfered geometric framing. Acceptance: `tests/y2k-futurism-visual.md`; recipe: `examples/y2k-futurism/metallic-surfaces.css`.
- Every other pack carries its own gate in `styles/<id>.md` (`## Style-specific quality gate`). Never apply one style's fidelity check to another.

### Material exceptions

- **Frutiger Aero:** purposeful CSS gradient backdrops, atmospheric nature-tech light fields, and acrylic specular horizon sheens are explicitly permitted — they define the optimistic mid-2000s aesthetic.
- **Y2K Futurism:** multi-stop metallic chrome gradients, liquid silver finishes, and iridescent spectral borders are explicitly permitted — they define millennium cyber-optimism.
- Do not remove these to satisfy generic anti-slop gradient warnings. Validate that the first viewport visibly reads as an authentic composition. Exemptions apply only to the selected material and never override usability, truthfulness, accessibility or user constraints. Full exemption matrix per style: `references/anti-slop.md`.

## 2. Zero-command invocation contract (detail)

- This is a **task-triggered skill**, not a slash-command workflow. The actual platform decides invocation; this skill cannot create an OS-level hook or guarantee compliance on every host. Exact transcripts and host notes: [auto-invocation](auto-invocation.md).
- **Implicit style:** "build me a portfolio website" → ask ONE concise style question, then end the turn. Never bundle unrelated questions.
- **Explicit style:** "build a portfolio website in skeumorphsm style" → normalize the typo (`skeuomorphism` → canonical `frutiger-aero`, variant `tactile`), read the pack, and build without asking. No question menu.
- **Established project:** approved project config or documented brand wins for incremental work; no menu.
- **Non-visual work:** API implementation, business-logic debugging, migrations, infrastructure, writing-only → no style selector.
- **Alias resolution:** read `styles/registry.json` for IDs, aliases, and misspellings. Normalize punctuation, casing, hyphens; respect negations ("not glassmorphism") and context. `python3 scripts/style_probe.py --prompt "..."` gives a deterministic hint; semantic interpretation and project context still win. Never call a standalone style skill by name — read the local `styles/<id>.md`.

## 3. Full-screen hero contract (detail)

For any **new public portfolio, landing page, showcase, or homepage with a hero**:

- Default to a full one-screen header + hero composition:
  - Header in normal/sticky flow before the hero: `min-height: calc(100vh - var(--pow-header-h, 58px)); min-height: calc(100svh - var(--pow-header-h, 58px)); display: flex; flex-direction: column; justify-content: center;`
  - Header overlays the hero: `min-height: 100vh; min-height: 100svh;`
- Always define `--pow-header-h` in `:root` (with fallback in `var(..., 58px)`) so the `calc()` never invalidates and lets the next section bleed into the first desktop viewport (`1440×900`).
- Never use fixed `height: 100vh` or `overflow: hidden` that clips text on short/mobile viewports. Keep content and CTA usable at narrow/short screens; allow natural growth at zoom/large text. Do not invent imagery, badges, fake statistics or looped motion just to fill the screen.
- Does **not** force a hero onto private dashboards, forms, app workspaces, or incremental edits that don't create/redesign the hero. An explicit user choice for a compact hero or no hero wins. Acceptance: `tests/hero-layout.md`.

## 4. Motion engine rules (detail)

- Motion **never becomes a new aesthetic selector** and never requires a second interview. `Tambahkan micro-interaction di dashboard ini` preserves the established style; no style question.
- No automatic dependency installs. Inspect the stack first; prefer CSS/native browser capabilities. Anime.js v4 only when it meaningfully simplifies coordinated motion or was explicitly requested. React/Next: `createScope()` + lifecycle cleanup. Reduced-motion users: disable nonessential effects, keep interactions functional. Do not force bounce, loops, or gratuitous stagger. Mapping: `styles/motion-profiles.json`; React recipe: `examples/react/anime-v4-press.jsx`. Non-web/native apps use platform motion APIs.

## 5. SEO routing rules (detail)

- **Explicit style + public website:** load pack + `references/seo.md` (+ `references/seo-implementation.md` when needed) and implement. No style question.
- **Missing style:** ask the one style question and stop; load style + SEO only **after** the answer. Do not bypass preflight merely to write metadata.
- **SEO-only task** (`fix canonical URLs and the sitemap`): read the SEO module immediately, **no style prompt or redesign**.
- **Private/internal application:** preserve confidentiality and existing indexability; don't generate public sitemaps or reveal private routes. Native mobile/backend-only tasks are out of scope.
- **Unknown domain:** do not fabricate live URLs, authorship, structured data, reviews or page content; implement safe semantics/title and report what remains pending.
- SEO and style share **FLOOR / REFLEX / FINISH** gates; privacy, truthful content, accessibility and functional behavior outrank aesthetic and search preferences. Acceptance: `tests/seo-routing.md`. The standalone `taste-seo` skill is for SEO-only installations; router users don't need it separately.

## 6. PoW showcase architecture (detail)

When building or modifying style showcase pages, Proof-of-Work demos, or interactive design studios (such as `docs/*.html`), reuse the canonical template `presets/templates/pow-showcase.template.html` and preserve the **7 canonical sections**:

1. **Sticky Header:** uniform `36px` action button heights, theme toggle, `< 768px` mobile hamburger drawer.
2. **Full 1-Screen Hero (100svh):** `min-height: calc(100vh - var(--pow-header-h, 58px)); min-height: calc(100svh - var(--pow-header-h, 58px)); display: flex; flex-direction: column; justify-content: center;` — zero next-section bleed on desktop, fluid `clamp()` typography, balanced natural-height hero columns, compact single-row horizontally scrollable command well (`flex-wrap: nowrap`).
3. **Interactive Studio Cockpit:** responsive workspace, title bar, touch containment, balanced split-column stacks (`align-items: stretch` + `flex: 1`), zero horizontal clipping.
4. **Component Anatomy & Quality Gates:** authentic specimen cards in equal-height balanced columns (zero dead vertical gaps, zero 3+1 orphan control wrapping) and explicit style-specific failure tests.
5. **Tabbed Terminal Installation:** 3-tab terminal (`Standalone`, `Full Engine`, `Presets`), window dots, dedicated top-right header copy button (zero overlapping text), agent support matrix strip.
6. **Core Architectural Principles:** 3 key design pillars in an equal-height grid.
7. **Canonical 10-Style Footer:** responsive auto-fit grid linking all 10 canonical styles.

Forbidden deviations: cramped 3-card installation layouts, unbalanced multi-column card stacks leaving empty vertical holes, orphan wrapped controls, copy buttons occluding text, mismatched header/cluster button heights, stretched single-column footers.

## 7. Applying the style after selection (detail)

1. **Domain pre-flight (mandatory):** state the product domain and primary audience in one sentence — e.g., *"A project management tool for indie developers."* Design direction follows from this statement, not the agent's default palette. If it can't be derived, fold it into the single style question.
2. **Load only the selected pack** plus shared references. Do not blend rules from unselected packs. **Style ≠ anatomy:** product flow comes from real user goals; the pack determines visual material. Write a one-sentence, product-grounded visual thesis (domain + audience + aesthetic intention). See [decision system](decision-system.md).
3. **Build project Design DNA:** type families + fallback, type scale, weights, writing tone, palette roles, density, spacing, radius, border, elevation, layout grid, component anatomy, states, navigation, motion, reduced-motion. See [translation](translation.md).
   - **Dark/light coupling:** paired tokens for canvas, cards, text, borders, inputs, status pills flip in tandem — zero black-on-black or white-on-white. Dark default is the warm dark slate in [Responsive Baseline](responsive-baseline.md) unless the pack dictates otherwise (Brutalism `#000000`, Retro-Terminal CRT phosphor).
   - **Responsive & card-balance safety:** follow [Responsive Baseline](responsive-baseline.md): 320px viewport safety, fluid mobile typography, small-viewport navigation, circular geometry (`aspect-ratio: 1/1; flex-shrink: 0;`), inline command pills, balanced mobile footers, strict multi-column card balance (`align-items: stretch` on grids, `flex: 1 1 0%` on stacked side cards, equal-height peers via `height: 100%; justify-content: space-between;`, matched grid multiples, zero 3+1 orphan wrapping). Packs may override scales for signature aesthetics.
4. **Precedence:** technical/safety/accessibility → explicit current request → confirmed project brand → selected pack → contextual conventions. Record dimensions that differ from the pack.
5. **Implement in the existing stack;** no automatic requirement for React, MUI, Tailwind, a font provider, or an animation library. Prefer semantic tokens and working responsive behavior.
6. **Anti-Slop Gate:** read [Anti-Slop Constitution](anti-slop.md) and [Anti-Slop Writing](anti-slop-copywriting.md); apply the chosen pack's `## Anti-slop: style-specific` section. Enforce:
   - **Five Structural Tests:** Deletion Test (verify losses, cut padding), Inversion Test (eliminate vacuous claims), Stranger Test (ground claims in product facts), Attribution Test (verify sources/counts), Load-Bearing Test (delete wrappers, unused handlers, echo comments; verify test breakages).
   - **Syntax & punctuation discipline:** no parataxis; break rule-of-three triads; vary sentence length (burstiness); max 1 em-dash per 500 words; max 1 exclamation per 1,000 words; no formulaic openers.
   - **Code surface hygiene:** no decorative separator banners (`// =====`), no echo comments, no passthrough ghost wrappers, no error-swallowing catch blocks, no assertion-free tests, no hallucinated packages or API methods.
   - **Zero rainbow text gradients** on headings unless mandated by authentic retro/cyberpunk themes.
   - **Vector icons over emoji (REFLEX):** Lucide/Radix/Feather/Heroicons, 1.5px–2px stroke, `currentColor`. Emojis only for deliberate user content, expressive badges, or playful genre themes.
   - **Zero fake widgets** (fabricated weather, audio spectrum, simulated telemetry, fake counters).
   - Preserve deliberate style-specific expression.
7. **Tiered quality:** [Three-Tier Gates](quality-tiers.md) — `FLOOR` non-waivable (integrity/accessibility/functionality), `REFLEX` overridable with evidence, `FINISH` nonblocking craft. A heuristic is not a ban on the selected style. Run [Writing Calibration](writing-calibration.md) for UI copy.
8. **Audit:** selected pack's quality gate + [universal gates](quality-gates.md) + [Anti-Slop Audit](anti-slop-audit.md). Check real layout, trustworthy data, functional interactions, empty/loading/error states, typography, keyboard focus, dark/light contrast integrity, mobile, long text, reduced motion. Fix Critical/High before presenting as finished; be truthful about checks not run.
9. **SEO where relevant:** public-facing pages get `references/seo.md` — real URL/metadata review, semantics, crawl controls, people-first copy, performance without invented measurements. Skip/limit on private routes.
10. **Refine** from feedback without rewriting unrelated decisions. See [feedback](feedback.md).

If style is one piece of a broader task, resolve it before the *visual* portion, not before non-visual research, planning or backend prep.

## 8. Mandatory first question (example in Indonesian)

> Before I start designing, which visual style would you like?

> 1. **Claymorphism** — lembut, tactile, kedalaman halus
> 2. **Frutiger Aero** — glossy, aqua, optimistik era 2000-an
> 3. **Brutalism** — tipografi tegas, grid mentah, kontras tinggi (varian: **Raw** & **Bento**)
> 4. **Neo-brutalism** — warna berani, border dan hard shadow
> 5. **Minimalism** — bersih, sederhana, fokus konten
> 6. **Swiss / Editorial** — grid presisi, tipografi dominan
>
> Atau ketik **lainnya**, **custom**, atau kirim referensi.

Adapt to the user's language. Keep it a **single question**; describe distinctions without declaring one "best". First present six plus a way to see the remaining options. If the user wants an interactive selector and the host supports it, present the same choices as UI controls.

## 9. Persistence and UX guardrails

- Do **not** write or update a global taste profile unless the user expressly requests saving it.
- An optional **project** config may be proposed with user approval; start from `assets/project-style.example.json` / `assets/project-style.schema.json`. An existing user-approved config avoids repeated questions.
- A user may choose different styles for different projects; do not infer taste from demographics, role, or a single unrelated UI.
- Images/references are evidence of particular properties, not permission to copy every component or override an explicit instruction.
- Avoid fabricated data, invented brand guidelines, low-contrast text, inaccessible motion, decorative status indicators, or implied availability of fonts/assets not present.
- Optional `design_controls` (`design_variance`, `motion_intensity`, `visual_density`, 1–10) are per-project and user-adjustable. No global preset overrides the selected pack or user instruction.

## 10. Interaction examples

**User:** "Build an app dashboard." → **Agent:** asks the mandatory style question; does not code yet.

**User:** "Build an app dashboard in brutalism." → **Agent:** reads `styles/brutalism.md`, follows raw grid/typography/no offset comic shadow, builds.

**User:** "Make the selected brutalism UI more colorful, but keep the grid." → **Agent:** preserves brutalist structure; updates project-level palette only, not a silent switch to neo-brutalism.

**User:** "Fix the API validation." → **Agent:** no visual preflight.

**User:** "Fix this existing glassmorphic form's mobile overflow." → **Agent:** preserves the current design, fixes responsive behavior, no new selector.

## 11. Compatibility note

This is an **instruction-based gate**, not a platform-enforced hook. For agents that do not reliably load or follow skill instructions, add the optional [`AGENTS.md` activation snippet](../assets/AGENTS.snippet.md) or a host-specific pre-tool policy. A coding agent must be capable of pausing for the user's reply. The portable Agent Skills specification allows `SKILL.md` plus referenced files, but does not define guaranteed inter-skill invocation or runtime interrupts.

## 12. Existing projects and visual evidence

For audits and redesigns read [redesign preservation](redesign-preservation.md) and keep established routes, data flow, approved content and handlers unless the user asks otherwise. For visual validation follow [browser validation](browser-validation.md) where tools permit; static checks never prove a rendered UI is correct. Cite [research notes](research-notes.md) for how these concepts were adapted from external work.
