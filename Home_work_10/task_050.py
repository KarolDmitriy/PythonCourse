# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Пример использования класса
radius = 5
circle = Circle(radius)

print(f"Длина окружности: {circle.circumference():.2f}")
print(f"Площадь окружности: {circle.area():.2f}")
