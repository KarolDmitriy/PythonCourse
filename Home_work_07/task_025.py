# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

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


generate_pseudonyms("pseudonyms.txt", 10)


