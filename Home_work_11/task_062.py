# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Unsupported operand type for +: 'Rectangle' and '{}'".format(type(other).__name__))
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Unsupported operand type for -: 'Rectangle' and '{}'".format(type(other).__name__))
        new_length = self.length - other.length
        new_width = self.width - other.width
        # Ограничиваем новые размеры, чтобы не было отрицательных значений
        new_length = max(new_length, 0)
        new_width = max(new_width, 0)
        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.area() == other.area()

    def __ne__(self, other):
        if not isinstance(other, Rectangle):
            return True
        return self.area() != other.area()

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Unsupported operand type for <: 'Rectangle' and '{}'".format(type(other).__name__))
        return self.area() < other.area()

    def __le__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Unsupported operand type for <=: 'Rectangle' and '{}'".format(type(other).__name__))
        return self.area() <= other.area()

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Unsupported operand type for >: 'Rectangle' and '{}'".format(type(other).__name__))
        return self.area() > other.area()

    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Unsupported operand type for >=: 'Rectangle' and '{}'".format(type(other).__name__))
        return self.area() >= other.area()

    def __str__(self):
        return f"Rectangle: length={self.length}, width={self.width}"

# Пример использования
rect1 = Rectangle(4, 5)
rect2 = Rectangle(2, 3)
rect3 = Rectangle(6, 2)

print(rect1 == rect2)  # Выводит: False
print(rect1 != rect2)  # Выводит: True
print(rect1 < rect2)   # Выводит: False
print(rect1 <= rect2)  # Выводит: False
print(rect1 > rect2)   # Выводит: True
print(rect1 >= rect2)  # Выводит: True

print(rect1 == rect3)  # Выводит: False
print(rect1 != rect3)  # Выводит: True
print(rect1 < rect3)   # Выводит: True
print(rect1 <= rect3)  # Выводит: True
print(rect1 > rect3)   # Выводит: False
print(rect1 >= rect3)  # Выводит: False
