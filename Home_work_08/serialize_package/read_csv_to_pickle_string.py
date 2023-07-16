# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle


def read_csv_to_pickle_string(csv_file):
    pickle_data = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_data = csv.reader(file)

        # Пропускаем заголовок
        next(csv_data)

        for row in csv_data:
            pickle_data.append(row)

    pickle_string = pickle.dumps(pickle_data)

    return pickle_string


# Пример использования функции
csv_file = 'processed_data.csv'
pickle_string = read_csv_to_pickle_string(csv_file)

# Распечатываем строку pickle
print(pickle_string)
