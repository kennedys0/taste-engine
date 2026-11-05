from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]

class ClayFidelityTests(unittest.TestCase):
    def test_pack_requires_visible_sculpted_material(self):
        text = (BASE / 'styles/claymorphism.md').read_text(encoding='utf-8')
        for token in ('Clay material fidelity gate', 'dual inner shadow', 'tactile', 'viewport', 'FAIL', 'inset', 'compression'):
            with self.subTest(token=token):
                self.assertIn(token.lower(), text.lower())

    def test_sculpted_recipe_and_tokens(self):
        css = (BASE / 'examples/claymorphism/sculpted-surfaces.css').read_text(encoding='utf-8')
        for token in ('--taste-clay-inner-primary', '--taste-clay-inner-light', '--taste-clay-inner-well', 'inset', 'prefers-reduced-motion', ':focus-visible', '.taste-clay-btn-primary', '.taste-clay-input-wrapper'):
            with self.subTest(token=token):
                self.assertIn(token, css)

    def test_clay_depth_is_explicit_exception_not_blanket_slop(self):
        text = (BASE / 'styles/claymorphism.md').read_text(encoding='utf-8').lower()
        for token in ('explicit clay depth exception', 'dual inner shadow', 'anti-slop', 'tactile depth'):
            with self.subTest(token=token):
                self.assertIn(token, text)
        universal = (BASE / 'references/anti-slop.md').read_text(encoding='utf-8').lower()
        self.assertIn('claymorphism explicitly permits', universal)

    def test_reference_palette_and_polarity_included(self):
        text = (BASE / 'styles/claymorphism.md').read_text(encoding='utf-8').lower()
        for token in ('#813ffc', '#ecebf5', '#d7d1f1', 'sunken', 'relief', 'submit', 'go back'):
            with self.subTest(token=token):
                self.assertIn(token, text)

    def test_acceptance_checks_present(self):
        check = (BASE / 'tests/claymorphism-visual.md').read_text(encoding='utf-8')
        for token in ('320, 390, 768', 'Submit >', 'Go Back', 'dual inner shadow', 'Pass the material when'):
            with self.subTest(token=token):
                self.assertIn(token, check)

if __name__ == '__main__':
    unittest.main()
