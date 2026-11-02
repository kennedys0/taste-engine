#!/usr/bin/env python3
"""No-dependency unit tests: python3 -m unittest discover -s tests -p 'test_*.py'"""
import importlib.util
import unittest
from pathlib import Path

module_path = Path(__file__).resolve().parents[1] / 'scripts' / 'seo_audit.py'
spec = importlib.util.spec_from_file_location('seo_audit', module_path)
seo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seo)


class SEOAuditTests(unittest.TestCase):
    def setUp(self):
        self.good = '''<!DOCTYPE html><html lang="id"><head><title>Portofolio Dev</title>
        <meta name="description" content="Portofolio publik seorang developer.">
        <meta property="og:title" content="Portofolio Dev">
        <link rel="canonical" href="https://my-real-domain.id/portfolio"></head>
        <body><main><h1>Portofolio</h1><img alt="Tampilan proyek" src="/work.webp"></main></body></html>'''

    def test_public_sane_html_has_no_error(self):
        f=seo.scan_html(self.good, public=True)
        self.assertFalse([x for x in f if x['level']=='ERROR'])

    def test_noindex_public_is_error(self):
        bad=self.good.replace('</head>', '<meta name="robots" content="noindex"></head>')
        f=seo.scan_html(bad, public=True)
        self.assertIn('public-noindex', [x['code'] for x in f if x['level']=='ERROR'])

    def test_duplicate_canonical(self):
        bad=self.good.replace('</head>', '<link rel="canonical" href="https://other.test/"></head>')
        f=seo.scan_html(bad, public=True)
        self.assertIn('multiple-canonical', [x['code'] for x in f])

    def test_unknown_host_canonical_not_fabricated(self):
        without=self.good.replace('<link rel="canonical" href="https://my-real-domain.id/portfolio">','')
        f=seo.scan_html(without, public=True)
        self.assertIn('canonical-pending', [x['code'] for x in f])
        self.assertFalse([x for x in f if x['level']=='ERROR'])

    def test_missing_alt_warns(self):
        bad=self.good.replace('alt="Tampilan proyek"','')
        f=seo.scan_html(bad, public=True)
        self.assertIn('image-alt', [x['code'] for x in f])

    def test_case_insensitive_robots(self):
        bad=self.good.replace('</head>', '<META NAME="Robots" CONTENT="NOINDEX, FOLLOW"></head>')
        f=seo.scan_html(bad, public=True)
        self.assertIn('public-noindex', [x['code'] for x in f])

    def test_private_auth_caveat(self):
        f=seo.scan_html(self.good, private=True)
        self.assertIn('private-auth', [x['code'] for x in f])


if __name__ == '__main__':
    unittest.main()
