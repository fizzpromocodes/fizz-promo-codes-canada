import unittest

from fizz_region import fizz_available, normalize, province_of


class FizzRegionTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize(" h2x 1y4 "), "H2X1Y4")

    def test_provinces(self):
        self.assertEqual(province_of("H2X 1Y4"), "Quebec")
        self.assertEqual(province_of("M5V 2T6"), "Ontario")
        self.assertEqual(province_of("R3C 0A5"), "Manitoba")
        self.assertEqual(province_of("T2P 1J9"), "Alberta")
        self.assertEqual(province_of("V6B 1A1"), "British Columbia")
        self.assertEqual(province_of("B3J 1S9"), "Nova Scotia")

    def test_availability(self):
        self.assertTrue(fizz_available("G1R 4P5"))
        self.assertFalse(fizz_available("E1C 1A1"))

    def test_invalid(self):
        for bad in ["", "12345", "D2X 1Y4", "H2X1Y"]:
            with self.assertRaises(ValueError):
                province_of(bad)


if __name__ == "__main__":
    unittest.main()
