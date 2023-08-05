# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.

import json

class User:
    def __init__(self, name, user_id, access_level):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

def read_users_from_json(file_path):
    users = set()
    with open(file_path, "r", encoding="utf-8") as file:
        user_data = json.load(file)
        for access_level, level_users in user_data.items():
            for user_id, name in level_users.items():
                users.add(User(name, user_id, int(access_level)))
    return users

# Пример использования функции read_users_from_json
users = read_users_from_json("user_data.json")
for user in users:
    print(f"Имя: {user.name}, Идентификатор: {user.user_id}, Уровень доступа: {user.access_level}")
