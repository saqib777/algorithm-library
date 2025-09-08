import unittest
from algorithms.searching.binary_search import binary_search

class TestSearching(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_linear_search(self):   # 👈 New test cases
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 1), 0)

if __name__ == "__main__":
    unittest.main()
