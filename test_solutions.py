import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).parent


def load_function(folder_name, function_name):
    module_path = ROOT / folder_name / "solution.py"
    module_name = folder_name.lower().replace(" ", "_")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


class PortfolioSolutionTests(unittest.TestCase):
    def test_diagonal_difference(self):
        diagonal_difference = load_function("Diagonal Difference", "diagonalDifference")
        self.assertEqual(
            diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]),
            15,
        )
        self.assertEqual(diagonal_difference([[7]]), 0)

    def test_dynamic_array(self):
        dynamic_array = load_function("Dynamic Array", "dynamicArray")
        queries = [[1, 0], [1, 1], [1, 2], [2, 1], [2, 1]]
        self.assertEqual(dynamic_array(2, queries), [1, 2])

    def test_time_conversion(self):
        time_conversion = load_function("Time Conversion", "timeConversion")
        self.assertEqual(time_conversion("07:05:45PM"), "19:05:45")
        self.assertEqual(time_conversion("12:01:00AM"), "00:01:00")
        self.assertEqual(time_conversion("12:01:00PM"), "12:01:00")

    def test_compare_triplets(self):
        compare_triplets = load_function("Compare the Triplets", "compareTriplets")
        self.assertEqual(compare_triplets([5, 6, 7], [3, 6, 10]), [1, 1])
        self.assertEqual(compare_triplets([1, 2, 3], [1, 2, 3]), [0, 0])

    def test_sparse_arrays(self):
        matching_strings = load_function("Sparse Arrays", "matchingStrings")
        self.assertEqual(
            matching_strings(
                ["aba", "baba", "aba", "xzxb"], ["aba", "xzxb", "ab"]
            ),
            [2, 1, 0],
        )
        self.assertEqual(matching_strings(["one", "one"], ["one", "one"]), [2, 2])


if __name__ == "__main__":
    unittest.main()
