# SEO implementation recipes by stack

**Always inspect project dependencies first.** These are conditional patterns, not mandatory package installations.

## Static HTML

In public pages, use real content, a descriptive `title`, useful `description`, `html lang`, semantic landmarks and real links. When domain is **verified**, add canonical and absolute Open Graph URL. Example skeleton uses placeholders that MUST be replaced before production and MUST NOT be emitted as live facts:

```html
<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Project Name | Available Services</title>
  <meta name="description" content="A factual description of the content on this page.">
  <!-- TODO: Add absolute canonical after verifying real origin and route. -->
</head>
<body>
  <header><nav aria-label="Navigasi utama"><a href="/">Beranda</a></nav></header>
  <main><h1>A heading that reflects the page content</h1><p>Real content, not keyword stuffing.</p></main>
</body>
</html>
```

## Next.js App Router

Use native `metadata`, `generateMetadata` for dynamic route content, `app/sitemap.ts`, and `app/robots.ts` **if required**; avoid installing a duplicate SEO library by default. Set `metadataBase` only with a confirmed origin. A page with private info must not be added to public sitemap. Confirm changes via generated HTML/HTTP after build; metadata TS compile is not a full crawl test.

## Next.js Pages Router

Inspect existing `next/head` conventions; set page-specific head elements and keep only one canonical per route. Where server rendering is available, prefer HTML containing searchable content over a shell requiring JS to fetch the entire page.

## React/Vite SPA

Static index.html may only describe the app shell. For multi-page public content, consider suitable prerender/SSR/static export with the existing toolchain. Don't claim each client-side route is fully crawlable just because the root has one metadata tag. Don't change routing strategy without an impact plan.

## Astro / SvelteKit / Nuxt / Vue

Prefer native head/metadata facilities and SSR/SSG paths already present in the app. Keep locale, canonical, and sitemap behavior consistent with actual router output; check generated pages rather than only source templates.

## WordPress / CMS

Discover the existing SEO plugin and CMS output before adding tags, schema, or redirects. Avoid duplicates and conflicting canonical, robots or sitemap generation. Follow the site's editorial workflow for titles/descriptions.

## SEO validation matrix

| Type | Verify |
|---|---|
| Static HTML | title, meta description, lang, main/H1, link hrefs, image alt, canonical uniqueness |
| Deployment | resolved host/HTTPS, status codes, noindex/robots, canonical & redirects, sitemap reachable |
| Rich results | relevant supported schema, required properties, genuine content; test with Google tools |
| Performance | real Lighthouse or web-vitals measurement; report source, device, date and percentile |
| Redesign | existing content/links/forms/functionality preserved; SEO config unchanged unless requested |

Accessibility and accurate copy are more important than speculative ranking tricks. Do not use an SEO score to substitute for evidence.
