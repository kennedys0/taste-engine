from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]

class MotionContracts(unittest.TestCase):
    def test_each_style_has_profile_and_motion_rule(self):
        registry = json.loads((ROOT / "styles/registry.json").read_text())
        profiles = json.loads((ROOT / "styles/motion-profiles.json").read_text())["styles"]
        ids = {style["id"] for style in registry["styles"]}
        self.assertEqual(ids, set(profiles))
        for style_id in ids:
            content = (ROOT / "styles" / f"{style_id}.md").read_text()
            self.assertIn("## Optional Anime.js v4 recipe", content)
            self.assertIn("## Motion", content)
            self.assertIn("reduced", (ROOT / "references/motion-engine.md").read_text().lower())
            self.assertGreaterEqual(profiles[style_id]["duration_ms"], 0)
            self.assertLessEqual(profiles[style_id]["duration_ms"], 300)
    def test_example_has_v4_api_cleanup_and_real_state(self):
        src = (ROOT / "examples/react/anime-v4-press.jsx").read_text()
        for part in ["createScope", "useEffect", "scope.revert()", "prefers-reduced-motion", "aria-expanded", "setExpanded", "animate("]:
            self.assertIn(part, src)
        self.assertNotIn("anime({", src)
    def test_standalone_copies_reference(self):
        standalone = ROOT.parent / "optional-standalone-skills/taste-motion"
        self.assertEqual((ROOT / "references/motion-engine.md").read_bytes(),(standalone / "references/motion-engine.md").read_bytes())
        self.assertEqual((ROOT / "examples/react/anime-v4-press.jsx").read_bytes(),(standalone / "examples/react/anime-v4-press.jsx").read_bytes())

if __name__ == "__main__":
    unittest.main()
