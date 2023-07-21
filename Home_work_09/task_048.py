# Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.

import csv
import math

def quadratic_equation_solver(a, b, c):
    discriminant = b**2 - 4*a*c

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

def read_csv_file(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            a, b, c = map(int, row)
            yield a, b, c

# Декоратор для запуска функции нахождения корней квадратного уравнения с каждой тройкой чисел
def process_csv_file(func):
    def wrapper(filename):
        for a, b, c in read_csv_file(filename):
            root1, root2 = func(a, b, c)
            print(f"Корни уравнения {a}x^2 + {b}x + {c} = 0: {root1}, {root2}")
    return wrapper

# Применяем декоратор к функции quadratic_equation_solver
@process_csv_file
def solve_quadratic_equation(a, b, c):
    return quadratic_equation_solver(a, b, c)

# Прочитаем данные из файла и найдем корни уравнения для каждой тройки чисел
solve_quadratic_equation('random_numbers.csv')
