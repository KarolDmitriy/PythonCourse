# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("Length cannot be negative.")
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative.")
        self._width = value

    def perimeter(self):
        return 2 * (self._length + self._width)

    def area(self):
        return self._length * self._width

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Unsupported operand type for +: 'Rectangle' and '{}'".format(type(other).__name__))
        new_length = self._length + other._length
        new_width = self._width + other._width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Unsupported operand type for -: 'Rectangle' and '{}'".format(type(other).__name__))
        new_length = self._length - other._length
        new_width = self._width - other._width
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
        return f"Rectangle: length={self._length}, width={self._width}"


# Создаем экземпляр класса Rectangle
rectangle = Rectangle(5, 3)

# Выводим информацию о прямоугольнике
print(rectangle)  # Выводит: Rectangle: length=5, width=3

# Получаем периметр и площадь
print("Perimeter:", rectangle.perimeter())  # Выводит: Perimeter: 16
print("Area:", rectangle.area())  # Выводит: Area: 15

# Изменяем длину и ширину с помощью свойств
rectangle.length = 10
rectangle.width = 7

# Выводим информацию о прямоугольнике после изменения
print(rectangle)  # Выводит: Rectangle: length=10, width=7

# Пытаемся задать отрицательные значения для длины и ширины
try:
    rectangle.length = -2
except ValueError as e:
    print(e)  # Выводит: Length cannot be negative.

try:
    rectangle.width = -5
except ValueError as e:
    print(e)  # Выводит: Width cannot be negative.

