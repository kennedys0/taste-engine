from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]

class RetroPixelFidelityTests(unittest.TestCase):
    def test_pack_requires_visible_pixel_material(self):
        text = (BASE / 'styles/retro-pixel.md').read_text(encoding='utf-8')
        for token in (
            'Retro pixel material fidelity gate',
            'image-rendering: pixelated',
            'Midnight canvas',
            'Retro teal',
            'Arcade orange',
            'Desktop purple',
            'Vintage cream',
            'first viewport',
            'FAIL',
            'integer',
            'stepped',
        ):
            with self.subTest(token=token):
                self.assertIn(token.lower(), text.lower())

    def test_pixel_recipe_and_tokens(self):
        css = (BASE / 'examples/retro-pixel/pixel-surfaces.css').read_text(encoding='utf-8')
        for token in (
            '--taste-pixel-bg',
            '--taste-pixel-teal',
            '--taste-pixel-orange',
            '--taste-pixel-purple',
            '--taste-pixel-cream',
            'image-rendering',
            'prefers-reduced-motion',
            ':focus-visible',
            '.taste-pixel-window',
            '.taste-pixel-btn',
        ):
            with self.subTest(token=token):
                self.assertIn(token, css)

    def test_pixel_exception_and_anti_slop(self):
        text = (BASE / 'styles/retro-pixel.md').read_text(encoding='utf-8').lower()
        for token in ('explicit retro pixel exception', 'pixel illustrations', 'stepped pixel borders', 'anti-slop'):
            with self.subTest(token=token):
                self.assertIn(token, text)
        universal = (BASE / 'references/anti-slop.md').read_text(encoding='utf-8').lower()
        self.assertIn('retro-pixel', universal)

    def test_acceptance_checks_present(self):
        check = (BASE / 'tests/retro-pixel-visual.md').read_text(encoding='utf-8')
        for token in ('320, 390, 768', 'First-viewport recognition test', 'Pass the material when', 'Fail the style when'):
            with self.subTest(token=token):
                self.assertIn(token, check)

if __name__ == '__main__':
    unittest.main()

