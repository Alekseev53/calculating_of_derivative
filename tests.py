import unittest
import lib
import math

class TestNumericalMethods(unittest.TestCase):
    H_BIG = 0.00001
    DELTA = 1e-4  # Абсолютный допуск для проверки точности

    # Добавление тестов для различных функций в методах прямой и центральной разности
    def test_forward_difference_various_functions(self):
        # Тестирование метода прямой разности с разными функциями
        test_functions = [
            (math.sin, 0, 1),
            (lambda x: x**2, 2, 4),
            (math.exp, 1, math.exp(1)),
        ]
        for f, x, expected in test_functions:
            with self.subTest(f=f, x=x):
                self.assertAlmostEqual(lib.forward_difference(f, x, self.H_BIG), expected, delta=self.DELTA)

    def test_central_difference_various_functions(self):
        # Тестирование центральной разностной схемы с разными функциями
        test_functions = [
            (math.cos, 0, 0),
            (lambda x: x**3, 1, 3),
            (math.log, 1, 1),
        ]
        for f, x, expected in test_functions:
            with self.subTest(f=f, x=x):
                self.assertAlmostEqual(lib.central_difference(f, x, self.H_BIG), expected, delta=self.DELTA)

    # Тесты для метода высшего порядка с разными функциями
    def test_higher_order_method_various_functions(self):
        test_functions = [
            (math.exp, 1, math.exp(1)),
            (math.sin, math.pi / 4, math.cos(math.pi / 4)),
        ]
        for f, x, expected in test_functions:
            with self.subTest(f=f, x=x):
                self.assertAlmostEqual(lib.higher_order_method(f, x, self.H_BIG), expected, delta=self.DELTA)

    # Оставляем специфические тесты для разных значений h
    def test_method_with_small_h(self):
        self.assertAlmostEqual(lib.central_difference(math.sin, math.pi / 4, 1e-6), math.cos(math.pi / 4), delta=self.DELTA)

    def test_method_with_large_h(self):
        self.assertNotAlmostEqual(lib.central_difference(math.sin, math.pi / 4, 1), math.cos(math.pi / 4), delta=self.DELTA)

    def test_forward_difference_with_negative_h(self):
        self.assertAlmostEqual(lib.forward_difference(math.sin, math.pi / 4, -self.H_BIG), math.cos(math.pi / 4), delta=self.DELTA)

    # Другие тесты могут быть добавлены по мере необходимости

if __name__ == '__main__':
    unittest.main()
