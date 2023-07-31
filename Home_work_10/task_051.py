# Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            self.length = self.width = length
        else:
            self.length = length
            self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

# Пример использования класса
length = 5
width = 10
rectangle = Rectangle(length, width)

print(f"Периметр прямоугольника: {rectangle.perimeter()}")
print(f"Площадь прямоугольника: {rectangle.area()}")
