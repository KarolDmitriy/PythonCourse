# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

import random

def guessing_game_validator(func):
    def wrapper():
        lower_bound = 1
        upper_bound = 100
        max_attempts = 10

        target_number = int(input(f"Загадайте число от {lower_bound} до {upper_bound}: "))
        num_attempts = int(input(f"Сколько попыток у вас будет: "))

        # Проверяем, что числа находятся в допустимых пределах
        if not (lower_bound <= target_number <= upper_bound) or not (1 <= num_attempts <= max_attempts):
            target_number = random.randint(lower_bound, upper_bound)
            num_attempts = random.randint(1, max_attempts)
            print("Введенные числа не входят в допустимые пределы. Будут использованы случайные числа.")

        func(target_number, num_attempts)

    return wrapper


@guessing_game_validator
def guess_number(target_number, num_attempts):
    print(f"У вас есть {num_attempts} попыток.")

    while num_attempts > 0:
        guess = int(input("Введите вашу догадку: "))

        if guess == target_number:
            print("Поздравляем! Вы угадали число!")
            break
        elif guess < target_number:
            print("Загаданное число больше вашей догадки.")
        else:
            print("Загаданное число меньше вашей догадки.")

        num_attempts -= 1

    else:
        print("К сожалению, попытки закончились. Вы не угадали число.")


# Пример использования декоратора и функции
guess_number()
