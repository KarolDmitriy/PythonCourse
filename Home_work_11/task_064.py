# Создайте класс Матрица. Добавьте методы для:
# вывода на печать,
# сравнения,
# сложения,
# умножения матриц

class Matrix:
    def __init__(self, matrix_data):
        """
        Создает объект матрицы на основе переданных данных.

        :param matrix_data: двумерный список, представляющий матрицу
        """
        self.matrix_data = matrix_data

    def __str__(self):
        """
        Возвращает строковое представление матрицы.

        :return: строковое представление матрицы
        """
        matrix_str = ""
        for row in self.matrix_data:
            matrix_str += " ".join(str(elem) for elem in row) + "\n"
        return matrix_str

    def __eq__(self, other):
        """
        Сравнивает матрицу с другой матрицей.

        :param other: другая матрица для сравнения
        :return: True, если матрицы равны, иначе False
        """
        if not isinstance(other, Matrix):
            return False
        return self.matrix_data == other.matrix_data

    def __add__(self, other):
        """
        Складывает матрицу с другой матрицей.

        :param other: другая матрица для сложения
        :return: новая матрица, результат сложения
        """
        if not isinstance(other, Matrix):
            raise TypeError("Unsupported operand type for +: 'Matrix' and '{}'".format(type(other).__name__))

        if len(self.matrix_data) != len(other.matrix_data) or len(self.matrix_data[0]) != len(other.matrix_data[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")

        result_matrix = []
        for i in range(len(self.matrix_data)):
            row = [self.matrix_data[i][j] + other.matrix_data[i][j] for j in range(len(self.matrix_data[i]))]
            result_matrix.append(row)
        return Matrix(result_matrix)

    def __mul__(self, other):
        """
        Умножает матрицу на другую матрицу или на скалярное значение.

        :param other: другая матрица или скалярное значение для умножения
        :return: новая матрица, результат умножения
        """
        if isinstance(other, Matrix):
            if len(self.matrix_data[0]) != len(other.matrix_data):
                raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
            result_matrix = []
            for i in range(len(self.matrix_data)):
                row = []
                for j in range(len(other.matrix_data[0])):
                    elem = sum(self.matrix_data[i][k] * other.matrix_data[k][j] for k in range(len(self.matrix_data[i])))
                    row.append(elem)
                result_matrix.append(row)
            return Matrix(result_matrix)
        elif isinstance(other, (int, float)):
            result_matrix = [[elem * other for elem in row] for row in self.matrix_data]
            return Matrix(result_matrix)
        else:
            raise TypeError("Unsupported operand type for *: 'Matrix' and '{}'".format(type(other).__name__))

# Пример использования
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])
print(matrix1)
print(matrix2)

print(matrix1 == matrix2)  # Выводит: False

matrix3 = matrix1 + matrix2
print(matrix3)

matrix4 = matrix1 * matrix2
print(matrix4)

matrix5 = matrix1 * 3
print(matrix5)
