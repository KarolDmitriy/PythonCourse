# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.


def power_recursive(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / power_recursive(a, -b)
    elif b % 2 == 0:
        half_power = power_recursive(a, b // 2)
        return half_power * half_power
    else:
        return a * power_recursive(a, b - 1)

# Получаем ввод от пользователя
a = float(input("Введите число A: "))
b = int(input("Введите степень B: "))

# Вызываем функцию для возведения в степень
result = power_recursive(a, b)

# Выводим результат
print("Результат:", result)
