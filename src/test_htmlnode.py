import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TesteHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "Google",
            None,
            {"href": "https://www.google.com", "target":"_blank"}
        )
        expect = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expect)


    def test_values(self):
        node = HTMLNode ("p", "Hello World")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello World")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        node = HTMLNode ("h1", "Title", None, {"class": "header"})
        expected = "HTMLNode(h1, Title, children:None, {'class': 'header'})"
        self.assertEqual(repr(node), expected)

    def test_props_to_html_empty(self):
        node = HTMLNode ("p", "No props here")
        self.assertEqual(node.props_to_html(), "")


    def test_leaf_to_html_p(self):
        node = LeafNode ("p", "Hello world")
        self.assertEqual(node.to_html(), "<p>Hello world</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><span><b>grandchild</b></span></div>')


if __name__ == "__main__":
    unittest.main()

