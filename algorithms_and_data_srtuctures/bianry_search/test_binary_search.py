import unittest
from  binary_search import binary_search

class Calculation(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([-10, -3, -1, 0, 2, 3, 5], -1), 2)
        self.assertEqual(binary_search([-10, -3, -1, 0, 2, 3, 5], 2), 4)
        self.assertEqual(binary_search([-10, -3, -1, 0, 2, 3, 5], 0), 3)
        self.assertEqual(binary_search([-10, -3, -1, 0, 2, 3, 5], -10), 0)
        self.assertEqual(binary_search([-10, -3, -1, 0, 2, 3, 5], 5), 6)

if __name__ == '__main__':
    unittest.main()