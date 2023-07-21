# Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.

import csv
import random

def generate_csv_file(rows):
    def generate_random_numbers():
        return [random.randint(1, 1000) for _ in range(3)]

    @write_to_csv_file
    def generate_data():
        return [generate_random_numbers() for _ in range(rows)]

    generate_data()

# Декоратор для записи данных в CSV файл
def write_to_csv_file(func):
    def wrapper():
        data = func()

        with open('random_numbers.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    return wrapper

# Генерируем CSV файл с 100-1000 строками
rows_count = random.randint(100, 1000)
generate_csv_file(rows_count)
