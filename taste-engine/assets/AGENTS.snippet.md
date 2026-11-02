# Taste Engine — frontend preflight for AGENTS.md / project agent instructions

For any task that creates or substantially redesigns visible frontend UI (website, portfolio, dashboard, app screen, landing page, mobile UI), **invoke `taste-engine` automatically** even if the user never mentions the skill name. Read `taste-engine/SKILL.md` from the installed skill folder.

1. If the current request **explicitly names a style**, including variants/typos (`skeumorphsm` → `skeuomorphism`), **do not ask about style**. Read its bundled `styles/<id>.md` and follow the shared Anti-Slop Quality System. Proceed.
2. Otherwise, if an approved project design system/style is established, keep it for incremental tasks. Do not interrupt.
3. Otherwise, ask **one style selection question** and **stop before UI code**. Resume after the user responds, retaining their original task.
4. For backend-only work, nonvisual bug fixes, tests, deployment, or writing-only tasks, **do not open style selection**.

Read `references/auto-invocation.md` for conflict and exclusion handling. Installing a skill does not guarantee every harness will automatically load it; keep this project instruction as an extra behavioral safeguard, not a substitute for an installed skill.

## Full-screen hero default (Taste Engine v0.8)

For new portfolio, landing, and public homepage UI **with a hero**, after the aesthetic is resolved read `taste-engine/references/hero-layout.md`. Compose the first visible screen as header + hero using mobile-safe `min-height: 100svh` (with `100vh` fallback); subtract header height when it lives in flow, but never subtract it for an overlay header. Avoid clipped CTA/nav, inflexible `height:100vh`, artificial decoration or scroll-jacking. Keep this cross-style rule on all styles. Respect explicit no-hero/compact-hero requests and do not retrofit a hero into dashboards and forms.

## Automatic public SEO companion (Taste Engine v0.6)

For new or substantially changed **public websites**, after style resolution load `taste-engine/references/seo.md` in addition to the chosen aesthetic. No second SEO questionnaire. For a user request limited to SEO audit/metadata/sitemap/canonical, load SEO immediately with **no style picker**. Preserve private routes, existing noindex/auth controls, and all existing branding. Avoid inventing domains, schema entities, keyword-stuffed content or ranking claims. For native apps/backend-only tasks, do not add web SEO. If a domain or published content is unknown, complete safe work and record it as pending.

## Optional motion adapter (Taste Engine v0.7)

For requested UI micro-interactions, preserve the established project style and inspect `taste-engine/references/motion-engine.md`. Use the style pack's motion section. Do not ask for a new style on incremental motion-only changes. CSS/native motion is preferred; adding `animejs` v4 is optional and requires a justified dependency decision. Always support reduced motion, avoid decorative loops, and clean up component animations.

## Conditional engineering quality (Taste Engine v0.9)

After the style preflight, read `taste-engine/references/engineering-router.md`. Every web UI task applies `web-interface-quality.md` without changing the chosen aesthetic. React/Next performance and composition rules load only after verifying framework and task; React Native/Expo loads native guidance instead; docs writing and view transitions are task-specific. Deployment and Vercel bill optimization never run automatically on UI creation. Preserve the full-viewport hero policy, optional Anime.js behavior, SEO and anti-slop rules.
