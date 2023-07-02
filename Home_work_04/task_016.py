# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def key_params_to_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        key_str = str(key)  # Преобразуем ключ в строку, если он не хешируем
        result_dict[value] = key_str
    return result_dict

# Пример использования функции:
params_dict = key_params_to_dict(param1=100, param2="hello", param3=True)
print(params_dict)
