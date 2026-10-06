import unittest

from solution import dynamicArray


class DynamicArrayTests(unittest.TestCase):
    def test_sample(self):
        queries = [[1, 0], [1, 1], [1, 2], [2, 1], [2, 1]]
        self.assertEqual(dynamicArray(2, queries), [1, 2])

    def test_multiple_sequences(self):
        queries = [[1, 5], [1, 7], [2, 5], [2, 7]]
        self.assertEqual(dynamicArray(3, queries), [5, 7])


if __name__ == "__main__":
    unittest.main()
