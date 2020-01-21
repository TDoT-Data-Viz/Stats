import unittest
import numpy as np
import calculate_vif as cv


class TestCalculateVIF(unittest.TestCase):

    def test_generate_vif(self):
        result = cv.generate_vif("test_vif.csv")
        self.assertEqual(result, "[1.04469526 3.42167043 3.37697517]")


if __name__ == '__main__':
    unittest.main()
