#!/usr/bin/env python3
"""
Test suite verifying the Proof-of-Work (PoW) showcase architectural contract
and preset invariants across the template and live documentation pages.
"""
from pathlib import Path
import unittest
import json

class TestPoWShowcaseStructure(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[1]
        self.project_root = self.root.parent
        self.template_path = self.root / 'presets' / 'templates' / 'pow-showcase.template.html'
        self.reference_path = self.root / 'references' / 'pow-showcase-structure.md'
        self.min_doc_path = self.project_root / 'docs' / 'minimalism.html'
        self.pixel_doc_path = self.project_root / 'docs' / 'retro-pixel.html'
        self.brutalism_doc_path = self.project_root / 'docs' / 'brutalism.html'
        registry_path = self.root / 'styles' / 'registry.json'
        self.registry = json.loads(registry_path.read_text(encoding='utf-8'))

    def test_preset_template_and_reference_exist(self):
        self.assertTrue(self.template_path.is_file(), "pow-showcase.template.html must exist")
        self.assertTrue(self.reference_path.is_file(), "pow-showcase-structure.md must exist")

    def test_template_contains_7_canonical_sections(self):
        content = self.template_path.read_text(encoding='utf-8')
        # Section 1: Header
        self.assertIn('pow-header', content)
        self.assertIn('pow-drawer-panel', content)
        # Section 2: Hero
        self.assertIn('id="hero"', content)
        self.assertIn('pow-hero-cmd', content)
        # Section 3: Interactive Studio
        self.assertIn('id="studio"', content)
        self.assertIn('pow-window-dots', content)
        # Section 4: Components
        self.assertIn('id="components"', content)
        # Section 5: Tabbed Terminal Installation
        self.assertIn('id="install"', content)
        self.assertIn('tabbed-terminal-card', content)
        self.assertIn('terminal-tab-bar', content)
        # Section 6: Core Principles
        self.assertIn('id="principles"', content)
        # Section 7: Canonical Footer
        self.assertIn('pow-footer', content)
        self.assertIn('pow-footer-grid', content)

    def test_terminal_prevents_copy_button_overlap(self):
        content = self.template_path.read_text(encoding='utf-8')
        # Terminal header must contain the copy button
        self.assertIn('terminal-header', content)
        self.assertIn('terminal-copy-btn', content)
        # Tab panes must be isolated
        self.assertIn('tab-standalone', content)
        self.assertIn('tab-global', content)
        self.assertIn('tab-presets', content)

    def test_minimalism_pow_satisfies_contract(self):
        if not self.min_doc_path.is_file():
            self.skipTest("docs/minimalism.html not present")
        content = self.min_doc_path.read_text(encoding='utf-8')
        self.assertIn('tabbed-terminal-card', content)
        self.assertIn('terminal-tab-bar', content)
        self.assertIn('terminal-copy-btn', content)
        self.assertIn('switchInstallTab', content)
        self.assertIn('agent-support-strip', content)

    def test_retro_pixel_pow_satisfies_contract(self):
        if not self.pixel_doc_path.is_file():
            self.skipTest("docs/retro-pixel.html not present")
        content = self.pixel_doc_path.read_text(encoding='utf-8')
        self.assertIn('tabbed-terminal-card', content)
        self.assertIn('terminal-tab-bar', content)
        self.assertIn('terminal-copy-btn', content)
        self.assertIn('switchInstallTab', content)
        self.assertIn('agent-support-strip', content)

    def test_brutalism_pow_satisfies_contract(self):
        if not self.brutalism_doc_path.is_file():
            self.skipTest("docs/brutalism.html not present")
        content = self.brutalism_doc_path.read_text(encoding='utf-8')
        # Section 1: Header
        self.assertIn('pow-header', content)
        # Section 2: Hero with dual variants
        self.assertIn('id="hero"', content)
        self.assertIn('pow-hero', content)
        self.assertIn('hero-view-raw', content)
        self.assertIn('hero-view-bento', content)
        self.assertIn('brut-hero-action-btn', content)
        self.assertIn('switchBrutalismDocVariant', content)
        # Section 3: Interactive Studio
        self.assertIn('id="studio"', content)
        self.assertIn('pow-studio', content)
        # Section 4: Component Anatomy & Gates
        self.assertIn('id="components"', content)
        self.assertIn('pow-components', content)
        # Section 5: Tabbed Terminal Installation
        self.assertIn('id="install"', content)
        self.assertIn('pow-install', content)
        self.assertIn('tabbed-terminal-card', content)
        self.assertIn('terminal-tab-bar', content)
        self.assertIn('terminal-copy-btn', content)
        self.assertIn('switchInstallTab', content)
        self.assertIn('agent-support-strip', content)
        # Section 6: Core Architectural Principles
        self.assertIn('id="principles"', content)
        self.assertIn('pow-principles', content)
        # Section 7: Responsive Footer
        self.assertIn('pow-footer', content)
        self.assertIn('pow-footer-grid', content)
        # Invariant: 10 canonical styles linked in footer
        expected_styles = [
            'minimalism.html', 'retro-pixel.html', 'claymorphism.html',
            'glassmorphism.html', 'neo-brutalism.html', 'bento.html',
            'skeuomorphism.html', 'editorial.html', 'brutalism.html',
            'retro-terminal.html'
        ]
        for s in expected_styles:
            self.assertIn(s, content, f"docs/brutalism.html must link to {s}")

    def test_canonical_10_styles_in_footer(self):
        content = self.template_path.read_text(encoding='utf-8')
        expected_styles = [
            'minimalism.html', 'retro-pixel.html', 'claymorphism.html',
            'glassmorphism.html', 'neo-brutalism.html', 'bento.html',
            'skeuomorphism.html', 'editorial.html', 'brutalism.html',
            'retro-terminal.html'
        ]
        for style_href in expected_styles:
            self.assertIn(style_href, content, f"Template footer must link to {style_href}")

    def test_uniform_navigation_button_height_preset(self):
        content = self.template_path.read_text(encoding='utf-8')
        # Checks that uniform 36px or --pow-btn-h is defined
        self.assertIn('--pow-btn-h: 36px', content)
        self.assertIn('height: var(--pow-btn-h)', content)
        self.assertIn('aspect-ratio: 1 / 1', content)

if __name__ == '__main__':
    unittest.main()

