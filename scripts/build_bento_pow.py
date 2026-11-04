"""
Generate the overhauled, authentic 1-page Proof of Work (PoW) for Bento Grid (docs/bento.html).
Features:
- Single-viewport fit: Complete Bento Grid fits into 1 desktop viewport (100svh)
- Clean profile: Removed redundant badges ("Available for select projects" & "ONLINE • taste-engine.dev")
- Name: fekojewan (FK avatar initials)
- Email: mail@fekojewan.my.id (punchy #ff5722 pill button)
- Location: Indonesia (live running WIB / GMT+7 clock)
- Non-pitch-black graphite slate (#13151B) with 28px tactile radii
- Horizontal capsule pills row (repeat(7, 1fr))
- Tabbed installation guide, tokens cheatsheet, and FAQ below viewport
"""
from pathlib import Path

OUT_FILE = Path("docs/bento.html")

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bento Grid Proof of Work & Installation Guide — Taste Engine</title>
  <meta name="description" content="Dedicated 1-page Proof of Work for Bento Grid aesthetic archetype. Authentic asymmetric modular cards, non-pitch-black graphite surfaces, two-tone typography, and contrast safety.">
  <link rel="icon" type="image/webp" href="assets/logo.webp">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    /* =========================================================
       BENTO GRID DESIGN SYSTEM TOKENS (REFINED GRAPHITE SLATE)
       ========================================================= */
    :root {
      /* Clean Architectural Light */
      --pow-bg: #f3f4f6;
      --pow-surface: #ffffff;
      --pow-surface-elevated: #e5e7eb;
      --pow-surface-hover: #f9fafb;
      --pow-well-bg: #eaecef;
      --pow-text: #111827;
      --pow-text-muted: #6b7280;
      --pow-border: 1px solid rgba(0, 0, 0, 0.08);
      --pow-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
      --pow-accent-cta: #ff5722;
      --pow-accent-cta-hover: #f4511e;
      --pow-accent-brand: #7c3aed;
      --pow-radius: 28px;
      --pow-radius-pill: 9999px;

      --pow-font-display: 'Space Grotesk', -apple-system, sans-serif;
      --pow-font-body: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --pow-font-mono: 'JetBrains Mono', monospace;
    }

    [data-theme="dark"] {
      /* Refined Matte Graphite Slate — Non-Pitch-Black */
      --pow-bg: #13151b;
      --pow-surface: #1e222b;
      --pow-surface-elevated: #262b36;
      --pow-surface-hover: #2c3240;
      --pow-well-bg: #181b22;
      --pow-text: #f4f4f7;
      --pow-text-muted: #8e95a5;
      --pow-border: 1px solid rgba(255, 255, 255, 0.08);
      --pow-shadow: 0 8px 32px rgba(0, 0, 0, 0.28);
      --pow-accent-cta: #ff5722;
      --pow-accent-cta-hover: #ff7043;
      --pow-accent-brand: #8b5cf6;
      --pow-radius: 28px;
      --pow-radius-pill: 9999px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      background-color: var(--pow-bg);
      color: var(--pow-text);
      font-family: var(--pow-font-body);
      font-size: 15px;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      transition: background-color 150ms ease, color 150ms ease;
    }

    /* Top Navigation (Compact & Functional) */
    .pow-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--pow-surface);
      border-bottom: var(--pow-border);
      padding: 0.6rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      height: 56px;
    }

    .nav-brand-group {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      text-decoration: none;
      color: var(--pow-text);
    }

    .brand-logo-img {
      width: 28px;
      height: 28px;
      object-fit: contain;
      border-radius: 6px;
      display: block;
    }

    .nav-title {
      font-family: var(--pow-font-display);
      font-size: 0.975rem;
      font-weight: 700;
      letter-spacing: -0.02em;
    }

    .nav-tag-badge {
      font-size: 0.7rem;
      font-weight: 600;
      padding: 0.15rem 0.55rem;
      border-radius: var(--pow-radius-pill);
      background: var(--pow-surface-elevated);
      color: var(--pow-accent-brand);
      border: var(--pow-border);
      font-family: var(--pow-font-mono);
    }

    .nav-command-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--pow-surface-elevated);
      border: var(--pow-border);
      border-radius: var(--pow-radius-pill);
      padding: 0.25rem 0.35rem 0.25rem 0.75rem;
      font-size: 0.75rem;
    }

    .nav-cmd-code {
      font-family: var(--pow-font-mono);
      font-weight: 600;
      color: var(--pow-text);
    }

    .nav-copy-btn {
      background: var(--pow-surface);
      border: var(--pow-border);
      color: var(--pow-text);
      border-radius: var(--pow-radius-pill);
      padding: 0.2rem 0.55rem;
      font-size: 0.675rem;
      font-weight: 700;
      cursor: pointer;
      line-height: 1;
      transition: all 120ms ease;
    }

    .nav-copy-btn:hover {
      border-color: var(--pow-accent-cta);
      color: var(--pow-accent-cta);
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }

    .nav-link-btn {
      font-size: 0.785rem;
      font-weight: 600;
      color: var(--pow-text-muted);
      text-decoration: none;
      padding: 0.35rem 0.75rem;
      border-radius: var(--pow-radius-pill);
      border: var(--pow-border);
      background: var(--pow-surface);
      transition: all 120ms ease;
    }

    .nav-link-btn:hover {
      color: var(--pow-text);
      background: var(--pow-surface-hover);
      border-color: var(--pow-text-muted);
    }

    .theme-toggle-btn {
      background: var(--pow-surface);
      border: var(--pow-border);
      color: var(--pow-text);
      padding: 0.35rem 0.75rem;
      border-radius: var(--pow-radius-pill);
      font-size: 0.785rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 120ms ease;
    }

    .theme-toggle-btn:hover {
      background: var(--pow-surface-hover);
      transform: translateY(-1px);
    }

    /* =========================================================
       1-PAGE BENTO HERO VIEWPORT (SINGLE-VIEWPORT FIT)
       ========================================================= */
    .bento-hero-viewport {
      min-height: calc(100svh - 56px);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 1rem 1.25rem;
      max-width: 1100px;
      margin: 0 auto;
      box-sizing: border-box;
    }

    .bento-master-canvas {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 0.85rem;
      width: 100%;
    }

    .bento-card {
      background: var(--pow-surface);
      border: var(--pow-border);
      border-radius: var(--pow-radius);
      padding: 1.4rem 1.6rem;
      box-shadow: var(--pow-shadow);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 160ms ease, box-shadow 160ms ease;
    }

    .bento-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }

    /* Tile 1: Profile & Two-Tone Headline (7 cols) */
    .card-profile-hero {
      grid-column: span 7;
      min-height: 200px;
    }

    .profile-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.85rem;
    }

    .avatar-wrapper {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .avatar-circle {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--pow-surface-elevated);
      border: 2px solid var(--pow-text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--pow-font-display);
      font-weight: 800;
      font-size: 1.05rem;
      color: var(--pow-text);
      letter-spacing: -0.02em;
    }

    .avatar-name {
      font-family: var(--pow-font-display);
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--pow-text);
    }

    .bento-two-tone-headline {
      font-family: var(--pow-font-display);
      font-size: clamp(1.25rem, 2.2vw, 1.55rem);
      font-weight: 700;
      line-height: 1.25;
      letter-spacing: -0.02em;
      margin-bottom: 1rem;
    }

    .two-tone-lead {
      color: var(--pow-text);
    }

    .two-tone-sub {
      color: var(--pow-text-muted);
      font-weight: 500;
    }

    .profile-bottom-tags {
      display: flex;
      align-items: center;
      gap: 0.45rem;
      flex-wrap: wrap;
    }

    .mini-capsule-tag {
      font-size: 0.68rem;
      font-weight: 600;
      padding: 0.2rem 0.65rem;
      border-radius: var(--pow-radius-pill);
      background: var(--pow-surface-elevated);
      color: var(--pow-text-muted);
      border: var(--pow-border);
      font-family: var(--pow-font-mono);
    }

    /* Tile 2: Contact & CTA Pill (5 cols) */
    .card-contact-cta {
      grid-column: span 5;
      min-height: 200px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .spring-icon-box {
      width: 38px;
      height: 24px;
      display: flex;
      align-items: center;
      color: var(--pow-text);
      margin-bottom: 0.5rem;
    }

    .contact-title {
      font-family: var(--pow-font-display);
      font-size: 1.35rem;
      font-weight: 700;
      line-height: 1.2;
      margin-bottom: 1rem;
      color: var(--pow-text);
    }

    .bento-action-pill-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.55rem;
      width: 100%;
      background: var(--pow-accent-cta);
      color: #ffffff;
      border: none;
      border-radius: var(--pow-radius-pill);
      padding: 0.75rem 1.25rem;
      font-size: 0.95rem;
      font-weight: 700;
      font-family: var(--pow-font-display);
      cursor: pointer;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(255, 87, 34, 0.35);
      transition: all 140ms ease;
    }

    .bento-action-pill-btn:hover {
      background: var(--pow-accent-cta-hover);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(255, 87, 34, 0.45);
    }

    /* Tile 3: Social Strip / Capsule Links (Full 12 cols, strictly horizontal side-by-side) */
    .bento-social-row {
      grid-column: span 12;
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 0.65rem;
      width: 100%;
    }

    .capsule-link-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--pow-surface);
      color: var(--pow-text-muted);
      border: var(--pow-border);
      border-radius: var(--pow-radius-pill);
      padding: 0.6rem 0.5rem;
      font-size: 0.825rem;
      font-weight: 600;
      text-decoration: none;
      white-space: nowrap;
      transition: all 140ms ease;
      cursor: pointer;
      box-shadow: var(--pow-shadow);
      width: 100%;
      text-align: center;
    }

    .capsule-link-btn:hover {
      color: var(--pow-text);
      background: var(--pow-surface-hover);
      border-color: var(--pow-accent-cta);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }

    /* Tile 4: Location & Live Indonesian Clock (4 cols) */
    .card-location-geo {
      grid-column: span 4;
      min-height: 180px;
    }

    .geo-icon-box {
      color: var(--pow-text);
      margin-bottom: 0.75rem;
    }

    .geo-title {
      font-family: var(--pow-font-display);
      font-size: 1.25rem;
      font-weight: 700;
      line-height: 1.2;
      margin-bottom: 0.35rem;
      color: var(--pow-text);
    }

    .geo-live-clock {
      font-family: var(--pow-font-mono);
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--pow-text-muted);
    }

    /* Tile 5: Philosophy & Principles (8 cols) */
    .card-philosophy {
      grid-column: span 8;
      min-height: 180px;
    }

    .card-eyebrow {
      font-size: 0.675rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--pow-accent-brand);
      font-family: var(--pow-font-mono);
      margin-bottom: 0.5rem;
    }

    .philosophy-paragraph {
      font-family: var(--pow-font-display);
      font-size: clamp(0.95rem, 1.6vw, 1.1rem);
      line-height: 1.45;
      letter-spacing: -0.015em;
    }

    .philosophy-paragraph .lead-text {
      color: var(--pow-text);
      font-weight: 700;
    }

    .philosophy-paragraph .sub-text {
      color: var(--pow-text-muted);
      font-weight: 500;
    }

    /* Tile 6: Capability & Telemetry Lab (12 cols) */
    .card-telemetry-lab {
      grid-column: span 12;
      padding: 1.15rem 1.6rem;
    }

    .telemetry-grid {
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr;
      gap: 1.25rem;
      align-items: center;
    }

    .telemetry-col h4 {
      font-family: var(--pow-font-display);
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
    }

    .telemetry-col p {
      font-size: 0.775rem;
      color: var(--pow-text-muted);
      line-height: 1.4;
    }

    .toggle-pills-wrap {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      margin-top: 0.45rem;
    }

    .interactive-filter-pill {
      background: var(--pow-surface-elevated);
      color: var(--pow-text-muted);
      border: var(--pow-border);
      border-radius: var(--pow-radius-pill);
      padding: 0.25rem 0.65rem;
      font-size: 0.7rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 120ms ease;
    }

    .interactive-filter-pill.active {
      background: var(--pow-accent-brand);
      color: #ffffff;
      border-color: var(--pow-accent-brand);
    }

    /* Secondary Anchor Jump Indicator */
    .viewport-scroll-hint {
      margin-top: 0.75rem;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.725rem;
      color: var(--pow-text-muted);
      text-decoration: none;
      transition: color 120ms ease;
    }

    .viewport-scroll-hint:hover {
      color: var(--pow-accent-cta);
    }

    /* =========================================================
       SECONDARY DOCUMENTATION SECTIONS (INSTALL, TOKENS, FAQ)
       ========================================================= */
    .pow-section {
      max-width: 1100px;
      margin: 4rem auto;
      padding: 0 1.5rem;
    }

    .section-header {
      margin-bottom: 1.75rem;
      text-align: left;
    }

    .section-badge {
      display: inline-block;
      font-size: 0.725rem;
      font-weight: 700;
      color: var(--pow-accent-cta);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-family: var(--pow-font-mono);
      margin-bottom: 0.35rem;
    }

    .section-title {
      font-family: var(--pow-font-display);
      font-size: 1.65rem;
      font-weight: 800;
      letter-spacing: -0.025em;
      margin-bottom: 0.35rem;
    }

    .section-desc {
      font-size: 0.9rem;
      color: var(--pow-text-muted);
      max-width: 680px;
      line-height: 1.55;
    }

    /* Tabbed Installation */
    .install-tabs-wrap {
      background: var(--pow-surface);
      border: var(--pow-border);
      border-radius: var(--pow-radius);
      box-shadow: var(--pow-shadow);
      overflow: hidden;
    }

    .install-tab-nav {
      display: flex;
      border-bottom: var(--pow-border);
      background: var(--pow-well-bg);
      overflow-x: auto;
    }

    .tab-nav-btn {
      padding: 0.85rem 1.35rem;
      font-size: 0.825rem;
      font-weight: 700;
      font-family: var(--pow-font-display);
      color: var(--pow-text-muted);
      background: none;
      border: none;
      border-bottom: 2px solid transparent;
      cursor: pointer;
      white-space: nowrap;
      transition: all 120ms ease;
    }

    .tab-nav-btn.active {
      color: var(--pow-accent-cta);
      border-bottom-color: var(--pow-accent-cta);
      background: var(--pow-surface);
    }

    .tab-body {
      padding: 1.5rem;
    }

    .tab-pane {
      display: none;
    }

    .tab-pane.active {
      display: block;
    }

    .terminal-box {
      background: var(--pow-well-bg);
      border: var(--pow-border);
      border-radius: 16px;
      overflow: hidden;
    }

    .terminal-header {
      padding: 0.55rem 0.95rem;
      background: var(--pow-surface-elevated);
      border-bottom: var(--pow-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .terminal-dots {
      display: flex;
      gap: 5px;
    }

    .dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: var(--pow-text-muted);
      opacity: 0.4;
    }

    .terminal-label {
      font-size: 0.725rem;
      color: var(--pow-text-muted);
      font-family: var(--pow-font-mono);
    }

    .terminal-copy-btn {
      background: var(--pow-surface);
      border: var(--pow-border);
      color: var(--pow-text);
      padding: 0.2rem 0.6rem;
      border-radius: var(--pow-radius-pill);
      font-size: 0.7rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 120ms ease;
    }

    .terminal-copy-btn:hover {
      border-color: var(--pow-accent-cta);
      color: var(--pow-accent-cta);
    }

    .terminal-content {
      padding: 1.15rem;
      font-family: var(--pow-font-mono);
      font-size: 0.825rem;
      line-height: 1.6;
      overflow-x: auto;
    }

    .terminal-line {
      display: flex;
      align-items: baseline;
      gap: 0.65rem;
      margin-bottom: 0.35rem;
    }

    .terminal-line:last-child {
      margin-bottom: 0;
    }

    .line-p {
      color: var(--pow-accent-cta);
      font-weight: 700;
      user-select: none;
    }

    .line-cmd {
      color: var(--pow-text);
      user-select: all;
    }

    .line-comment {
      color: var(--pow-text-muted);
      font-style: italic;
    }

    /* Token Cheatsheet Table */
    .token-table-wrap {
      background: var(--pow-surface);
      border: var(--pow-border);
      border-radius: var(--pow-radius);
      box-shadow: var(--pow-shadow);
      overflow-x: auto;
    }

    .pow-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.85rem;
    }

    .pow-table th {
      padding: 0.85rem 1.15rem;
      background: var(--pow-well-bg);
      border-bottom: var(--pow-border);
      font-family: var(--pow-font-display);
      font-weight: 700;
      color: var(--pow-text);
    }

    .pow-table td {
      padding: 0.85rem 1.15rem;
      border-bottom: var(--pow-border);
      color: var(--pow-text-muted);
    }

    .pow-table tr:last-child td {
      border-bottom: none;
    }

    .token-code {
      font-family: var(--pow-font-mono);
      font-size: 0.785rem;
      color: var(--pow-accent-brand);
      font-weight: 600;
    }

    .color-swatch-box {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
    }

    .color-swatch {
      width: 15px;
      height: 15px;
      border-radius: 4px;
      border: 1px solid rgba(255, 255, 255, 0.15);
      flex-shrink: 0;
    }

    /* FAQ Section */
    .faq-accordion {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .pow-faq-item {
      background: var(--pow-surface);
      border: var(--pow-border);
      border-radius: 18px;
      overflow: hidden;
      box-shadow: var(--pow-shadow);
    }

    .pow-faq-header {
      padding: 1rem 1.35rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--pow-font-display);
      font-weight: 700;
      font-size: 0.95rem;
      user-select: none;
    }

    .faq-arrow {
      font-weight: 700;
      transition: transform 140ms ease;
    }

    .pow-faq-body {
      padding: 0 1.35rem 1.15rem 1.35rem;
      font-size: 0.85rem;
      color: var(--pow-text-muted);
      line-height: 1.55;
      display: none;
    }

    .pow-faq-item.open .pow-faq-body {
      display: block;
    }

    .pow-faq-item.open .faq-arrow {
      transform: rotate(45deg);
    }

    /* Footer */
    .pow-footer {
      border-top: var(--pow-border);
      background: var(--pow-surface);
      padding: 3rem 1.5rem 2rem 1.5rem;
      margin-top: 4.5rem;
    }

    .footer-inner {
      max-width: 1100px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 2.5rem;
      padding-bottom: 2rem;
      border-bottom: var(--pow-border);
    }

    .footer-brand h3 {
      font-family: var(--pow-font-display);
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 0.45rem;
    }

    .footer-brand p {
      font-size: 0.825rem;
      color: var(--pow-text-muted);
      max-width: 380px;
      line-height: 1.5;
    }

    .footer-col h4 {
      font-family: var(--pow-font-display);
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.85rem;
      color: var(--pow-text);
    }

    .footer-col ul {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }

    .footer-col a {
      font-size: 0.8rem;
      color: var(--pow-text-muted);
      text-decoration: none;
      transition: color 120ms ease;
    }

    .footer-col a:hover {
      color: var(--pow-accent-cta);
    }

    .footer-bottom {
      max-width: 1100px;
      margin: 1.75rem auto 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.785rem;
      color: var(--pow-text-muted);
    }

    /* Toast Notification */
    .pow-toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--pow-text);
      color: var(--pow-bg);
      padding: 0.65rem 1.15rem;
      border-radius: var(--pow-radius-pill);
      font-size: 0.8rem;
      font-weight: 700;
      font-family: var(--pow-font-display);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
      z-index: 1000;
      opacity: 0;
      pointer-events: none;
      transform: translateY(10px);
      transition: opacity 140ms ease, transform 140ms ease;
    }

    .pow-toast.show {
      opacity: 1;
      transform: translateY(0);
    }

    /* Responsive Breakpoints */
    @media (max-width: 900px) {
      .bento-hero-viewport { min-height: auto; padding: 2rem 1rem; }
      .card-profile-hero { grid-column: span 12; }
      .card-contact-cta { grid-column: span 12; }
      .card-location-geo { grid-column: span 12; }
      .card-philosophy { grid-column: span 12; }
      .bento-social-row { grid-template-columns: repeat(4, 1fr); gap: 0.5rem; }
      .telemetry-grid { grid-template-columns: 1fr; }
      .nav-command-pill { display: none; }
    }

    @media (max-width: 768px) {
      .pow-nav { padding: 0.65rem 1rem; }
      .nav-title { font-size: 0.9rem; }
      .nav-tag-badge { display: none; }
      .footer-inner {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem 1rem;
      }
      .footer-brand {
        grid-column: 1 / -1;
        padding-bottom: 0.75rem;
        border-bottom: var(--pow-border);
      }
    }

    @media (max-width: 600px) {
      .bento-social-row {
        display: flex;
        flex-direction: row;
        overflow-x: auto;
        scrollbar-width: none;
        padding-bottom: 4px;
        gap: 0.45rem;
      }
      .bento-social-row::-webkit-scrollbar {
        display: none;
      }
      .capsule-link-btn {
        flex: 0 0 auto;
        width: auto;
        padding: 0.45rem 0.85rem;
      }
    }

    @media (max-width: 480px) {
      .bento-card { padding: 1.15rem 1rem; border-radius: 20px; }
      .bento-action-pill-btn { font-size: 0.875rem; padding: 0.7rem 1rem; }
      .section-title { font-size: 1.25rem; }
      .tab-body { padding: 0.85rem; }
      .terminal-content { font-size: 0.725rem; padding: 0.75rem; }
      .footer-bottom { flex-direction: column; gap: 0.65rem; text-align: center; }
    }
  </style>
