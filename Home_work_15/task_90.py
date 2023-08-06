# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели, текущий.
# Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.
import re
import datetime
import logging
import argparse

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
                'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12,
                '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12
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

def main():
    parser = argparse.ArgumentParser(description="Converts date text to a date in the current year.")
    parser.add_argument("text", nargs="?", help="Date text in the format '1-й четверг ноября'")
    args = parser.parse_args()

    if args.text:
        converted_date = convert_text_to_date(args.text)
        if converted_date:
            formatted_date = converted_date.strftime("%d.%m.%Y")
            print(f"Converted '{args.text}' to {formatted_date}")
        else:
            print(f"Error converting '{args.text}'")
    else:
        print("Please provide a date text.")

if __name__ == "__main__":
    main()
