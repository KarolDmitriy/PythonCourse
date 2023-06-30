# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def to_hex(num):
    hex_str = hex(num)[2:]  # преобразование в шестнадцатеричную строку без префикса "0x"
    return hex_str.upper()  # преобразование всех символов в верхний регистр

# Пример использования
num = int(input("Введите целое число: "))
hex_str = to_hex(num)
print("Шестнадцатеричное представление:", hex_str)