</head>
<body>

  <!-- Top Navigation with Integrated Quick-Install Pill -->
  <header class="pow-nav">
    <a href="index.html" class="nav-brand-group">
      <img src="assets/logo.webp" alt="Taste Engine Logo" class="brand-logo-img">
      <span class="nav-title">Taste Engine</span>
      <span class="nav-tag-badge">#01 BENTO</span>
    </a>

    <!-- Single-Line Inline Command Pill (Aligned) -->
    <div class="nav-command-pill">
      <span style="color: var(--pow-text-muted); font-family: var(--pow-font-mono); font-weight: 700;">$</span>
      <code class="nav-cmd-code" id="navCmdText">npx skills add kennedys0/taste-engine --skill taste-style-bento</code>
      <button class="nav-copy-btn" id="navCopyBtn" title="Copy command">Copy</button>
    </div>

    <div class="nav-actions">
      <a href="#install" class="nav-link-btn">Install Guide</a>
      <a href="index.html" class="nav-link-btn">All Styles</a>
      <button class="theme-toggle-btn" id="themeToggleBtn" aria-label="Toggle theme">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
        <span>Theme</span>
      </button>
    </div>
  </header>

  <main>
    <!-- =========================================================
         1-PAGE BENTO HERO VIEWPORT (SINGLE-VIEWPORT FIT)
         ========================================================= -->
    <section class="bento-hero-viewport">
      
      <div class="bento-master-canvas">
        
        <!-- Tile 1: Profile & Value Prop (7 cols) - fekojewan (No badge) -->
        <article class="bento-card card-profile-hero">
          <div class="profile-top-bar">
            <div class="avatar-wrapper">
              <div class="avatar-circle">FK</div>
              <div class="avatar-name">fekojewan</div>
            </div>
          </div>

          <div class="bento-two-tone-headline">
            <span class="two-tone-lead">fekojewan is a digital systems architect</span>
            <span class="two-tone-sub">currently engineering autonomous agent runtimes.</span>
          </div>

          <div class="profile-bottom-tags">
            <span class="mini-capsule-tag">Design Systems</span>
            <span class="mini-capsule-tag">Agentic UX</span>
            <span class="mini-capsule-tag">Token Scale</span>
            <span class="mini-capsule-tag">Zero-Slop</span>
          </div>
        </article>

        <!-- Tile 2: Contact & CTA Pill (5 cols) - mail@fekojewan.my.id -->
        <article class="bento-card card-contact-cta">
          <div class="spring-icon-box">
            <!-- Wireframe spring vector icon -->
            <svg width="40" height="24" viewBox="0 0 54 28" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
              <path d="M4 14C4 6 12 2 18 2C26 2 26 26 34 26C42 26 42 2 50 2"/>
              <ellipse cx="14" cy="14" rx="6" ry="11"/>
              <ellipse cx="22" cy="14" rx="6" ry="11"/>
              <ellipse cx="30" cy="14" rx="6" ry="11"/>
              <ellipse cx="38" cy="14" rx="6" ry="11"/>
            </svg>
          </div>

          <div>
            <h3 class="contact-title">Have a project<br>in mind?</h3>
            <a href="mailto:mail@fekojewan.my.id" class="bento-action-pill-btn" onclick="handleBtnClick('Email: mail@fekojewan.my.id')">
              <span>mail@fekojewan.my.id</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
            </a>
          </div>
        </article>

        <!-- Tile 3: Social & Ecosystem Capsule Strip (Full 12 cols, side-by-side horizontally) -->
        <div class="bento-social-row">
          <button class="capsule-link-btn" onclick="handleBtnClick('Navigating to GitHub')">github.</button>
          <button class="capsule-link-btn" onclick="handleBtnClick('Navigating to Figma')">figma.</button>
          <button class="capsule-link-btn" onclick="handleBtnClick('Navigating to Dribbble')">dribbble.</button>
          <button class="capsule-link-btn" onclick="handleBtnClick('Navigating to Behance')">behance.</button>
          <button class="capsule-link-btn" onclick="handleBtnClick('Navigating to X / Twitter')">x.com.</button>
          <button class="capsule-link-btn" onclick="handleBtnClick('Navigating to Unsplash')">unsplash.</button>
          <button class="capsule-link-btn" onclick="handleBtnClick('Navigating to LinkedIn')">linkedin.</button>
        </div>

        <!-- Tile 4: Location & Live Indonesian Timezone (4 cols) - Indonesia (WIB) -->
        <article class="bento-card card-location-geo">
          <div class="geo-icon-box">
            <!-- Wireframe Globe Vector -->
            <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
              <circle cx="12" cy="12" r="10"/>
              <ellipse cx="12" cy="12" rx="4.5" ry="10"/>
              <line x1="2" y1="12" x2="22" y2="12"/>
            </svg>
          </div>

          <div>
            <h4 class="geo-title">Based in<br>Indonesia</h4>
            <div class="geo-live-clock" id="liveClockDisplay">WIB • GMT+7 • 16:30:00</div>
          </div>
        </article>

        <!-- Tile 5: Philosophy & Principles (8 cols) -->
        <article class="bento-card card-philosophy">
          <span class="card-eyebrow">Design Philosophy & Anti-Slop</span>
          <p class="philosophy-paragraph">
            <span class="lead-text">As a digital systems designer, I specialize in creating resilient interfaces with mathematical token hierarchy.</span>
            <span class="sub-text"> I believe that exceptional design starts with common values, honest contrast pairing, strict spatial rhythm, zero fake metrics, and deep respect for your audience.</span>
          </p>
          <div style="margin-top: 0.65rem;">
            <span class="mini-capsule-tag" style="color: var(--pow-accent-cta); border-color: rgba(255,87,34,0.3);">Rule: No Uniform 3x2 Generic Grid</span>
          </div>
        </article>

        <!-- Tile 6: Capability & Telemetry Lab (12 cols) - (No online badge) -->
        <article class="bento-card card-telemetry-lab">
          <div class="telemetry-grid">
            <div class="telemetry-col">
              <h4>Modular Architecture</h4>
              <p>Test live capability filtering. Bento tiles reflect distinct functional purposes rather than repeating duplicate card patterns.</p>
              <div class="toggle-pills-wrap">
                <button class="interactive-filter-pill active" onclick="toggleCapability(this, 'Design Tokens')">Design Tokens</button>
                <button class="interactive-filter-pill" onclick="toggleCapability(this, '3D Systems')">3D Modeling</button>
                <button class="interactive-filter-pill" onclick="toggleCapability(this, 'Motion Runtimes')">Motion Engine</button>
                <button class="interactive-filter-pill" onclick="toggleCapability(this, 'Contrast Gates')">WCAG AA Safety</button>
              </div>
            </div>

            <div class="telemetry-col" style="text-align: center; border-left: var(--pow-border); border-right: var(--pow-border); padding: 0 1rem;">
              <div style="font-family: var(--pow-font-display); font-size: 2.25rem; font-weight: 800; line-height: 1; color: var(--pow-text); margin-bottom: 0.2rem;">
                42<span style="font-size: 1.35rem; color: var(--pow-accent-cta);">ms</span>
              </div>
              <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--pow-text-muted);">
                Global Edge Latency
              </div>
              <div style="font-size: 0.725rem; color: #10b981; margin-top: 0.25rem; font-weight: 600;">
                ● Zero Cold Start
              </div>
            </div>

            <div class="telemetry-col" style="padding-left: 0.5rem;">
              <div style="color: #f59e0b; font-size: 1.05rem; margin-bottom: 0.2rem;">
                ★ ★ ★ ★ ★
              </div>
              <h4>Production Proven</h4>
              <p>+1,456 developer installations across Google Antigravity, Claude Code, and Codex runtimes.</p>
              <div style="margin-top: 0.5rem;">
                <span class="mini-capsule-tag" style="background: rgba(139, 92, 246, 0.15); color: var(--pow-accent-brand); border-color: rgba(139, 92, 246, 0.3);">v0.10.6 Synchronized</span>
              </div>
            </div>
          </div>
        </article>

      </div>

      <!-- Quick Jump Down Indicator -->
      <a href="#install" class="viewport-scroll-hint">
        <span>Installation Guide & Tokens Below</span>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 13l5 5 5-5M12 6v12"/></svg>
      </a>
    </section>

    <!-- =========================================================
         TABBED INSTALLATION GUIDE
         ========================================================= -->
    <section class="pow-section" id="install">
      <div class="section-header">
        <span class="section-badge">Fast-Track Setup</span>
        <h2 class="section-title">Install Bento Grid Pack</h2>
        <p class="section-desc">
          Choose whether to install Bento Grid as a lightweight standalone skill or as part of the full 10-style Taste Engine suite.
        </p>
      </div>

      <div class="install-tabs-wrap">
        <div class="install-tab-nav">
          <button class="tab-nav-btn active" onclick="switchTab(0)">1. Standalone Skill</button>
          <button class="tab-nav-btn" onclick="switchTab(1)">2. Full Multi-Agent Suite</button>
          <button class="tab-nav-btn" onclick="switchTab(2)">3. Tailwind Preset</button>
        </div>

        <div class="tab-body">
          <!-- Tab 1: Standalone -->
          <div class="tab-pane active" id="tab0">
            <div class="terminal-box">
              <div class="terminal-header">
                <div class="terminal-dots">
                  <span class="dot"></span><span class="dot"></span><span class="dot"></span>
                </div>
                <span class="terminal-label">bash - standalone skill install</span>
                <button class="terminal-copy-btn" onclick="copySnippet('cmdStandaloneCli')">Copy</button>
              </div>
              <div class="terminal-content" id="cmdStandaloneCli">
                <div class="terminal-line">
                  <span class="line-comment"># Install standalone Bento Grid pack via Agent Skills CLI</span>
                </div>
                <div class="terminal-line">
                  <span class="line-p">$</span>
                  <span class="line-cmd">npx skills add kennedys0/taste-engine --skill taste-style-bento</span>
                </div>
                <div class="terminal-line">
                  <span class="line-comment"># Or clone directly into Antigravity IDE global config</span>
                </div>
                <div class="terminal-line">
                  <span class="line-p">$</span>
                  <span class="line-cmd">git clone https://github.com/kennedys0/taste-engine.git && cp -r taste-engine/optional-standalone-skills/taste-style-bento ~/.gemini/config/skills/</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Tab 2: Full Suite -->
          <div class="tab-pane" id="tab1">
            <div class="terminal-box">
              <div class="terminal-header">
                <div class="terminal-dots">
                  <span class="dot"></span><span class="dot"></span><span class="dot"></span>
                </div>
                <span class="terminal-label">bash - full engine suite</span>
                <button class="terminal-copy-btn" onclick="copySnippet('cmdGlobalCli')">Copy</button>
              </div>
              <div class="terminal-content" id="cmdGlobalCli">
                <div class="terminal-line">
                  <span class="line-comment"># 1. Universal 1-click Agent Skills install (includes all 10 styles)</span>
                </div>
                <div class="terminal-line">
                  <span class="line-p">$</span>
                  <span class="line-cmd">npx skills add kennedys0/taste-engine</span>
                </div>
                <div class="terminal-line">
                  <span class="line-comment"># 2. Or install globally for Google Antigravity IDE / CLI (agy)</span>
                </div>
                <div class="terminal-line">
                  <span class="line-p">$</span>
                  <span class="line-cmd">node bin/taste-engine.mjs install --agent antigravity --global</span>
                </div>
                <div class="terminal-line">
                  <span class="line-comment"># 3. Or install for Claude Code or OpenAI Codex</span>
                </div>
                <div class="terminal-line">
                  <span class="line-p">$</span>
                  <span class="line-cmd">node bin/taste-engine.mjs install --agent claude --global</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Tab 3: Tailwind -->
          <div class="tab-pane" id="tab2">
            <div class="terminal-box">
              <div class="terminal-header">
                <div class="terminal-dots">
                  <span class="dot"></span><span class="dot"></span><span class="dot"></span>
                </div>
                <span class="terminal-label">tailwind.config.js - preset integration</span>
                <button class="terminal-copy-btn" onclick="copySnippet('cmdTailwindPreset')">Copy</button>
              </div>
              <div class="terminal-content" id="cmdTailwindPreset">
                <div class="terminal-line">
                  <span class="line-comment">// Add Taste Engine official presets to your Tailwind config</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">module.exports = {</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">&nbsp;&nbsp;presets: [require('./presets/tailwind/tailwind.preset.js')],</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">&nbsp;&nbsp;theme: {</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">&nbsp;&nbsp;&nbsp;&nbsp;extend: {</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colors: {</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'bento-bg': '#13151b',</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'bento-surface': '#1e222b',</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'bento-cta': '#ff5722'</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;borderRadius: { 'bento': '28px' }</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">&nbsp;&nbsp;&nbsp;&nbsp;}</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">&nbsp;&nbsp;}</span>
                </div>
                <div class="terminal-line">
                  <span class="line-cmd">};</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
         DESIGN TOKEN CHEATSHEET
         ========================================================= -->
    <section class="pow-section">
      <div class="section-header">
        <span class="section-badge">Design Tokens & Math</span>
        <h2 class="section-title">Bento Grid Design Tokens</h2>
        <p class="section-desc">
          Official CSS custom properties for Bento Grid. Copy and drop directly into your stylesheets or design system configuration.
        </p>
      </div>

      <div class="token-table-wrap">
        <table class="pow-table">
          <thead>
            <tr>
              <th>Token Name</th>
              <th>Dark Mode (Refined Slate / Non-Pitch-Black)</th>
              <th>Light Mode</th>
              <th>Role & Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="token-code">--taste-bento-bg</td>
              <td>
                <div class="color-swatch-box">
                  <span class="color-swatch" style="background: #13151b;"></span>
                  <code>#13151b</code>
                </div>
              </td>
              <td>
                <div class="color-swatch-box">
                  <span class="color-swatch" style="background: #f3f4f6;"></span>
                  <code>#f3f4f6</code>
                </div>
              </td>
              <td>Canvas backdrop base (warm graphite slate)</td>
            </tr>
            <tr>
              <td class="token-code">--taste-bento-surface</td>
              <td>
                <div class="color-swatch-box">
                  <span class="color-swatch" style="background: #1e222b;"></span>
                  <code>#1e222b</code>
                </div>
              </td>
              <td>
                <div class="color-swatch-box">
                  <span class="color-swatch" style="background: #ffffff;"></span>
                  <code>#ffffff</code>
                </div>
              </td>
              <td>Elevated modular card surface</td>
            </tr>
            <tr>
              <td class="token-code">--taste-bento-surface-elevated</td>
              <td>
                <div class="color-swatch-box">
                  <span class="color-swatch" style="background: #262b36;"></span>
                  <code>#262b36</code>
                </div>
              </td>
              <td>
                <div class="color-swatch-box">
                  <span class="color-swatch" style="background: #e5e7eb;"></span>
                  <code>#e5e7eb</code>
                </div>
              </td>
              <td>Sub-elements, capsule pills, and inner chips</td>
            </tr>
            <tr>
              <td class="token-code">--taste-bento-accent-cta</td>
              <td>
                <div class="color-swatch-box">
                  <span class="color-swatch" style="background: #ff5722;"></span>
                  <code>#ff5722</code>
                </div>
              </td>
              <td>
                <div class="color-swatch-box">
                  <span class="color-swatch" style="background: #ff5722;"></span>
                  <code>#ff5722</code>
                </div>
              </td>
              <td>High-impact action pill button (Warm Tangerine)</td>
            </tr>
            <tr>
              <td class="token-code">--taste-bento-radius</td>
              <td><code>28px</code></td>
              <td><code>28px</code></td>
              <td>Tactile rounded corner radius</td>
            </tr>
            <tr>
              <td class="token-code">--taste-bento-border</td>
              <td><code>1px solid rgba(255,255,255,0.08)</code></td>
              <td><code>1px solid rgba(0,0,0,0.08)</code></td>
              <td>Subtle hairline structural divider</td>
            </tr>
            <tr>
              <td class="token-code">--taste-bento-text-muted</td>
              <td><code>#8e95a5</code></td>
              <td><code>#6b7280</code></td>
              <td>Two-tone continuation text (4.8:1 WCAG AA)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- =========================================================
         FREQUENTLY ASKED QUESTIONS
         ========================================================= -->
    <section class="pow-section">
      <div class="section-header">
        <span class="section-badge">Fidelity Knowledge</span>
        <h2 class="section-title">Bento Grid FAQ</h2>
        <p class="section-desc">
          Key architectural decisions behind Taste Engine's Bento Grid archetype.
        </p>
      </div>

      <div class="faq-accordion">
        <div class="pow-faq-item">
          <div class="pow-faq-header" onclick="toggleFaq(this)">
            <span>Why does Taste Engine's Bento Grid use warm graphite slate instead of pitch black?</span>
            <span class="faq-arrow">+</span>
          </div>
          <div class="pow-faq-body">
            Pure pitch black (<code>#000000</code>) creates harsh visual vibration, destroys depth perception, and accelerates eye fatigue. By using refined matte graphite slate (<code>#13151b</code> for canvas base and <code>#1e222b</code> for card surfaces), the composition gains tactile depth and allows 1px hairline borders (<code>rgba(255, 255, 255, 0.08)</code>) to render softly and naturally.
          </div>
        </div>

        <div class="pow-faq-item">
          <div class="pow-faq-header" onclick="toggleFaq(this)">
            <span>What is the Two-Tone Typographic Contrast rule?</span>
            <span class="faq-arrow">+</span>
          </div>
          <div class="pow-faq-body">
            In authentic Bento design, narrative and value statements avoid monochromatic text rendering. The primary hook or subject uses high-contrast crisp white (<code>#f4f4f7</code>, weight 700), while the sentence continuation or supporting role transitions seamlessly to warm muted slate (<code>#8e95a5</code>, weight 400–500). This provides immediate visual scanning hierarchy without creating an imposing wall of text.
          </div>
        </div>

        <div class="pow-faq-item">
          <div class="pow-faq-header" onclick="toggleFaq(this)">
            <span>How does Bento Grid prevent generic uniform card slop?</span>
            <span class="faq-arrow">+</span>
          </div>
          <div class="pow-faq-body">
            Taste Engine's fidelity gate strictly rejects repetitive 3x2 uniform cards (the generic icon + heading + paragraph pattern). Every compartment in a Bento Grid must serve a distinct functional anatomy: a profile hero with avatar, a high-contrast pill CTA, a full-width horizontal capsule link strip, and live telemetry status monitors.
          </div>
        </div>

        <div class="pow-faq-item">
          <div class="pow-faq-header" onclick="toggleFaq(this)">
            <span>Can I install Bento Grid as a standalone skill?</span>
            <span class="faq-arrow">+</span>
          </div>
          <div class="pow-faq-body">
            Yes! Run <code>npx skills add kennedys0/taste-engine --skill taste-style-bento</code>. This installs only the Bento Grid tokens, CSS recipes, and fidelity gates, keeping your AI agent's context window lightweight and focused.
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="pow-footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <div style="display: flex; align-items: center; gap: 0.65rem; margin-bottom: 0.75rem;">
          <img src="assets/logo.webp" alt="Taste Engine Logo" class="brand-logo-img">
          <h3 style="margin: 0; font-family: var(--pow-font-display); font-size: 1.15rem;">Taste Engine</h3>
        </div>
        <p>
          Frontend Design Intelligence & Aesthetic Archetypes for Autonomous AI Agents. Built strictly to eliminate generic AI-slop and ensure WCAG AA contrast coupling.
        </p>
      </div>

      <div class="footer-col">
        <h4>10 Archetypes</h4>
        <ul>
          <li><a href="bento.html" style="color: var(--pow-accent-cta); font-weight: 700;">Bento Grid (PoW)</a></li>
          <li><a href="neo-brutalism.html">Neo-Brutalism (PoW)</a></li>
          <li><a href="claymorphism.html">Claymorphism (PoW)</a></li>
          <li><a href="enterprise.html">Enterprise (PoW)</a></li>
          <li><a href="glassmorphism.html">Glassmorphism (PoW)</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>More Archetypes</h4>
        <ul>
          <li><a href="minimalism.html">Minimalism (PoW)</a></li>
          <li><a href="retro-terminal.html">Retro Terminal (PoW)</a></li>
          <li><a href="skeuomorphism.html">Skeuomorphism (PoW)</a></li>
          <li><a href="swiss-editorial.html">Swiss Editorial (PoW)</a></li>
          <li><a href="brutalism.html">Brutalism (PoW)</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <div>&copy; 2026 Taste Engine. MIT Licensed. Open Source on GitHub.</div>
      <div>Designed for Antigravity, Claude Code, and OpenAI Codex.</div>
    </div>
  </footer>

  <!-- Toast Element -->
  <div class="pow-toast" id="powToast">Notification</div>

  <!-- Interactive Logic -->
  <script>
    // Theme Management
    const themeBtn = document.getElementById('themeToggleBtn');
    const htmlElem = document.documentElement;

    const savedTheme = localStorage.getItem('taste-theme') || 'dark';
    htmlElem.setAttribute('data-theme', savedTheme);

    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        const current = htmlElem.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        htmlElem.setAttribute('data-theme', next);
        localStorage.setItem('taste-theme', next);
        showToast(`Theme switched to ${next} mode`);
      });
    }

    // Toast Notification
    function showToast(msg) {
      const toast = document.getElementById('powToast');
      if (!toast) return;
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2200);
    }

    // Nav Command Copy
    const navCopyBtn = document.getElementById('navCopyBtn');
    if (navCopyBtn) {
      navCopyBtn.addEventListener('click', () => {
        const text = document.getElementById('navCmdText').textContent.trim();
        navigator.clipboard.writeText(text).then(() => {
          showToast('Copied: ' + text);
        });
      });
    }

    // Generic Snippet Copy
    function copySnippet(elementId) {
      const el = document.getElementById(elementId);
      if (!el) return;
      const text = el.innerText.trim();
      navigator.clipboard.writeText(text).then(() => {
        showToast('Snippet copied to clipboard!');
      });
    }

    // Generic Action Button Click Feedback
    function handleBtnClick(msg) {
      showToast(msg);
      if (navigator.vibrate) navigator.vibrate(20);
    }

    // Capability Pills Toggle
    function toggleCapability(btn, name) {
      btn.classList.toggle('active');
      const isActive = btn.classList.contains('active');
      showToast(`${name}: ${isActive ? 'Enabled' : 'Disabled'}`);
    }

    // Installation Tabs
    function switchTab(index) {
      const buttons = document.querySelectorAll('.tab-nav-btn');
      const panes = document.querySelectorAll('.tab-pane');
      buttons.forEach((b, i) => b.classList.toggle('active', i === index));
      panes.forEach((p, i) => p.classList.toggle('active', i === index));
    }

    // FAQ Accordion
    function toggleFaq(header) {
      const item = header.parentElement;
      item.classList.toggle('open');
    }

    // Live Clock Update (WIB / GMT+7 - Western Indonesian Time)
    function updateLiveClock() {
      const clockEl = document.getElementById('liveClockDisplay');
      if (!clockEl) return;
      const now = new Date();
      // UTC + 7 hours for WIB (Jakarta / Indonesia)
      const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
      const wibTime = new Date(utc + (3600000 * 7));
      const hours = String(wibTime.getHours()).padStart(2, '0');
      const minutes = String(wibTime.getMinutes()).padStart(2, '0');
      const seconds = String(wibTime.getSeconds()).padStart(2, '0');
      clockEl.textContent = `WIB • GMT+7 • ${hours}:${minutes}:${seconds}`;
    }
    setInterval(updateLiveClock, 1000);
    updateLiveClock();
  </script>
</body>
</html>
"""

OUT_FILE.write_text(HTML_CONTENT, encoding="utf-8")
print(f"PASS: successfully generated {OUT_FILE} ({len(HTML_CONTENT)} bytes)")
