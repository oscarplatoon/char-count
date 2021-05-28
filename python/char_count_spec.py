# Can you translate this driver code to unit tests?
import unittest
from char_count import char_count

class CharCountTestCase(unittest.TestCase):
    """Tests for anagram2.py"""

    def test_char_count_returns_a_dict(self):
        """When you call char_count(), you should get a dict back"""
        self.assertIsInstance(char_count("aaabbc"), dict)

    def test_char_count_for_correct_output(self):
         """
         Verify that correct number of chars are found
         """
         self.assertDictEqual(char_count("an apple a day will keep the doctor away"), {'a': 6, 'e': 4, 'p': 3, 'l': 3, 'd': 2, 'y': 2, 'w': 2, 't': 2, 'o': 2, 'n': 1, 'i': 1, 'k': 1, 'h': 1, 'c': 1, 'r': 1})

if __name__ == '__main__':
     unittest.main()
