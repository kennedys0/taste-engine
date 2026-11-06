from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]

class Y2KFidelityTests(unittest.TestCase):
    def test_pack_requires_metallic_chrome_material(self):
        text = (BASE / 'styles/y2k-futurism.md').read_text(encoding='utf-8')
        for token in ('Y2K Futurism material fidelity gate', 'chrome', 'Chrome', 'Holographic', 'Retro Tech', 'first viewport', 'FAIL'):
            with self.subTest(token=token):
                self.assertIn(token.lower(), text.lower())

    def test_recipe_and_tokens(self):
        css = (BASE / 'examples/y2k-futurism/metallic-surfaces.css').read_text(encoding='utf-8')
        for token in ('--taste-y2k-silver', '--taste-y2k-chrome', '--taste-y2k-violet', 'prefers-reduced-motion', ':focus-visible', '.taste-y2k-btn', '.taste-y2k-card'):
            with self.subTest(token=token):
                self.assertIn(token, css)

    def test_y2k_chrome_is_explicit_exception_not_blanket_slop(self):
        text = (BASE / 'styles/y2k-futurism.md').read_text(encoding='utf-8').lower()
        for token in ('explicit y2k futurism material exception', 'chrome', 'anti-slop'):
            with self.subTest(token=token):
                self.assertIn(token, text)
        universal = (BASE / 'references/anti-slop.md').read_text(encoding='utf-8').lower()
        self.assertIn('y2k futurism', universal)

    def test_three_expressions_and_palettes_included(self):
        text = (BASE / 'styles/y2k-futurism.md').read_text(encoding='utf-8').lower()
        for token in ('chrome', 'holographic', 'retro tech', '#c5cbd3', '#f1f3f6', '#252833', '#8865dd', '#8fcfe9', '#e6abd8', '#181821'):
            with self.subTest(token=token):
                self.assertIn(token, text)

    def test_acceptance_checks_present(self):
        check = (BASE / 'tests/y2k-futurism-visual.md').read_text(encoding='utf-8')
        for token in ('320, 390, 768', 'Pass the material when', 'Fail the style when', 'chrome'):
            with self.subTest(token=token):
                self.assertIn(token, check)

    def test_standalone_sync(self):
        canonical = (BASE / 'styles/y2k-futurism.md').read_text(encoding='utf-8')
        project_root = BASE.parent if (BASE.parent / 'optional-standalone-skills').is_dir() else BASE.parents[1]
        standalone_path = project_root / 'optional-standalone-skills' / 'taste-style-y2k-futurism' / 'SKILL.md'
        self.assertTrue(standalone_path.is_file(), "Standalone skill must exist")
        standalone = standalone_path.read_text(encoding='utf-8')
        before_part = canonical.split('## Anti-slop: style-specific')[0].strip()
        after_part = ('## Anti-slop: style-specific' + canonical.split('## Anti-slop: style-specific')[1]).strip()
        self.assertIn(before_part, standalone)
        self.assertIn(after_part, standalone)

if __name__ == '__main__':
    unittest.main()
