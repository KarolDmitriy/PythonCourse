# Угарай число
from Home_work_06.my_package.guess_module import guess_number


# Ввод параметров игры
lower_bound = int(input("Введите нижнюю границу: "))
upper_bound = int(input("Введите верхнюю границу: "))
attempts = int(input("Введите количество попыток: "))

# Вызов функции угадывания числа
result = guess_number(lower_bound, upper_bound, attempts)

# Вывод результата
if result:
    print("Вы победили!")
else:
    print("Вы проиграли!")
