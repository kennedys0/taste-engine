#!/usr/bin/env python3
"""
Rebuild docs/index.html with:
1. Zero slop: No arbitrary multi-gradient text, no fake weather/audio widgets. Pure authoritative typography and restrained tactile depth.
2. Zero emojis: Handcrafted, crisp, scalable SVG icons throughout (navigation, tabs, buttons, pipeline, verification).
3. Fully responsive installation guide: Seamlessly stacks/adapts on mobile (< 640px), responsive terminal headers, pre-wrapped code blocks, no overflow cutoffs.
4. Tactile Matte Dark Mode (referenced from charcoal chassis + soft inset/elevated depth) with guaranteed WCAG AA contrast coupling.
5. Official assets: assets/logo.webp and assets/banner.webp cleanly integrated.
6. 100% clean English documentation.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_FILE = ROOT / "docs" / "index.html"

content = INDEX_FILE.read_text(encoding="utf-8")

# Extract the existing CSS rules for styles 1 to 10
style_rules_match = re.search(r'(/\* =========================================================\s*STYLE 1: BENTO GRID.*?\*/.*?)(?=\s*</style>)', content, re.DOTALL)
if not style_rules_match:
    raise SystemExit("ERROR: could not locate style 1-10 CSS block in docs/index.html")
style_css_block = style_rules_match.group(1)

# Extract the 10 showcase card articles
cards_match = re.search(r'(<article class="showcase-card" data-style="bento">.*?</article>\s*<!-- 10\. SWISS / EDITORIAL -->\s*<article class="showcase-card" data-style="swiss-editorial">.*?</article>)', content, re.DOTALL)
if not cards_match:
    raise SystemExit("ERROR: could not locate 10 showcase cards in docs/index.html")
showcase_cards_html = cards_match.group(1)

new_html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Taste Engine — Frontend Design Intelligence for AI Agents</title>
  <meta name="description" content="10 curated frontend aesthetic archetypes with paired Dark/Light mode contrast safety (WCAG AA), mathematical tokens, and anti-slop quality gates for AI agents.">
  <link rel="icon" type="image/webp" href="assets/logo.webp">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    /* =========================================================
       CODEX-INSPIRED SLATE GREY DESIGN TOKENS (NON-PITCH-BLACK)
       ========================================================= */
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    
    html {{
      scroll-behavior: smooth;
    }}

    :root {{
      /* Dark Theme (Codex / ChatGPT Neutral Slate-Grey Palette) */
      --shell-bg: #212328;
      --shell-surface: #2b2e36;
      --shell-surface-elevated: #343842;
      --shell-surface-hover: #3d424e;
      --shell-well-bg: #1a1c21;
      --shell-border: rgba(255, 255, 255, 0.12);
      --shell-border-subtle: rgba(255, 255, 255, 0.06);
      --shell-border-focus: #10b981;
      
      --shell-text: #f3f4f6;
      --shell-text-muted: #a6adbb;
      --shell-text-dim: #717887;
      
      /* Codex Emerald Accent Tokens */
      --shell-accent: #10b981;
      --shell-accent-hover: #059669;
      --shell-accent-subtle: rgba(16, 185, 129, 0.14);
      --shell-accent-border: rgba(16, 185, 129, 0.35);

      /* Tactile Elevation Profiles */
      --shell-shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.22);
      --shell-shadow-card: 0 4px 14px rgba(0, 0, 0, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.06);
      --shell-shadow-elevated: 0 10px 28px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.08);
      --shell-well-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.35);
      --shell-specular-bevel: inset 0 1px 0 rgba(255, 255, 255, 0.08);

      --shell-font: 'Inter', system-ui, -apple-system, sans-serif;
      --shell-font-mono: 'JetBrains Mono', monospace;
      --shell-radius-sm: 8px;
      --shell-radius: 14px;
      --shell-radius-lg: 20px;
      --shell-radius-pill: 9999px;
      
      transition: background-color 180ms ease, color 180ms ease;
    }}

    [data-theme="light"] {{
      --shell-bg: #f7f7f8;
      --shell-surface: #ffffff;
      --shell-surface-elevated: #f0f0f2;
      --shell-surface-hover: #e3e3e8;
      --shell-well-bg: #ededf0;
      --shell-border: rgba(0, 0, 0, 0.10);
      --shell-border-subtle: rgba(0, 0, 0, 0.05);
      --shell-border-focus: #059669;

      --shell-text: #202123;
      --shell-text-muted: #565869;
      --shell-text-dim: #8e8ea0;

      --shell-accent: #059669;
      --shell-accent-hover: #047857;
      --shell-accent-subtle: rgba(5, 150, 105, 0.10);
      --shell-accent-border: rgba(5, 150, 105, 0.30);

      --shell-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
      --shell-shadow-card: 0 2px 8px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
      --shell-shadow-elevated: 0 10px 25px rgba(0, 0, 0, 0.08);
      --shell-well-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.06);
      --shell-specular-bevel: inset 0 1px 0 rgba(255, 255, 255, 0.9);
    }}

    body {{
      background-color: var(--shell-bg);
      color: var(--shell-text);
      font-family: var(--shell-font);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }}

    /* SVG Icon Helper */
    .icon {{
      display: inline-block;
      width: 1em;
      height: 1em;
      stroke-width: 0;
      stroke: currentColor;
      fill: currentColor;
      flex-shrink: 0;
      vertical-align: -0.125em;
    }}
    .icon-stroke {{
      fill: none;
      stroke: currentColor;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
    }}

    /* =========================================================
       TOP STICKY NAVIGATION
       ========================================================= */
    .top-nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(33, 35, 40, 0.90);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--shell-border);
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}

    [data-theme="light"] .top-nav {{
      background: rgba(247, 247, 248, 0.92);
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }}

    .brand-title {{
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      font-weight: 700;
      font-size: 1.05rem;
      letter-spacing: -0.02em;
      color: var(--shell-text);
      text-decoration: none;
    }}

    .brand-logo-img {{
      width: 28px;
      height: 28px;
      object-fit: contain;
      border-radius: 6px;
    }}

    .brand-badge {{
      font-size: 0.7rem;
      font-weight: 600;
      padding: 1px 7px;
      border-radius: var(--shell-radius-pill);
      background: var(--shell-accent-subtle);
      color: var(--shell-accent);
      border: 1px solid var(--shell-accent-border);
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 1.5rem;
      list-style: none;
    }}

    .nav-links a {{
      color: var(--shell-text-muted);
      text-decoration: none;
      font-size: 0.875rem;
      font-weight: 500;
      transition: color 140ms ease;
    }}

    .nav-links a:hover {{
      color: var(--shell-text);
    }}

    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .theme-toggle-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      background: var(--shell-surface);
      color: var(--shell-text);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius-pill);
      padding: 0.4rem 0.85rem;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      box-shadow: var(--shell-shadow-sm);
      transition: all 140ms ease;
    }}

    .theme-toggle-btn:hover {{
      background: var(--shell-surface-elevated);
      border-color: var(--shell-border-focus);
    }}

    .gh-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      background: var(--shell-surface);
      color: var(--shell-text);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius-pill);
      padding: 0.4rem 0.85rem;
      font-size: 0.8rem;
      font-weight: 600;
      text-decoration: none;
      box-shadow: var(--shell-shadow-sm);
      transition: all 140ms ease;
    }}

    .gh-btn:hover {{
      background: var(--shell-surface-elevated);
      border-color: var(--shell-border-focus);
    }}

    /* =========================================================
       HERO BANNER
       ========================================================= */
    .hero-banner {{
      max-width: 1120px;
      margin: 3rem auto 2.5rem auto;
      padding: 0 1.25rem;
      text-align: center;
    }}

    .hero-badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--shell-surface);
      border: 1px solid var(--shell-border);
      padding: 0.35rem 0.95rem;
      border-radius: var(--shell-radius-pill);
      font-size: 0.785rem;
      font-weight: 600;
      color: var(--shell-text-muted);
      margin-bottom: 1.5rem;
      box-shadow: var(--shell-shadow-sm);
    }}

    .hero-badge-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 6px #10b981;
    }}

    .hero-title {{
      font-size: clamp(2.1rem, 4.5vw, 3.4rem);
      font-weight: 800;
      letter-spacing: -0.035em;
      line-height: 1.15;
      color: var(--shell-text);
      margin-bottom: 1rem;
    }}

    .hero-subtitle {{
      font-size: clamp(0.975rem, 1.8vw, 1.15rem);
      color: var(--shell-text-muted);
      max-width: 740px;
      margin: 0 auto 2rem auto;
      line-height: 1.6;
    }}

    /* Official Brand Banner Frame */
    .hero-banner-frame {{
      max-width: 960px;
      margin: 0 auto 2.5rem auto;
      border-radius: var(--shell-radius);
      overflow: hidden;
      background: var(--shell-surface);
      border: 1px solid var(--shell-border);
      box-shadow: var(--shell-shadow-card);
    }}

    .hero-banner-img {{
      width: 100%;
      height: auto;
      display: block;
      object-fit: cover;
    }}

    /* Quick Install Pill with Clean Well */
    .hero-quick-install {{
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      background: var(--shell-well-bg);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius-pill);
      padding: 0.35rem 0.45rem 0.35rem 1.1rem;
      margin-bottom: 1.75rem;
      box-shadow: var(--shell-well-shadow);
      max-width: 100%;
    }}

    .quick-install-prompt {{
      color: var(--shell-text-dim);
      font-family: var(--shell-font-mono);
      font-size: 0.85rem;
      user-select: none;
    }}

    .quick-install-code {{
      font-family: var(--shell-font-mono);
      font-size: 0.85rem;
      color: var(--shell-text);
      user-select: all;
    }}

    .quick-copy-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: var(--shell-surface-elevated);
      color: var(--shell-text);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius-pill);
      padding: 0.4rem 0.85rem;
      font-size: 0.75rem;
      font-weight: 600;
      cursor: pointer;
      box-shadow: var(--shell-shadow-sm);
      transition: background 120ms ease, border-color 120ms ease;
    }}

    .quick-copy-btn:hover {{
      background: var(--shell-surface-hover);
      border-color: var(--shell-accent);
    }}

    .quick-copy-btn:active {{
      transform: translateY(1px);
    }}

    .hero-cta-group {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.85rem;
      margin-bottom: 3rem;
      flex-wrap: wrap;
    }}

    .cta-primary-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--shell-accent);
      color: #ffffff;
      text-decoration: none;
      padding: 0.75rem 1.6rem;
      border-radius: var(--shell-radius-pill);
      font-weight: 600;
      font-size: 0.9rem;
      box-shadow: 0 2px 8px rgba(99, 102, 241, 0.35);
      transition: background 140ms ease, transform 120ms ease;
    }}

    .cta-primary-btn:hover {{
      background: var(--shell-accent-hover);
      transform: translateY(-1px);
    }}

    .cta-primary-btn:active {{
      transform: translateY(1px);
    }}

    .cta-secondary-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--shell-surface);
      color: var(--shell-text);
      border: 1px solid var(--shell-border);
      text-decoration: none;
      padding: 0.75rem 1.6rem;
      border-radius: var(--shell-radius-pill);
      font-weight: 600;
      font-size: 0.9rem;
      box-shadow: var(--shell-shadow-sm);
      transition: background 140ms ease, border-color 140ms ease, transform 120ms ease;
    }}

    .cta-secondary-btn:hover {{
      background: var(--shell-surface-elevated);
      border-color: var(--shell-accent);
      transform: translateY(-1px);
    }}

    .cta-secondary-btn:active {{
      transform: translateY(1px);
    }}

    /* Key Stats Strip (Solid, Authoritative Typography) */
    .hero-stats-strip {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1rem;
      max-width: 980px;
      margin: 0 auto;
    }}

    .stat-card {{
      background: var(--shell-surface);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius);
      padding: 1.25rem 1rem;
      text-align: center;
      box-shadow: var(--shell-shadow-sm);
    }}

    .stat-num {{
      display: block;
      font-size: 1.65rem;
      font-weight: 800;
      letter-spacing: -0.025em;
      color: var(--shell-text);
      margin-bottom: 0.2rem;
    }}

    .stat-desc {{
      font-size: 0.8rem;
      color: var(--shell-text-muted);
      font-weight: 500;
    }}

    /* =========================================================
       SECTION CONTAINERS & HEADERS
       ========================================================= */
    .content-section {{
      max-width: 1240px;
      margin: 4.5rem auto;
      padding: 0 1.25rem;
      width: 100%;
    }}

    .section-header {{
      text-align: center;
      margin-bottom: 2.75rem;
    }}

    .section-eyebrow {{
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--shell-accent);
      margin-bottom: 0.4rem;
    }}

    .section-title {{
      font-size: clamp(1.75rem, 3.2vw, 2.35rem);
      font-weight: 800;
      letter-spacing: -0.025em;
      color: var(--shell-text);
      margin-bottom: 0.65rem;
    }}

    .section-desc {{
      font-size: 0.975rem;
      color: var(--shell-text-muted);
      max-width: 650px;
      margin: 0 auto;
      line-height: 1.6;
    }}

    /* =========================================================
       SHOWCASE GALLERY
       ========================================================= */
    .filter-bar {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.5rem;
      max-width: 1100px;
      margin: 0 auto 2.25rem auto;
      padding: 0 0.5rem;
    }}

    .filter-chip {{
      background: var(--shell-surface);
      color: var(--shell-text-muted);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius-pill);
      padding: 0.4rem 0.95rem;
      font-size: 0.825rem;
      font-weight: 600;
      cursor: pointer;
      box-shadow: var(--shell-shadow-sm);
      transition: all 140ms ease;
    }}

    .filter-chip:hover {{
      color: var(--shell-text);
      border-color: var(--shell-accent);
    }}

    .filter-chip.active {{
      background: var(--shell-accent);
      color: #ffffff;
      border-color: var(--shell-accent);
    }}

    .gallery-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(540px, 1fr));
      gap: 1.75rem;
    }}

    .showcase-card {{
      background: var(--shell-surface);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shell-shadow-card);
      transition: transform 160ms ease, box-shadow 160ms ease;
    }}

    .showcase-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shell-shadow-elevated);
    }}

    .showcase-header {{
      padding: 1.15rem 1.35rem;
      border-bottom: 1px solid var(--shell-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      background: rgba(0, 0, 0, 0.12);
    }}

    [data-theme="light"] .showcase-header {{
      background: rgba(0, 0, 0, 0.02);
    }}

    .showcase-title-group h2 {{
      font-size: 1.2rem;
      font-weight: 700;
      letter-spacing: -0.01em;
      color: var(--shell-text);
    }}

    .showcase-signature {{
      font-size: 0.785rem;
      color: var(--shell-text-muted);
    }}

    .copy-token-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: var(--shell-surface);
      color: var(--shell-text);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius-pill);
      padding: 0.35rem 0.8rem;
      font-size: 0.75rem;
      font-weight: 600;
      cursor: pointer;
      box-shadow: var(--shell-shadow-sm);
      transition: all 120ms ease;
      white-space: nowrap;
    }}

    .copy-token-btn:hover {{
      background: var(--shell-surface-elevated);
      border-color: var(--shell-accent);
    }}

    .showcase-body {{
      padding: 1.35rem;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}

    /* =========================================================
       PIPELINE / ARCHITECTURE (HOW IT WORKS)
       ========================================================= */
    .pipeline-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
    }}

    .pipeline-card {{
      background: var(--shell-surface);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius);
      padding: 1.75rem 1.35rem;
      position: relative;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shell-shadow-card);
      transition: transform 160ms ease, border-color 160ms ease;
    }}

    .pipeline-card:hover {{
      transform: translateY(-2px);
      border-color: var(--shell-accent-border);
    }}

    .pipeline-step-badge {{
      display: inline-block;
      align-self: flex-start;
      font-size: 0.685rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 2px 8px;
      border-radius: var(--shell-radius-pill);
      background: var(--shell-accent-subtle);
      color: var(--shell-accent);
      border: 1px solid var(--shell-accent-border);
      margin-bottom: 1.25rem;
    }}

    .pipeline-icon-box {{
      width: 44px;
      height: 44px;
      border-radius: 10px;
      background: var(--shell-well-bg);
      border: 1px solid var(--shell-border);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--shell-accent);
      font-size: 1.25rem;
      margin-bottom: 1.15rem;
    }}

    .pipeline-card h3 {{
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: -0.01em;
      color: var(--shell-text);
      margin-bottom: 0.65rem;
    }}

    .pipeline-card p {{
      font-size: 0.85rem;
      color: var(--shell-text-muted);
      line-height: 1.55;
      margin-bottom: 1.15rem;
      flex: 1;
    }}

    .pipeline-features {{
      list-style: none;
      border-top: 1px solid var(--shell-border);
      padding-top: 0.95rem;
    }}

    .pipeline-features li {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.785rem;
      color: var(--shell-text-muted);
      margin-bottom: 0.45rem;
    }}

    .pipeline-features svg {{
      color: #10b981;
      flex-shrink: 0;
    }}

    /* =========================================================
       FULLY RESPONSIVE INSTALLATION GUIDE (MOBILE-FIRST ARCHITECTURE)
       ========================================================= */
    .install-container {{
      max-width: 940px;
      margin: 0 auto;
      width: 100%;
    }}

    /* Responsive Segmented Tabs Bar */
    .install-tabs {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 0.45rem;
      margin-bottom: 1rem;
      background: var(--shell-well-bg);
      border: 1px solid var(--shell-border);
      padding: 0.45rem;
      border-radius: var(--shell-radius);
    }}

    .install-tab-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.45rem;
      background: transparent;
      color: var(--shell-text-muted);
      border: 1px solid transparent;
      border-radius: var(--shell-radius-sm);
      padding: 0.55rem 0.75rem;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      text-align: center;
      transition: background 120ms ease, color 120ms ease;
    }}

    .install-tab-btn:hover {{
      color: var(--shell-text);
      background: var(--shell-surface);
    }}

    .install-tab-btn.active {{
      background: var(--shell-surface);
      color: var(--shell-text);
      border-color: var(--shell-border);
      box-shadow: var(--shell-shadow-sm);
    }}

    .install-tab-btn svg {{
      color: var(--shell-text-dim);
    }}

    .install-tab-btn.active svg {{
      color: var(--shell-accent);
    }}

    /* Installation Terminal Panel */
    .install-panel {{
      display: none;
      background: var(--shell-surface);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius);
      overflow: hidden;
      box-shadow: var(--shell-shadow-card);
    }}

    .install-panel.active {{
      display: block;
      animation: tabFadeIn 180ms ease-out;
    }}

    @keyframes tabFadeIn {{
      from {{ opacity: 0; transform: translateY(3px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .panel-header {{
      background: rgba(0, 0, 0, 0.2);
      border-bottom: 1px solid var(--shell-border);
      padding: 0.75rem 1.15rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      flex-wrap: wrap;
    }}

    [data-theme="light"] .panel-header {{
      background: rgba(0, 0, 0, 0.02);
    }}

    .window-dots {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
    }}

    .dot {{
      width: 9px;
      height: 9px;
      border-radius: 50%;
    }}

    .dot-red {{ background: #ef4444; }}
    .dot-yellow {{ background: #f59e0b; }}
    .dot-green {{ background: #10b981; }}

    .window-title {{
      font-family: var(--shell-font-mono);
      font-size: 0.785rem;
      color: var(--shell-text-muted);
      font-weight: 500;
      flex: 1;
      min-width: 140px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .copy-cmd-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: var(--shell-surface-elevated);
      color: var(--shell-text);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius-pill);
      padding: 0.3rem 0.75rem;
      font-size: 0.75rem;
      font-weight: 600;
      cursor: pointer;
      box-shadow: var(--shell-shadow-sm);
      transition: all 120ms ease;
      flex-shrink: 0;
    }}

    .copy-cmd-btn:hover {{
      background: var(--shell-surface-hover);
      border-color: var(--shell-accent);
    }}

    .copy-cmd-btn:active {{
      transform: translateY(1px);
    }}

    /* Pre-wrapped, Mobile-safe Terminal Code Container */
    .terminal-body {{
      padding: 1.25rem;
      font-family: var(--shell-font-mono);
      font-size: 0.85rem;
      line-height: 1.7;
      color: var(--shell-text);
      background: var(--shell-well-bg);
      box-shadow: var(--shell-well-shadow);
      margin: 0;
      overflow-x: auto;
      white-space: pre-wrap;
      word-break: break-all;
    }}

    .terminal-body code {{
      font-family: inherit;
    }}

    .panel-footer-note {{
      border-top: 1px solid var(--shell-border);
      padding: 0.95rem 1.25rem;
      background: var(--shell-surface);
      font-size: 0.825rem;
      color: var(--shell-text-muted);
      line-height: 1.55;
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
    }}

    .panel-footer-note svg {{
      color: var(--shell-accent);
      flex-shrink: 0;
      margin-top: 2px;
    }}

    .panel-footer-note code {{
      font-family: var(--shell-font-mono);
      font-size: 0.785rem;
      background: var(--shell-well-bg);
      border: 1px solid var(--shell-border);
      padding: 1px 6px;
      border-radius: 4px;
      color: var(--shell-text);
    }}

    /* Responsive CLI Verification Box */
    .cli-verify-card {{
      margin-top: 1.75rem;
      background: var(--shell-surface);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius);
      padding: 1.25rem 1.35rem;
      display: flex;
      align-items: center;
      gap: 1.15rem;
      box-shadow: var(--shell-shadow-card);
    }}

    .verify-icon-box {{
      width: 44px;
      height: 44px;
      border-radius: 10px;
      background: var(--shell-accent-subtle);
      border: 1px solid var(--shell-accent-border);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--shell-accent);
      flex-shrink: 0;
    }}

    .verify-text h4 {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--shell-text);
      margin-bottom: 0.25rem;
    }}

    .verify-text p {{
      font-size: 0.825rem;
      color: var(--shell-text-muted);
      margin-bottom: 0.5rem;
    }}

    .inline-code {{
      display: inline-block;
      font-family: var(--shell-font-mono);
      font-size: 0.8rem;
      background: var(--shell-well-bg);
      border: 1px solid var(--shell-border);
      padding: 3px 10px;
      border-radius: 6px;
      color: var(--shell-accent);
      font-weight: 600;
      word-break: break-all;
    }}

    /* =========================================================
       FAQ ACCORDION
       ========================================================= */
    .faq-container {{
      max-width: 860px;
      margin: 0 auto;
      width: 100%;
    }}

    .faq-accordion {{
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }}

    .faq-item {{
      background: var(--shell-surface);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius);
      overflow: hidden;
      box-shadow: var(--shell-shadow-sm);
      transition: border-color 140ms ease;
    }}

    .faq-item:hover {{
      border-color: var(--shell-accent-border);
    }}

    .faq-item.open {{
      border-color: var(--shell-accent);
    }}

    .faq-question {{
      width: 100%;
      background: none;
      border: none;
      padding: 1.15rem 1.35rem;
      text-align: left;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      font-size: 0.975rem;
      font-weight: 600;
      color: var(--shell-text);
      cursor: pointer;
      font-family: inherit;
    }}

    .faq-chevron {{
      color: var(--shell-text-dim);
      flex-shrink: 0;
      transition: transform 200ms ease, color 140ms ease;
    }}

    .faq-item.open .faq-chevron {{
      transform: rotate(180deg);
      color: var(--shell-accent);
    }}

    .faq-answer {{
      max-height: 0;
      overflow: hidden;
      transition: max-height 240ms ease-out;
    }}

    .faq-answer-inner {{
      padding: 0 1.35rem 1.25rem 1.35rem;
      color: var(--shell-text-muted);
      font-size: 0.9rem;
      line-height: 1.6;
    }}

    .faq-answer-inner p:not(:last-child) {{
      margin-bottom: 0.65rem;
    }}

    .faq-answer-inner code {{
      font-family: var(--shell-font-mono);
      font-size: 0.8rem;
      background: var(--shell-well-bg);
      border: 1px solid var(--shell-border);
      padding: 2px 6px;
      border-radius: 4px;
      color: var(--shell-text);
    }}

    /* =========================================================
       DESIGN TOKEN CHEATSHEET
       ========================================================= */
    .token-ref-card {{
      background: var(--shell-surface);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius);
      overflow: hidden;
      box-shadow: var(--shell-shadow-card);
    }}

    .token-table-wrap {{
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }}

    .token-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.85rem;
      min-width: 600px;
    }}

    .token-table th {{
      background: rgba(0, 0, 0, 0.18);
      border-bottom: 1px solid var(--shell-border);
      padding: 0.95rem 1.25rem;
      font-weight: 700;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--shell-text-muted);
    }}

    [data-theme="light"] .token-table th {{
      background: rgba(0, 0, 0, 0.02);
    }}

    .token-table td {{
      padding: 0.95rem 1.25rem;
      border-bottom: 1px solid var(--shell-border);
      vertical-align: middle;
    }}

    .token-table tr:last-child td {{
      border-bottom: none;
    }}

    .token-table code {{
      font-family: var(--shell-font-mono);
      font-size: 0.8rem;
      color: var(--shell-accent);
      background: var(--shell-accent-subtle);
      padding: 2px 7px;
      border-radius: 5px;
      border: 1px solid var(--shell-accent-border);
    }}

    .boilerplate-box {{
      border-top: 1px solid var(--shell-border);
      background: var(--shell-well-bg);
    }}

    .boilerplate-header {{
      padding: 0.85rem 1.25rem;
      border-bottom: 1px solid var(--shell-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      font-size: 0.825rem;
      font-weight: 600;
    }}

    /* =========================================================
       FOOTER
       ========================================================= */
    .site-footer {{
      margin-top: 5.5rem;
      background: var(--shell-surface);
      border-top: 1px solid var(--shell-border);
      padding: 4rem 1.5rem 2rem 1.5rem;
    }}

    .footer-inner {{
      max-width: 1140px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 2.5rem;
      margin-bottom: 3rem;
    }}

    .footer-tagline {{
      font-size: 0.875rem;
      color: var(--shell-text-muted);
      margin: 0.85rem 0;
      line-height: 1.55;
      max-width: 360px;
    }}

    .footer-credit {{
      font-size: 0.8rem;
      color: var(--shell-text-muted);
    }}

    .footer-credit a {{
      color: var(--shell-accent);
      text-decoration: none;
      font-weight: 600;
    }}

    .footer-col h4 {{
      font-size: 0.825rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 1.15rem;
      color: var(--shell-text);
    }}

    .footer-col ul {{
      list-style: none;
    }}

    .footer-col ul li {{
      margin-bottom: 0.55rem;
    }}

    .footer-col ul a {{
      color: var(--shell-text-muted);
      text-decoration: none;
      font-size: 0.85rem;
      transition: color 120ms ease;
    }}

    .footer-col ul a:hover {{
      color: var(--shell-text);
    }}

    .footer-bottom {{
      max-width: 1140px;
      margin: 0 auto;
      padding-top: 1.75rem;
      border-top: 1px solid var(--shell-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      font-size: 0.8rem;
      color: var(--shell-text-dim);
    }}

    .back-to-top-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      color: var(--shell-text-muted);
      text-decoration: none;
      font-weight: 500;
      transition: color 120ms ease;
    }}

    .back-to-top-btn:hover {{
      color: var(--shell-accent);
    }}

    /* =========================================================
       RESPONSIVE BREAKPOINTS (FLUID & COMPACT MOBILE TYPOGRAPHY)
       Scales down typography, padding, and layout to prevent bloating
       ========================================================= */
    @media (max-width: 1024px) {{
      .pipeline-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .hero-stats-strip {{ grid-template-columns: repeat(2, 1fr); }}
      .footer-inner {{ grid-template-columns: 1fr 1fr; gap: 2rem; }}
      .gallery-grid {{ grid-template-columns: 1fr; }}
    }}

    @media (max-width: 768px) {{
      .top-nav {{ padding: 0.65rem 1rem; }}
      .nav-links {{ display: none; }}
      .brand-title {{ font-size: 0.95rem; }}
      .brand-logo-img {{ width: 24px; height: 24px; }}
      .brand-badge {{ font-size: 0.65rem; padding: 1px 6px; }}
      .theme-toggle-btn, .gh-btn {{ padding: 0.35rem 0.75rem; font-size: 0.75rem; }}

      .hero-banner {{ margin: 2rem auto 1.5rem auto; padding: 0 1rem; }}
      .hero-badge-pill {{ font-size: 0.725rem; padding: 0.3rem 0.75rem; margin-bottom: 1.15rem; }}
      .hero-title {{ font-size: clamp(1.65rem, 5.5vw, 2.35rem); letter-spacing: -0.025em; line-height: 1.2; margin-bottom: 0.75rem; }}
      .hero-subtitle {{ font-size: 0.925rem; line-height: 1.5; margin-bottom: 1.4rem; }}

      .hero-quick-install {{
        border-radius: var(--shell-radius);
        flex-direction: column;
        align-items: flex-start;
        padding: 0.65rem 0.85rem;
        gap: 0.45rem;
        width: 100%;
      }}
      .quick-install-code {{ font-size: 0.785rem; word-break: break-all; }}
      .quick-copy-btn {{ align-self: flex-end; padding: 0.35rem 0.75rem; font-size: 0.725rem; }}

      .hero-cta-group {{ flex-direction: column; width: 100%; gap: 0.65rem; margin-bottom: 2rem; }}
      .cta-primary-btn, .cta-secondary-btn {{ width: 100%; justify-content: center; padding: 0.7rem 1.25rem; font-size: 0.85rem; }}

      .hero-stats-strip {{ gap: 0.65rem; }}
      .stat-card {{ padding: 0.85rem 0.65rem; }}
      .stat-num {{ font-size: 1.35rem; }}
      .stat-desc {{ font-size: 0.75rem; }}

      .content-section {{ margin: 3rem auto; padding: 0 1rem; }}
      .section-header {{ margin-bottom: 2rem; }}
      .section-eyebrow {{ font-size: 0.7rem; }}
      .section-title {{ font-size: 1.5rem; letter-spacing: -0.02em; }}
      .section-desc {{ font-size: 0.875rem; line-height: 1.5; }}

      .filter-bar {{ gap: 0.4rem; margin-bottom: 1.75rem; }}
      .filter-chip {{ padding: 0.35rem 0.8rem; font-size: 0.775rem; }}

      .showcase-header {{ padding: 0.9rem 1.1rem; }}
      .showcase-title-group h2 {{ font-size: 1.05rem; }}
      .showcase-signature {{ font-size: 0.75rem; }}
      .showcase-body {{ padding: 1.15rem; }}
      .swiss-headline {{ font-size: 1.35rem; line-height: 1.2; }}

      .pipeline-card {{ padding: 1.35rem 1.1rem; }}
      .pipeline-icon-box {{ width: 38px; height: 38px; font-size: 1.1rem; margin-bottom: 0.9rem; }}
      .pipeline-card h3 {{ font-size: 1rem; }}
      .pipeline-card p {{ font-size: 0.825rem; line-height: 1.5; }}
      .pipeline-features li {{ font-size: 0.75rem; }}

      .install-tabs {{ grid-template-columns: repeat(2, 1fr); gap: 0.35rem; }}
      .install-tab-btn {{ padding: 0.5rem 0.65rem; font-size: 0.75rem; }}
      .panel-header {{ padding: 0.65rem 0.95rem; }}
      .window-title {{ font-size: 0.75rem; }}
      .copy-cmd-btn {{ padding: 0.28rem 0.65rem; font-size: 0.725rem; }}
      .terminal-body {{ font-size: 0.775rem; padding: 1rem; line-height: 1.6; }}
      .panel-footer-note {{ padding: 0.85rem 1rem; font-size: 0.785rem; }}
      .cli-verify-card {{ flex-direction: column; align-items: flex-start; padding: 1.1rem; gap: 0.85rem; }}
      .verify-icon-box {{ width: 38px; height: 38px; }}
      .verify-text h4 {{ font-size: 0.9rem; }}
      .verify-text p {{ font-size: 0.8rem; }}
      .inline-code {{ font-size: 0.75rem; }}

      .faq-question {{ padding: 1rem 1.15rem; font-size: 0.9rem; }}
      .faq-answer-inner {{ padding: 0 1.15rem 1rem 1.15rem; font-size: 0.835rem; }}

      .token-table th, .token-table td {{ padding: 0.8rem 1rem; font-size: 0.8rem; }}
      .boilerplate-header {{ padding: 0.75rem 1rem; font-size: 0.785rem; }}

      .footer-inner {{ grid-template-columns: 1fr; gap: 1.75rem; }}
      .site-footer {{ margin-top: 3.5rem; padding: 3rem 1rem 1.5rem 1rem; }}
      .footer-tagline {{ font-size: 0.825rem; }}
      .footer-col h4 {{ font-size: 0.785rem; margin-bottom: 0.85rem; }}
      .footer-col ul a {{ font-size: 0.8rem; }}
    }}

    @media (max-width: 480px) {{
      .hero-title {{ font-size: 1.4rem; line-height: 1.22; }}
      .hero-subtitle {{ font-size: 0.825rem; }}
      .hero-stats-strip {{ grid-template-columns: 1fr 1fr; gap: 0.45rem; }}
      .stat-card {{ padding: 0.75rem 0.5rem; }}
      .stat-num {{ font-size: 1.2rem; }}
      .stat-desc {{ font-size: 0.7rem; }}

      .section-title {{ font-size: 1.25rem; }}
      .section-desc {{ font-size: 0.8125rem; }}

      .pipeline-grid {{ grid-template-columns: 1fr; }}
      .install-tabs {{ grid-template-columns: 1fr; }}
      .panel-header {{ flex-direction: column; align-items: flex-start; gap: 0.45rem; }}
      .copy-cmd-btn {{ align-self: flex-end; }}
      .terminal-body {{ font-size: 0.725rem; padding: 0.85rem; }}

      .showcase-header {{ flex-direction: column; align-items: flex-start; gap: 0.5rem; }}
      .copy-token-btn {{ align-self: flex-start; }}

      .faq-question {{ font-size: 0.85rem; padding: 0.85rem 0.95rem; }}
      .faq-answer-inner {{ font-size: 0.8rem; padding: 0 0.95rem 0.85rem 0.95rem; }}

      .footer-bottom {{ flex-direction: column; text-align: center; gap: 0.65rem; font-size: 0.75rem; }}
    }}

    /* Toast Notification */
    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--shell-surface-elevated);
      color: var(--shell-text);
      border: 1px solid var(--shell-border-focus);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
      padding: 10px 18px;
      border-radius: var(--shell-radius-pill);
      font-size: 0.825rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      opacity: 0;
      transform: translateY(10px);
      transition: opacity 180ms ease, transform 180ms ease;
      pointer-events: none;
      z-index: 1000;
    }}
    .toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}

    /* =========================================================
       10 SHOWCASE STYLES CSS RECIPES
       ========================================================= */
{style_css_block}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation -->
  <header class="top-nav">
    <div class="brand-group">
      <a href="#" class="brand-title">
        <img src="assets/logo.webp" alt="Taste Engine Logo" class="brand-logo-img">
        <span>Taste Engine</span>
        <span class="brand-badge">v0.10.5</span>
      </a>
    </div>
    
    <nav class="nav-links" aria-label="Main Navigation">
      <a href="#showcase">Showcase</a>
      <a href="#how-it-works">How It Works</a>
      <a href="#installation">Installation</a>
      <a href="#faq">FAQ</a>
      <a href="#tokens">Tokens</a>
    </nav>

    <div class="nav-actions">
      <button id="themeToggle" class="theme-toggle-btn" aria-label="Toggle Theme">
        <svg id="themeIcon" class="icon icon-stroke" width="15" height="15" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
        <span id="themeLabel">Light Mode</span>
      </button>
      <a href="https://github.com/kennedys0/taste-engine" target="_blank" rel="noopener" class="gh-btn" aria-label="GitHub Repository">
        <svg class="icon" width="15" height="15" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
        <span>GitHub</span>
      </a>
    </div>
  </header>

  <!-- Hero Banner -->
  <section class="hero-banner">
    <div class="hero-badge-pill">
      <span class="hero-badge-dot"></span>
      <span>10 Curated Aesthetics · Zero AI-Slop · 100% Contrast Safe (WCAG AA)</span>
    </div>
    
    <h1 class="hero-title">
      Frontend Design Intelligence<br>
      for Autonomous AI Agents
    </h1>
    
    <p class="hero-subtitle">
      Taste Engine equips Antigravity, Claude Code, and OpenAI Codex with 10 distinctive aesthetic archetypes, mathematical token scales, and paired dark/light mode contrast gating.
    </p>

    <!-- Official Brand Banner Frame -->
    <div class="hero-banner-frame">
      <img src="assets/banner.webp" alt="Taste Engine Official Banner" class="hero-banner-img">
    </div>

    <!-- Quick 1-click Install Pill -->
    <div class="hero-quick-install">
      <span class="quick-install-prompt">$</span>
      <code class="quick-install-code" id="heroInstallCmd">npx skills add kennedys0/taste-engine</code>
      <button class="quick-copy-btn" id="heroCopyBtn" title="Copy install command" aria-label="Copy install command">
        <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
        <span>Copy</span>
      </button>
    </div>

    <!-- CTA Group -->
    <div class="hero-cta-group">
      <a href="#showcase" class="cta-primary-btn">
        <span>Explore 10 Styles</span>
        <svg class="icon-stroke" width="14" height="14" viewBox="0 0 24 24"><path d="M7 13l5 5 5-5M12 6v12"/></svg>
      </a>
      <a href="#installation" class="cta-secondary-btn">
        <span>Installation Guide</span>
        <svg class="icon-stroke" width="14" height="14" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
    </div>

    <!-- Key Stats Strip -->
    <div class="hero-stats-strip">
      <div class="stat-card">
        <span class="stat-num">10</span>
        <span class="stat-desc">Aesthetic Archetypes</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">100%</span>
        <span class="stat-desc">WCAG AA Contrast Gated</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">0</span>
        <span class="stat-desc">AI-Slop Clichés</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">Multi-Agent</span>
        <span class="stat-desc">Antigravity · Claude · Codex</span>
      </div>
    </div>
  </section>

  <!-- =========================================================
       SECTION 1: SHOWCASE GALLERY
       ========================================================= -->
  <section id="showcase" class="content-section">
    <div class="section-header">
      <span class="section-eyebrow">Interactive Gallery</span>
      <h2 class="section-title">Live Material Fidelity Preview</h2>
      <p class="section-desc">Test all 10 styles across dark and light modes. Every component adheres to paired token coupling with guaranteed WCAG AA readability.</p>
    </div>

    <!-- Filter Buttons -->
    <nav class="filter-bar" aria-label="Style pack filters">
      <button class="filter-chip active" data-filter="all">All Styles (10)</button>
      <button class="filter-chip" data-filter="bento">Bento Grid</button>
      <button class="filter-chip" data-filter="brutalism">Brutalism</button>
      <button class="filter-chip" data-filter="claymorphism">Claymorphism</button>
      <button class="filter-chip" data-filter="cockpit">Data Cockpit</button>
      <button class="filter-chip" data-filter="cyberpunk">Cyberpunk</button>
      <button class="filter-chip" data-filter="glassmorphism">Glassmorphism</button>
      <button class="filter-chip" data-filter="minimalist">Minimalist</button>
      <button class="filter-chip" data-filter="retro">Retro Terminal</button>
      <button class="filter-chip" data-filter="skeuomorphism">Skeuomorphism</button>
      <button class="filter-chip" data-filter="swiss-editorial">Swiss Editorial</button>
    </nav>

    <!-- 10 Showcase Cards -->
    <main class="gallery-grid">
{showcase_cards_html}
    </main>
  </section>

  <!-- =========================================================
       SECTION 2: HOW IT WORKS / PIPELINE ARCHITECTURE
       ========================================================= -->
  <section id="how-it-works" class="content-section">
    <div class="section-header">
      <span class="section-eyebrow">Architecture Flow</span>
      <h2 class="section-title">How Taste Engine Works</h2>
      <p class="section-desc">From a user prompt to a production-grade interface — here is the 4-phase transformation pipeline executed by your AI agent.</p>
    </div>

    <div class="pipeline-grid">
      <!-- Step 1 -->
      <div class="pipeline-card">
        <span class="pipeline-step-badge">Phase 01</span>
        <div class="pipeline-icon-box">
          <svg class="icon-stroke" width="22" height="22" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M22 12h-4M6 12H2M12 6V2M12 22v-4"/></svg>
        </div>
        <h3>Archetype Discovery</h3>
        <p>The agent inspects project context, domain, and user persona. It maps requirements to the optimal visual archetype (e.g. Fintech → Data Cockpit, Dev Tools → Retro Terminal or Swiss Editorial) before writing UI code.</p>
        <ul class="pipeline-features">
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Context-to-aesthetic mapping</span>
          </li>
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Persona & tone calibration</span>
          </li>
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Eliminates generic blue templates</span>
          </li>
        </ul>
      </div>

      <!-- Step 2 -->
      <div class="pipeline-card">
        <span class="pipeline-step-badge">Phase 02</span>
        <div class="pipeline-icon-box">
          <svg class="icon-stroke" width="22" height="22" viewBox="0 0 24 24"><path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/></svg>
        </div>
        <h3>Mathematical Tokens</h3>
        <p>Injects structured design tokens: calibrated typographic ratios, strict 4px/8px spatial rhythm, specific border radii, and predictable CSS variables instead of arbitrary inline styles.</p>
        <ul class="pipeline-features">
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Strict font & scale pairings</span>
          </li>
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Consistent shadow elevations</span>
          </li>
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Standardized CSS variables</span>
          </li>
        </ul>
      </div>

      <!-- Step 3 -->
      <div class="pipeline-card">
        <span class="pipeline-step-badge">Phase 03</span>
        <div class="pipeline-icon-box">
          <svg class="icon-stroke" width="22" height="22" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 1 0 20z"/></svg>
        </div>
        <h3>Paired Dark/Light Coupling</h3>
        <p>Background, surface, ink (text), and border tokens invert in mathematically synchronized pairs. Completely prevents contrast collisions such as black text on dark surfaces or white on white.</p>
        <ul class="pipeline-features">
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Guaranteed WCAG AA (min 4.5:1)</span>
          </li>
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Automatic [data-theme] inversion</span>
          </li>
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Zero manual color patching</span>
          </li>
        </ul>
      </div>

      <!-- Step 4 -->
      <div class="pipeline-card">
        <span class="pipeline-step-badge">Phase 04</span>
        <div class="pipeline-icon-box">
          <svg class="icon-stroke" width="22" height="22" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
        </div>
        <h3>Anti-Slop Quality Gate</h3>
        <p>Before delivering code, the agent validates the UI against the 7 Universal Quality Gates: no floating ungrounded cards, no generic AI glow halos, no meaningless glassmorphism, and full state completeness.</p>
        <ul class="pipeline-features">
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Bans repetitive AI cliches</span>
          </li>
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Enforces hover & active states</span>
          </li>
          <li>
            <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            <span>Production-ready clean CSS</span>
          </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- =========================================================
       SECTION 3: FULLY RESPONSIVE INSTALLATION GUIDE
       ========================================================= -->
  <section id="installation" class="content-section">
    <div class="section-header">
      <span class="section-eyebrow">Installation</span>
      <h2 class="section-title">Install in Seconds</h2>
      <p class="section-desc">Select your target AI Agent environment below to get the single-line installation command.</p>
    </div>

    <div class="install-container">
      <!-- Responsive Segmented Tabs Bar -->
      <div class="install-tabs" role="tablist" aria-label="Installation agent targets">
        <button class="install-tab-btn active" data-tab="antigravity" role="tab" aria-selected="true">
          <svg class="icon-stroke" width="14" height="14" viewBox="0 0 24 24"><path d="M4 17l6-6-6-6M12 19h8"/></svg>
          <span>Antigravity IDE</span>
        </button>
        <button class="install-tab-btn" data-tab="agy" role="tab" aria-selected="false">
          <svg class="icon-stroke" width="14" height="14" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          <span>Antigravity CLI</span>
        </button>
        <button class="install-tab-btn" data-tab="claude" role="tab" aria-selected="false">
          <svg class="icon-stroke" width="14" height="14" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4M8 16h0M16 16h0"/></svg>
          <span>Claude Code</span>
        </button>
        <button class="install-tab-btn" data-tab="codex" role="tab" aria-selected="false">
          <svg class="icon-stroke" width="14" height="14" viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
          <span>Codex / Copilot</span>
        </button>
        <button class="install-tab-btn" data-tab="skills-cli" role="tab" aria-selected="false">
          <svg class="icon-stroke" width="14" height="14" viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
          <span>Skills CLI</span>
        </button>
        <button class="install-tab-btn" data-tab="standalone" role="tab" aria-selected="false">
          <svg class="icon-stroke" width="14" height="14" viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
          <span>Single Style</span>
        </button>
      </div>

      <!-- Tab Panels -->
      <div class="install-tab-content">
        <!-- 1. Antigravity IDE -->
        <div class="install-panel active" id="panel-antigravity">
          <div class="panel-header">
            <div class="window-dots">
              <span class="dot dot-red"></span>
              <span class="dot dot-yellow"></span>
              <span class="dot dot-green"></span>
            </div>
            <span class="window-title">Antigravity IDE — Global or Project Setup</span>
            <button class="copy-cmd-btn" data-target="cmd-antigravity" aria-label="Copy command">
              <svg class="icon-stroke" width="12" height="12" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              <span>Copy</span>
            </button>
          </div>
          <pre class="terminal-body"><code id="cmd-antigravity"># Global install across all Antigravity workspaces:
node bin/taste-engine.mjs install --agent antigravity --global

# OR local install into the current project workspace:
node bin/taste-engine.mjs install --agent antigravity</code></pre>
          <div class="panel-footer-note">
            <svg class="icon-stroke" width="15" height="15" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            <div><strong>Antigravity IDE:</strong> Installed to <code>~/.gemini/config/skills/taste-engine</code>. The IDE discovers the skill automatically. Prompt in chat: <em>"Apply Neo-Brutalism in Dark Mode for this dashboard."</em></div>
          </div>
        </div>

        <!-- 2. Antigravity CLI (agy) -->
        <div class="install-panel" id="panel-agy">
          <div class="panel-header">
            <div class="window-dots">
              <span class="dot dot-red"></span>
              <span class="dot dot-yellow"></span>
              <span class="dot dot-green"></span>
            </div>
            <span class="window-title">Antigravity CLI (agy)</span>
            <button class="copy-cmd-btn" data-target="cmd-agy" aria-label="Copy command">
              <svg class="icon-stroke" width="12" height="12" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              <span>Copy</span>
            </button>
          </div>
          <pre class="terminal-body"><code id="cmd-agy"># Add via Universal Skills CLI:
npx skills add kennedys0/taste-engine

# Verify installed skill in agy CLI:
agy skills list</code></pre>
          <div class="panel-footer-note">
            <svg class="icon-stroke" width="15" height="15" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            <div><strong>CLI Environment:</strong> The <code>agy</code> command line discovers skills registered in user configuration paths or workspace roots.</div>
          </div>
        </div>

        <!-- 3. Claude Code -->
        <div class="install-panel" id="panel-claude">
          <div class="panel-header">
            <div class="window-dots">
              <span class="dot dot-red"></span>
              <span class="dot dot-yellow"></span>
              <span class="dot dot-green"></span>
            </div>
            <span class="window-title">Anthropic Claude Code</span>
            <button class="copy-cmd-btn" data-target="cmd-claude" aria-label="Copy command">
              <svg class="icon-stroke" width="12" height="12" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              <span>Copy</span>
            </button>
          </div>
          <pre class="terminal-body"><code id="cmd-claude"># Installation via Taste Engine installer:
node bin/taste-engine.mjs install --agent claude --global

# OR installation via Skills CLI:
npx skills add kennedys0/taste-engine</code></pre>
          <div class="panel-footer-note">
            <svg class="icon-stroke" width="15" height="15" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            <div><strong>Claude Code:</strong> Installed to <code>~/.claude/skills/taste-engine</code>. Readily loaded by the Claude CLI.</div>
          </div>
        </div>

        <!-- 4. OpenAI Codex / Copilot -->
        <div class="install-panel" id="panel-codex">
          <div class="panel-header">
            <div class="window-dots">
              <span class="dot dot-red"></span>
              <span class="dot dot-yellow"></span>
              <span class="dot dot-green"></span>
            </div>
            <span class="window-title">OpenAI Codex & GitHub Copilot Workspace</span>
            <button class="copy-cmd-btn" data-target="cmd-codex" aria-label="Copy command">
              <svg class="icon-stroke" width="12" height="12" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              <span>Copy</span>
            </button>
          </div>
          <pre class="terminal-body"><code id="cmd-codex"># Global installation for Codex / Copilot:
node bin/taste-engine.mjs install --agent codex --global

# OR project installation:
node bin/taste-engine.mjs install --agent codex</code></pre>
          <div class="panel-footer-note">
            <svg class="icon-stroke" width="15" height="15" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            <div><strong>Codex / Copilot:</strong> Files saved to <code>~/.codex/skills/taste-engine</code> or <code>.agents/skills/taste-engine</code>.</div>
          </div>
        </div>

        <!-- 5. Universal Skills CLI -->
        <div class="install-panel" id="panel-skills-cli">
          <div class="panel-header">
            <div class="window-dots">
              <span class="dot dot-red"></span>
              <span class="dot dot-yellow"></span>
              <span class="dot dot-green"></span>
            </div>
            <span class="window-title">Universal Skills CLI (npx skills)</span>
            <button class="copy-cmd-btn" data-target="cmd-skills-cli" aria-label="Copy command">
              <svg class="icon-stroke" width="12" height="12" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              <span>Copy</span>
            </button>
          </div>
          <pre class="terminal-body"><code id="cmd-skills-cli"># Install the entire Taste Engine pack in one command:
npx skills add kennedys0/taste-engine

# List installed skills on your machine:
npx skills list</code></pre>
          <div class="panel-footer-note">
            <svg class="icon-stroke" width="15" height="15" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            <div><strong>Ecosystem Standard:</strong> Compatible with all agents and hosts adopting the open Agent Skills standard.</div>
          </div>
        </div>

        <!-- 6. Standalone Single Style -->
        <div class="install-panel" id="panel-standalone">
          <div class="panel-header">
            <div class="window-dots">
              <span class="dot dot-red"></span>
              <span class="dot dot-yellow"></span>
              <span class="dot dot-green"></span>
            </div>
            <span class="window-title">Single Standalone Style Installation</span>
            <button class="copy-cmd-btn" data-target="cmd-standalone" aria-label="Copy command">
              <svg class="icon-stroke" width="12" height="12" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              <span>Copy</span>
            </button>
          </div>
          <pre class="terminal-body"><code id="cmd-standalone"># Install only the Cyberpunk HUD style:
npx skills add kennedys0/taste-style-cyberpunk-hud

# Install only the Neo-Brutalism style:
npx skills add kennedys0/taste-style-neo-brutalism

# Install only the Claymorphism style:
npx skills add kennedys0/taste-style-claymorphism

# Install only the Swiss / Editorial style:
npx skills add kennedys0/taste-style-swiss-editorial</code></pre>
          <div class="panel-footer-note">
            <svg class="icon-stroke" width="15" height="15" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            <div><strong>Save Context Tokens:</strong> If your project strictly targets one design language, use standalone packages to minimize context consumption.</div>
          </div>
        </div>
      </div>

      <!-- Offline Gallery Tip -->
      <div class="cli-verify-card">
        <div class="verify-icon-box">
          <svg class="icon-stroke" width="22" height="22" viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
        </div>
        <div class="verify-text">
          <h4>Preview All Styles Offline in Your Browser</h4>
          <p>Run this command in your repository terminal at any time to open this interactive showcase locally:</p>
          <code class="inline-code">node bin/taste-engine.mjs gallery</code>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================================================
       SECTION 4: FAQ ACCORDION (100% CLEAN ENGLISH)
       ========================================================= -->
  <section id="faq" class="content-section">
    <div class="section-header">
      <span class="section-eyebrow">FAQ</span>
      <h2 class="section-title">Frequently Asked Questions</h2>
      <p class="section-desc">Technical answers on framework independence, contrast gating, codebase preservation, and custom styling.</p>
    </div>

    <div class="faq-container">
      <div class="faq-accordion" id="faqAccordion">

        <!-- Question 1 -->
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            <span>What is Taste Engine and why do I need it?</span>
            <svg class="faq-chevron icon-stroke" width="16" height="16" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              <p>By default, AI coding agents generate uniform, repetitive frontend designs (often termed <em>AI-slop</em>): ungrounded floating cards, low-contrast text, purposeless blur effects, and generic blue-purple gradients.</p>
              <p><strong>Taste Engine</strong> is an intelligence skill pack that equips AI agents with 10 distinctive aesthetic archetypes (Bento, Brutalism, Claymorphism, Cockpit, Cyberpunk, Glassmorphism, Minimalism, Retro Terminal, Skeuomorphism, Swiss Editorial) backed by strict quality gates to produce production-grade frontend code.</p>
            </div>
          </div>
        </div>

        <!-- Question 2 -->
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            <span>Is Taste Engine tied to any specific JavaScript UI framework?</span>
            <svg class="faq-chevron icon-stroke" width="16" height="16" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              <p><strong>No. Taste Engine is 100% framework-agnostic.</strong> It injects pure design principles, mathematical tokens, and native CSS recipes.</p>
              <p>You can use it seamlessly with React, Next.js, Vue, Svelte, Nuxt, Astro, HTML/CSS, Tailwind CSS, shadcn/ui, MUI, or any other UI stack.</p>
            </div>
          </div>
        </div>

        <!-- Question 3 -->
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            <span>How does Taste Engine prevent contrast collisions in Dark & Light modes?</span>
            <svg class="faq-chevron icon-stroke" width="16" height="16" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              <p>Every style in Taste Engine enforces <strong>Strict Paired Coupling</strong>. Tokens for background, surface, ink (text), and borders are defined as synchronized mathematical pairs.</p>
              <p>When toggling between <code>[data-theme="dark"]</code> and <code>[data-theme="light"]</code>, all token pairs invert symmetrically and are guaranteed to meet minimum <strong>WCAG AA (≥ 4.5:1)</strong> readability standards. Anti-slop quality gates explicitly ban dark text on dark surfaces or pale text on light cards.</p>
            </div>
          </div>
        </div>

        <!-- Question 4 -->
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            <span>Will Taste Engine overwrite or conflict with my existing codebase CSS?</span>
            <svg class="faq-chevron icon-stroke" width="16" height="16" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              <p><strong>No.</strong> Taste Engine is non-destructive and additive. All tokens and CSS classes use unique namespaces such as <code>--taste-[style]-*</code>, ensuring zero collision with your global stylesheets.</p>
              <p>Quality gates also instruct the agent to respect existing component architecture and naming conventions in established projects.</p>
            </div>
          </div>
        </div>

        <!-- Question 5 -->
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            <span>Can I install just one specific style instead of the whole bundle?</span>
            <svg class="faq-chevron icon-stroke" width="16" height="16" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              <p><strong>Yes.</strong> Taste Engine provides 10 independent standalone skills in the <code>optional-standalone-skills/</code> directory. You can install each style individually using:</p>
              <code>npx skills add kennedys0/taste-style-[style-name]</code>
              <p style="margin-top:0.5rem;">For example: <code>npx skills add kennedys0/taste-style-cyberpunk-hud</code>. This minimizes token usage if your project only requires a single aesthetic.</p>
            </div>
          </div>
        </div>

        <!-- Question 6 -->
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            <span>How do I verify that Taste Engine is active in my AI Agent?</span>
            <svg class="faq-chevron icon-stroke" width="16" height="16" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              <p>In Antigravity IDE, check your installed skills list or run <code>agy skills list</code> in the CLI.</p>
              <p>To test directly in chat, ask: <em>"Use Taste Engine to review and redesign this card component with a Bento Grid aesthetic."</em> Your agent will recognize the skill and apply its architectural constraints.</p>
            </div>
          </div>
        </div>

        <!-- Question 7 -->
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            <span>Can I customize color tokens or add new custom styles?</span>
            <svg class="faq-chevron icon-stroke" width="16" height="16" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              <p>Yes. You can override CSS custom properties in your stylesheets (for example, overriding <code>--taste-cyber-accent: #00ffcc;</code>).</p>
              <p>To contribute a new aesthetic pack, add a markdown specification in <code>taste-engine/styles/</code> and validate it with our test runner: <code>python taste-engine/scripts/validate-pack.py</code>.</p>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- =========================================================
       SECTION 5: DESIGN TOKEN CHEATSHEET
       ========================================================= */
  <section id="tokens" class="content-section">
    <div class="section-header">
      <span class="section-eyebrow">Design Tokens</span>
      <h2 class="section-title">Standard Token Architecture</h2>
      <p class="section-desc">Every style follows a standardized CSS variable naming convention, easily mapped to Tailwind CSS theme configuration or plain CSS custom properties.</p>
    </div>

    <div class="token-ref-card">
      <div class="token-table-wrap">
        <table class="token-table">
          <thead>
            <tr>
              <th>CSS Variable Pattern</th>
              <th>Semantic Role</th>
              <th>Dark Mode Behavior</th>
              <th>Light Mode Behavior</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>--taste-[style]-bg</code></td>
              <td>Canvas background layer</td>
              <td>Deep matte charcoal / velvety graphite</td>
              <td>Crisp white / soft pale slate tint</td>
            </tr>
            <tr>
              <td><code>--taste-[style]-surface</code></td>
              <td>Card, panel, and modal containers</td>
              <td>Elevated matte surface with subtle bevel</td>
              <td>Clean elevated card with soft rim</td>
            </tr>
            <tr>
              <td><code>--taste-[style]-text</code></td>
              <td>Primary readable typography</td>
              <td>High-contrast crisp white (min 4.5:1)</td>
              <td>High-contrast slate/black (min 4.5:1)</td>
            </tr>
            <tr>
              <td><code>--taste-[style]-muted</code></td>
              <td>Secondary labels & subtitles</td>
              <td>Medium cool grey (accessible contrast)</td>
              <td>Medium slate grey (accessible contrast)</td>
            </tr>
            <tr>
              <td><code>--taste-[style]-border</code></td>
              <td>Card outlines & structural lines</td>
              <td>Subtle translucent white rim</td>
              <td>Subtle translucent dark rim</td>
            </tr>
            <tr>
              <td><code>--taste-[style]-accent</code></td>
              <td>Primary action buttons & indicators</td>
              <td>High-chroma highlight</td>
              <td>Deep, contrast-anchored highlight</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="boilerplate-box">
        <div class="boilerplate-header">
          <span>Quick Starter CSS Boilerplate</span>
          <button class="copy-cmd-btn" data-target="cmd-boilerplate" aria-label="Copy boilerplate">
            <svg class="icon-stroke" width="12" height="12" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span>Copy CSS</span>
          </button>
        </div>
        <pre class="terminal-body"><code id="cmd-boilerplate">/* Root Dark Theme Default (Codex Slate-Grey) */
:root {{
  --app-bg: var(--taste-bento-bg, #212328);
  --app-surface: var(--taste-bento-surface, #2b2e36);
  --app-text: var(--taste-bento-text, #f3f4f6);
  --app-border: var(--taste-bento-border, rgba(255, 255, 255, 0.12));
  --app-accent: var(--taste-bento-accent, #10b981);
}}

/* Light Theme Transition */
[data-theme="light"] {{
  --app-bg: #f7f7f8;
  --app-surface: #ffffff;
  --app-text: #202123;
  --app-border: rgba(0, 0, 0, 0.10);
  --app-accent: #059669;
}}</code></pre>
      </div>
    </div>
  </section>

  <!-- =========================================================
       SITE FOOTER
       ========================================================= -->
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col-brand">
        <div class="brand-group">
          <img src="assets/logo.webp" alt="Taste Engine Logo" class="brand-logo-img">
          <strong style="font-size: 1.05rem; font-weight: 700;">Taste Engine</strong>
          <span class="brand-badge">v0.10.5</span>
        </div>
        <p class="footer-tagline">Open-source frontend design intelligence pack for AI coding agents. Elevate design fidelity, eliminate AI-slop, and enforce contrast safety.</p>
        <p class="footer-credit">Created by <a href="https://github.com/kennedys0" target="_blank" rel="noopener">Mochamad Vikry (@kennedys0)</a></p>
      </div>

      <div class="footer-col">
        <h4>Aesthetic Archetypes</h4>
        <ul>
          <li><a href="#showcase">Bento Grid</a></li>
          <li><a href="#showcase">Neo-Brutalism</a></li>
          <li><a href="#showcase">Claymorphism</a></li>
          <li><a href="#showcase">Data Cockpit</a></li>
          <li><a href="#showcase">Cyberpunk HUD</a></li>
          <li><a href="#showcase">Swiss Editorial</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Navigation & Docs</h4>
        <ul>
          <li><a href="#how-it-works">Architecture Flow</a></li>
          <li><a href="#installation">Installation Guide</a></li>
          <li><a href="#faq">FAQ</a></li>
          <li><a href="#tokens">Design Tokens</a></li>
          <li><a href="https://github.com/kennedys0/taste-engine" target="_blank" rel="noopener">GitHub Repository</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Supported Agents</h4>
        <ul>
          <li><a href="#installation">Google Antigravity IDE</a></li>
          <li><a href="#installation">Antigravity CLI (agy)</a></li>
          <li><a href="#installation">Anthropic Claude Code</a></li>
          <li><a href="#installation">OpenAI Codex / Copilot</a></li>
          <li><a href="#installation">Universal Skills CLI</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <p>© 2026 Mochamad Vikry. Released under the MIT License.</p>
      <a href="#" class="back-to-top-btn">
        <span>Back to top</span>
        <svg class="icon-stroke" width="13" height="13" viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
      </a>
    </div>
  </footer>

  <!-- Toast Notification -->
  <div id="toast" class="toast" role="status" aria-live="polite">
    <svg class="icon-stroke" width="15" height="15" viewBox="0 0 24 24" style="color: #10b981;"><path d="M20 6L9 17l-5-5"/></svg>
    <span id="toastMsg">Command copied to clipboard!</span>
  </div>

  <script>
    // =========================================================
    // 1. THEME TOGGLE LOGIC
    // =========================================================
    const html = document.documentElement;
    const themeBtn = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const themeLabel = document.getElementById('themeLabel');

    const sunSvg = '<circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>';
    const moonSvg = '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>';

    function updateThemeUI(theme) {{
      if (theme === 'light') {{
        html.setAttribute('data-theme', 'light');
        themeIcon.innerHTML = moonSvg;
        themeLabel.textContent = 'Dark Mode';
      }} else {{
        html.setAttribute('data-theme', 'dark');
        themeIcon.innerHTML = sunSvg;
        themeLabel.textContent = 'Light Mode';
      }}
    }}

    themeBtn.addEventListener('click', () => {{
      const current = html.getAttribute('data-theme') || 'dark';
      const next = current === 'dark' ? 'light' : 'dark';
      updateThemeUI(next);
    }});

    // =========================================================
    // 2. SHOWCASE STYLE FILTER
    // =========================================================
    const filterChips = document.querySelectorAll('.filter-chip');
    const cards = document.querySelectorAll('.showcase-card');

    filterChips.forEach(chip => {{
      chip.addEventListener('click', () => {{
        filterChips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        const filter = chip.getAttribute('data-filter');

        cards.forEach(card => {{
          if (filter === 'all' || card.getAttribute('data-style') === filter) {{
            card.style.display = 'flex';
          }} else {{
            card.style.display = 'none';
          }}
        }});
      }});
    }});

    // =========================================================
    // 3. TOAST NOTIFICATION UTILITY
    // =========================================================
    const toast = document.getElementById('toast');
    const toastMsg = document.getElementById('toastMsg');
    let toastTimeout;

    function showToast(text) {{
      toastMsg.textContent = text;
      toast.classList.add('show');
      clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {{
        toast.classList.remove('show');
      }}, 2200);
    }}

    // =========================================================
    // 4. COPY TOKENS BUTTONS
    // =========================================================
    document.querySelectorAll('.copy-token-btn').forEach(btn => {{
      btn.addEventListener('click', async (e) => {{
        e.stopPropagation();
        const tokens = btn.getAttribute('data-tokens');
        try {{
          await navigator.clipboard.writeText(tokens);
          showToast('Copied CSS tokens to clipboard');
        }} catch {{
          showToast('Tokens copied');
        }}
      }});
    }});

    // =========================================================
    // 5. HERO QUICK INSTALL COPY
    // =========================================================
    const heroCopyBtn = document.getElementById('heroCopyBtn');
    const heroInstallCmd = document.getElementById('heroInstallCmd');
    if (heroCopyBtn && heroInstallCmd) {{
      heroCopyBtn.addEventListener('click', async () => {{
        try {{
          await navigator.clipboard.writeText(heroInstallCmd.textContent.trim());
          showToast('Copied installation command');
        }} catch {{
          showToast('Command copied');
        }}
      }});
    }}

    // =========================================================
    // 6. INSTALLATION GUIDE TABS
    // =========================================================
    const tabBtns = document.querySelectorAll('.install-tab-btn');
    const panels = document.querySelectorAll('.install-panel');

    tabBtns.forEach(btn => {{
      btn.addEventListener('click', () => {{
        const targetTab = btn.getAttribute('data-tab');
        
        tabBtns.forEach(b => {{
          b.classList.remove('active');
          b.setAttribute('aria-selected', 'false');
        }});
        panels.forEach(p => p.classList.remove('active'));

        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');
        const targetPanel = document.getElementById('panel-' + targetTab);
        if (targetPanel) {{
          targetPanel.classList.add('active');
        }}
      }});
    }});

    // Generic Copy Command Buttons in Panels & Boilerplate
    document.querySelectorAll('.copy-cmd-btn').forEach(btn => {{
      btn.addEventListener('click', async () => {{
        const targetId = btn.getAttribute('data-target');
        const codeEl = document.getElementById(targetId);
        if (codeEl) {{
          try {{
            await navigator.clipboard.writeText(codeEl.textContent.trim());
            showToast('Copied command to clipboard');
          }} catch {{
            showToast('Copied to clipboard');
          }}
        }}
      }});
    }});

    // =========================================================
    // 7. INTERACTIVE FAQ ACCORDION
    // =========================================================
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {{
      const questionBtn = item.querySelector('.faq-question');
      const answer = item.querySelector('.faq-answer');

      questionBtn.addEventListener('click', () => {{
        const isOpen = item.classList.contains('open');

        // Close other accordion items
        faqItems.forEach(otherItem => {{
          if (otherItem !== item) {{
            otherItem.classList.remove('open');
            otherItem.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
            otherItem.querySelector('.faq-answer').style.maxHeight = null;
          }}
        }});

        if (isOpen) {{
          item.classList.remove('open');
          questionBtn.setAttribute('aria-expanded', 'false');
          answer.style.maxHeight = null;
        }} else {{
          item.classList.add('open');
          questionBtn.setAttribute('aria-expanded', 'true');
          answer.style.maxHeight = answer.scrollHeight + 'px';
        }}
      }});
    }});
  </script>
</body>
</html>
'''

INDEX_FILE.write_text(new_html, encoding="utf-8")
print(f"PASS: successfully updated {INDEX_FILE} ({len(new_html)} bytes)")
