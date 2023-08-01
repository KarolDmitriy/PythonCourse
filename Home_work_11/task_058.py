# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

import time

class MyString(str):
    """
        Класс МояСтрока наследует все возможности стандартного типа str и дополнительно хранит информацию
        о имени автора строки и времени её создания.

        Атрибуты:
            author (str): Имя автора строки.
            creation_time (float): Время создания строки в формате timestamp.

        Методы:
            get_author(): Возвращает имя автора строки.
            get_creation_time(): Возвращает время создания строки.

    """
    def __new__(cls, value, author=None):
        obj = str.__new__(cls, value)
        obj.author = author
        obj.creation_time = time.time()
        return obj

    def get_author(self):
        return self.author

    def get_creation_time(self):
        return self.creation_time

# Пример использования класса
if __name__ == "__main__":
    my_string = MyString("Привет, мир!", author="John")
    print(my_string)  # Выводит: Привет, мир!
    print(my_string.get_author())  # Выводит: John
    print(my_string.get_creation_time())  # Выводит: текущее время в формате timestamp
