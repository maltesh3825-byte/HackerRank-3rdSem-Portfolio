import unittest

from solution import compareTriplets


class CompareTripletsTests(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(compareTriplets([5, 6, 7], [3, 6, 10]), [1, 1])

    def test_tie(self):
        self.assertEqual(compareTriplets([1, 2, 3], [1, 2, 3]), [0, 0])


if __name__ == "__main__":
    unittest.main()
