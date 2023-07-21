# Создайте функцию-замыкание, которая запрашивает два целых числа:
# - от 1 до 100 для загадывания,
# - от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

def guessing_game():
    lower_bound = 1
    upper_bound = 100
    max_attempts = 10

    def create_guessing_function():
        # Запрашиваем загадываемое число и количество попыток у пользователя
        target_number = int(input(f"Загадайте число от {lower_bound} до {upper_bound}: "))
        num_attempts = int(input(f"Сколько попыток у вас будет: "))

        # Проверяем, что числа находятся в допустимых пределах
        target_number = max(lower_bound, min(upper_bound, target_number))
        num_attempts = max(1, min(max_attempts, num_attempts))

        def guess_number():
            nonlocal num_attempts

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

        return guess_number

    return create_guessing_function


# Пример использования функции-замыкания
game = guessing_game()
play_game = game()
play_game()
