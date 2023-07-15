# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

import random
import string

def create_files_with_extensions(extensions, num_files_per_extension):
    for extension, num_files in zip(extensions, num_files_per_extension):
        create_files_with_extension(extension, num_files=num_files)

def create_files_with_extension(extension, min_length=6, max_length=30, min_size=256, max_size=4096, num_files=42):
    for i in range(num_files):
        name_length = random.randint(min_length, max_length)
        file_name = ''.join(random.choices(string.ascii_lowercase, k=name_length)) + extension

        file_size = random.randint(min_size, max_size)
        random_bytes = bytearray(random.getrandbits(8) for _ in range(file_size))

        with open(file_name, 'wb') as file:
            file.write(random_bytes)


extensions = [".txt", ".csv", ".jpg"]
num_files_per_extension = [2, 1, 3]

create_files_with_extensions(extensions, num_files_per_extension)
