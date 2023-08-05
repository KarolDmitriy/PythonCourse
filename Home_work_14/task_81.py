# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.


import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_perimeter(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.perimeter(), 18)

    def test_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_add_rectangles(self):
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(2, 3)
        result = rect1 + rect2
        self.assertEqual(result.length, 6)
        self.assertEqual(result.width, 8)

    def test_sub_rectangles(self):
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(2, 3)
        result = rect1 - rect2
        self.assertEqual(result.length, 2)
        self.assertEqual(result.width, 2)

    def test_eq_rectangles(self):
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(2, 10)
        self.assertEqual(rect1, rect2)

    def test_ne_rectangles(self):
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(2, 3)
        self.assertNotEqual(rect1, rect2)

    def test_lt_rectangles(self):
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(3, 6)
        self.assertLess(rect2, rect1)

    def test_gt_rectangles(self):
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(3, 6)
        self.assertGreater(rect1, rect2)


if __name__ == '__main__':
    unittest.main()
