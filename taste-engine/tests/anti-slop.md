# Anti-Slop acceptance scenarios — manual / agent evaluation

Test by asking an agent to build or review real screens and code. These are scenarios, not claims of automatic UI execution.

1. **Nested cards:** dashboard has an owning panel with an empty-state panel inside it. Expected: remove redundant inner panel, keep content and CTA in parent; preserve nesting only when it represents another real workflow boundary.
2. **Four synthetic KPIs:** no backend/fixture supplied. Expected: no fabricated values, charts or deltas. Show truthful no-data/loading state.
3. **Marketing hype:** draft says "Unlock your potential with seamless analytics!" Expected: product-specific feature/outcome copy or neutral placeholder, no unsupported performance claims.
4. **Button copy:** ten generic `Learn more` CTAs. Expected: unique action-oriented accessible labels (or explicit contextual accessible names) tied to real destinations.
5. **Failure copy:** saving fails. Expected: preserve input, say what did not save, explain retry; never show success toast before save confirmation.
6. **Status dots:** agent auto-adds green `LIVE` dots for a static page. Expected: remove unless a real live status exists and changes a user decision.
7. **Mobile 360px:** long translated button clips and one desktop card floats on screen. Expected: recompose group, preserve readable text and actionable button.
8. **Artificial motion:** large bouncing hero orb and endlessly pulsing CTA. Expected: remove, replace with purposeful state/interaction transitions when useful.
9. **Claymorphism:** all inner cards have giant donut shadows. Expected: flatten unnecessary nesting, maintain sculpted material consistency and directional light; do not discard clay aesthetic.
10. **Glassmorphism:** overlaid translucent card contains glass subcards on busy image. Expected: limit glass layers, ensure contrast and solid fallback, not a blanket ban on blur.
11. **Classic brutalism:** assistant adds colorful comic shadows to "make it pop". Expected: restore flat raw borders/grid and blunt readable copy.
12. **Neo-brutalism:** every icon and label gains a hard offset shadow. Expected: keep characteristic shadow on meaningful controls/surfaces, remove decorative repetition.
13. **Bento:** empty tiles are added only to fill symmetrical grid. Expected: content-first spans, honest empty state or recompose; bento tiles allowed for meaningful modules.
14. **Enterprise:** mock `99.9% SLA`, vanity chart and four KPI cards added by default. Expected: remove invented figures, use real table/filter/task structure.
15. **Custom style:** user explicitly requests a psychedelic gradient editorial hero. Expected: preserve expression if usable; do not flag merely for being colorful.
16. **Accessibility:** selected aesthetic calls for subtle low-contrast secondary labels. Expected: preserve character while retaining legibility, focus and zoom.
17. **Review transparency:** agent cannot run browser or inspect screenshot. Expected: give instruction/code review only, note visual checks not performed.
18. **Backend-only fix:** user asks to patch API validation. Expected: no style selector or anti-slop UI questionnaire.
19. **Style selector preflight:** new UI request without an approved style. Expected: ask one style-choice question and stop before UI coding; no forced default.
20. **User taste override:** user approves asymmetrical cards or an editorial hero. Expected: respect preference unless it harms accessibility, truth or functionality.
21. **Deletion Test verification (Prose):** Marketing text contains filler like *"marking a pivotal milestone in the evolution of modern analytics"*. Expected: apply Deletion Test; cut the span; artifact records *"Lost: nothing"*; replace with concrete user action or remove.
22. **Inversion Test verification (Claims):** Draft contains *"Our system is built for optimal reliability and maximum efficiency"*. Expected: apply Inversion Test; write out negation (*"Our system is built for unreliability and inefficiency"*); artifact shows negation is an absurd assertion nobody would make; rewrite with verifiable SLA/metrics or cut.
23. **Parataxis and burstiness correction:** Agent writes 4 short robotic sentences in a row (*"The tool reads files. It parses ASTs. It outputs tokens. It returns exit code 0."*). Expected: rewrite with connective syntax and varied sentence length (*"When given a source directory, the tool parses the AST of each file and emits token metrics before terminating with exit code 0."*).
24. **Rule of three break and punctuation limits:** Draft contains 5 em-dashes and repeated triads (*"secure, fast, and modern"*). Expected: break default triads to 2 or 4 items; limit em-dashes to maximum 1 per 500 words.
25. **Code slop — Load-bearing test on ghost wrapper:** Agent creates `class UserFetcherWrapper` that passes `fetch()` arguments directly without caching, conversion, or validation. Expected: delete wrapper, wire caller directly; verify all tests pass; remove ghost abstraction.
26. **Code slop — Comment hygiene:** File contains `// ================== AUTH ==================` and `counter += 1 // increment counter`. Expected: delete decorative banner and redundant echo comment; retain only comments recording non-obvious invariants or bug workarounds.
27. **Code slop — Assertion-free test (coverage padding):** Test file has `def test_save(): res = save(data); assert res is not None`. Expected: apply Load-Bearing mutation (mutate `save()` to `return object()`); test still passes; rewrite test to verify saved database row and returned payload.
28. **Decidable package & API verification (anti-hallucination):** Agent drafts code importing a plausible-sounding library `@company/fast-query-react`. Expected: run Layer 0 check against npm registry; reject non-existent package; use verified pinned dependencies.
