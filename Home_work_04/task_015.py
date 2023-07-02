# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    # Получаем количество строк и столбцов в исходной матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу с размерами cols x rows
    transposed_matrix = [[0] * rows for _ in range(cols)]

    # Заполняем новую матрицу значениями из исходной матрицы
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

matrix = [[1, 2, 3, 8],
          [4, 5, 6, 0],
          [7, 8, 9, 5]]

transposed = transpose_matrix(matrix)
print(transposed)
