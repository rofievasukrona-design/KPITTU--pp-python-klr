from sliding import max_sum
import unittest

class TestMaxSum(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 2), 9)

    def test_negative_values(self):
        self.assertEqual(max_sum([-1, -2, -3], 2), -3)

    def test_full_length(self):
        self.assertEqual(max_sum([1, 2, 3], 3), 6)

    def test_invalid_k_too_large(self):
        with self.assertRaises(ValueError):
            max_sum([1, 2], 5)

    def test_invalid_k_zero(self):
        with self.assertRaises(ValueError):
            max_sum([1, 2, 3], 0)


if __name__ == "__main__":
    unittest.main()
