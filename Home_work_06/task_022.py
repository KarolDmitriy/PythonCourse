# Запгадки
from Home_work_06.my_package.riddles import Riddles


def main():
    riddles = Riddles()

    riddles.guess_riddle("Загадка 1: Что можно увидеть с закрытыми глазами?", ["мечту", "сон", "птицу"], 3)
    riddles.guess_riddle("Загадка 2: Какой месяц имеет 28 дней?", ["все", "февраль", "январь"], 2)
    riddles.guess_riddle("Загадка 3: Что можно сломать, но нельзя исправить?", ["зеркало", "обещание", "стекло"], 4)

    riddles.print_results()


if __name__ == "__main__":
    main()
