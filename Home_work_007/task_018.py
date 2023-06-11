# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    # Печатаем заголовок таблицы с номерами столбцов
    print("\t", end="")
    for column in range(1, num_columns + 1):
        print(column, end="\t")
    print()

    # Печатаем содержимое таблицы
    for row in range(1, num_rows + 1):
        print(row, end="\t")  # Номер строки

        for column in range(1, num_columns + 1):
            result = operation(row, column)  # Вычисляем результат операции
            print(result, end="\t")  # Печатаем результат

        print()  # Переходим на новую строку

# Пример использования функции print_operation_table()

# Определяем функцию для операции умножения
def multiplication(row, column):
    return row * column

print_operation_table(lambda x, y: x * y)