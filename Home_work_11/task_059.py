# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

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

# Пример использования класса
if __name__ == "__main__":
    arch1 = Arch(42, "Hello")
    arch2 = Arch(123, "World")

    print(arch1.get_number())  # Выводит: 42
    print(arch1.get_string())  # Выводит: Hello

    print(arch2.get_number())  # Выводит: 123
    print(arch2.get_string())  # Выводит: World

    print(Arch.get_number_archive())  # Выводит: [42, 123]
    print(Arch.get_string_archive())  # Выводит: ['Hello', 'World']
