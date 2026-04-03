from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "github-pr-checklist"
SHOWCASE_DIR = ROOT / "showcase"


class RepoLayoutTests(unittest.TestCase):
    def test_readme_exists_and_mentions_value_props(self):
        readme = ROOT / "README.md"
        self.assertTrue(readme.exists(), "README.md should exist")
        content = readme.read_text(encoding="utf-8")
        self.assertIn("Review faster", content)
        self.assertIn("Miss fewer risky changes", content)
        self.assertIn("Avoid fluffy summaries", content)

    def test_skill_structure_exists(self):
        self.assertTrue(SKILL_DIR.exists(), "Skill directory should exist")
        self.assertTrue((SKILL_DIR / "SKILL.md").exists(), "SKILL.md should exist")
        self.assertTrue((SKILL_DIR / "agents" / "openai.yaml").exists(), "agents/openai.yaml should exist")

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

    def test_showcase_handoff_exists(self):
        self.assertTrue(SHOWCASE_DIR.exists(), "showcase directory should exist")
        self.assertTrue((SHOWCASE_DIR / "README.md").exists(), "showcase README should exist")
        self.assertTrue((SHOWCASE_DIR / "content" / "landing-copy.md").exists(), "landing copy should exist")
        self.assertTrue((SHOWCASE_DIR / "content" / "showcase-brief.json").exists(), "showcase brief should exist")
        self.assertTrue((SHOWCASE_DIR / "content" / "demo-script.md").exists(), "demo script should exist")
        self.assertTrue((SHOWCASE_DIR / "ANTIGRAVITY_PROMPT.md").exists(), "antigravity prompt should exist")


if __name__ == "__main__":
    unittest.main()
