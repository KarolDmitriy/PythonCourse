# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import csv
import json


def process_user_data_csv(csv_file, json_file):
    processed_data = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_data = csv.reader(file)

        # Пропускаем первую строку (заголовок)
        next(csv_data)

        for row in csv_data:
            # Дополнение идентификатора до 10 цифр незначащими нулями
            user_id = row[0].zfill(10)

            # Преобразование имени, чтобы первая буква была прописной
            name = row[1].capitalize()

            # Создание хеша на основе имени и идентификатора
            hash_value = hash(name + user_id)

            # Создание словаря с обработанными данными
            processed_row = {
                'id': user_id,
                'name': name,
                'hash': hash_value
            }

            processed_data.append(processed_row)

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(processed_data, file, indent=4, ensure_ascii=False)


# Пример использования функции
process_user_data_csv('user_data.csv', 'processed_data.json')

