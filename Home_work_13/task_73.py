# Создайте класс с базовым исключением и дочерние классы-исключения:
# ошибка уровня,
# ошибка доступа.

# Базовый класс исключения
class MyBaseException(Exception):
    pass

# Дочерний класс исключения "Ошибка уровня"
class LevelError(MyBaseException):
    pass

# Дочерний класс исключения "Ошибка доступа"
class AccessError(MyBaseException):
    pass


def check_level(level):
    if level < 1 or level > 10:
        raise LevelError("Недопустимый уровень")

def check_access(user):
    if not user.has_access:
        raise AccessError("Отказано в доступе")

class User:
    def __init__(self, name, has_access):
        self.name = name
        self.has_access = has_access

try:
    user = User("John", has_access=False)
    check_level(5)
    check_access(user)
except LevelError as le:
    print(f"Ошибка уровня: {le}")
except AccessError as ae:
    print(f"Ошибка доступа: {ae}")
