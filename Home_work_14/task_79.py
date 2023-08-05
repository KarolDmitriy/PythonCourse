# Напишите для задачи тесты doctest. Проверьте следующие варианты:
# 1. возврат строки без изменений
# 2. возврат строки с преобразованием регистра без потери символов
# 3. возврат строки с удалением знаков пунктуации
# 4. возврат строки с удалением букв других алфавитов
# 5. возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import re


def clean_text(text):
    """
    Cleans the input text by removing all non-Latin alphabet letters and spaces and returns the cleaned text in lowercase.

    >>> clean_text("Hello, 123 World!")
    'hello  world'

    >>> clean_text("TEST Text")
    'test text'

    >>> clean_text("This is a test with punctuations: !@#$")
    'this is a test with punctuations'

    >>> clean_text("Привет, мир!")
    ''

    >>> clean_text("Hello, 123 World! This is a test with punctuations: !@#$ Привет, мир!")
    'hello  world this is a test with punctuations'
    """
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower().strip()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

