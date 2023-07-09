# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.


__all__ = ['Riddles']

class Riddles:
    def __init__(self):
        self._results = {}

    def guess_riddle(self, riddle, options, attempts):
        print(riddle)
        for attempt in range(1, attempts + 1):
            guess = input(f"Попытка {attempt}. Введите вашу отгадку: ")
            if guess in options:
                self._results[riddle] = attempt
                return attempt
            else:
                print("Неверная отгадка.")
        self._results[riddle] = 0
        return 0

    def print_results(self):
        print("Результаты угадывания:")
        for riddle, attempt in self._results.items():
            result = "Угадано" if attempt > 0 else "Не угадано"
            print(f"Загадка: {riddle} | Попытка: {attempt} | Результат: {result}")

if __name__ == "__main__":
    riddles = Riddles()
    riddles.guess_riddle("Загадка 1: Что можно увидеть с закрытыми глазами?", ["Мечту", "Сон", "Птицу"], 3)
    riddles.guess_riddle("Загадка 2: Какой месяц имеет 28 дней?", ["Все", "Февраль", "Январь"], 2)
    riddles.guess_riddle("Загадка 3: Что можно сломать, но нельзя исправить?", ["Зеркало", "Обещание", "Стекло"], 4)

    riddles.print_results()
