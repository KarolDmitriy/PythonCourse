# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю;
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла, возвращайтесь в его начало.

from decimal import Decimal

def process_files(numbers_file, names_file, output_file):
    with open(numbers_file, 'r') as numbers_file, open(names_file, 'r') as names_file, open(output_file, 'w') as output_file:
        numbers_lines = numbers_file.readlines()
        names_lines = names_file.readlines()

        numbers_count = len(numbers_lines)
        names_count = len(names_lines)

        for i in range(numbers_count):
            number_line = numbers_lines[i % numbers_count]
            name_line = names_lines[i % names_count]

            number_parts = number_line.strip().split('|')
            name = name_line.strip()
            number = Decimal(number_parts[1])

            result = number * int(number_parts[0])

            if result < 0:
                output_file.write(f"{name.lower()}|{abs(result)}\n")
            else:
                output_file.write(f"{name.upper()}|{round(result)}\n")


process_files("random_pairs.txt", "pseudonyms.txt", "result.txt")

