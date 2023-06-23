# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

# Генерация случайного числа
num = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Программа загадала число от 0 до 1000. Попробуйте угадать!")

for attempt in range(1, MAX_ATTEMPTS + 1):
    print(f"Попытка {attempt}:")

    # Ввод числа пользователем
    guess = int(input("Введите ваше предположение: "))

    # Проверка угаданного числа
    if guess == num:
        print("Поздравляю! Вы угадали число.")
        break
    elif guess < num:
        print("Загаданное число больше вашего предположения.")
    else:
        print("Загаданное число меньше вашего предположения.")

    if attempt == MAX_ATTEMPTS:
        print("Вы использовали все попытки. Игра окончена.")

print(f"Загаданное число: {num}")
