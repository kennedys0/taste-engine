from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]

class ArtDecoFidelityTests(unittest.TestCase):
    def test_pack_requires_geometric_architectural_material(self):
        text = (BASE / 'styles/art-deco.md').read_text(encoding='utf-8')
        for token in ('Art Deco material fidelity gate', 'architectural', 'symmetry', 'stepped', 'FAIL', 'viewport', 'metallic'):
            with self.subTest(token=token):
                self.assertIn(token.lower(), text.lower())

    def test_recipe_and_tokens(self):
        css = (BASE / 'examples/art-deco/geometric-surfaces.css').read_text(encoding='utf-8')
        for token in ('--taste-deco-bg', '--taste-deco-accent', '--taste-deco-border', 'prefers-reduced-motion', ':focus-visible', '.taste-deco-btn', '.taste-deco-card'):
            with self.subTest(token=token):
                self.assertIn(token, css)

    def test_art_deco_ornamentation_is_explicit_exception_not_blanket_slop(self):
        text = (BASE / 'styles/art-deco.md').read_text(encoding='utf-8').lower()
        for token in ('explicit art deco ornamentation exception', 'structured geometry', 'anti-slop'):
            with self.subTest(token=token):
                self.assertIn(token, text)
        universal = (BASE / 'references/anti-slop.md').read_text(encoding='utf-8').lower()
        self.assertIn('art deco:', universal)

    def test_three_expressions_and_palettes_included(self):
        text = (BASE / 'styles/art-deco.md').read_text(encoding='utf-8').lower()
        for token in ('modern deco', 'classic deco', 'minimal deco', '#24453d', '#b69a68', '#171715', '#b89b5e', '#693b43', '#a98462'):
            with self.subTest(token=token):
                self.assertIn(token, text)

    def test_acceptance_checks_present(self):
        check = (BASE / 'tests/art-deco-visual.md').read_text(encoding='utf-8')
        for token in ('320, 390, 768', 'Pass the material when', 'Fail the style when', 'stepped'):
            with self.subTest(token=token):
                self.assertIn(token, check)

    def test_standalone_sync(self):
        canonical = (BASE / 'styles/art-deco.md').read_text(encoding='utf-8')
        standalone_path = BASE.parent / 'optional-standalone-skills' / 'taste-style-art-deco' / 'SKILL.md'
        self.assertTrue(standalone_path.is_file(), "Standalone skill must exist")
        standalone = standalone_path.read_text(encoding='utf-8')
        before_part = canonical.split('## Anti-slop: style-specific')[0].strip()
        after_part = ('## Anti-slop: style-specific' + canonical.split('## Anti-slop: style-specific')[1]).strip()
        self.assertIn(before_part, standalone)
        self.assertIn(after_part, standalone)

if __name__ == '__main__':
    unittest.main()

