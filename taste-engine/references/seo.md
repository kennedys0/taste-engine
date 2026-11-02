# SEO Integration — cross-style search readiness

> **Scope:** public, search-discoverable web pages. This is NOT an aesthetic style pack. Load after style resolution, or immediately for a standalone SEO task with no visual redesign.
>
> Verified reference basis: Google Search Central SEO Starter Guide, Search Essentials, JavaScript SEO Basics, Structured Data Policies, Core Web Vitals, and Helpful Content guidance. See links at the end. This skill cannot guarantee indexing, search-result features, rankings, or traffic.

## Invocation decision (must resolve before editing)

1. **Public website created or redesigned** (portfolio, landing page, brochure site, publicly indexable blog, store, docs, public project pages): SEO baseline **ON**, silently alongside the selected visual style. No second style/SEO questionnaire.
2. **Pure SEO request** ("audit SEO", "fix metadata", "technical SEO", "SEO optimization", sitemap/robots/canonical): run this module **directly**, with no style picker unless the user explicitly requests a visual redesign.
3. **Authenticated / internal UI** (admin, account settings, private dashboard, internal tools): do **not** expose private pages, generate public sitemaps for protected routes or turn on indexing. Retain existing privacy settings. Public marketing pages in the same project can still receive SEO.
4. **Existing site minor visual fix:** preserve SEO metadata/canonical/indexability and routes. Only update SEO if the task or changed content warrants it.
5. **Explicit noindex / staging / preview:** retain noindex; never expose drafts or previews for marketing SEO. Reconcile environment and indexing intent before release.
6. **No website** (mobile APK, native app view, backend only): ordinary web SEO **NOT APPLICABLE**. Offer app store optimization only if requested; don't quietly add SEO files.

Priority: security and privacy > user/project configuration > accurate discoverability > rich previews > optional optimizations. A user-specified style never justifies breaking semantic markup or hiding meaningful text from crawlers.

## First pass: determine what's real

- Identify framework/router, deployment target, domain/hostname if known, locale(s), available published pages, intended public vs private routes, and pre-existing metadata/SEO plugins.
- Infer a public portfolio's search intent from the brief; do not interrupt style selection with an SEO interview. If the origin/domain or real content is unknown, implement what is safe and report the unresolved inputs. Never invent a live domain, author credential, project result, social handle, customer name or canonical URL.
- Identify one clear topic and visitor purpose per indexable page. Titles and headings describe actual content; don't force a keyword on pages where it doesn't fit.
- Respect established infrastructure; avoid adding competing SEO libraries or replacing working metadata APIs.

## Mandatory search-readiness baseline

### Content and semantics

- Useful, original, people-first text. Use the product's truthful description, work, services, or projects. Preserve voice according to the chosen style; no keyword stuffing or mass-generated thin pages.
- Meaningful semantic HTML: `html[lang]`, document title, navigational landmarks, main content, headings that reflect structure, descriptive text links and image alt for informative images. No promise that a fixed heading count is a ranking factor.
- Visible meaningful content should be discoverable without requiring interaction, authentication or purely client-side asynchronous fetching when targeting search. Prefer the framework's existing SSR/SSG/static HTML support for crawl-critical content when appropriate. Do not require a framework migration just for SEO.

### Page metadata (one source of truth)

- Give each public indexable page a concise, distinctive, accurate `<title>` and helpful unique `meta name="description"` when appropriate. Google can rewrite titles and snippets; there is no rigid 60-character/160-character rule or promise of exact output.
- Set absolute canonical URL **only after the verified public origin and preferred route are known**. Don't use example.com, localhost, fake hostnames, or canonicalize every distinct page to `/`. Avoid duplicate/conflicting canonicals, trailing slash conflicts and staging canonicals in production. Use redirects when a URL has been permanently replaced and appropriate.
- OG/Twitter metadata is for sharing and presentation, not a direct Google ranking lever; create meaningful `og:title`, `og:description`, image and image alt only with assets actually available. Use public absolute image URLs when required by consuming platforms; never invent an OG asset or claim it was generated.
- For language variants: use real locale/lang values and only add reciprocal hreflang where genuine equivalents exist; do not mark an untranslated page as translated.

### Crawl, index and architecture

