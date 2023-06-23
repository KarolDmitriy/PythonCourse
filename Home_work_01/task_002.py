# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

print("Сколько рядов у ёлки?")
rows = int(input())

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
