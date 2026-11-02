# Full-screen hero — acceptance scenarios

Behavior and screenshots must be checked in a real host/browser; static tests only confirm the correct instructions are packaged.

| User prompt / situation | Expected | Failure to catch |
| --- | --- | --- |
| `Build a portfolio website` | Ask one style question; after selection, public full-screen hero + SEO | Agent codes before style choice |
| `Build a Skeuomorphism portfolio` | Read style automatically, implement one-viewport header+hero, SEO; no interview | Half-screen hero, style re-ask |
| `Landing page brutalism hero 1 layar` | Typographic opening viewport, real content; header accounted for | `100vh` *plus* 80px nav (double counted) |
| `Create glass homepage` | Full-screen composition with contrast-safe glass | Overblurred text on a busy background |
| `Create bento portfolio` | Dominant hero and only useful tiles | Filler tiles/cards-inside-cards for 100svh |
| `Buat dashboard privat enterprise` | No marketing hero; preserve functional dashboard layout | Blank fake hero over table |
| `Build a portfolio without a hero; show the work immediately` | No hero; user instruction wins | Forced full-screen intro |
| `Build a page with a 60vh hero` | Honor deliberate compact size | Silently overriding to 100svh |
| Existing site, `ubah warna tombol` | Preserve existing hero size/structure | Unrequested 100svh restyle |
| Mobile toolbar visible at 390×844 | 100svh default, CTA/nav clear | `height:100vh` clips CTA |
| Short mobile 320×568 + long heading | Hero may grow naturally; no hidden content, no horizontal overflow | fixed-height + overflow hidden |
| Desktop 1440×900 header in normal flow | hero `min-height: calc(100svh - realHeaderHeight)` | header+hero accidentally > 1 viewport |
| Overlay header | hero `min-height:100svh` with adequate top padding | double subtraction; heading under nav |
| Landscape + 200% zoom | natural document scroll preserves all content | forced clipping / focus trap |
| Reduced motion | Full hero remains visible/functional with scripts disabled | intro/CTA waits for animation to appear |

### Manual QA expectations

Check common browser widths and short heights, inspect screenshots and DOM measurements, verify header layout mode, toolbar behavior on an actual mobile browser if possible. Pass only those checks actually performed; note untested items plainly.
