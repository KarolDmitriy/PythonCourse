# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv
import codecs

def convert_pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as file:
        data = pickle.load(file)

    if not data:
        print("Список словарей пуст.")
        return

    # Извлечение ключей словаря для заголовков столбца
    fieldnames = list(data[0].keys())

    with codecs.open(csv_file, 'w', encoding='utf-8', errors='replace') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Файл {csv_file} успешно создан.")

# Пример использования функции
convert_pickle_to_csv('pickle/processed_data.pickle', 'processed_data.csv')

