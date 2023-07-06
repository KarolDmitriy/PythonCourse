# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_path(path):
    # Разделение пути по символу "\"
    parts = path.split("\\")

    # Извлечение имени файла и расширения
    filename = parts[-1]
    filename_parts = filename.split(".")
    name = ".".join(filename_parts[:-1])
    extension = filename_parts[-1]

    # Составление кортежа из трех элементов
    result = ("\\".join(parts[:-1]), name, extension)

    return result


# Пример использования функции
path = input("Введите абсолютный путь до файла: ")
result = split_path(path)
print("Путь:", result[0])
print("Имя файла:", result[1])
print("Расширение файла:", result[2])