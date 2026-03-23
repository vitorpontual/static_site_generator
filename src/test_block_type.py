import unittest
from block_types import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### heading"), BlockType.HEADING)

    def test_code(self):
        code = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote(self):
        quote = "> blockquote\n> still blockquote"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_unordered_list(self):
        ul = "- item 1\n- item 2"
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        ol = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        p = "Just a normal paragraph with some **bold** text."
        self.assertEqual(block_to_block_type(p), BlockType.PARAGRAPH)

    def test_ordered_list_fail(self):
        # Falha porque pula o número 2
        ol = "1. first\n3. third"
        self.assertEqual(block_to_block_type(ol), BlockType.PARAGRAPH)



if __name__ == "__main__":
    unittest.main()
