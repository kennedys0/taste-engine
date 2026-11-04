# Anti-Slop Writing — UI copy, microcopy, and product language

**Writing must be human, specific, verifiable, and appropriate to the chosen style.** This is not a prohibition on creativity, humor, personality, marketing, or warm tone. It is a prohibition on vague substitute content, fake persuasion, and statistically detectable AI writing tropes.

For cadence, punctuation and user-voice calibration, read [writing-calibration.md](writing-calibration.md). Treat suspicious words as review prompts rather than proof a passage is AI-generated. Do not rewrite user-approved contractual/legal copy for visual taste.

---

## The Four Structural Tests for Copy

Before shipping any headline, description, or microcopy, apply these mechanical tests:

1. **The Deletion Test:** Cut the adjective, clause, or entire sentence. Does anything of substance disappear? If the answer is "nothing" (no factual ordering, constraint, or state was lost), it was padding. Delete it.
2. **The Inversion Test:** Invert the claim into a full sentence someone might assert. (e.g. *"Our platform is designed to be unreliable"* or *"The feature plays no role in your work"*). If nobody would ever assert the inversion, the original states an empty truism and carries zero information. Rewrite with concrete mechanics or delete.
3. **The Stranger Test:** Could someone who has never touched or seen the product write this sentence given only a 3-word prompt? If yes, it is generic AI filler. Ground it in the actual tool, user task, or specific data.
4. **The Attribution Test:** Does the text claim *"trusted by thousands"*, *"industry reports show"*, or *"proven to increase revenue"*? If there is no real verifiable source or internal datum backing it, remove the claim. Fabricated specificity destroys trust.

---

## Cadence, Syntax, and Punctuation Discipline

Statistical AI writing patterns are visible even when vocabulary is sanitized. Enforce these mechanical writing rules:

### 1. No Parataxis (Connect Ideas with Real Syntax)
Parataxis is the robotic AI default: *Short sentence. Then another. Then another.* It reads like a list of disconnected declarations and immediately signals machine generation.
- **Fix:** Connect related thoughts using subordinate clauses, conjunctions, semicolons, or commas. Write with syntax that shows how ideas relate—causation, contrast, qualification—not just a series of blunt bullet-like statements.
- **Before:** "Our pipeline parses logs. It flags syntax errors. It notifies your team in Slack."
- **After:** "When the pipeline detects syntax errors in incoming logs, it sends an alert directly to your team's Slack channel."

### 2. Break the Rule of Three (Tricolon Default)
AI has an overwhelming reflex to list exactly three items: *"fast, secure, and scalable"*, *"build, test, and deploy"*, *"design, refine, and deliver"*.
- **Fix:** Break the default triad. Use two, four, one, or five items. Only use three when the underlying reality genuinely has three parts.

### 3. Sentence Length Rhythm (Burstiness)
Uniform sentence length is the single most measurable AI detection signal. AI writes strings of sentences that all hover around 12–16 words.
- **Fix:** Mix 4-word punchy sentences with 25–30 word detailed explanations. Never write three consecutive sentences of approximately the same length.

### 4. Punctuation Limits
- **Em dashes (`—`):** Maximum **ONE per 500 words**. The em-dash is the most overused AI crutch in prose. Use commas, semicolons, colons, parentheses, or separate sentences instead.
- **Exclamation marks (`!`):** Maximum **ONE per 1,000 words**. Excitement comes from clear facts and value, not typographical cheerleading.
- **Semicolons (`;`):** Use them naturally; AI underuses them, whereas precise human writers use them to link closely related independent clauses.
- **Colons (`:`):** Use them to deliver a concrete payoff promised in the preceding clause.

### 5. Formatting Restraint
- **Zero emojis in UI:** Never use emojis as icons, button prefixes, or badges. Use clean vector SVGs (Lucide, Radix, Feather).
- **No bold random words:** Do not bold every third phrase for fake emphasis. Let clear sentence structure carry importance.
- **No asterisks in plain text:** Do not leak markdown formatting (`**important**`) into email, SMS, or plain text outputs.

---

## Reject Default AI Marketing Patterns & Banned Vocabulary

Avoid empty corporate cheerleading and formulaic templates.

### Banned Formulaic Openers
- *"In today's [fast-paced / ever-evolving / digital] world..."*
- *"It's worth noting that..."* / *"It's important to note that..."*
- *"Let's dive in..."* / *"Let's delve into..."*
- *"As a [developer / designer / manager], I..."*
- *"Whether you're X or Y, [Product] has you covered..."*

