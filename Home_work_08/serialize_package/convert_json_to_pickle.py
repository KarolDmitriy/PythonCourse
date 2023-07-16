# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import json
import pickle


def convert_json_to_pickle(directory):
    # Проверяем, что указанный путь является директорией
    if not os.path.isdir(directory):
        print(f"Ошибка: '{directory}' не является директорией.")
        return

    # Перебираем все файлы в указанной директории
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Проверяем, что файл имеет расширение .json
        if os.path.isfile(file_path) and filename.endswith(".json"):
            # Открываем JSON файл для чтения
            with open(file_path, "r", encoding="utf-8") as json_file:
                try:
                    # Загружаем содержимое JSON файла
                    json_data = json.load(json_file)

                    # Создаем имя для pickle файла
                    pickle_filename = os.path.splitext(filename)[0] + ".pickle"
                    pickle_file_path = os.path.join(directory, pickle_filename)

                    # Сохраняем содержимое JSON файла в виде pickle файла
                    with open(pickle_file_path, "wb") as pickle_file:
                        pickle.dump(json_data, pickle_file)

                    print(f"Преобразован файл: {filename}")

                except json.JSONDecodeError as e:
                    print(f"Ошибка при чтении файла {filename}: {str(e)}")


# Пример использования функции
convert_json_to_pickle("pickle")

