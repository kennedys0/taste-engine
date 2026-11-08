from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]

class GlassFidelityTests(unittest.TestCase):
    """Legacy glassmorphism pack is a redirect to frutiger-aero (variant glass);
    the canonical fidelity gate lives in frutiger-aero.md."""

    def test_legacy_pack_is_redirect_stub(self):
        text = (BASE / 'styles/glassmorphism.md').read_text(encoding='utf-8')
        for token in ('Redirect', 'frutiger-aero.md', 'variant', 'glass'):
            with self.subTest(token=token):
                self.assertIn(token.lower(), text.lower())
        # A stub must not pretend to be a full pack.
        self.assertNotIn('## Style-specific quality gate', text)
        self.assertLess(len(text), 2000)

    def test_canonical_gate_requires_visible_material(self):
        text = (BASE / 'styles/frutiger-aero.md').read_text(encoding='utf-8')
        for token in ('Frutiger Aero material fidelity gate', 'backdrop-filter', 'aqua', 'viewport', 'FAIL'):
            with self.subTest(token=token):
                self.assertIn(token.lower(), text.lower())

    def test_light_dark_recipe_and_fallback(self):
        css = (BASE / 'examples/glassmorphism/frosted-surfaces.css').read_text(encoding='utf-8')
        for token in ('data-glass-theme="dark"', 'backdrop-filter:', '-webkit-backdrop-filter:', '@supports not', 'prefers-reduced-transparency', 'prefers-reduced-motion', ':focus-visible'):
            with self.subTest(token=token):
                self.assertIn(token, css)

    def test_gradient_is_explicit_exception_not_blanket_style(self):
        text = (BASE / 'styles/frutiger-aero.md').read_text(encoding='utf-8').lower()
        for token in ('explicit frutiger aero material exception', 'material-enabling properties'):
            with self.subTest(token=token):
                self.assertIn(token, text)
        universal = (BASE / 'references/anti-slop.md').read_text(encoding='utf-8').lower()
        self.assertIn('glassmorphism explicitly permits', universal)

    def test_gradient_examples_are_real_and_static(self):
        css = (BASE / 'examples/glassmorphism/frosted-surfaces.css').read_text(encoding='utf-8')
        self.assertIn('radial-gradient', css)
        self.assertIn('linear-gradient', css)
        self.assertNotIn('@keyframes', css)

    def test_acceptance_checks_present(self):
        check = (BASE / 'tests/glassmorphism-visual.md').read_text(encoding='utf-8')
        self.assertIn('flat navy', check)
        self.assertIn('320, 390, 768, 1440', check)

if __name__ == '__main__':
    unittest.main()
