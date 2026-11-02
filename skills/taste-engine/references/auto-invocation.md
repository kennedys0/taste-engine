# Automatic Invocation Contract (v0.5)

The feature is **automatic discovery via SKILL.md metadata**, not a shell hook. A compliant autonomous-skill host indexes skill names and descriptions and decides relevance each user turn. This router may not activate if the platform disables skills or cannot discover this folder. Installation and project agent instructions increase reliability but cannot promise universal execution.

## Intent gate (evaluate in order)

1. **Visual task?** Build/create/design/redesign a website, landing page, portfolio, dashboard, UI screen, mobile app, component, or update design tokens? Continue. For code-only/backend/security/operations/content writing, skip the selector. UI audit/review can audit existing style without new-selection prompts.
2. **Style explicitly named for this request?** Recognize registered ID, aliases, normal spelling variants, and visually specific user descriptions. Respect negation (`no glass`, `no glassmorphism`) and context: "compare brutalism with glass" is not permission to design a mixed UI. Explicit current-request preference overrides old project choice unless the user is merely discussing options.
3. **If a style is named**, resolve style ID via `styles/registry.json` (optional `scripts/style_probe.py`), read exactly that `styles/<id>.md` pack and the shared anti-slop/quality references, and execute without a style interview. A minor typo ("skeumorphsm") must not cause an unnecessary question.
4. **If no style is named**, check whether an explicitly approved project style config or existing product system already defines one for the task. If yes, use it without asking. Do not import taste preferences from a different project.
5. **If still unresolved**, ask exactly one question listing ~6 distinct styles, plus an option for more/custom/reference, then **end the current agent turn without UI implementation**. On the next user message, continue the same task with the selected style (retain the original requirements).
6. **If user delegates** ("you decide" / "choose for me"), choose a justified provisional direction, disclose the assumption, proceed. If the host cannot ask, cannot pause, or the task explicitly requires unattended execution, do not pretend the user selected a style. Respect higher-priority constraints and report the limitation.

## Style normalization and safety

- Case and separators: `NeoBrutalism`, `neo-brutalism`, `neo brutalism`, `NEOBRUTALISM` → `neo-brutalism`.
- Minor typo: `skeumorphsm`, `skeumorphism`, `skeuomorfisme`, `skeuomorphic` → `skeuomorphism`.
- Longer and more specific aliases win over shorter embedded ones: `neo-brutalism` must never accidentally load `brutalism`.
- Aesthetic ≠ category. "Enterprise dashboard" may mean *product type* rather than a visual request. Do not silently label that an explicit enterprise design preference.
- A **negative-only** instruction ("no glassmorphism") is a constraint, not a positive choice. Ask for a positive style if otherwise unresolved.
- More than one positive style may indicate a requested hybrid; assign primary + explicit secondary dimensions. If user is **comparing** styles, don't merge.
- For unregistered yet clear style names (e.g. "Y2K"), derive custom project spec; do not silently substitute a registered style. Consult references only when needed.

## Worked examples

**A: Missing style (stop):**

User: `Build a portfolio website for me.`

Agent: `Before I begin, which portfolio style would you prefer? Claymorphism, Glassmorphism, Brutalism, Neo-brutalism, Minimalism, Swiss/Editorial, or a custom style? You can also share a visual reference.`

Agent **ends its turn**. On reply `Neo-brutalism`, reads that pack and starts implementation. No extra interview.

**B: Explicit and misspelled (skip prompt):**

User: `Build me a skeumorphsm portfolio website.`

Agent resolves `skeuomorphism`, opens `styles/skeuomorphism.md`, derives tactile and physical control design and checks readability + anti-slop. It does **not** ask which style.

**C: Existing app (preserve):**

User: `Fix the settings page overflow on mobile.`

Agent inspects existing design system and fixes only the overflow. No style selection unless asked to redesign the page.

**D: Explicit exclusion (do not guess):**

User: `Make a portfolio, but don't use glassmorphism.`

Agent asks one style question with the excluded option omitted; does not treat the word "glassmorphism" as requested style.

## Precedence

Accessibility, usability and security floor > explicit current user selection > approved project style/brand > selected style pack > product conventions > the agent's subjective preferences. If updating an existing design without redesign intent, avoid replacing brand/style tokens just because a new style appears in an unrelated comment or sample text.

## Host-specific guidance

- Antigravity IDE/App: project `.agents/skills/taste-engine/`; global `~/.gemini/config/skills/taste-engine/`. `.agent/skills` is a legacy compatibility path. Check Customizations/active skills. Automatic discovery is based on metadata relevance.
- Codex: project `.agents/skills/taste-engine/`; local skill discovery depends on client/harness. Project-level `AGENTS.md` strengthens instruction priority for frontend preflight.
- Claude Code: project `.claude/skills/taste-engine/`; a project `CLAUDE.md` can reinforce preflight if autonomous selection is unreliable.
- Other coding agents: use their documented skill discovery paths. **Don't assume installing a file forcibly injects an always-on system prompt.**

See `INSTALL.md` at repository root for copy commands and a test prompt. No network is needed to use bundled style packs.

## SEO routing addendum (v0.6)

SEO is **orthogonal** to aesthetics. For public website builds, resolve style first then load `references/seo.md` automatically in the same build, preserving the selected material and voice. **No extra style/SEO question**. For an SEO-only request, skip visual selection and run SEO reference directly. Private dashboards and native applications do not automatically receive public SEO. For unknown domain never invent canonical/OG URL. The style selector does not ask whether the user wants SEO. See `tests/seo-routing.md`.
