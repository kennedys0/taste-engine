#!/usr/bin/env python3
"""Build dedicated Neo-Brutalism Proof of Work & Installation Guide HTML page."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
OUT_FILE = DOCS_DIR / "neo-brutalism.html"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neo-Brutalism Proof of Work & Installation Guide — Taste Engine</title>
  <meta name="description" content="Dedicated Proof of Work and installation guide for Taste Engine's Neo-Brutalism aesthetic archetype. Experience authentic 2.5px borders, 0-blur mechanical shadows, and zero AI-slop.">
  <link rel="icon" type="image/webp" href="assets/logo.webp">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    /* =========================================================
       NEO-BRUTALISM DESIGN SYSTEM TOKENS
       Authentic 2.5px solid strokes, 0-blur directional shadows,
       mechanical tactile physics, saturated pop accents.
       ========================================================= */
    :root {
      --neo-bg: #FFFDF7;
      --neo-surface: #FFFFFF;
      --neo-surface-elevated: #FFF9E6;
      --neo-well-bg: #F4F0EA;
      --neo-ink: #121212;
      --neo-ink-muted: #4B4B4B;
      --neo-border-color: #121212;
      --neo-border-width: 2.5px;
      --neo-border: var(--neo-border-width) solid var(--neo-border-color);
      --neo-shadow-color: #121212;
      --neo-shadow-sm: 3px 3px 0 var(--neo-shadow-color);
      --neo-shadow-md: 5px 5px 0 var(--neo-shadow-color);
      --neo-shadow-lg: 8px 8px 0 var(--neo-shadow-color);
      
      /* Vibrant Saturated Pop Palette */
      --neo-yellow: #FFE600;
      --neo-coral: #FF5C00;
      --neo-cyan: #00F0FF;
      --neo-lime: #52FF00;
      --neo-pink: #FF66C4;
      --neo-purple: #9D4EDD;

      /* Primary Active Accents */
      --neo-accent-primary: var(--neo-yellow);
      --neo-accent-secondary: var(--neo-cyan);
      --neo-accent-contrast: #121212;

      /* Radii */
      --neo-radius: 4px;
      --neo-radius-pill: 999px;

      /* Typography */
      --neo-font-display: 'Space Grotesk', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --neo-font-body: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --neo-font-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }

    [data-theme="dark"] {
      /* Neo-Brutalism Dark Pop Palette - STARK LIGHT STROKES */
      --neo-bg: #18181B;
      --neo-surface: #222227;
      --neo-surface-elevated: #2B2B32;
      --neo-well-bg: #121215;
      --neo-ink: #FAFAFA;
      --neo-ink-muted: #A1A1AA;
      --neo-border-color: #FAFAFA;
      --neo-border: var(--neo-border-width) solid var(--neo-border-color);
      --neo-shadow-color: #FAFAFA;
      --neo-shadow-sm: 3px 3px 0 var(--neo-shadow-color);
      --neo-shadow-md: 5px 5px 0 var(--neo-shadow-color);
      --neo-shadow-lg: 8px 8px 0 var(--neo-shadow-color);

      --neo-accent-primary: #FFE600;
      --neo-accent-secondary: #00F0FF;
      --neo-accent-contrast: #121212;
    }

    /* Base Reset */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--neo-bg);
      color: var(--neo-ink);
      font-family: var(--neo-font-body);
      font-size: 16px;
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      transition: background-color 150ms ease, color 150ms ease;
    }

    /* Top Navigation Bar */
    .neo-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--neo-surface);
      border-bottom: var(--neo-border);
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .nav-brand-group {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: var(--neo-ink);
    }

    .nav-logo-box {
      width: 34px;
      height: 34px;
      background: var(--neo-yellow);
      border: var(--neo-border);
      box-shadow: 2px 2px 0 var(--neo-shadow-color);
      border-radius: var(--neo-radius);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-family: var(--neo-font-display);
    }

    .nav-title {
      font-family: var(--neo-font-display);
      font-weight: 800;
      font-size: 1.1rem;
      letter-spacing: -0.02em;
    }

    .nav-tag-badge {
      background: var(--neo-cyan);
      color: #121212;
      font-family: var(--neo-font-mono);
      font-size: 0.7rem;
      font-weight: 700;
      padding: 0.2rem 0.55rem;
      border: var(--neo-border);
      border-radius: var(--neo-radius);
      box-shadow: 2px 2px 0 var(--neo-shadow-color);
      transform: rotate(-1.5deg);
      text-transform: uppercase;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .neo-btn-sm {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.45rem 0.85rem;
      background: var(--neo-surface);
      color: var(--neo-ink);
      border: var(--neo-border);
      box-shadow: var(--neo-shadow-sm);
      border-radius: var(--neo-radius);
      font-family: var(--neo-font-display);
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      text-decoration: none;
      cursor: pointer;
      transition: transform 90ms ease, box-shadow 90ms ease;
    }

    .neo-btn-sm:hover {
      transform: translate(-1px, -1px);
      box-shadow: 4px 4px 0 var(--neo-shadow-color);
    }

    .neo-btn-sm:active {
      transform: translate(2px, 2px);
      box-shadow: 1px 1px 0 var(--neo-shadow-color);
    }

    /* Hero Section (100svh safe viewport) */
    .pow-hero {
      min-height: calc(100svh - 60px);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 3.5rem 1.25rem 2.5rem 1.25rem;
      position: relative;
      max-width: 1080px;
      margin: 0 auto;
    }

    .hero-sticker-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--neo-coral);
      color: #FAFAFA;
      border: var(--neo-border);
      box-shadow: var(--neo-shadow-sm);
      border-radius: var(--neo-radius);
      padding: 0.35rem 0.9rem;
      font-family: var(--neo-font-mono);
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      margin-bottom: 1.5rem;
      transform: rotate(-1deg);
    }

    .hero-title {
      font-family: var(--neo-font-display);
      font-size: clamp(2rem, 6vw, 3.8rem);
      font-weight: 800;
      line-height: 1.1;
      letter-spacing: -0.035em;
      text-transform: uppercase;
      margin-bottom: 1.25rem;
      max-width: 900px;
    }

    .hero-title span.highlight {
      background: var(--neo-yellow);
      color: #121212;
      padding: 0.1rem 0.45rem;
      border: var(--neo-border);
      box-shadow: 4px 4px 0 var(--neo-shadow-color);
      display: inline-block;
      margin: 0 0.15rem;
    }

    .hero-desc {
      font-size: clamp(0.95rem, 2vw, 1.15rem);
      color: var(--neo-ink-muted);
      max-width: 720px;
      margin-bottom: 2rem;
      line-height: 1.6;
      font-weight: 500;
    }

    /* Single-Line Inline Command Pill ("Sejajarin") */
    .neo-command-pill {
      display: inline-flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      gap: 0.65rem;
      background: var(--neo-surface);
      border: var(--neo-border);
      box-shadow: var(--neo-shadow-md);
      border-radius: var(--neo-radius);
      padding: 0.4rem 0.5rem 0.4rem 1.1rem;
      max-width: 100%;
      box-sizing: border-box;
      margin-bottom: 2rem;
    }

    .neo-prompt {
      font-family: var(--neo-font-mono);
      font-weight: 800;
      color: var(--neo-coral);
      flex-shrink: 0;
      line-height: 1;
      font-size: 0.95rem;
      user-select: none;
    }

    .neo-code {
      font-family: var(--neo-font-mono);
      font-size: clamp(0.72rem, 3.2vw, 0.875rem);
      font-weight: 600;
      color: var(--neo-ink);
      white-space: nowrap;
      overflow-x: auto;
      scrollbar-width: none;
      line-height: 1;
      user-select: all;
    }

    .neo-code::-webkit-scrollbar {
      display: none;
    }

    .neo-copy-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: var(--neo-yellow);
      color: #121212;
      border: var(--neo-border);
      border-radius: var(--neo-radius);
      padding: 0.4rem 0.8rem;
      font-family: var(--neo-font-display);
      font-size: 0.75rem;
      font-weight: 800;
      cursor: pointer;
      flex-shrink: 0;
      line-height: 1;
      box-shadow: 2px 2px 0 var(--neo-shadow-color);
      transition: transform 90ms ease, box-shadow 90ms ease;
    }

    .neo-copy-btn:hover {
      transform: translate(-1px, -1px);
      box-shadow: 3px 3px 0 var(--neo-shadow-color);
    }

    .neo-copy-btn:active {
      transform: translate(1px, 1px);
      box-shadow: 1px 1px 0 var(--neo-shadow-color);
    }

    /* Hero CTA Group */
    .hero-btn-group {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1rem;
      margin-bottom: 2.75rem;
      flex-wrap: wrap;
    }

    .neo-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0.8rem 1.6rem;
      font-family: var(--neo-font-display);
      font-weight: 800;
      font-size: 0.95rem;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      border: var(--neo-border);
      border-radius: var(--neo-radius);
      box-shadow: var(--neo-shadow-md);
      cursor: pointer;
      transition: transform 90ms ease, box-shadow 90ms ease;
      text-decoration: none;
    }

    .neo-btn-primary {
      background: var(--neo-yellow);
      color: #121212;
    }

    .neo-btn-secondary {
      background: var(--neo-surface);
      color: var(--neo-ink);
    }

    .neo-btn:hover {
      transform: translate(-2px, -2px);
      box-shadow: 7px 7px 0 var(--neo-shadow-color);
    }

    .neo-btn:active {
      transform: translate(2px, 2px);
      box-shadow: 2px 2px 0 var(--neo-shadow-color);
    }

    /* 4-Stat Neo Strip */
    .neo-stat-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1rem;
      width: 100%;
      max-width: 960px;
    }

    .stat-box {
      background: var(--neo-surface);
      border: var(--neo-border);
      box-shadow: var(--neo-shadow-sm);
      border-radius: var(--neo-radius);
      padding: 1rem 0.85rem;
      text-align: center;
    }

    .stat-val {
      font-family: var(--neo-font-display);
      font-size: 1.6rem;
      font-weight: 800;
      line-height: 1.1;
      margin-bottom: 0.25rem;
      color: var(--neo-ink);
    }

    .stat-label {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--neo-ink-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Content Sections */
    .neo-section {
      max-width: 1080px;
      margin: 4.5rem auto;
      padding: 0 1.25rem;
    }

    .section-header {
      margin-bottom: 2.25rem;
    }

    .section-badge {
      display: inline-block;
      font-family: var(--neo-font-mono);
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      padding: 0.25rem 0.65rem;
      background: var(--neo-lime);
      color: #121212;
      border: var(--neo-border);
      border-radius: var(--neo-radius);
      box-shadow: 2px 2px 0 var(--neo-shadow-color);
      margin-bottom: 0.75rem;
    }

    .section-title {
      font-family: var(--neo-font-display);
      font-size: clamp(1.6rem, 4vw, 2.4rem);
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: -0.02em;
      line-height: 1.2;
    }

    .section-desc {
      font-size: 1rem;
      color: var(--neo-ink-muted);
      max-width: 680px;
      margin-top: 0.5rem;
      line-height: 1.6;
    }

    /* Tabbed Installation Card */
    .neo-card {
      background: var(--neo-surface);
      border: var(--neo-border);
      box-shadow: var(--neo-shadow-lg);
      border-radius: var(--neo-radius);
      overflow: hidden;
    }

    .tab-header-strip {
      display: flex;
      background: var(--neo-well-bg);
      border-bottom: var(--neo-border);
      overflow-x: auto;
      scrollbar-width: none;
    }

    .tab-header-strip::-webkit-scrollbar {
      display: none;
    }

    .tab-switch-btn {
      padding: 0.85rem 1.4rem;
      background: transparent;
      border: none;
      border-right: var(--neo-border);
      font-family: var(--neo-font-display);
      font-size: 0.85rem;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--neo-ink-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: background 120ms ease, color 120ms ease;
    }

    .tab-switch-btn:hover {
      background: var(--neo-surface-elevated);
      color: var(--neo-ink);
    }

    .tab-switch-btn.active {
      background: var(--neo-yellow);
      color: #121212;
    }

    .tab-body {
      padding: 1.75rem;
      display: none;
    }

    .tab-body.active {
      display: block;
    }

    .install-step-title {
      font-family: var(--neo-font-display);
      font-size: 1.15rem;
      font-weight: 800;
      text-transform: uppercase;
      margin-bottom: 0.65rem;
    }

    .install-step-desc {
      font-size: 0.9rem;
      color: var(--neo-ink-muted);
      margin-bottom: 1.25rem;
    }

    /* Terminal Console Window */
    .neo-terminal {
      background: #121215;
      color: #FAFAFA;
      border: var(--neo-border);
      box-shadow: var(--neo-shadow-md);
      border-radius: var(--neo-radius);
      overflow: hidden;
      margin-bottom: 1.5rem;
    }

    .terminal-topbar {
      background: #1E1E24;
      padding: 0.65rem 1rem;
      border-bottom: 2px solid #33333D;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .terminal-dots {
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      border: 1.5px solid #000;
    }

    .dot.red { background: #FF5E5B; }
    .dot.yellow { background: #FFDE59; }
    .dot.green { background: #00F0A8; }

    .terminal-label {
      font-family: var(--neo-font-mono);
      font-size: 0.75rem;
      color: #A1A1AA;
      font-weight: 700;
    }

    .terminal-content {
      padding: 1.15rem;
      font-family: var(--neo-font-mono);
      font-size: 0.85rem;
      line-height: 1.6;
      overflow-x: auto;
    }

    .terminal-line {
      display: flex;
      align-items: baseline;
      gap: 0.75rem;
      margin-bottom: 0.45rem;
    }

    .terminal-line:last-child {
      margin-bottom: 0;
    }

    .line-p {
      color: var(--neo-coral);
      font-weight: 800;
      user-select: none;
      flex-shrink: 0;
    }

    .line-cmd {
      color: #FAFAFA;
      word-break: break-all;
    }

    .line-comment {
      color: #71717A;
      font-style: italic;
    }

    /* Interactive Component Showcase Grid */
    .component-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.5rem;
    }

    .comp-card {
      background: var(--neo-surface);
      border: var(--neo-border);
      box-shadow: var(--neo-shadow-md);
      border-radius: var(--neo-radius);
      padding: 1.5rem;
    }

    .comp-card h3 {
      font-family: var(--neo-font-display);
      font-size: 1.15rem;
      font-weight: 800;
      text-transform: uppercase;
      margin-bottom: 0.5rem;
    }

    .comp-card p {
      font-size: 0.85rem;
      color: var(--neo-ink-muted);
      margin-bottom: 1.25rem;
    }

    .btn-row {
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .btn-pop-yellow {
      background: var(--neo-yellow);
      color: #121212;
    }

    .btn-pop-coral {
      background: var(--neo-coral);
      color: #FAFAFA;
    }

    .btn-pop-cyan {
      background: var(--neo-cyan);
      color: #121212;
    }

    .btn-pop-lime {
      background: var(--neo-lime);
      color: #121212;
    }

    /* Interactive Neo Form Field */
    .neo-form-group {
      margin-bottom: 1rem;
    }

    .neo-label {
      display: block;
      font-family: var(--neo-font-display);
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      margin-bottom: 0.4rem;
    }

    .neo-input {
      width: 100%;
      padding: 0.65rem 0.85rem;
      background: var(--neo-surface);
      color: var(--neo-ink);
      border: var(--neo-border);
      box-shadow: 3px 3px 0 var(--neo-shadow-color);
      border-radius: var(--neo-radius);
      font-family: var(--neo-font-mono);
      font-size: 0.875rem;
      outline: none;
      transition: transform 90ms ease, box-shadow 90ms ease;
    }

    .neo-input:focus {
      box-shadow: 5px 5px 0 var(--neo-coral);
      transform: translate(-1px, -1px);
    }

    /* Accordion / FAQ */
    .neo-faq-item {
      background: var(--neo-surface);
      border: var(--neo-border);
      box-shadow: var(--neo-shadow-sm);
      border-radius: var(--neo-radius);
      margin-bottom: 1rem;
      overflow: hidden;
    }

    .neo-faq-header {
      padding: 1rem 1.25rem;
      font-family: var(--neo-font-display);
      font-size: 0.95rem;
      font-weight: 800;
      text-transform: uppercase;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
      background: var(--neo-surface);
      transition: background 120ms ease;
    }

    .neo-faq-header:hover {
      background: var(--neo-surface-elevated);
    }

    .faq-arrow {
      font-family: var(--neo-font-mono);
      font-weight: 800;
      transition: transform 180ms ease;
    }

    .neo-faq-item.open .faq-arrow {
      transform: rotate(90deg);
    }

    .neo-faq-body {
      padding: 0 1.25rem 1.25rem 1.25rem;
      font-size: 0.875rem;
      color: var(--neo-ink-muted);
      line-height: 1.6;
      display: none;
      border-top: 2px dashed var(--neo-border-color);
      margin-top: -1px;
      padding-top: 1rem;
    }

    .neo-faq-item.open .neo-faq-body {
      display: block;
    }

    /* Token Specification Table */
    .token-table-wrap {
      background: var(--neo-surface);
      border: var(--neo-border);
      box-shadow: var(--neo-shadow-lg);
      border-radius: var(--neo-radius);
      overflow-x: auto;
    }

    .neo-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }

    .neo-table th, .neo-table td {
      padding: 0.9rem 1.25rem;
      border-bottom: var(--neo-border);
      font-size: 0.85rem;
    }

    .neo-table th {
      background: var(--neo-well-bg);
      font-family: var(--neo-font-display);
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .neo-table tr:last-child td {
      border-bottom: none;
    }

    .token-code {
      font-family: var(--neo-font-mono);
      font-weight: 700;
      color: var(--neo-coral);
    }

    .swatch-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
    }

    .color-swatch {
      width: 18px;
      height: 18px;
      border: 1.5px solid #000;
      border-radius: 2px;
    }

    /* Footer (Balanced 2-column mobile architecture) */
    .neo-footer {
      background: var(--neo-surface);
      border-top: var(--neo-border);
      margin-top: 5rem;
      padding: 3rem 1.25rem 2rem 1.25rem;
    }

    .footer-inner {
      max-width: 1080px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 2.5rem;
      margin-bottom: 2.5rem;
    }

    .footer-brand h4 {
      font-family: var(--neo-font-display);
      font-size: 1.2rem;
      font-weight: 800;
      text-transform: uppercase;
      margin-bottom: 0.5rem;
    }

    .footer-brand p {
      font-size: 0.85rem;
      color: var(--neo-ink-muted);
      max-width: 380px;
      line-height: 1.6;
    }

    .footer-col h5 {
      font-family: var(--neo-font-display);
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 1rem;
      color: var(--neo-ink);
    }

    .footer-col ul {
      list-style: none;
    }

    .footer-col ul li {
      margin-bottom: 0.5rem;
    }

    .footer-col ul a {
      color: var(--neo-ink-muted);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 500;
      transition: color 90ms ease;
    }

    .footer-col ul a:hover {
      color: var(--neo-coral);
      text-decoration: underline;
    }

    .footer-bottom {
      max-width: 1080px;
      margin: 0 auto;
      padding-top: 1.5rem;
      border-top: var(--neo-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      font-size: 0.8rem;
      color: var(--neo-ink-muted);
    }

    /* Toast Notification */
    .neo-toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--neo-yellow);
      color: #121212;
      border: var(--neo-border);
      box-shadow: 4px 4px 0 var(--neo-shadow-color);
      padding: 0.65rem 1.2rem;
      border-radius: var(--neo-radius);
      font-family: var(--neo-font-display);
      font-size: 0.85rem;
      font-weight: 800;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      opacity: 0;
      transform: translateY(10px);
      transition: opacity 150ms ease, transform 150ms ease;
      pointer-events: none;
      z-index: 1000;
    }

    .neo-toast.show {
      opacity: 1;
      transform: translateY(0);
    }

    /* =========================================================
       RESPONSIVE BREAKPOINTS (FLUID & COMPACT MOBILE)
       ========================================================= */
    @media (max-width: 768px) {
      .neo-nav { padding: 0.65rem 1rem; }
      .nav-title { font-size: 0.95rem; }
      .nav-tag-badge { display: none; }
      
      .pow-hero { padding: 2.5rem 1rem 1.5rem 1rem; }
      .hero-title { font-size: clamp(1.6rem, 5.5vw, 2.3rem); }
      .hero-desc { font-size: 0.9rem; margin-bottom: 1.5rem; }

      .hero-btn-group { flex-direction: column; width: 100%; gap: 0.65rem; }
      .neo-btn { width: 100%; }

      .neo-stat-strip { grid-template-columns: repeat(2, 1fr); gap: 0.65rem; }
      .stat-val { font-size: 1.35rem; }

      .component-grid { grid-template-columns: 1fr; }

      .footer-inner {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.75rem 1.25rem;
      }
      .footer-brand {
        grid-column: 1 / -1;
        padding-bottom: 1rem;
        border-bottom: var(--neo-border);
      }
      .footer-bottom {
        flex-direction: column-reverse;
        text-align: center;
        gap: 1rem;
      }
    }

    @media (max-width: 480px) {
      .hero-title { font-size: 1.45rem; line-height: 1.18; }
      .hero-desc { font-size: 0.825rem; }
      .neo-stat-strip { grid-template-columns: 1fr 1fr; gap: 0.45rem; }
      .stat-box { padding: 0.75rem 0.5rem; }
      .stat-val { font-size: 1.2rem; }
      .stat-label { font-size: 0.65rem; }

      .section-title { font-size: 1.3rem; }
      .section-desc { font-size: 0.825rem; }

      .tab-body { padding: 1rem; }
      .terminal-content { font-size: 0.75rem; padding: 0.85rem; }

      .neo-command-pill {
        gap: 0.4rem;
        padding: 0.3rem 0.35rem 0.3rem 0.75rem;
      }
      .neo-copy-btn {
        padding: 0.35rem 0.6rem;
        font-size: 0.7rem;
      }
    }
  </style>
</head>
<body>

  <!-- Top Navigation -->
  <header class="neo-nav">
    <a href="index.html" class="nav-brand-group">
      <div class="nav-logo-box">TE</div>
      <strong class="nav-title">Taste Engine</strong>
      <span class="nav-tag-badge">Neo-Brutalism PoW</span>
    </a>
    <div class="nav-actions">
      <a href="index.html" class="neo-btn-sm" title="Back to main gallery">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        <span>All 10 Styles</span>
      </a>
      <button class="neo-btn-sm" id="themeToggleBtn" aria-label="Toggle theme">
        <span id="themeLabel">☀️ LIGHT</span>
      </button>
    </div>
  </header>

  <main>
    <!-- Opening Hero Viewport -->
    <section class="pow-hero">
      <div class="hero-sticker-badge">
        <span>★ Proof of Work: Archetype #02</span>
      </div>

      <h1 class="hero-title">
        Loud, Tactile & <span class="highlight">Unapologetic.</span>
      </h1>

      <p class="hero-desc">
        This entire page is generated directly using Taste Engine’s <strong>Neo-Brutalism</strong> design DNA. Experience authentic 2.5px solid strokes, 0-blur mechanical offset shadows, and zero AI-slop firsthand.
      </p>

      <!-- Single-Line Inline Command Pill ("Sejajarin") -->
      <div class="neo-command-pill">
        <span class="neo-prompt">$</span>
        <code class="neo-code" id="heroCmdText">npx skills add kennedys0/taste-style-neo-brutalism</code>
        <button class="neo-copy-btn" id="heroCopyBtn" aria-label="Copy command">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          <span>COPY</span>
        </button>
      </div>

      <div class="hero-btn-group">
        <a href="#install" class="neo-btn neo-btn-primary">
          <span>Installation Guide ↓</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 13l5 5 5-5M12 6v12"/></svg>
        </a>
        <a href="#playground" class="neo-btn neo-btn-secondary">
          <span>Test Interactive UI →</span>
        </a>
      </div>

      <!-- 4-Stat Strip -->
      <div class="neo-stat-strip">
        <div class="stat-box">
          <div class="stat-val">2.5px</div>
          <div class="stat-label">Solid Ink Stroke</div>
        </div>
        <div class="stat-box">
          <div class="stat-val">0px Blur</div>
          <div class="stat-label">Hard Offset Shadow</div>
        </div>
        <div class="stat-box">
          <div class="stat-val">130ms</div>
          <div class="stat-label">Mechanical Press</div>
        </div>
        <div class="stat-box">
          <div class="stat-val">WCAG AA</div>
          <div class="stat-label">Contrast Gated</div>
        </div>
      </div>
    </section>

    <!-- Interactive Installation Guide Section -->
    <section class="neo-section" id="install">
      <div class="section-header">
        <span class="section-badge">How to Install</span>
        <h2 class="section-title">Install Neo-Brutalism or Full Engine</h2>
        <p class="section-desc">
          Choose whether you want this single standalone Neo-Brutalism skill or the full 10-style automated Taste Engine suite for your AI coding agents.
        </p>
      </div>

      <div class="neo-card">
        <!-- Tab Headers -->
        <div class="tab-header-strip">
          <button class="tab-switch-btn active" data-tab="tab-standalone">1. Standalone Style Skill</button>
          <button class="tab-switch-btn" data-tab="tab-global">2. Full Taste Engine (Global)</button>
          <button class="tab-switch-btn" data-tab="tab-tailwind">3. Tailwind & shadcn Preset</button>
        </div>

        <!-- Tab 1: Standalone Skill -->
        <div class="tab-body active" id="tab-standalone">
          <h3 class="install-step-title">Option A: Install Dedicated Neo-Brutalism Skill</h3>
          <p class="install-step-desc">
            Installs only the Neo-Brutalism style pack. Perfect if your project has already committed to this exact aesthetic and does not need a 10-style selector.
          </p>

          <div class="neo-terminal">
            <div class="terminal-topbar">
              <div class="terminal-dots">
                <span class="dot red"></span>
                <span class="dot yellow"></span>
                <span class="dot green"></span>
              </div>
              <span class="terminal-label">bash — universal agent skills cli</span>
              <button class="neo-btn-sm" onclick="copySnippet('cmdStandaloneCli')">Copy</button>
            </div>
            <div class="terminal-content" id="cmdStandaloneCli">
              <div class="terminal-line">
                <span class="line-comment"># Install standalone Neo-Brutalism pack via Agent Skills CLI</span>
              </div>
              <div class="terminal-line">
                <span class="line-p">$</span>
                <span class="line-cmd">npx skills add kennedys0/taste-engine --skill taste-style-neo-brutalism</span>
              </div>
              <div class="terminal-line">
                <span class="line-comment"># Or install directly for Antigravity IDE global config</span>
              </div>
              <div class="terminal-line">
                <span class="line-p">$</span>
                <span class="line-cmd">git clone https://github.com/kennedys0/taste-engine.git && cp -r taste-engine/optional-standalone-skills/taste-style-neo-brutalism ~/.gemini/config/skills/</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Tab 2: Global Engine -->
        <div class="tab-body" id="tab-global">
          <h3 class="install-step-title">Option B: Install Full Taste Engine (All 10 Styles + SEO + Anti-Slop)</h3>
          <p class="install-step-desc">
            Equips your AI agent with the autonomous style router, preflight interviews, 10 aesthetic packs, full-screen hero gating, and automatic SEO audit.
          </p>

          <div class="neo-terminal">
            <div class="terminal-topbar">
              <div class="terminal-dots">
                <span class="dot red"></span>
                <span class="dot yellow"></span>
                <span class="dot green"></span>
              </div>
              <span class="terminal-label">bash — multi-agent native installer</span>
              <button class="neo-btn-sm" onclick="copySnippet('cmdGlobalCli')">Copy</button>
            </div>
            <div class="terminal-content" id="cmdGlobalCli">
              <div class="terminal-line">
                <span class="line-comment"># 1. Universal 1-click Agent Skills install</span>
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
              <div class="terminal-line">
                <span class="line-p">$</span>
                <span class="line-cmd">node bin/taste-engine.mjs install --agent codex --global</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Tab 3: Tailwind & shadcn -->
        <div class="tab-body" id="tab-tailwind">
          <h3 class="install-step-title">Option C: Tailwind CSS & shadcn/ui Preset</h3>
          <p class="install-step-desc">
            Scaffold Neo-Brutalism utility tokens directly into your React, Next.js, or Vite frontend stack.
          </p>

          <div class="neo-terminal">
            <div class="terminal-topbar">
              <div class="terminal-dots">
                <span class="dot red"></span>
                <span class="dot yellow"></span>
                <span class="dot green"></span>
              </div>
              <span class="terminal-label">tailwind.config.js — preset integration</span>
              <button class="neo-btn-sm" onclick="copySnippet('cmdTailwindPreset')">Copy</button>
            </div>
            <div class="terminal-content" id="cmdTailwindPreset">
              <div class="terminal-line">
                <span class="line-comment">// Add to your Tailwind config or copy presets/tailwind/</span>
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
                <span class="line-cmd">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boxShadow: { 'neo': '5px 5px 0 #121212', 'neo-active': '1px 1px 0 #121212' },</span>
              </div>
              <div class="terminal-line">
                <span class="line-cmd">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;borderWidth: { 'neo': '2.5px' }</span>
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
    </section>

    <!-- Interactive Component Playground (PoW) -->
    <section class="neo-section" id="playground">
      <div class="section-header">
        <span class="section-badge">Live Interactive PoW</span>
        <h2 class="section-title">Neo-Brutalist Component Lab</h2>
        <p class="section-desc">
          Test interactive mechanical buttons, accessible form controls, and responsive cards built to strict Taste Engine fidelity rules.
        </p>
      </div>

      <div class="component-grid">
        <!-- Card 1: Button Physics -->
        <div class="comp-card">
          <h3>1. Mechanical Button Physics</h3>
          <p>Click these buttons to feel the 130ms physical 2px displacement and shadow collapse along the axis.</p>
          <div class="btn-row">
            <button class="neo-btn btn-pop-yellow" onclick="handleBtnClick('Yellow Pop')">Yellow Pop</button>
            <button class="neo-btn btn-pop-coral" onclick="handleBtnClick('Coral Action')">Coral Action</button>
            <button class="neo-btn btn-pop-cyan" onclick="handleBtnClick('Cyan Signal')">Cyan Signal</button>
            <button class="neo-btn btn-pop-lime" onclick="handleBtnClick('Lime Confirm')">Lime Confirm</button>
          </div>
        </div>

        <!-- Card 2: Interactive Input -->
        <div class="comp-card">
          <h3>2. High-Contrast Form Controls</h3>
          <p>Inputs feature solid strokes and hard offset glow that tightens on focus without fuzzy halos.</p>
          <div class="neo-form-group">
            <label class="neo-label" for="sampleInput">PROJECT REPOSITORY NAME</label>
            <input type="text" id="sampleInput" class="neo-input" value="kennedys0/taste-engine">
          </div>
          <button class="neo-btn neo-btn-primary" style="width: 100%; justify-content: center;" onclick="handleBtnClick('Saved to Registry')">Save Component State</button>
        </div>
      </div>
    </section>

    <!-- Design Token Cheatsheet -->
    <section class="neo-section">
      <div class="section-header">
        <span class="section-badge">Tokens & Math</span>
        <h2 class="section-title">Neo-Brutalism Design Tokens</h2>
        <p class="section-desc">
          Standardized CSS custom properties for instant copy-pasting into any stylesheet.
        </p>
      </div>

      <div class="token-table-wrap">
        <table class="neo-table">
          <thead>
            <tr>
              <th>Token Name</th>
              <th>Light Mode</th>
              <th>Dark Mode</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="token-code">--taste-neo-bg</td>
              <td><span class="swatch-pill"><span class="color-swatch" style="background:#FFFDF7"></span>#FFFDF7</span></td>
              <td><span class="swatch-pill"><span class="color-swatch" style="background:#18181B"></span>#18181B</span></td>
              <td>Canvas backdrop base</td>
            </tr>
            <tr>
              <td class="token-code">--taste-neo-card-bg</td>
              <td><span class="swatch-pill"><span class="color-swatch" style="background:#FFFFFF"></span>#FFFFFF</span></td>
              <td><span class="swatch-pill"><span class="color-swatch" style="background:#222227"></span>#222227</span></td>
              <td>Card surface background</td>
            </tr>
            <tr>
              <td class="token-code">--taste-neo-ink</td>
              <td><span class="swatch-pill"><span class="color-swatch" style="background:#121212"></span>#121212</span></td>
              <td><span class="swatch-pill"><span class="color-swatch" style="background:#FAFAFA"></span>#FAFAFA</span></td>
              <td>Primary text & icon color</td>
            </tr>
            <tr>
              <td class="token-code">--taste-neo-border</td>
              <td>2.5px solid #121212</td>
              <td>2.5px solid #FAFAFA</td>
              <td>Crisp high-contrast structural stroke</td>
            </tr>
            <tr>
              <td class="token-code">--taste-neo-shadow</td>
              <td>5px 5px 0 #121212</td>
              <td>5px 5px 0 #FAFAFA</td>
              <td>0-blur sharp directional shadow</td>
            </tr>
            <tr>
              <td class="token-code">--taste-neo-accent</td>
              <td><span class="swatch-pill"><span class="color-swatch" style="background:#FFE600"></span>#FFE600</span></td>
              <td><span class="swatch-pill"><span class="color-swatch" style="background:#FFE600"></span>#FFE600</span></td>
              <td>Electric canary primary action</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- FAQ Accordion -->
    <section class="neo-section">
      <div class="section-header">
        <span class="section-badge">FAQ & Verification</span>
        <h2 class="section-title">Frequently Asked Questions</h2>
      </div>

      <div class="neo-faq-item open">
        <div class="neo-faq-header" onclick="toggleFaq(this)">
          <span>Why is this Proof of Work built in Neo-Brutalism?</span>
          <span class="faq-arrow">▶</span>
        </div>
        <div class="neo-faq-body">
          Taste Engine operates on the principle that aesthetic fidelity must be recognizable from the rendered interface. By building this entire installation guide in Neo-Brutalism, you can directly verify the physics, contrast pairing, and lack of AI-slop before adopting the skill into your agents.
        </div>
      </div>

      <div class="neo-faq-item">
        <div class="neo-faq-header" onclick="toggleFaq(this)">
          <span>Can I use Neo-Brutalism without installing the other 9 styles?</span>
          <span class="faq-arrow">▶</span>
        </div>
        <div class="neo-faq-body">
          Yes! Run <code>npx skills add kennedys0/taste-engine --skill taste-style-neo-brutalism</code> to install only this standalone style pack. It provides full typography, colors, and recipes without the 10-style selector router.
        </div>
      </div>

      <div class="neo-faq-item">
        <div class="neo-faq-header" onclick="toggleFaq(this)">
          <span>How does Dark Mode handle hard shadows without collision?</span>
          <span class="faq-arrow">▶</span>
        </div>
        <div class="neo-faq-body">
          In dark mode, Neo-Brutalism flips both borders and 0-blur offset shadows from black to stark white (<code>#FAFAFA</code>) or vivid yellow. This ensures zero black-on-black collision and preserves tactile depth on dark surfaces.
        </div>
      </div>
    </section>
  </main>

  <!-- Site Footer (2-column balanced mobile grid) -->
  <footer class="neo-footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <h4>Taste Engine</h4>
        <p>Open-source frontend design intelligence pack for AI coding agents. Elevate design fidelity, eliminate AI-slop, and enforce contrast safety.</p>
        <p style="margin-top: 0.5rem; font-size: 0.775rem;">Created by <a href="https://github.com/kennedys0" target="_blank" rel="noopener" style="color: var(--neo-coral); font-weight: 700;">Mochamad Vikry (@kennedys0)</a></p>
      </div>

      <div class="footer-col">
        <h5>Aesthetic Archetypes</h5>
        <ul>
          <li><a href="index.html#showcase">Bento Grid</a></li>
          <li><a href="neo-brutalism.html">Neo-Brutalism (PoW)</a></li>
          <li><a href="index.html#showcase">Claymorphism</a></li>
          <li><a href="index.html#showcase">Data Cockpit</a></li>
          <li><a href="index.html#showcase">Cyberpunk HUD</a></li>
          <li><a href="index.html#showcase">Swiss Editorial</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h5>Navigation & Source</h5>
        <ul>
          <li><a href="index.html">Main Style Gallery</a></li>
          <li><a href="index.html#installation">Installation Guide</a></li>
          <li><a href="index.html#tokens">Token Matrix</a></li>
          <li><a href="https://github.com/kennedys0/taste-engine" target="_blank" rel="noopener">GitHub Repository</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <p>&copy; 2026 Mochamad Vikry. Released under the MIT License.</p>
      <a href="#" class="neo-btn-sm" style="text-decoration:none;">
        <span>↑ Back to Top</span>
      </a>
    </div>
  </footer>

  <!-- Neo Toast Notification -->
  <div class="neo-toast" id="neoToast">
    <span id="toastMsg">COPIED TO CLIPBOARD</span>
  </div>

  <script>
    // Theme Toggling with LocalStorage Persistence
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const themeLabel = document.getElementById('themeLabel');
    const htmlEl = document.documentElement;

    function applyTheme(theme) {
      htmlEl.setAttribute('data-theme', theme);
      localStorage.setItem('taste-theme-pow', theme);
      if (theme === 'dark') {
        themeLabel.textContent = '☀️ LIGHT';
      } else {
        themeLabel.textContent = '🌙 DARK';
      }
    }

    const savedTheme = localStorage.getItem('taste-theme-pow') || 'dark';
    applyTheme(savedTheme);

    themeToggleBtn.addEventListener('click', () => {
      const current = htmlEl.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      showToast(`Switched to ${next.toUpperCase()} mode`);
    });

    // Toast Notification Utility
    let toastTimeout;
    function showToast(msg) {
      const toast = document.getElementById('neoToast');
      const toastMsg = document.getElementById('toastMsg');
      toastMsg.textContent = msg;
      toast.classList.add('show');
      clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {
        toast.classList.remove('show');
      }, 2200);
    }

    // Hero Quick Copy Button
    const heroCopyBtn = document.getElementById('heroCopyBtn');
    const heroCmdText = document.getElementById('heroCmdText');
    if (heroCopyBtn && heroCmdText) {
      heroCopyBtn.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(heroCmdText.textContent.trim());
          showToast('Copied installation command!');
        } catch (e) {
          showToast('Command copied');
        }
      });
    }

    // Tab Switcher
    const tabButtons = document.querySelectorAll('.tab-switch-btn');
    const tabBodies = document.querySelectorAll('.tab-body');

    tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        tabButtons.forEach(b => b.classList.remove('active'));
        tabBodies.forEach(b => b.classList.remove('active'));

        btn.classList.add('active');
        const targetId = btn.getAttribute('data-tab');
        const targetBody = document.getElementById(targetId);
        if (targetBody) targetBody.classList.add('active');
      });
    });

    // Snippet Copier
    async function copySnippet(elemId) {
      const el = document.getElementById(elemId);
      if (!el) return;
      const text = el.innerText.trim();
      try {
        await navigator.clipboard.writeText(text);
        showToast('Terminal snippet copied!');
      } catch (e) {
        showToast('Snippet copied');
      }
    }

    // Component Button Click Handler
    function handleBtnClick(name) {
      showToast(`Clicked: ${name}`);
    }

    // FAQ Accordion Toggle
    function toggleFaq(header) {
      const item = header.parentElement;
      item.classList.toggle('open');
    }
  </script>
</body>
</html>
"""

OUT_FILE.write_text(HTML_CONTENT, encoding="utf-8")
print(f"PASS: successfully generated {OUT_FILE} ({len(HTML_CONTENT)} bytes)")

