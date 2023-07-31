# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

import os
import json
import csv
import pickle

class DirectoryInfo:
    def __init__(self, directory):
        self.directory = directory
        self.info = self.directory_recursive_info()

    def directory_recursive_info(self):
        result = []

        # Обход директории и всех вложенных объектов
        for root, dirs, files in os.walk(self.directory):
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

    def save_info_to_json(self, json_file):
        with open(json_file, 'w') as file:
            json.dump(self.info, file, indent=4)

    def save_info_to_csv(self, csv_file):
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Type', 'Size (bytes)'])
            for item in self.info:
                writer.writerow([item['name'], item['type'], item['size']])

    def save_info_to_pickle(self, pickle_file):
        with open(pickle_file, 'wb') as file:
            pickle.dump(self.info, file)

# Пример использования класса
directory = "path/to/directory"
directory_info = DirectoryInfo(directory)
directory_info.save_info_to_json("info.json")
directory_info.save_info_to_csv("info.csv")
directory_info.save_info_to_pickle("info.pickle")
