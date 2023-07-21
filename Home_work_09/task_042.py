# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат,
# который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json
import os

def save_to_json(func):
    def wrapper(*args, **kwargs):
        # Получаем имя декорируемой функции
        function_name = func.__name__

        # Проверяем, есть ли уже файл с таким именем
        if not os.path.exists(f"{function_name}.json"):
            with open(f"{function_name}.json", 'w') as file:
                pass

        # Загружаем данные из файла (если он не пустой)
        with open(f"{function_name}.json", 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

        # Вызываем декорируемую функцию и получаем результат
        result = func(*args, **kwargs)

        # Подготавливаем данные для сохранения
        params = {
            'args': args,
            'kwargs': kwargs,
            'result': result
        }

        # Добавляем данные в список
        data.append(params)

        # Сохраняем данные в файл
        with open(f"{function_name}.json", 'w') as file:
            json.dump(data, file, indent=4)

        return result

    return wrapper

# Пример использования декоратора
@save_to_json
def add(a, b):
    return a + b

@save_to_json
def multiply(a, b):
    return a * b

# Пример вызовов декорированных функций
add(2, 3)
add(5, 6)

multiply(2, 3)
multiply(4, 5)
