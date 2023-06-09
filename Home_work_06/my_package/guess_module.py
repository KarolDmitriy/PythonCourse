# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.


import random
import sys

__all__ = ['guess_number']

def guess_number(lower, upper, attempts):
    number = random.randint(lower, upper)

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Попытка {attempt}. Угадайте число: "))

        if guess == number:
            print("Поздравляю! Вы угадали число!")
            return True
        elif guess < number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

    print(f"К сожалению, попытки исчерпаны. Загаданное число было {number}.")
    return False

if __name__ == "__main__":
    # Получение аргументов командной строки
    args = sys.argv[1:]

    # Преобразование строковых аргументов в числовые параметры
    lower_bound = int(args[0])
    upper_bound = int(args[1])
    attempts = int(args[2])

    # Вызов функции угадывания числа
    result = guess_number(lower_bound, upper_bound, attempts)

    # Вывод результата
    if result:
        print("Вы победили!")
    else:
        print("Вы проиграли!")
