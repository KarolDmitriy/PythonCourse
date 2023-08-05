# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_from_dict(dictionary, key, default=None):
    try:
        value = dictionary[key]
    except KeyError:
        value = default
    return value


data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Попробуем получить значение по существующему ключу
name = get_from_dict(data, 'name', 'Unknown')
print(name)  # Вывод: 'John'

# Попробуем получить значение по несуществующему ключу
gender = get_from_dict(data, 'gender', 'Not specified')
print(gender)  # Вывод: 'Not specified'
