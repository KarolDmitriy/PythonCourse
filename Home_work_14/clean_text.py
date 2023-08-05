# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

import re

def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower().strip()

# Пример использования
input_text = "Hello, 123 World! This is a test text. Проверка русских слов."
cleaned_text = clean_text(input_text)
print(cleaned_text)  # Выводит: hello  world this is a test text


