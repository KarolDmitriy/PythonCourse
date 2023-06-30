# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается каждая буква в строке без использования
# метода count.
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
# символа в строке.
# Обратите внимание на порядок ключей.

text = input("Введите строку текста: ")

frequency = {}
for char in text:
    if char.isalpha():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

# Сортировка словаря по ключу
sorted_frequency = dict(sorted(frequency.items()))

# Вывод результатов
for char, count in sorted_frequency.items():
    print(f"Буква '{char}' встречается {count} раз(а)")
