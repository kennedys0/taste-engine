from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]

class FrutigerAeroFidelityTests(unittest.TestCase):
    def test_pack_requires_glossy_nature_tech_material(self):
        text = (BASE / 'styles/frutiger-aero.md').read_text(encoding='utf-8')
        for token in ('Frutiger Aero material fidelity gate', 'specular', 'Classic Aero', 'Aero Glass', 'Aero Tactile', 'first viewport', 'FAIL'):
            with self.subTest(token=token):
                self.assertIn(token.lower(), text.lower())

    def test_recipe_and_tokens(self):
        css = (BASE / 'examples/frutiger-aero/glossy-surfaces.css').read_text(encoding='utf-8')
        for token in ('--taste-aero-aqua', '--taste-aero-ocean', '--taste-aero-leaf', 'prefers-reduced-motion', ':focus-visible', '.taste-aero-btn', '.taste-aero-card'):
            with self.subTest(token=token):
                self.assertIn(token, css)

    def test_frutiger_aero_gloss_is_explicit_exception_not_blanket_slop(self):
        text = (BASE / 'styles/frutiger-aero.md').read_text(encoding='utf-8').lower()
        for token in ('explicit frutiger aero material exception', 'horizon sheens', 'anti-slop'):
            with self.subTest(token=token):
                self.assertIn(token, text)
        universal = (BASE / 'references/anti-slop.md').read_text(encoding='utf-8').lower()
        self.assertIn('frutiger aero:', universal)

    def test_three_expressions_and_palettes_included(self):
        text = (BASE / 'styles/frutiger-aero.md').read_text(encoding='utf-8').lower()
        for token in ('classic aero', 'aero glass', 'aero tactile', '#48bfd3', '#247ea3', '#70b981', '#c9edf8', '#f4fafc', '#173f61', '#243642'):
            with self.subTest(token=token):
                self.assertIn(token, text)

    def test_acceptance_checks_present(self):
        check = (BASE / 'tests/frutiger-aero-visual.md').read_text(encoding='utf-8')
        for token in ('320, 390, 768', 'Pass the material when', 'Fail the style when', 'specular'):
            with self.subTest(token=token):
                self.assertIn(token, check)

    def test_standalone_sync(self):
        canonical = (BASE / 'styles/frutiger-aero.md').read_text(encoding='utf-8')
        project_root = BASE.parent if (BASE.parent / 'optional-standalone-skills').is_dir() else BASE.parents[1]
        standalone_path = project_root / 'optional-standalone-skills' / 'taste-style-frutiger-aero' / 'SKILL.md'
        self.assertTrue(standalone_path.is_file(), "Standalone skill must exist")
        standalone = standalone_path.read_text(encoding='utf-8')
        before_part = canonical.split('## Anti-slop: style-specific')[0].strip()
        after_part = ('## Anti-slop: style-specific' + canonical.split('## Anti-slop: style-specific')[1]).strip()
        self.assertIn(before_part, standalone)
        self.assertIn(after_part, standalone)

if __name__ == '__main__':
    unittest.main()
