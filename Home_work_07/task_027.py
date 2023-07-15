# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

import random
import string

def create_files_with_extension(extension, min_length=6, max_length=30, min_size=256, max_size=4096, num_files=42):
    for i in range(num_files):
        name_length = random.randint(min_length, max_length)
        file_name = ''.join(random.choices(string.ascii_lowercase, k=name_length)) + extension

        file_size = random.randint(min_size, max_size)
        random_bytes = bytearray(random.getrandbits(8) for _ in range(file_size))

        with open(file_name, 'wb') as file:
            file.write(random_bytes)


create_files_with_extension(".txt", min_length=8, max_length=20, min_size=512, max_size=2048, num_files=10)
