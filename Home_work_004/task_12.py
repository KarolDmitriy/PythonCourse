# Напишите программу для нахождения максимального числа ягод, которое может 
# собрать  за  один  заход  собирающий  модуль,  находясь  перед  некоторым  кустом 
# заданной во входном файле грядки.


def max_berry_count(garden):
    n = len(garden)
    max_berries = 0
    
    for i in range(n):
        curr_berries = garden[i] + garden[(i+1) % n] + garden[(i-1) % n]
        max_berries = max(max_berries, curr_berries)
    
    return max_berries

# Получаем ввод от пользователя
n = int(input("Введите количество кустов: "))

garden = []
print("Введите число ягод на каждом кусте:")
for _ in range(n):
    berries = int(input())
    garden.append(berries)

# Вызываем функцию для нахождения максимального числа ягод
max_berries = max_berry_count(garden)

# Выводим результат
print("Максимальное число ягод, которое может собрать собирающий модуль:", max_berries)
