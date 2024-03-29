# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json

def convert_to_json(input_file, output_file):
    data = []

    with open(input_file, 'r') as file:
        for line in file:
            name, value = line.strip().split('|')
            data.append({"Name": name.capitalize(), "Value": value})

    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

input_file = "result.txt"
output_file = "result.json"

convert_to_json(input_file, output_file)
