

class Arch:
    """
        Класс Arch хранит пару свойств и архивирует данные для всех экземпляров класса.

        Атрибуты:
            num_arch (list): Список-архив для числовых данных.
            str_arch (list): Список-архив для строковых данных.

        Методы:
            __init__(number, string): Инициализирует объект и добавляет новые данные в архивы.
            get_number(): Возвращает числовое значение объекта.
            get_string(): Возвращает строковое значение объекта.
            get_number_archive(): Возвращает список числовых данных из архива.
            get_string_archive(): Возвращает список строковых данных из архива.
    """
    # Списки-архивы, которые хранят старые данные
    num_arch = []
    str_arch = []

    def __init__(self, number, string):
        # Сохраняем новые данные в атрибуты экземпляра
        self.number = number
        self.string = string

        # Добавляем новые данные в архивы
        Arch.num_arch.append(number)
        Arch.str_arch.append(string)

    def get_number(self):
        return self.number

    def get_string(self):
        return self.string

    @classmethod
    def get_number_archive(cls):
        return cls.num_arch

    @classmethod
    def get_string_archive(cls):
        return cls.str_arch
    def __repr__(self):
        return f"Arch({self.number}, '{self.string}')"

    def __str__(self):
        return f"Number: {self.number}, String: '{self.string}'"

# Пример использования
arch1 = Arch(42, "Hello")
print(repr(arch1))  # Выводит: Arch(42, 'Hello')
print(str(arch1))   # Выводит: Number: 42, String: 'Hello'
