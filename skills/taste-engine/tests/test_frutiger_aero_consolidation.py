#!/usr/bin/env python3
"""
Unit test suite verifying the Frutiger Aero style consolidation:
- Frutiger Aero is registered as a canonical top-level style
- Glassmorphism and Skeuomorphism are consolidated as internal variants (glass, tactile)
- All three variants (classic, glass, tactile) are defined and functional
- Legacy aliases safely route to frutiger-aero with variant: 'glass' or 'tactile'
- Unrelated styles remain independent and unregressed
"""
import importlib.util
import json
from pathlib import Path
import unittest

class TestFrutigerAeroConsolidation(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[1]
        self.project_root = self.root.parent if (self.root.parent / 'optional-standalone-skills').is_dir() else self.root.parents[1]
        self.registry_path = self.root / 'styles' / 'registry.json'
        self.registry = json.loads(self.registry_path.read_text(encoding='utf-8'))
        self.styles_by_id = {s['id']: s for s in self.registry.get('styles', [])}
        
        # Load style_probe
        spec = importlib.util.spec_from_file_location('style_probe', self.root / 'scripts' / 'style_probe.py')
        self.style_probe = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.style_probe)

    def test_frutiger_aero_registered(self):
        self.assertIn('frutiger-aero', self.styles_by_id, "frutiger-aero must exist as a top-level style")
        self.assertNotIn('glassmorphism', self.styles_by_id, "glassmorphism must not exist as an independent top-level style")
        self.assertNotIn('skeuomorphism', self.styles_by_id, "skeuomorphism must not exist as an independent top-level style")

    def test_frutiger_aero_three_variants(self):
        aero = self.styles_by_id['frutiger-aero']
        self.assertEqual(aero.get('default_variant'), 'classic')
        variants = aero.get('variants', [])
        variant_ids = [v['id'] for v in variants]
        self.assertEqual(variant_ids, ['classic', 'glass', 'tactile'])

    def test_legacy_glassmorphism_routing(self):
        res = self.style_probe.candidates('Create a glassmorphism landing page', self.registry)
        self.assertEqual(res['status'], 'ready')
        self.assertEqual(res['primary_style'], 'frutiger-aero')
        self.assertEqual(res['variant'], 'glass')

        res_frosted = self.style_probe.candidates('Build a frosted glass interface', self.registry)
        self.assertEqual(res_frosted['primary_style'], 'frutiger-aero')
        self.assertEqual(res_frosted['variant'], 'glass')

    def test_legacy_skeuomorphism_routing(self):
        res = self.style_probe.candidates('Buat website portfolio bertema skeumorphsm', self.registry)
        self.assertEqual(res['status'], 'ready')
        self.assertEqual(res['primary_style'], 'frutiger-aero')
        self.assertEqual(res['variant'], 'tactile')

        res_tactile = self.style_probe.candidates('Build realistic physical controls', self.registry)
        self.assertEqual(res_tactile['primary_style'], 'frutiger-aero')
        self.assertEqual(res_tactile['variant'], 'tactile')

    def test_direct_frutiger_aero_routing(self):
        res = self.style_probe.candidates('Design a frutiger aero website', self.registry)
        self.assertEqual(res['status'], 'ready')
        self.assertEqual(res['primary_style'], 'frutiger-aero')
        self.assertEqual(res['variant'], 'classic')

        res_glass = self.style_probe.candidates('Create an aero glass interface', self.registry)
        self.assertEqual(res_glass['status'], 'ready')
        self.assertEqual(res_glass['primary_style'], 'frutiger-aero')
        self.assertEqual(res_glass['variant'], 'glass')

        res_tactile = self.style_probe.candidates('Build an aero tactile dashboard', self.registry)
        self.assertEqual(res_tactile['status'], 'ready')
        self.assertEqual(res_tactile['primary_style'], 'frutiger-aero')
        self.assertEqual(res_tactile['variant'], 'tactile')

    def test_unrelated_styles_unregressed(self):
        unrelated = ['claymorphism', 'brutalism', 'neo-brutalism', 'minimalism', 'swiss-editorial', 'retro-terminal', 'retro-pixel', 'art-deco']
        for style_id in unrelated:
            self.assertIn(style_id, self.styles_by_id, f"{style_id} must remain registered")

if __name__ == '__main__':
    unittest.main()
