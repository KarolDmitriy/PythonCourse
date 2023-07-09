# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY.
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.


__all__ = ['is_valid_date']

def _is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_valid_date(date):
    day, month, year = map(int, date.split('.'))

    # Проверка валидности дня
    if day < 1 or day > 31:
        return False

    # Проверка валидности месяца
    if month < 1 or month > 12:
        return False

    # Проверка валидности года
    if year < 1 or year > 9999:
        return False
    # Проверка високосности года
    if month == 2:
        if _is_leap_year(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True


if __name__ == "__main__":
    date_input = input("Введите дату в формате DD.MM.YYYY: ")

    if is_valid_date(date_input):
        print("Введенная дата является валидной.")
    else:
        print("Введенная дата невалидна.")
