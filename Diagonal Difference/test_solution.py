import unittest

from solution import diagonalDifference


class DiagonalDifferenceTests(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(
            diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]),
            15,
        )

    def test_single_element(self):
        self.assertEqual(diagonalDifference([[7]]), 0)


if __name__ == "__main__":
    unittest.main()
