# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def calculate_fraction_operations(fraction1, fraction2):
    # Преобразование строк в объекты Fraction
    fraction1 = Fraction(fraction1)
    fraction2 = Fraction(fraction2)

    # Вычисление суммы дробей
    sum_fraction = fraction1 + fraction2

    # Вычисление произведения дробей
    product_fraction = fraction1 * fraction2

    return sum_fraction, product_fraction

# Ввод дробей
fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

# Вычисление операций с дробями
sum_fraction, product_fraction = calculate_fraction_operations(fraction1, fraction2)

# Вывод результатов
print("Сумма дробей:", sum_fraction)
print("Произведение дробей:", product_fraction)
