import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class EngineeringRoutingTests(unittest.TestCase):
    def setUp(self):
        self.router=(ROOT/'references/engineering-router.md').read_text(encoding='utf-8')
        self.skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
    def test_universal_web_gate_exists(self):
        self.assertIn('web-interface-quality.md',self.router)
        self.assertIn('Web Interface Quality',self.skill)
    def test_react_is_conditional(self):
        self.assertIn('React/Next',self.router)
        self.assertIn('Inspect actual project signals',self.router)
        self.assertIn('do not force React packages',self.router)
    def test_style_preflight_priority(self):
        self.assertIn('ask once and stop',self.router)
        self.assertIn('WITHOUT asking again', self.skill)
        self.assertIn('preflight first',self.router)
    def test_native_not_web(self):
        self.assertIn('SEO/canonical/sitemap and Anime.js-on-DOM do not apply', (ROOT/'references/native-mobile.md').read_text())
    def test_motion_not_duplicate(self):
        self.assertIn('Never duplicate animations', (ROOT/'references/view-transitions.md').read_text())
    def test_user_style_wins(self):
        self.assertIn('Explicit chosen visual style',self.router)
    def test_external_routing_not_deployment(self):
        self.assertIn("Don't deploy automatically",self.router)
    def test_research_provenance(self):
        self.assertIn('has not copied their text or code',(ROOT/'references/vercel-research.md').read_text())

if __name__=='__main__':unittest.main()
