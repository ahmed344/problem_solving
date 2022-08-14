import unittest
from  merge_sort import merge_sort

class Calculation(unittest.TestCase):

    def test_merge_sort(self):
        self.assertEqual(merge_sort([3, -3, 0, -10, 2, -1, 5]), [-10, -3, -1, 0, 2, 3, 5])
        self.assertEqual(merge_sort([3, -3, 2, 0, 2, -10, 2, -1, 5]), [-10, -3, -1, 0, 2, 2, 2, 3, 5])
        self.assertEqual(merge_sort([3, -3, -10, 0, -10, -10, 2, -1, 5]), [-10, -10, -10, -3, -1, 0, 2, 3, 5])
        self.assertEqual(merge_sort([3, -3, 5, 0, 5, -10, 2, -1, 5]), [-10, -3, -1, 0, 2, 3, 5, 5, 5])
        self.assertEqual(merge_sort([-10, -10, -10]), [-10, -10, -10])
        self.assertEqual(merge_sort([0]), [0])
        self.assertEqual(merge_sort([]), [])

if __name__ == '__main__':
    unittest.main()