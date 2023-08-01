# Создайте класс-функцию, которая считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

import math

class FactorialCalculator:
    def __init__(self, k):
        """
        Создает объект для вычисления факториалов чисел и запоминания последних k значений.

        :param k: количество последних значений для запоминания
        """
        self.k = k
        self.history = {}

    def __call__(self, n):
        """
        Вычисляет факториал числа n и запоминает результат.

        :param n: число для вычисления факториала
        :return: факториал числа n
        """
        if n not in self.history:
            self.history[n] = math.factorial(n)
        return self.history[n]

    def get_history(self):
        """
        Возвращает словарь с последними k вызываемыми значениями и их факториалами.

        :return: словарь с последними k значениями и их факториалами
        """
        return {n: self.history[n] for n in sorted(self.history, reverse=True)[:self.k]}

# Пример использования
factorial_calculator = FactorialCalculator(k=5)

print(factorial_calculator(5))  # Выводит: 120
print(factorial_calculator(7))  # Выводит: 5040
print(factorial_calculator(3))  # Выводит: 6

history = factorial_calculator.get_history()
print(history)  # Выводит: {7: 5040, 5: 120, 3: 6}

