import unittest
from dataformat import DataFormat


class TestDataformat(unittest.TestCase):
    def setUp(self):
        self.data_format = DataFormat(**{"a": "b", "c": "d"})
        self.data_format2 = DataFormat()

    def test_delete(self):
        self.assertEqual(self.data_format.delete_tag("b"), {"a": "b", "c": "d"})
        self.assertEqual(self.data_format.delete_tag("a"), {"c": "d"})
        self.assertEqual(self.data_format.delete_tag(5), {"c": "d"})
        self.assertEqual(self.data_format.delete_tag("c"), {})

    def test_add(self):
        self.assertEqual(
            self.data_format.add_tag("e", "f"), {"a": "b", "c": "d", "e": "f"}
        )
        self.assertEqual(
            self.data_format.add_tag("e", "g"), {"a": "b", "c": "d", "e": "g"}
        )
        self.assertRaises(TypeError, self.data_format.add_tag, "a")
        self.assertRaises(TypeError, self.data_format.add_tag, "a", "b", "c")

    def test_get_tags(self):
        self.assertEqual(self.data_format.get_tags(), ["a", "c"])

    def test_get_description(self):
        self.assertEqual(self.data_format.get_description("a"), "b")
        self.assertRaises(KeyError, self.data_format.get_description, "b")
        self.assertRaises(KeyError, self.data_format.get_description, 3)

    def test_get_tag_with_description(self):
        self.assertEqual(
            self.data_format.get_tags_with_description(), {"a": "b", "c": "d"}
        )
        self.assertEqual(self.data_format2.get_tags_with_description(), {})
        self.assertRaises(TypeError, self.data_format2.get_tags_with_description, "b")

    def test_get_tags(self):
        self.assertEqual(self.data_format.get_tags(), ["a", "c"])
        self.assertEqual(self.data_format2.get_tags(), [])
        self.assertRaises(TypeError, self.data_format2.get_tags, "b")


if __name__ == "__main__":
    unittest.main()