- Make intended public routes accessible without login and link them through real navigational links. Keep sensible URL structure, working 200/301/404 status and consistent canonical targets.
- Generate `sitemap.xml` for known, indexable canonical public URLs when meaningful and domain is known. Don't include blocked, private, staging, redirected, noindex or fictional pages. `robots.txt` is not a privacy or noindex mechanism; noindex requires crawler access to be seen. For restricted content use authentication, not robots rules.
- Never globally remove `noindex` or loosen `robots.txt` to boost search presence without identifying why the restriction exists. For staging keep it restricted; for production compare environment configs.

### Structured data

- JSON-LD is **optional and conditional**. Choose a schema type that matches visible page content (e.g. `Person` when an actual person is represented, `Organization` for a real organization, `BreadcrumbList` for real navigation, `Article` for a real article). Verify schema requirements against Google's current feature documentation.
- Never claim fabricated reviews, awards, ratings, employer history, addresses, authorship, social links or achievements. Do not force `ProfilePage` onto every portfolio landing page. Markup is not a guaranteed rich result.
- Validate JSON, URLs, required properties, visible-content alignment. Use Google Rich Results Test for supported types and Schema Markup Validator where appropriate; report which was actually run.

### Performance / inclusive UX

- Preserve readable text, keyboard navigation, accessibility, logical headings and content even in highly expressive styles (glass, neo-brutalism, skeuomorphism).
- Optimize responsive layout, meaningful image dimensions, image formats, important image loading and JS payload. Use Core Web Vitals as diagnostic targets (field data at 75th percentile, where available): LCP <= 2.5 s; INP <= 200 ms; CLS <= 0.1. Values are not a universal 'SEO score'. Don't invent Lighthouse results.
- Never block a useful page behind a full-screen animation, intro overlay or client-only delayed fetch just to match a style. Avoid hiding critical content in CSS-only visual effects; offer text equivalents to media.

## SEO anti-slop and integrity floor

**FLOOR (block until corrected or transparently reported):** private content accidentally indexable; production accidentally noindexed when intended public; fabricated schema identity/reviews/claims; empty main content behind failed JS; contradictory canonicals, broken critical public links and false descriptions; false audit/performance assertions.

**REFLEX (challenge, style or content reason allowed):** duplicate generic titles, keywords crammed into headings, every page using one meta description, boilerplate `best / #1 / top-rated` claims, bloated decorative JS and huge assets, needless schema types, generic keyword-stuffed FAQs, fake 'recent updates' and duplicate thin routes.

**FINISH (improve if applicable):** better internal anchors and snippet clarity, OG images, sitemap completeness, semantic refinement, asset compression and field monitoring plans.

Aesthetics do not alter these requirements. A minimal landing page may have a single title and main section; a brutalist page can keep bold type while still having a usable document outline. Don't add content sections just to satisfy a checklist. Every SEO-generated visible sentence also passes `references/anti-slop-copywriting.md`.

## Workflow and report

1. Determine search applicability and indexable URL set. Record unknown domain/locale as open variables.
2. Inspect existing pages, SSR/rendering, metadata source, robots, sitemap, canonical handling, navigation and content.
3. Implement minimal framework-native SEO changes; do not duplicate scripts/configs or lose forms, routes, actions or visual style.
4. Audit static files with `scripts/seo_audit.py` when HTML output exists. For dynamic sites, also inspect actual rendered/resolved output; static checks cannot establish indexability. If tools are available, verify HTTP status, robots, response headers, canonical consistency and real page rendering.
5. Report **Implemented / Verified / Pending** separately. Do not say Search Console connected, indexed, Core Web Vitals passed or Rich Results valid without evidence.
6. For deployment, recommend site owner verify with Search Console and gather real field/traffic data only after a real domain exists.

## Official source references

- SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Helpful, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- JavaScript SEO: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
- Title links: https://developers.google.com/search/docs/appearance/title-link
- Robots.txt: https://developers.google.com/search/docs/crawling-indexing/robots/intro
- Blocking indexing with noindex: https://developers.google.com/search/docs/crawling-indexing/block-indexing
- Sitemaps: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Structured data: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Core Web Vitals: https://developers.google.com/search/docs/appearance/core-web-vitals
