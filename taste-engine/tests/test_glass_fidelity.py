from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]

class GlassFidelityTests(unittest.TestCase):
    def test_pack_requires_visible_material(self):
        text = (BASE / 'styles/glassmorphism.md').read_text()
        for token in ('Glass material fidelity gate', 'backdrop-filter', 'frost', 'light', 'dark', 'viewport', 'FAIL'):
            with self.subTest(token=token):
                self.assertIn(token.lower(), text.lower())

    def test_light_dark_recipe_and_fallback(self):
        css = (BASE / 'examples/glassmorphism/frosted-surfaces.css').read_text()
        for token in ('data-glass-theme="dark"', 'backdrop-filter:', '-webkit-backdrop-filter:', '@supports not', 'prefers-reduced-transparency', 'prefers-reduced-motion', ':focus-visible'):
            with self.subTest(token=token):
                self.assertIn(token, css)

    def test_gradient_is_explicit_exception_not_blanket_style(self):
        text = (BASE / 'styles/glassmorphism.md').read_text().lower()
        for token in ('explicit background gradient exception', 'radial-gradient', 'anti-slop', 'material purpose', 'performance and accessibility'):
            with self.subTest(token=token): self.assertIn(token, text)
        universal = (BASE / 'references/anti-slop.md').read_text().lower()
        self.assertIn('glassmorphism explicitly permits', universal)

    def test_gradient_examples_are_real_and_static(self):
        css = (BASE / 'examples/glassmorphism/frosted-surfaces.css').read_text()
        self.assertIn('radial-gradient', css)
        self.assertIn('linear-gradient', css)
        self.assertNotIn('@keyframes', css)

    def test_acceptance_checks_present(self):
        check = (BASE / 'tests/glassmorphism-visual.md').read_text()
        self.assertIn('flat navy', check)
        self.assertIn('320, 390, 768, 1440', check)

if __name__ == '__main__':
    unittest.main()
