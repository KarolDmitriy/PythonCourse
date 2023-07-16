# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import json
import csv

def save_as_csv():
    user_data = {}

    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        print("Файл user_data.json не найден.")
        return

    with open('user_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Access Level'])

        for access_level, users in user_data.items():
            for user_id, name in users.items():
                writer.writerow([user_id, name, access_level])

    print("Файл user_data.csv сохранен.")

save_as_csv()

