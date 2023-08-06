# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.


import re
import datetime
import logging

# Настройка логгирования
logging.basicConfig(filename='date_conversion_log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def find_nth_weekday(year, month, day_name, n):
    weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    day_number = weekdays.index(day_name)
    found_days = 0
    for day in range(1, 32):
        try:
            date = datetime.date(year, month, day)
            if date.weekday() == day_number:
                found_days += 1
                if found_days == n:
                    return date
        except ValueError:
            pass
    return None

def convert_text_to_date(text):
    try:
        current_year = datetime.datetime.now().year
        pattern = r'(\d+)-[йя]+ (\w+) (\w+)'
        match = re.match(pattern, text)

        if match:
            day_number = int(match.group(1))
            day_name = match.group(2)
            month_name = match.group(3)

            months = {
                'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
                'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
                'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
            }

            month_number = months.get(month_name.lower())

            if month_number:
                date = find_nth_weekday(current_year, month_number, day_name, day_number)
                return date
            else:
                raise ValueError("Invalid month name")
        else:
            raise ValueError("Invalid input format")
    except Exception as e:
        logging.error("Error while converting text to date: %s", e)
        return None

# Примеры использования
dates_to_convert = ["1-й четверг ноября", "3-я среда мая", "5-я пятница июня"]

for date_text in dates_to_convert:
    converted_date = convert_text_to_date(date_text)
    if converted_date:
        print(f"Converted {date_text} to {converted_date}")
    else:
        print(f"Error converting {date_text}")

