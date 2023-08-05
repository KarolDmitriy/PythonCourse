# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# 1. doctest,
# 2. unittest,
# 3. pytest.

import unittest

from Home_work_14.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_perimeter(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.perimeter(), 18)

    def test_perimeter(self):
        rect1 = Rectangle(4, 5)
        self.assertEqual(rect1.perimeter(), 18)

        rect2 = Rectangle(3, 7)
        self.assertEqual(rect2.perimeter(), 20)

        rect3 = Rectangle(0, 0)
        self.assertEqual(rect3.perimeter(), 0)

    def test_add(self):
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(3, 7)
        result = rect1 + rect2
        self.assertEqual(result.length, 7)
        self.assertEqual(result.width, 12)

        rect3 = Rectangle(0, 0)
        result = rect1 + rect3
        self.assertEqual(result.length, 4)
        self.assertEqual(result.width, 5)

    def test_subtract(self):
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(3, 3)
        result = rect1 - rect2
        self.assertEqual(result.length, 1)
        self.assertEqual(result.width, 2)

        result = rect2 - rect1
        self.assertEqual(result.length, 0)
        self.assertEqual(result.width, 0)

if __name__ == '__main__':
    unittest.main()
