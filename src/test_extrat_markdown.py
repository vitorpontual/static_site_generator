import unittest

from extract_markdown_images import emi

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = emi(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