### Banned Negative Parallelism
- Avoid the formula: *"Not just X, but Y"* or *"It's not about X; it's about Y"*. Say directly what it is without setting up a synthetic contrast.

### Corpus-Validated Banned Buzzwords
Replace these empty words with specific actions, real numbers, or plain verbs:
- *delve, tapestry, landscape (abstract), testament to, vibrant, pivotal, crucial, intricate, meticulous, bolster, garner, underscore, interplay, multifaceted, nuanced (as filler), foster, leverage (as verb → use 'use'), utilize (say 'use'), commence (say 'start'), facilitate, encompass, paramount, groundbreaking, cutting-edge, game-changing, transformative, revolutionize, seamless, robust (outside engineering), comprehensive (describing own output), aforementioned, harnessing, spearheading, navigating (figurative), showcasing, highlighting, emphasizing, enhancing, unprecedented.*

---

## Before → After Examples (Adapt to the Actual Product)

| Slop | Better (only if feature is real) | Why |
|---|---|---|
| "Unlock the power of your finances" | "Catat pemasukan dan pengeluaran" | Names a real user task |
| "Supercharge your workflow" | "Create a report from completed work" | Concrete outcome, no hype |
| "Seamless collaboration for everyone" | "Share the report link with the team" | Explains action and recipient |
| "Experience next-gen analytics" | "Lihat transaksi per kategori" | Specific information hierarchy |
| "Get Started Now! 🚀" | "Buat proyek" | Button predicts next screen/action; no emoji |
| "Something went wrong" | "The report was not saved. Try again." | Tells user what failed and what to do |
| "Success! Amazing work! 🎉" | "Report saved successfully" | Confirms actual state without cheering |
| "Nothing here yet!" | "No reports yet. Create your first report." | Honest empty state and useful next step |
| "10,000+ teams trust us" | Omit, unless backed by verifiable data | Avoids invented social proof |
| "Your dashboard is ready" | "No data is available yet" | Honest initial condition |
| "AI-powered magic" | Explain the actual input, model, and output | No unearned mystique |
| "It's not just a tool; it's a revolution" | "Runs deterministic checks in under 50ms" | Concrete metric over negative parallelism |

---

## Component-Level Writing Rules

- **Navigation:** Short, predictable nouns matching actual destinations; don't rename simple tasks with poetic metaphors.
- **Buttons:** Action verb + object/result, e.g. `Simpan perubahan`, `Unduh CSV`, `Kirim undangan`. Avoid multiple identical `Learn more` buttons.
- **Labels & Forms:** Explicit labels; placeholders are examples, not substitutes for labels. Helper text provides real constraints.
- **Empty States:** Describe what is absent, why if known, and one relevant next action.
- **Loading:** Explain what is in progress; never imply completed or verified before the response arrives.
- **Errors:** Identify the failed action, meaningful cause if known, impact, and recovery step. Retain user input.
- **Success & Status:** Reflect confirmed application state only. Never mark saved, paid, connected, or complete before verification.
- **Marketing:** Product-aware claim + demonstrable mechanism or result. Never manufacture customer logos or statistics.

---

## Voice Adapts to Styles (Tone, Not Truth)

- **Brutalism:** Blunt, concise, specific: `CREATE REPORT` / `No reports.`; reserve uppercase for short labels.
- **Neo-brutalism:** Lively, punchy, direct: `Proyek baru` / `Mulai dari template kosong` without celebratory cheerleading.
- **Claymorphism:** Warm and calm: `Your report has been saved.` instead of saccharine encouragement.
- **Glassmorphism:** Crisp and legible: `Lihat aktivitas` rather than abstract luminous marketing.
- **Enterprise:** Precise and actionable: `3 permintaan menunggu persetujuan` only when the count is backed by data.
- **Terminal:** Console-flavored: `0 matching records found` only if search actually returned zero.
- **Swiss / Editorial:** Disciplined, typographic clarity, clear section index numbering (`01`, `02`).
- **Minimalism / Bento / Skeuomorphism:** Match visual density; visual style never justifies vague or bloated prose.

---

## Agent Editing Sequence

1. **Identify real task and domain facts:** Never invent features, metrics, or credentials.
2. **Draft plain labels and content outline first:** Establish content before visual ornament.
3. **Run the 4 Structural Tests:** Check Deletion, Inversion, Stranger, and Attribution.
4. **Audit Cadence & Punctuation:** Check burstiness, eliminate parataxis, break rule-of-three, check em-dash count.
5. **Calibrate Voice to Selected Style:** Adjust tone without adding fluff.
6. **Validate Edge States:** Empty, loading, error, disabled, confirmation, and narrow mobile viewports.
