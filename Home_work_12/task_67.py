# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

import math

class FactorialGenerator:
    def __init__(self, start, stop=None, step=1):
        """
        Создает объект для генерации факториалов чисел в заданном диапазоне.

        :param start: начало диапазона
        :param stop: конец диапазона (не включается)
        :param step: шаг генерации
        """
        if stop is None:
            stop = start
            start = 1
        if step == 0:
            raise ValueError("Step must not be zero.")
        self.start = start
        self.stop = stop
        self.step = step

    def factorial(self, n):
        """
        Возвращает факториал числа n.

        :param n: число для вычисления факториала
        :return: факториал числа n
        """
        return math.factorial(n)

    def __iter__(self):
        """
        Возвращает итератор для генерации факториалов в заданном диапазоне.
        """
        current = self.start
        while current < self.stop:
            yield self.factorial(current)
            current += self.step

# Пример использования
generator1 = FactorialGenerator(1, 6)
for factorial in generator1:
    print(factorial)

generator2 = FactorialGenerator(1, 11, 2)
for factorial in generator2:
    print(factorial)

generator3 = FactorialGenerator(3)
for factorial in generator3:
    print(factorial)  
