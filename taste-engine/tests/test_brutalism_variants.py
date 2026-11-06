#!/usr/bin/env python3
"""
Unit test suite verifying the Brutalism x Bento style consolidation:
- Brutalism has two native variants: 'raw' (default) and 'bento'
- Bento is removed as a top-level style (top-level styles count = 9)
- Bento aliases resolve to brutalism with variant: 'bento'
- Neo-Brutalism remains 100% independent
- CSS tokens, motion profiles, and schemas are aligned
"""
import importlib.util
import json
from pathlib import Path
import unittest

class TestBrutalismVariants(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[1]
        self.project_root = self.root.parent
        self.registry_path = self.root / 'styles' / 'registry.json'
        self.registry = json.loads(self.registry_path.read_text(encoding='utf-8'))
        self.styles_by_id = {s['id']: s for s in self.registry.get('styles', [])}
        
        # Load style_probe
        spec = importlib.util.spec_from_file_location('style_probe', self.root / 'scripts' / 'style_probe.py')
        self.style_probe = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.style_probe)

    def test_top_level_styles_count_restored_to_ten(self):
        styles = self.registry.get('styles', [])
        self.assertEqual(len(styles), 10, f"Expected exactly 10 top-level styles, found {len(styles)}: {list(self.styles_by_id.keys())}")
        self.assertNotIn('bento', self.styles_by_id, "bento must not exist as an independent top-level style")
        self.assertIn('brutalism', self.styles_by_id, "brutalism must exist as a top-level style")
        self.assertIn('neo-brutalism', self.styles_by_id, "neo-brutalism must exist as an independent top-level style")
        self.assertIn('art-deco', self.styles_by_id, "art-deco must exist as a top-level style")

    def test_brutalism_variants_in_registry(self):
        brutalism = self.styles_by_id['brutalism']
        self.assertEqual(brutalism.get('default_variant'), 'raw')
        variant_ids = [v['id'] for v in brutalism.get('variants', [])]
        self.assertEqual(variant_ids, ['raw', 'bento'])
        
        # Check bento aliases are present under brutalism
        aliases = brutalism.get('aliases', [])
        self.assertIn('bento', aliases)
        self.assertIn('bento grid', aliases)
        self.assertIn('bento box', aliases)
        self.assertIn('brutalist bento', aliases)

    def test_neo_brutalism_independence(self):
        neo_brutalism = self.styles_by_id['neo-brutalism']
        self.assertEqual(neo_brutalism.get('id'), 'neo-brutalism')
        # Neo-brutalism must not reference brutalism variants
        self.assertNotIn('variants', neo_brutalism)
        self.assertNotIn('bento', neo_brutalism.get('aliases', []))
        
        # Neo-brutalism must preserve its own distinct identity and aliases
        aliases = neo_brutalism.get('aliases', [])
        self.assertIn('neobrutalism', aliases)
        self.assertIn('neo brutalism', aliases)

    def test_style_probe_variant_resolution(self):
        # Raw Brutalism resolution
        res_raw1 = self.style_probe.candidates("Build a brutalist portfolio", self.registry)
        self.assertEqual(res_raw1['primary_style'], 'brutalism')
        self.assertEqual(res_raw1.get('variant'), 'raw')

        res_raw2 = self.style_probe.candidates("Design a raw brutalist landing page", self.registry)
        self.assertEqual(res_raw2['primary_style'], 'brutalism')
        self.assertEqual(res_raw2.get('variant'), 'raw')

        # Brutalist Bento resolution
        res_bento1 = self.style_probe.candidates("Create a bento grid website", self.registry)
        self.assertEqual(res_bento1['primary_style'], 'brutalism')
        self.assertEqual(res_bento1.get('variant'), 'bento')

        res_bento2 = self.style_probe.candidates("Make a brutalist bento layout", self.registry)
        self.assertEqual(res_bento2['primary_style'], 'brutalism')
        self.assertEqual(res_bento2.get('variant'), 'bento')

        res_bento3 = self.style_probe.candidates("I want an apple bento dashboard", self.registry)
        self.assertEqual(res_bento3['primary_style'], 'brutalism')
        self.assertEqual(res_bento3.get('variant'), 'bento')

        # Neo-brutalism resolution should NOT have brutalism variant
        res_neo = self.style_probe.candidates("Build a neo-brutalism app", self.registry)
        self.assertEqual(res_neo['primary_style'], 'neo-brutalism')
        self.assertIsNone(res_neo.get('variant'))

    def test_motion_profiles_has_ten_styles(self):
        motion_path = self.root / 'styles' / 'motion-profiles.json'
        profiles = json.loads(motion_path.read_text(encoding='utf-8'))
        styles = profiles.get('styles', {})
        self.assertEqual(len(styles), 10)
        self.assertNotIn('bento', styles)
        self.assertIn('brutalism', styles)
        self.assertIn('neo-brutalism', styles)
        self.assertIn('art-deco', styles)

    def test_project_style_schema_supports_variant(self):
        schema_path = self.root / 'assets' / 'project-style.schema.json'
        schema = json.loads(schema_path.read_text(encoding='utf-8'))
        props = schema.get('properties', {})
        self.assertIn('variant', props)
        self.assertIn('string', props['variant'].get('type', []))

    def test_brutalist_bento_css_classes(self):
        css_path = self.root / 'examples' / 'brutalism' / 'raw-surfaces.css'
        css_content = css_path.read_text(encoding='utf-8')
        self.assertIn('.taste-brutal-bento-grid', css_content)
        self.assertIn('.taste-brutal-bento-tile', css_content)
        self.assertIn('.taste-brutal-bento-tile.hero', css_content)
        self.assertIn('border-radius: var(--taste-brutal-radius, 0px);', css_content)

    def test_brutalism_documentation_covers_both_variants(self):
        doc_path = self.root / 'styles' / 'brutalism.md'
        doc_content = doc_path.read_text(encoding='utf-8')
        self.assertIn('Raw Brutalism', doc_content)
        self.assertIn('Brutalist Bento', doc_content)
        self.assertIn('variant: raw', doc_content)
        self.assertIn('variant: bento', doc_content)

    def test_merged_style_assets_removed(self):
        bento_doc = self.root / 'styles' / 'bento.md'
        self.assertFalse(bento_doc.exists(), "styles/bento.md must be removed")
        bento_examples = self.root / 'examples' / 'bento'
        self.assertFalse(bento_examples.exists(), "examples/bento must be removed")
        enterprise_examples = self.root / 'examples' / 'enterprise'
        self.assertFalse(enterprise_examples.exists(), "examples/enterprise must be removed")
        bento_html = self.project_root / 'docs' / 'bento.html'
        self.assertFalse(bento_html.exists(), "docs/bento.html must be removed")
        enterprise_html = self.project_root / 'docs' / 'enterprise.html'
        self.assertFalse(enterprise_html.exists(), "docs/enterprise.html must be removed")

    def test_standalone_bento_skill_removed(self):
        standalone_bento = self.project_root / 'optional-standalone-skills' / 'taste-style-bento'
        self.assertFalse(standalone_bento.exists(), "optional-standalone-skills/taste-style-bento must be removed")

    def test_standalone_brutalism_skill_covers_both_variants(self):
        standalone_brutal = self.project_root / 'optional-standalone-skills' / 'taste-style-brutalism' / 'SKILL.md'
        self.assertTrue(standalone_brutal.is_file())
        content = standalone_brutal.read_text(encoding='utf-8')
        self.assertIn('Raw Brutalism', content)
        self.assertIn('Brutalist Bento', content)

if __name__ == '__main__':
    unittest.main()
