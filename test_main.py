import unittest
from main import get_info_with_description, parser, clear_tag


class TestMain(unittest.TestCase):
    def test_clear_tag(self):
        tag1 = "{http://www.adv-online.de/namespaces/adv/gid/6.0}AX_Bestandsdatenauszug"
        tag2 = "{{}}}}onetwo}land"
        tag3 = "enthaelt"
        tag4 = ""
        tag5 = 4
        tag6 = "}}}"

        self.assertEqual(clear_tag(tag1), "AX_Bestandsdatenauszug")
        self.assertEqual(clear_tag(tag2), "land")
        self.assertEqual(clear_tag(tag3), "enthaelt")
        self.assertEqual(clear_tag(tag4), "")
        self.assertRaises(AttributeError, clear_tag, tag5)
        self.assertEqual(clear_tag(tag6), "")

    def test_parser(self):
        file = "parcel_aaa.xml"
        output = parser(file, ["landschl", "flaeche"])
        self.assertEqual(next(output), ("landschl", "05"))
        self.assertEqual(next(output), ("flaeche", "2.00"))

    def test_get_info_with_description(self):
        out = get_info_with_description(
            "parcel_aaa.xml", {"flaeche": "Wielkość działki"}
        )
        self.assertEqual(next(out), ("Wielkość działki", "2.00"))
