# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def directory_recursive_info(directory):
    result = []

    # Обход директории и всех вложенных объектов
    for root, dirs, files in os.walk(directory):
        directory_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        directory_size += sum(os.path.getsize(os.path.join(root, dir)) for dir in dirs)

        # Добавление информации о директории
        directory_info = {
            'name': root,
            'type': 'directory',
            'size': directory_size
        }
        result.append(directory_info)

        # Добавление информации о файлах в директории
        for file in files:
            file_path = os.path.join(root, file)
            file_info = {
                'name': file,
                'type': 'file',
                'size': os.path.getsize(file_path)
            }
            result.append(file_info)

    return result


def save_info_to_json(directory, json_file):
    info = directory_recursive_info(directory)
    with open(json_file, 'w') as file:
        json.dump(info, file, indent=4)


def save_info_to_csv(directory, csv_file):
    info = directory_recursive_info(directory)
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Type', 'Size (bytes)'])
        for item in info:
            writer.writerow([item['name'], item['type'], item['size']])


def save_info_to_pickle(directory, pickle_file):
    info = directory_recursive_info(directory)
    with open(pickle_file, 'wb') as file:
        pickle.dump(info, file)


# Пример использования функций
directory = 'pickle'

save_info_to_json(directory, 'directory_info.json')
save_info_to_csv(directory, 'directory_info.csv')
save_info_to_pickle(directory, 'directory_info.pickle')
