# 1. В проекте создать новый модуль test_python.py
 
# 2. В модуле написать тесты для встроенных функций filter, map, sorted, 
# а также для функций из библиотеки math: pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше

import unittest
import math

class TestBuiltInFunctions(unittest.TestCase):
    def test_filter(self):
        # Проверяем, что filter правильно отфильтровывает элементы
        result = list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))
        self.assertEqual(result, [6, 7])

    def test_map(self):
        # Проверяем, что map правильно применяет функцию к каждому элементу
        result = list(map(lambda x: x * 2, [1, 2, 3]))
        self.assertEqual(result, [2, 4, 6])

    def test_sorted(self):
        # Проверяем, что sorted правильно сортирует элементы
        result = sorted([3, 1, 2], reverse=True)
        self.assertEqual(result, [3, 2, 1])

class TestMathFunctions(unittest.TestCase):
    def test_pi(self):
        # Проверяем значение math.pi
        self.assertEqual(math.pi, 3.141592653589793)

    def test_sqrt(self):
        # Проверяем корректность вычисления квадратного корня
        self.assertEqual(math.sqrt(4), 2.0)

    def test_pow(self):
        # Проверяем корректность возведения в степень
        self.assertEqual(math.pow(2, 3), 8.0)

    def test_hypot(self):
        # Проверяем корректность вычисления гипотенузы
        self.assertEqual(math.hypot(3, 4), 5.0)

if __name__ == '__main__':
    unittest.main()