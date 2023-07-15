# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число = -1000, максимальное = +1000.
# Количество строк и имя файла передаются как аргументы функции.

import random

def fill_file_with_random_pairs(file_name, num_lines):
    with open(file_name, 'a') as file:
        for _ in range(num_lines):
            random_int = random.randint(-1000, 1000)
            random_float = round(random.uniform(-1000, 1000), 2)
            line = f"{random_int}|{random_float}"
            file.write(line + '\n')


fill_file_with_random_pairs("random_pairs.txt", 5)

