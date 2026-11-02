# Anti-Slop Writing — UI copy, microcopy, and product language

**Writing must be human, specific, verifiable, and appropriate to the chosen style.** This is not a prohibition on creativity, humor, personality, marketing, or warm tone. It is a prohibition on vague substitute content and fake persuasion.

For cadence, punctuation and user-voice calibration, read [writing-calibration.md](writing-calibration.md). Treat suspicious words as review prompts rather than proof a passage is AI-generated. Do not rewrite user-approved contractual/legal copy for visual taste.

## The copy test (apply to every interface string)

1. **What does it say?** Does it describe a real feature, task, condition, outcome, or concrete benefit?
2. **Who is speaking?** Match the user's audience, brand voice, language, and domain. Avoid a uniform generic AI narrator.
3. **Can it be believed?** Do not invent performance, scale, trust, compliance, endorsements, counts, or certainty.
4. **Does it help an action?** CTA names the result; status names the state; error explains next step; empty state explains what to do.
5. **Is it concise without losing meaning?** Remove filler, tautology, repeated subtitles, and unnecessary jargon.
6. **Is it understandable?** Use accessible language, appropriate technical vocabulary, and clear localization. Avoid unexplained acronyms and awkward English calques in Indonesian UI.

## Reject default AI marketing patterns

Avoid generic fillers such as "Unlock your potential", "Experience the future", "Take your workflow to the next level", "Seamless intelligence", "Supercharge productivity", "Revolutionize your journey", "All-in-one solution", "Powerful features for everyone", "Elevate your experience", and their localized translations. These may appear only as deliberately quoted/referenced text or when the user explicitly approves that exact brand voice.

Avoid repetitive abstract words: *innovative, seamless, effortlessly, powerful, robust, cutting-edge, world-class, transformative*. Replace with evidence-based detail about what the user can actually do. Avoid AI-esque sentence formulas: "Not just X, but Y", "Meet the future of X", "X, reimagined", "Designed to empower", "Everything you need to ...", "Whether you're X or Y ..." when used as default filler.

## Before → after examples (adapt to the actual product)

| Slop | Better (only if feature is real) | Why |
|---|---|---|
| "Unlock the power of your finances" | "Catat pemasukan dan pengeluaran" | Names a real user task |
| "Supercharge your workflow" | "Create a report from completed work" | Concrete outcome, no hype |
| "Seamless collaboration for everyone" | "Share the report link with the team" | Explains action and recipient |
| "Experience next-gen analytics" | "Lihat transaksi per kategori" | Specific information hierarchy |
| "Get Started Now! 🚀" | "Buat proyek" | Button predicts next screen/action |
| "Something went wrong" | "The report was not saved. Try again." | Tells user what failed and what to do |
| "Success! Amazing work!" | "Report saved successfully" | Confirms actual state without cheering |
| "Nothing here yet!" | "No reports yet. Create your first report." | Honest empty state and useful next step |
| "1000+ users trust us" | Omit, unless backed by verifiable data and approved | Avoids invented social proof |
| "Your dashboard is ready" | "No data is available yet" | Honest initial condition |
| "AI-powered magic" | Explain the actual operation, input and limitation | No unearned mystique |

Do not make the *better* examples into fixed product copy: they are only correct when the stated functionality exists.

## Component-level writing rules

- **Navigation:** short, predictable nouns matching actual destinations; don't rename simple tasks with poetic metaphors unless the product requires it.
- **Buttons:** action verb + object/result, e.g. `Simpan perubahan`, `Unduh CSV`, `Kirim undangan`. Avoid multiple identical `Learn more`/`Submit` buttons when context is ambiguous. Preserve standard familiar labels where clearest.
- **Labels & forms:** explicit labels; placeholders are examples, not substitutes for labels. Helper text provides constraints or explanation, never gratuitous reassurance.
- **Empty state:** describe what is absent, why if known, and one relevant next action. Do not suggest creating items that aren't allowed.
- **Loading:** say what's happening when useful; never imply finished or live without a real source.
- **Errors:** identify failed action, meaningful cause if known, impact and next step. No fake root-cause certainty. Retain user input where possible.
- **Success & status:** reflect confirmed application state only. Don't mark saved, paid, connected, secure, verified, online or complete before evidence exists.
- **Marketing:** product-aware claim + demonstrable mechanism or result; if facts are missing, draft neutral language or mark copy for review. Never manufacture logos, testimonials or comparative metrics.
- **Onboarding:** minimize introductory story; tell users what they'll do now, what data is needed, and why.
- **Accessible copy:** no unexplained icon-only actions, ambiguous link text, all-caps paragraphs, emoji as the sole status cue, or unnecessary punctuation.

## Voice adapts to styles (examples, not mandatory labels)

- **Brutalism:** blunt, concise, specific: `CREATE REPORT` / `No reports.`; reserve uppercase for short labels.
- **Neo-brutalism:** lively but helpful: `Proyek baru` / `Mulai dari template kosong` instead of fabricated celebratory hype.
- **Claymorphism:** warm and calm: `Your report has been saved.` instead of saccharine encouragement.
- **Glassmorphism:** crisp and legible: `Lihat aktivitas` rather than abstract luminous marketing.
- **Enterprise:** precise and actionable: `3 permintaan menunggu persetujuan` only when the count is backed by data.
- **Terminal:** console-flavored *when usable*: `No matching files` only if search actually returned zero.
- **Minimalism / Swiss / Bento / Skeuomorphism:** match layout/voice; do not conflate visual aesthetic with a requirement for vagueness or unusual punctuation.

## Agent editing sequence

1. Identify real task and product language (do not invent audience, feature, or metrics).
2. Draft labels and headings as a content outline before ornamental UI composition.
3. Audit for formulaic hype, duplicate meaning, unverified claims, inaccessible jargon, and action ambiguity.
4. Adapt voice to the chosen style without changing facts.
5. Validate all empty, loading, error, disabled, confirmation, and long/translated text variants.

Use copy review notes only for decisions that require user input; do not bury a useful UI under warnings or filler explanations.
