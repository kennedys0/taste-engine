# Auto-trigger acceptance scenarios (agent/harness tests)

These are **agent behavior** tests, not proofs of runtime automatic invocation. Start each test in a fresh chat with the router installed; check observable first reply and loaded files/logs when available.

| Case | User prompt | First action / style choice | Must NOT happen |
| --- | --- | --- | --- |
| UI implicit (Indonesian) | `Build me a portfolio website` | Ask exactly one style question, then stop | No UI code, default clay choice, unrelated questions |
| UI implicit (English) | `Build a landing page for my product` | Ask one style question, stop | No arbitrary framework/style selection |
| Explicit typo | `Build a portfolio website in skeumorphsm style` | Resolve `frutiger-aero` (variant `tactile`), load `frutiger-aero.md` immediately | No menu and no invalid-style response |
| Explicit canonical | `Create a skeuomorphism music player` | Resolve `frutiger-aero` (variant `tactile`), load `frutiger-aero.md` | No redundant question |
| Explicit case/spacing | `Build portfolio in NeoBrutalism` | Load `neo-brutalism.md` | No brutalism-only file |
| Explicit glass | `Build a landing page glassmorphism` | Resolve `frutiger-aero` (variant `glass`), load `frutiger-aero.md` | No menu; no clay |
| Negated only | `Create portfolio but not glassmorphism` | Ask for remaining styles | Do not select glass/aero from the negation alone |
| Mixed constraints | `Build a brutalist portfolio with editorial typography` | Load primary brutalism and typographic editorial reference | Do not mix all style defaults |
| User delegation | `Build a portfolio; choose the style yourself` | Pick justified provisional style and proceed | Do not claim user chose it |
| Approved project config | `Build an about page` with existing approved minimalism config | Preserve minimalism | No redundant style prompt |
| Minor UI bug | `Fix navbar overflow on existing page` | Preserve existing style, fix bug | No preflight menu |
| Pure backend | `Write an API route and database migration` | No style preflight | No UI-specific conversation |
| Comparative discussion | `Compare brutalism and neo-brutalism` | Explain contrast as information task | Do not build/merge UI |
| Custom explicit | `Buat portfolio gaya Y2K` | Derive custom Y2K style and implement | No menu of unrelated presets |
| Auto invoker missing | `Buat portfolio` and host doesn't discover skills | Mark as platform test failure / add project agent instruction | Do not report 'auto trigger passed' based on static validation |

Pass criteria: the host actually invokes the router (via metadata), first-turn ask/skip behavior matches, style pack selection matches and anti-slop checks are applied. Record exact host/version and whether the prompt was answered by skill or generic model behavior.

## SEO companion activation tests (v0.6)

For public website builds, the first-turn style-selection gate still wins. Once style is chosen, load `references/seo.md` without a second SEO confirmation. When user explicitly requests SEO-only work, activate SEO immediately without style selection or unrelated visual edits. For internal dashboards/native-only apps, do not automatically create public SEO files. Full matrix: `tests/seo-routing.md`.
