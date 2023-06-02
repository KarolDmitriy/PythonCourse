# Требуется найти в массиве A[1..N] самый близкий по 
# величине элемент к заданному числу X. Пользователь в первой строке 
# вводит натуральное число N – количество элементов в массиве. В 
# последующих строках записаны N целых чисел Ai. Последняя строка 
# содержит число X

def find_closest_element(array, x):
    closest_element = None
    min_difference = float('inf')
    
    for num in array:
        difference = abs(num - x)
        
        if difference < min_difference:
            min_difference = difference
            closest_element = num
    
    return closest_element

# Получаем ввод от пользователя
n = int(input("Введите количество элементов в массиве: "))

array = []
print("Введите элементы массива:")
for _ in range(n):
    num = int(input())
    array.append(num)

x = int(input("Введите число X: "))

# Вызываем функцию для поиска ближайшего элемента
closest_element = find_closest_element(array, x)

# Выводим результат
print("Ближайший элемент к числу X:", closest_element)
