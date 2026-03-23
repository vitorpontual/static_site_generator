import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_with_url(self):
        node = TextNode("This Link", TextType.LINK, "www.www.www")
        nodeb = TextNode("This Link", TextType.LINK, "www.www.www")
        self.assertEqual(node, nodeb)

    def test_neq_with_url(self):
        node=TextNode("Link2", TextType.LINK, "link1")
        nodeb=TextNode("Link2", TextType.LINK, "link2")
        self.assertNotEqual(node,nodeb)

    def test_not_eq_type(self):
        node= TextNode("Text A", TextType.BOLD)
        nodeb= TextNode("Text B", TextType.ITALIC)

    def  test_url_none_vs_string(self):
        node=TextNode("Text Url", TextType.IMAGE, None)
        nodeb=TextNode("Text B",TextType.IMAGE, "url.url ulr" )
        self.assertNotEqual(node, nodeb)

    def test_text(self):
        node = TextNode('This is a text node', TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")




if __name__ == "__main__":
    unittest.main()
