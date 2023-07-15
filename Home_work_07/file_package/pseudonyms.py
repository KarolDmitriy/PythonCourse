# Функция, которая генерирует псевдоимена.
# Имя начинаеться с заглавной буквы, состоит из 4-7 букв, среди которых обязательно есть гласные.
# Полученные имена сохраняются в файл.

import random
import string


def generate_pseudonyms(file_name, num_names):
    vowels = "aeiou"
    pseudonyms = []

    while len(pseudonyms) < num_names:
        name_length = random.randint(4, 7)
        name = random.choice(string.ascii_uppercase)

        for _ in range(name_length - 1):
            name += random.choice(string.ascii_lowercase)

        if any(vowel in name for vowel in vowels): # проверка на наличие гласных
            pseudonyms.append(name)

    with open(file_name, 'w') as file:
        file.write('\n'.join(pseudonyms))
