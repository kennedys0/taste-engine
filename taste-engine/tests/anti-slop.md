# Anti-Slop acceptance scenarios — manual / agent evaluation

Test by asking an agent to build or review real screens. These are scenarios, not claims of automatic UI execution.

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
