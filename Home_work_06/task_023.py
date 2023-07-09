# Может ли дата существовать
from Home_work_06.my_package.date_validation import is_valid_date


date = input("Введите дату в формате DD.MM.YYYY: ")
if is_valid_date(date):
    print("Дата валидна.")
else:
    print("Неверный формат или неверная дата.")
