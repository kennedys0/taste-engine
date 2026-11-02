# Documentation Writing — task-oriented and anti-slop

For README, onboarding docs, guides, API reference, troubleshooting and usage instructions. Not a command to impose Vercel's editorial house style on every user's brand. Source ideas: https://github.com/vercel-labs/agent-skills/tree/main/skills/writing-guidelines and https://github.com/vercel-labs/writing-guidelines .

- **Pick the document's job**: tutorial (learn), how-to (finish a task), reference (look up an exact detail), concept (understand), troubleshooting (fix a problem), or marketing (make a decision). Do not force them into one page when a split helps.
- **Write for reader intent**: headings explain what comes next. Setup steps show prerequisites, commands, expected output, failure recovery and any security constraints. Code examples must match the actual platform/version.
- **Prefer concrete language** over claims such as “easy”, “powerful”, “seamless”, “revolutionary”. State exactly what an action does and what it does *not* do.
- **Accuracy is FLOOR**: no invented performance claims, fake testimonials, APIs, sample output presented as real or silently fabricated examples. Mark placeholders clearly and never expose real secrets.
- **Make scans helpful**: small sections, recognizable command names, meaningful links, code fences with language, readable tables only when comparison helps. Don't make the reader cross-reference a giant hidden example to understand a critical step.
- **Preserve voice**: for user-authored prose, honor language, style and terminology. Avoid rigid universal punctuation bans, forced sentence length or word quotas. Use brevity and variety intentionally, not mechanically.
- **Audit**: docs describe behavior actually implemented and tested. Change examples when APIs change. Review onboarding as a newcomer; note steps you could not validate.

The existing [anti-slop-copywriting](anti-slop-copywriting.md) governs interface copy. This document adds instructional specificity and testable examples for docs, not another mandatory style-interview.
