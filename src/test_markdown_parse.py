import unittest
from inline_markdown import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        md =  "# Hello"
        result = extract_title(md)
        self.assertEqual(result, "Hello")

    def test_title_with_spaces(self):
        md = "#   Hello World   "
        result = extract_title(md)
        self.assertEqual(result, "Hello World")


    def test_title_with_content_after(self):
        md =  "# Main Title\n\n\Some Content\n## Subtitle"
        result = extract_title(md)
        self.assertEqual(result, "Main Title")

    def test_no_title_raises_error(self):
        md = "## Subtitle only\nContent"
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()
