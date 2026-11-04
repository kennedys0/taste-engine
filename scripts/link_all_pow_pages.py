#!/usr/bin/env python3
"""Link all 10 PoW pages on showcase cards and footer in docs/index.html."""
from pathlib import Path
import re

INDEX_FILE = Path("docs/index.html")
text = INDEX_FILE.read_text(encoding="utf-8")

# 1. Add CSS for .pow-link-btn and .showcase-actions
css_target = ".copy-token-btn {"
css_addition = """    .showcase-actions {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .pow-link-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: var(--shell-surface-elevated);
      color: var(--shell-accent);
      border: 1px solid var(--shell-border);
      border-radius: var(--shell-radius-pill);
      padding: 0.35rem 0.8rem;
      font-size: 0.75rem;
      font-weight: 700;
      text-decoration: none;
      box-shadow: var(--shell-shadow-sm);
      transition: all 120ms ease;
      white-space: nowrap;
    }

    .pow-link-btn:hover {
      background: var(--shell-surface-hover);
      border-color: var(--shell-accent);
      transform: translateY(-1px);
    }

    .copy-token-btn {"""

if ".pow-link-btn {" not in text:
    text = text.replace(css_target, css_addition, 1)
    print("Added .pow-link-btn CSS")

# 2. Add PoW Guide link to each showcase card header
STYLES = [
    "bento", "brutalism", "claymorphism", "enterprise", "glassmorphism",
    "minimalism", "neo-brutalism", "retro-terminal", "skeuomorphism", "swiss-editorial"
]

for s in STYLES:
    pattern = rf'(<article class="showcase-card" data-style="{s}">\s*<div class="showcase-header">[\s\S]*?)(<button class="copy-token-btn")'
    match = re.search(pattern, text)
    if match and f'href="{s}.html"' not in match.group(0):
        replacement = match.group(1) + f'<div class="showcase-actions">\n          <a href="{s}.html" class="pow-link-btn">PoW Guide &rarr;</a>\n          ' + match.group(2)
        text = text.replace(match.group(0), replacement, 1)
        # also close the .showcase-actions wrapper after </button>
        # find where button ends
        btn_end = text.find('</button>', text.find(f'data-style="{s}"'))
        if btn_end != -1:
            text = text[:btn_end+9] + '\n        </div>' + text[btn_end+9:]
        print(f"Linked {s}.html in showcase header")

# 3. Update footer links to point to PoW pages
old_footer_links = """        <h4>Aesthetic Archetypes</h4>
        <ul>
          <li><a href="#showcase">Bento Grid</a></li>
          <li><a href="#showcase">Neo-Brutalism</a></li>
          <li><a href="#showcase">Claymorphism</a></li>
          <li><a href="#showcase">Data Cockpit</a></li>
          <li><a href="#showcase">Cyberpunk HUD</a></li>
          <li><a href="#showcase">Swiss Editorial</a></li>
        </ul>"""

new_footer_links = """        <h4>Aesthetic Archetypes (PoW)</h4>
        <ul>
          <li><a href="bento.html">Bento Grid (PoW)</a></li>
          <li><a href="neo-brutalism.html">Neo-Brutalism (PoW)</a></li>
          <li><a href="claymorphism.html">Claymorphism (PoW)</a></li>
          <li><a href="enterprise.html">Enterprise (PoW)</a></li>
          <li><a href="glassmorphism.html">Glassmorphism (PoW)</a></li>
          <li><a href="minimalism.html">Minimalism (PoW)</a></li>
          <li><a href="retro-terminal.html">Retro Terminal (PoW)</a></li>
          <li><a href="skeuomorphism.html">Skeuomorphism (PoW)</a></li>
          <li><a href="swiss-editorial.html">Swiss Editorial (PoW)</a></li>
          <li><a href="brutalism.html">Brutalism (PoW)</a></li>
        </ul>"""

if old_footer_links in text:
    text = text.replace(old_footer_links, new_footer_links, 1)
    print("Updated footer links in docs/index.html")

INDEX_FILE.write_text(text, encoding="utf-8")
print("SUCCESS: docs/index.html successfully updated with PoW links.")

