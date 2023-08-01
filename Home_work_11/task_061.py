# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    def __init__(self, length, width):
        """
        Создает прямоугольник с заданными длиной и шириной.

        :param length: длина прямоугольника
        :param width: ширина прямоугольника
        """
        self.length = length
        self.width = width

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        :return: периметр прямоугольника
        """
        return 2 * (self.length + self.width)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        :return: площадь прямоугольника
        """
        return self.length * self.width

    def __add__(self, other):
        """
        Складывает два прямоугольника, создавая новый прямоугольник.

        :param other: прямоугольник, который нужно сложить с текущим
        :return: новый прямоугольник, результат сложения
        """
        if not isinstance(other, Rectangle):
            raise TypeError("Unsupported operand type for +: 'Rectangle' and '{}'".format(type(other).__name__))
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        """
        Вычитает прямоугольник из текущего, создавая новый прямоугольник.

        :param other: прямоугольник, который нужно вычесть из текущего
        :return: новый прямоугольник, результат вычитания
        """
        if not isinstance(other, Rectangle):
            raise TypeError("Unsupported operand type for -: 'Rectangle' and '{}'".format(type(other).__name__))
        new_length = self.length - other.length
        new_width = self.width - other.width
        # Ограничиваем новые размеры, чтобы не было отрицательных значений
        new_length = max(new_length, 0)
        new_width = max(new_width, 0)
        return Rectangle(new_length, new_width)

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        :return: строковое представление прямоугольника
        """
        return f"Rectangle: length={self.length}, width={self.width}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника для программиста.

        :return: строковое представление прямоугольника для программиста
        """
        return f"Rectangle({self.length}, {self.width})"

