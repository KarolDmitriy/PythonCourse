# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import random
import string
import os


def create_files_with_extensions(extensions, num_files_per_extension, directory):
    for extension, num_files in zip(extensions, num_files_per_extension):
        create_files_with_extension(extension, num_files=num_files, directory=directory)


def create_files_with_extension(extension, min_length=6, max_length=30, min_size=256, max_size=4096, num_files=42, directory=""):
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    existing_files = set(os.listdir(directory))

    for i in range(num_files):
        name_length = random.randint(min_length, max_length)
        file_name = ''.join(random.choices(string.ascii_lowercase, k=name_length)) + extension

        while file_name in existing_files:
            name_length = random.randint(min_length, max_length)
            file_name = ''.join(random.choices(string.ascii_lowercase, k=name_length)) + extension

        file_path = os.path.join(directory, file_name)

        file_size = random.randint(min_size, max_size)
        random_bytes = bytearray(random.getrandbits(8) for _ in range(file_size))

        with open(file_path, 'wb') as file:
            file.write(random_bytes)


extensions = [".txt", ".csv", ".jpg", ".avi"]
num_files_per_extension = [3, 1, 3, 2]
directory = "directory"

create_files_with_extensions(extensions, num_files_per_extension, directory)
