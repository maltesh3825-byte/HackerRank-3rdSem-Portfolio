import unittest

from solution import matchingStrings


class SparseArraysTests(unittest.TestCase):
    def test_sample(self):
        strings = ["aba", "baba", "aba", "xzxb"]
        queries = ["aba", "xzxb", "ab"]
        self.assertEqual(matchingStrings(strings, queries), [2, 1, 0])

    def test_repeated_query(self):
        self.assertEqual(matchingStrings(["one", "one"], ["one", "one"]), [2, 2])


if __name__ == "__main__":
    unittest.main()
