# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def remove_duplicates(input_list):
    return list(set(input_list))

# Пример использования
input_list = [1, 2, 3, 4, 2, 3, 4, 5]
result_list = remove_duplicates(input_list)
print(result_list)
