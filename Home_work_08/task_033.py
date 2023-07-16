# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
import os

def add_user_data_to_json():
    user_data = {}
    used_ids = set()
    file_path = "user_data.json"

    # Проверяем, существует ли уже файл с данными
    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            user_data = json.load(file)
            # Получаем все использованные идентификаторы из существующих данных
            used_ids = set(user_id for level in user_data.values() for user_id in level.keys())

    while True:
        name = input("Введите имя пользователя: ")
        user_id = input("Введите личный идентификатор: ")
        access_level = input("Введите уровень доступа (от 1 до 7): ")

        # Проверяем, что введенный уровень доступа является числом от 1 до 7
        if not access_level.isdigit() or not (1 <= int(access_level) <= 7):
            print("Некорректный уровень доступа. Попробуйте снова.")
            continue

        # Проверяем, что идентификатор пользователя уникален независимо от уровня доступа
        if user_id in used_ids:
            print("Идентификатор пользователя уже использован. Попробуйте другой.")
            continue

        # Проверяем, существует ли уже группа пользователей с таким уровнем доступа
        if access_level not in user_data:
            user_data[access_level] = {}

        # Добавляем новую информацию в соответствующую группу по уровню доступа
        user_data[access_level][user_id] = name

        # Обновляем множество использованных идентификаторов
        used_ids.add(user_id)

        # Записываем обновленные данные в JSON файл
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(user_data, file, indent=4, ensure_ascii=False)

        choice = input("Продолжить ввод данных? (Y/N): ")
        if choice.lower() != "y":
            break

add_user_data_to_json()

