
import unittest
from pyquery.helpers import keys_and_values, keys_with_values, keys_only

class helperTest(unittest.TestCase):
    
    def test_keys_and_values(self):
        self.assertEqual(
            keys_and_values(user="adam", country="libya", level="low"),
            "user=adam AND country=libya AND level=low"
        )
        self.assertEqual(
            keys_and_values(user="john", country="UK", level="low"),
            "user=john AND country=UK AND level=low"
        )

    def test_keys_with_values(self):
        keys_with_values_tuple = keys_with_values(user="adam", country="libya", level="low")
        self.assertTupleEqual(
            keys_with_values_tuple,
            ("user, country, level", "adam, libya, low")
        )

    def test_keys_only(self):
        self.assertEqual(
            keys_only(("user", "country", "level")),
            "user, country, level"
        )

unittest.main()