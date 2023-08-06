# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        logging.error("Division by zero error: %s", e)
        return None
    return result

def main():
    logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    num1 = 10
    num2 = 0

    result = divide(num1, num2)

    if result is None:
        print("An error occurred. Check the error_log.txt file for details.")
    else:
        print(f"The result of division is: {result}")

if __name__ == "__main__":
    main()
