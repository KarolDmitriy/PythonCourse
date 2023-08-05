# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

class RectangleError(Exception):
    pass

class NegativeSideError(RectangleError):
    def __init__(self, side_name, value):
        self.side_name = side_name
        self.value = value
        super().__init__(f"Side {side_name} cannot be negative. Value: {value}")

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
            raise NegativeSideError("length", value)
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise NegativeSideError("width", value)
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
except NegativeSideError as e:
    print(e)  # Выводит: Side length cannot be negative. Value: -2

try:
    rectangle.width = -5
except NegativeSideError as e:
    print(e)  # Выводит: Side width cannot be negative. Value: -5
