# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.


import sys
import logging

logging.basicConfig(filename='rectangle_operations_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle: length={self.length}, width={self.width}"

def main():
    try:
        if len(sys.argv) < 3:
            raise ValueError("Usage: python script_name.py <length> <width>")

        length = float(sys.argv[1])
        width = float(sys.argv[2])

        rectangle = Rectangle(length, width)
        print("Rectangle:", rectangle)
        print("Perimeter:", rectangle.perimeter())
        print("Area:", rectangle.area())
    except ValueError as ve:
        print(f"Error: {ve}")
        logging.error("Error: %s", ve)
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()

