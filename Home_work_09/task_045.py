# Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.

import json
import random
from functools import wraps

# Декоратор для сохранения параметров в JSON файл
def save_to_json(func):
    @wraps(func)
    def wrapper(target_number, num_attempts):
        # Вызываем декорируемую функцию и получаем результат
        result = func(target_number, num_attempts)

        # Подготавливаем данные для сохранения
        params = {
            'target_number': target_number,
            'num_attempts': num_attempts,
            'result': result
        }

        # Сохраняем данные в файл
        with open("game_params.json", 'a') as file:
            json.dump(params, file, indent=4)
            file.write('\n')

    return wrapper

# Декоратор для многократного запуска
def repeat_times(num_repeats):
    def decorator(func):
        @wraps(func)
        def wrapper(target_number, num_attempts):
            for _ in range(num_repeats):
                func(target_number, num_attempts)

        return wrapper
    return decorator

# Применяем декораторы
@repeat_times(num_repeats=3)
@save_to_json
def guess_number(target_number, num_attempts):
    print(f"Число загадано. У вас есть {num_attempts} попыток.")

    while num_attempts > 0:
        guess = int(input("Введите вашу догадку: "))

        if guess == target_number:
            print("Поздравляем! Вы угадали число!")
            return True
        elif guess < target_number:
            print("Загаданное число больше вашей догадки.")
        else:
            print("Загаданное число меньше вашей догадки.")

        num_attempts -= 1

    else:
        print("К сожалению, попытки закончились. Вы не угадали число.")
        return False

# Пример использования декорированной функции
guess_number(50, 5)
