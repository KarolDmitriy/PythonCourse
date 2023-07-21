# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. Верните все возможные варианты комплектации рюкзака.

def find_combinations(items, max_weight, current_combination=[], current_weight=0, start_index=0):
    if current_weight == max_weight:
        print(current_combination)
        return

    if current_weight > max_weight:
        return

    for i in range(start_index, len(items)):
        item = items[i]
        if item[1] + current_weight <= max_weight:
            find_combinations(items, max_weight, current_combination + [item[0]], current_weight + item[1], i + 1)

# Словарь с вещами и их массами
items = {
    'Тент': 2,
    'Спальный мешок': 1,
    'Палатка': 4,
    'Спички': 2,
    'Еда': 3,
    'Вода': 5
}

# Ввод максимальной грузоподъемности рюкзака
max_weight = int(input("Введите максимальную грузоподъемность рюкзака: "))

# Преобразование словаря в список кортежей (название вещи, масса)
items_list = list(items.items())

# Поиск возможных вариантов комплектации рюкзака
find_combinations(items_list, max_weight)
