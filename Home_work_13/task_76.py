# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.


import json

class MyBaseException(Exception):
    def __init__(self, message, user=None):
        super().__init__(message)
        self.user = user

class LevelError(MyBaseException):
    def __init__(self, message, user=None):
        super().__init__(message, user)

class AccessError(MyBaseException):
    def __init__(self, message, user=None):
        super().__init__(message, user)

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
            raise AccessError("Отказано в доступе", user=user)
        return user.access_level

    def add_user(self, user):
        if user.access_level < self.access_level:
            raise LevelError("Недопустимый уровень доступа", user=user)
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
    print(f"Ошибка доступа: {ae}. Пользователь: {ae.user.name}, ID: {ae.user.user_id}")

new_user = User("Alice", "456", 3)
try:
    project.add_user(new_user)
    print("Пользователь успешно добавлен")
except LevelError as le:
    print(f"Ошибка уровня: {le}. Пользователь: {le.user.name}, ID: {le.user.user_id}")
