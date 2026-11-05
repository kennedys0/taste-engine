"""Static hero-policy pack consistency tests; not a substitute for browser QA."""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT.parent if (ROOT.parent / 'optional-standalone-skills').is_dir() else ROOT.parents[1]

class HeroPolicyTest(unittest.TestCase):
    def test_global_contract(self):
        contract = (ROOT / 'references/hero-layout.md').read_text(encoding='utf-8')
        for term in ('100svh', '100vh', 'min-height', 'header', '320×568', '200% zoom', 'normal flow'):
            self.assertIn(term, contract)
        self.assertIn('do **not**', contract.lower())

    def test_root_invocation(self):
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('references/hero-layout.md', skill)
        self.assertRegex(skill, r'version:\s*[\"]?\d+\.\d+\.\d+')
        self.assertIn('without asking', skill.lower())

    def test_every_pack_and_standalone(self):
        registry = json.loads((ROOT / 'styles/registry.json').read_text(encoding='utf-8'))
        self.assertEqual(len(registry['styles']), 11)
        for style in registry['styles']:
            id = style['id']
            text = (ROOT / 'styles' / (id+'.md')).read_text(encoding='utf-8')
            standalone = (BUNDLE / 'optional-standalone-skills' / ('taste-style-'+id) / 'SKILL.md').read_text(encoding='utf-8')
            for content in (text, standalone):
                self.assertIn('## Hero composition (full first viewport)', content, id)
                self.assertIn('100svh', content, id)
                self.assertIn('dashboard', content, id)
                self.assertIn('short mobile screens', content, id)

if __name__ == '__main__':
    unittest.main()
