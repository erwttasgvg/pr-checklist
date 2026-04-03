from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "github-pr-checklist"


class RepoLayoutTests(unittest.TestCase):
    def test_readme_exists_and_mentions_value_props(self):
        readme = ROOT / "README.md"
        self.assertTrue(readme.exists(), "README.md should exist")
        content = readme.read_text(encoding="utf-8")
        self.assertIn("Review faster", content)
        self.assertIn("Miss fewer risky changes", content)
        self.assertIn("Avoid fluffy summaries", content)
        self.assertIn("Who this is for", content)
        self.assertIn("Why this beats PR diff summaries", content)
        self.assertIn("Before", content)
        self.assertIn("After", content)

    def test_skill_structure_exists(self):
        self.assertTrue(SKILL_DIR.exists(), "Skill directory should exist")
        self.assertTrue((SKILL_DIR / "SKILL.md").exists(), "SKILL.md should exist")
        self.assertTrue((SKILL_DIR / "agents" / "openai.yaml").exists(), "agents/openai.yaml should exist")

    def test_license_exists(self):
        license_file = ROOT / "LICENSE"
        self.assertTrue(license_file.exists(), "LICENSE should exist")
        self.assertIn("MIT License", license_file.read_text(encoding="utf-8"))

    def test_demo_asset_exists(self):
        demo_asset = ROOT / "docs" / "assets" / "demo-before-after.svg"
        self.assertTrue(demo_asset.exists(), "demo asset should exist")

    def test_skill_markdown_documents_fallback_and_output_contract(self):
        skill_md = SKILL_DIR / "SKILL.md"
        self.assertTrue(skill_md.exists(), "SKILL.md should exist")
        content = skill_md.read_text(encoding="utf-8")
        self.assertIn("PR URL", content)
        self.assertIn("owner/repo#number", content)
        self.assertIn("diff", content.lower())
        self.assertIn("Actionable PR Checklist", content)
        self.assertIn("Critical Points Found", content)
        self.assertIn("Key Changes", content)
        self.assertIn("Risks", content)
        self.assertIn("Questions", content)
        self.assertIn("Suggested Tests", content)
        self.assertIn("Reply Draft", content)

if __name__ == "__main__":
    unittest.main()
