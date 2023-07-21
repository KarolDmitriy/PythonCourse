# Нахождение корней квадратного уравнения

import math

def quadratic_equation_solver(a, b, c):
    def calculate_discriminant():
        return b**2 - 4*a*c

    @check_discriminant
    def calculate_roots():
        discriminant = calculate_discriminant()
        if discriminant < 0:
            return None, None
        elif discriminant == 0:
            root = -b / (2*a)
            return root, None
        else:
            sqrt_discriminant = math.sqrt(discriminant)
            root1 = (-b + sqrt_discriminant) / (2*a)
            root2 = (-b - sqrt_discriminant) / (2*a)
            return root1, root2

    return calculate_roots()

# Декоратор для проверки значения дискриминанта
def check_discriminant(func):
    def wrapper():
        root1, root2 = func()
        if root1 is None and root2 is None:
            print("Уравнение не имеет корней.")
        elif root2 is None:
            print(f"Уравнение имеет один корень: x = {root1:.2f}")
        else:
            print(f"Уравнение имеет два корня: x1 = {root1:.2f}, x2 = {root2:.2f}")

    return wrapper

# Пример использования функции
a, b, c = 3, -5, 2
quadratic_equation_solver(a, b, c)
