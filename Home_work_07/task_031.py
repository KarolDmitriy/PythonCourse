# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

import os

def batch_rename_files(desired_name, num_digits, source_extension, destination_extension, name_range=None):
    directory = 'directory'  # текущий каталог, можно изменить на нужный

    # Получаем список файлов в каталоге
    file_list = os.listdir(directory)

    # Фильтруем файлы по расширению исходного файла
    filtered_files = [f for f in file_list if f.endswith(source_extension)]

    counter = 1

    for filename in filtered_files:
        # Создаем новое имя файла
        new_filename = ''

        # Добавляем желаемое конечное имя, если оно передано
        if desired_name:
            new_filename += desired_name

        # Добавляем диапазон сохраняемого оригинального имени
        if name_range:
            start_pos, end_pos = name_range
            original_name = filename[start_pos-1:end_pos]
            new_filename += original_name

        # Добавляем порядковый номер
        counter_str = str(counter).zfill(num_digits)
        new_filename += counter_str

        # Добавляем расширение конечного файла
        new_filename += destination_extension

        # Переименовываем файл
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

        counter += 1

# Пример использования
batch_rename_files('new_file', 3, '.txt', '.docx', [3, 6])
