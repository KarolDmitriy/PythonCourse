# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

import math
import json

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

    def save_to_json(self, file_name):
        """
        Сохраняет историю значений и их факториалов в JSON файл.

        :param file_name: имя файла для сохранения
        """
        with open(file_name, 'w') as file:
            json.dump(self.history, file)

    def __enter__(self):
        """
        Метод, вызываемый при входе в контекстный блок.
        Ничего не делаем.
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Метод, вызываемый при выходе из контекстного блока.
        Сохраняем историю значений и их факториалов в JSON файл.
        """
        self.save_to_json("history.json")

# Пример использования
with FactorialCalculator(k=5) as factorial_calculator:
    print(factorial_calculator(5))  # Выводит: 120
    print(factorial_calculator(7))  # Выводит: 5040
    print(factorial_calculator(3))  # Выводит: 6

# После выхода из контекстного блока данные автоматически сохраняются в файл "history.json"
