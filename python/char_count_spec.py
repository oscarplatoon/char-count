# Can you translate this driver code to unit tests?
import unittest
from char_count import char_count

class TestStringMethods(unittest.TestCase):

    def test_propper_output(self):
        self.assertEqual(char_count('foo'), {'o': 2, 'f': 1})

    # def test_isupper(self):
        

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()

# print(char_count("aaabbc") == {
#   "a": 3,
#   "b": 2,
#   "c": 1
# })

# print(char_count("an apple a day will keep the doctor away") == {
#   "a":6,
#   "e":4,
#   "l":3,
#   "p":3,
#   "w":2,
#   "d":2,
#   "o":2,
#   "t":2,
#   "y":2,
#   "k":1,
#   "h":1,
#   "i":1,
#   "c":1,
#   "n":1,
#   "r":1
# })
