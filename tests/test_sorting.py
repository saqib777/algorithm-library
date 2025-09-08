import unittest
from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.merge_sort import merge_sort

class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([5, 3, 8, 4, 2]), [2, 3, 4, 5, 8])

if __name__ == "__main__":
    unittest.main()
