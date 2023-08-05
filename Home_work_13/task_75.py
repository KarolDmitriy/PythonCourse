# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4) вход в систему - требует указать имя и id пользователя.
# Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа.
# А если пользователь есть, получите его уровень из множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.


import json

# Базовый класс исключения
class MyBaseException(Exception):
    pass

# Дочерний класс исключения "Ошибка уровня"
class LevelError(MyBaseException):
    pass

# Дочерний класс исключения "Ошибка доступа"
class AccessError(MyBaseException):
    pass

class User:
    def __init__(self, name, user_id, access_level):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __hash__(self):
        return hash(self.user_id)

class Project:
    def __init__(self, file_path, access_level):
        self.users = read_users_from_json(file_path)
        self.access_level = access_level

    def enter_system(self, name, user_id):
        user = User(name, user_id, 0)
        if user not in self.users:
            raise AccessError("Отказано в доступе")
        return user.access_level

    def add_user(self, user):
        if user.access_level < self.access_level:
            raise LevelError("Недопустимый уровень доступа")
        self.users.add(user)

def read_users_from_json(file_path):
    users = set()
    with open(file_path, "r", encoding="utf-8") as file:
        user_data = json.load(file)
        for access_level, level_users in user_data.items():
            for user_id, name in level_users.items():
                users.add(User(name, user_id, int(access_level)))
    return users

# Пример использования
project = Project("user_data.json", access_level=5)

try:
    user_level = project.enter_system("John", "123")
    print(f"Уровень доступа пользователя: {user_level}")
except AccessError as ae:
    print(f"Ошибка доступа: {ae}")

new_user = User("Alice", "456", 3)
try:
    project.add_user(new_user)
    print("Пользователь успешно добавлен")
except LevelError as le:
    print(f"Ошибка уровня: {le}")
