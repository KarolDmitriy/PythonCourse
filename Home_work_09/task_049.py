# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
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

# Декоратор для сохранения переданных параметров и результатов работы функции в JSON файл
def save_to_json(func):
    def wrapper(a, b, c):
        result = func(a, b, c)

        data = {
            'a': a,
            'b': b,
            'c': c,
            'result': result
        }

        with open('quadratic_equation_results.json', 'a') as file:
            json.dump(data, file)
            file.write('\n')

        return result

    return wrapper

# Применяем декоратор к функции quadratic_equation_solver
@save_to_json
def solve_quadratic_equation(a, b, c):
    return quadratic_equation_solver(a, b, c)

# Прочитаем данные из файла и найдем корни уравнения для каждой тройки чисел
for a, b, c in read_csv_file('random_numbers.csv'):
    solve_quadratic_equation(a, b, c)
