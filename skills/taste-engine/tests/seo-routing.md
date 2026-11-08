# SEO auto-routing / quality acceptance scenarios

Run these in agent/harness tests. `scripts/seo_audit.py` is a **static HTML heuristic**, not Google indexing proof.

| Prompt / context | Expected behavior | Failure |
|---|---|---|
| "Build a portfolio website" no style | Ask one **style** question, stop. After reply implement chosen style **and public SEO baseline** | Interrogate SEO as second unrelated choice; code before style reply |
| "Build an SEO-friendly brutalist portfolio" | Load brutalism + SEO, proceed | Style question; replace brutalism with generic SEO aesthetic |
| "Buat website portfolio skeumorphsm" | Resolve frutiger-aero (variant tactile) + SEO, no question | Incorrect typo handling; missed SEO |
| "Audit SEO landing page sekarang" | Load SEO immediately; audit only | Ask style; redesign without permission |
| "Buat aplikasi dashboard internal" with style | Apply style and privacy/accessibility, don't expose private routes in sitemap | Treat authenticated data as public |
| "Buat APK Android" | No web SEO | Add meta tags to native screen |
| "Fix tombol navbar" existing public site | Preserve SEO and style, fix button | Rebuild metadata unnecessarily |
| "Portfolio site, domain not known yet" | Safe titles/headings and mark canonical/OG URL pending | Invent example.com as real canonical |
| "Staging page with noindex" | Preserve indexability restriction | Remove noindex automatically |
| "Optimize for Google: add 5-star rating schema" no reviews | Reject fabricated markup and explain | Generate fake Review/aggregateRating |
| "Translate Indonesian portfolio to English" | Add hreflang only when actual translated pages/routes exist | Fake translations or inconsistent links |
| "Write SEO for three projects" with no work details | Use TODO for missing evidence rather than false results/metrics | Invent client names/achievements |
| "Glassmorphism portfolio" | Keep glass while making text readable/indexable | Remove style automatically due to SEO |
| "Only private account page" | No public sitemap, no Search Console suggestion required | Expose protected URLs |
| "Build SEO-ready portfolio with real domain provided" | Canonical and sitemap match actual origin/route | localhost canonicals and staging links |

## Runbook

- Verify router is actually invoked by a supported agent; static files alone do not prove discovery.
- Compare source and rendered HTML, then check HTTP headers in staging/production if reachable.
- Run `python3 scripts/seo_audit.py path/to/exported.html --public` for public static output; a passing scan does not prove Google crawling/indexing.
- Record `not checked` for Search Console, field vitals, rich result validation, or live robots access when unavailable.
