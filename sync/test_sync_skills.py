import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import unittest
from sync_skills import clean_obsidian_syntax, strip_agent_instructions, file_content_hash
import tempfile


class TestCleanObsidianSyntax(unittest.TestCase):
    def test_removes_image_embeds(self):
        content = "Before ![[image.png]] After"
        result = clean_obsidian_syntax(content, "Test.md")
        self.assertNotIn("![[image.png]]", result)
        self.assertIn("Before", result)
        self.assertIn("After", result)

    def test_converts_wiki_links(self):
        content = "See [[Some Page]] for details"
        result = clean_obsidian_syntax(content, "Test.md")
        self.assertNotIn("[[", result)
        self.assertIn("Some Page", result)

    def test_converts_aliased_wiki_links(self):
        content = "See [[Some Page|the page]] for details"
        result = clean_obsidian_syntax(content, "Test.md")
        self.assertIn("the page", result)
        self.assertNotIn("Some Page", result)

    def test_injects_agent_instructions(self):
        content = "# My Skill\nSome content"
        result = clean_obsidian_syntax(content, "My Skill.md")
        self.assertIn("<agent_instructions>", result)
        self.assertIn("My Skill", result)

    def test_does_not_double_inject_instructions(self):
        content = "<agent_instructions>\n# Existing\n</agent_instructions>\n# Content"
        result = clean_obsidian_syntax(content, "Test.md")
        self.assertEqual(result.count("<agent_instructions>"), 1)


class TestStripAgentInstructions(unittest.TestCase):
    def test_removes_agent_instructions_block(self):
        content = "<agent_instructions>\nSome instructions\n</agent_instructions>\n\n# Content"
        result = strip_agent_instructions(content)
        self.assertNotIn("<agent_instructions>", result)
        self.assertIn("# Content", result)

    def test_no_op_without_instructions(self):
        content = "# Just content\nNo instructions here"
        result = strip_agent_instructions(content)
        self.assertEqual(result, content)


class TestFileContentHash(unittest.TestCase):
    def test_same_content_same_hash(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write("test content")
            path1 = f.name
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write("test content")
            path2 = f.name
        try:
            self.assertEqual(file_content_hash(path1), file_content_hash(path2))
        finally:
            os.unlink(path1)
            os.unlink(path2)

    def test_different_content_different_hash(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write("content A")
            path1 = f.name
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write("content B")
            path2 = f.name
        try:
            self.assertNotEqual(file_content_hash(path1), file_content_hash(path2))
        finally:
            os.unlink(path1)
            os.unlink(path2)


if __name__ == "__main__":
    unittest.main()
