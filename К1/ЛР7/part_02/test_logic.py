"""
Unit-тесты для генератора sliding_sum
"""
import unittest
from logic import sliding_sum

class TestSlidingSum(unittest.TestCase):
    def test_basic_sliding_sum(self):
        result = list(sliding_sum([1, 2, 3, 4], k=2))
        expected = [3, 5, 7]
        self.assertEqual(result, expected)
    
    def test_sliding_sum_k3(self): # окно размера 3
        result = list(sliding_sum([1, 2, 3, 4, 5], k=3))
        expected = [6, 9, 12]
        self.assertEqual(result, expected)
    
    def test_sliding_sum_single_window(self): # k = длине данных
        result = list(sliding_sum([1, 2, 3, 4], k=4))
        expected = [10]
        self.assertEqual(result, expected)
    
    def test_invalid_k_zero(self): # проверка k=0
        with self.assertRaises(ValueError) as context:
            list(sliding_sum([1, 2, 3], k=0))
        self.assertIn("положительным", str(context.exception))
    
    def test_invalid_k_negative(self): # проверка отрицательного k
        with self.assertRaises(ValueError) as context:
            list(sliding_sum([1, 2, 3], k=-1))
        self.assertIn("положительным", str(context.exception))
    
    def test_invalid_k_too_large(self): # k больше длины данных
        with self.assertRaises(ValueError) as context:
            list(sliding_sum([1, 2, 3], k=5))
        self.assertIn("больше длины", str(context.exception))

    def test_lazy_evaluation(self): # Тест ленивых вычислений
        gen = sliding_sum([1, 2, 3, 4, 5], k=2)
        first = next(gen)
        self.assertEqual(first, 3, "Первое значение должно быть 3")
        second = next(gen)
        self.assertEqual(second, 5, "Второе значение должно быть 5")

print(list(sliding_sum([1, 2, 3, 4], k=2)))
print(list(sliding_sum([1, 2, 3, 4, 5], k=3)))
print(list(sliding_sum([1, 2, 3, 4], k=4)))
print(list(sliding_sum(range(1, 1000001), k=3))[:5])  # первые 5 сумм для большого диапазона

if __name__ == '__main__':
    unittest.main()
