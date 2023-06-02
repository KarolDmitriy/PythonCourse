# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def intersection(n, m):
    set1 = set()
    set2 = set()
    
    # Ввод элементов первого множества
    print("Введите элементы первого множества:")
    for i in range(n):
        num = int(input())
        set1.add(num)
    
    # Ввод элементов второго множества
    print("Введите элементы второго множества:")
    for i in range(m):
        num = int(input())
        set2.add(num)
    
    # Нахождение пересечения множеств
    intersection_set = set1.intersection(set2)
    
    # Вывод результатов
    sorted_intersection = sorted(intersection_set)
    print("Числа, встречающиеся в обоих множествах без повторений и в порядке возрастания:")
    for num in sorted_intersection:
        print(num)

# Получаем ввод от пользователя
n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

# Вызываем функцию для решения задачи
intersection(n, m)
