import unittest

from solution import timeConversion


class TimeConversionTests(unittest.TestCase):
    def test_evening(self):
        self.assertEqual(timeConversion("07:05:45PM"), "19:05:45")

    def test_midnight_and_noon(self):
        self.assertEqual(timeConversion("12:01:00AM"), "00:01:00")
        self.assertEqual(timeConversion("12:01:00PM"), "12:01:00")


if __name__ == "__main__":
    unittest.main()
