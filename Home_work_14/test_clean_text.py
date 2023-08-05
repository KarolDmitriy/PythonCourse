# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# 1. возврат строки без изменений
# 2. возврат строки с преобразованием регистра без потери символов
# 3. возврат строки с удалением знаков пунктуации
# 4. возврат строки с удалением букв других алфавитов
# 5. возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from clean_text import clean_text

def test_no_changes():
    result = clean_text("This is a simple test")
    assert result == "this is a simple test"

def test_change_case():
    result = clean_text("UPPERCASE and lowercase")
    assert result == "uppercase and lowercase"

def test_remove_punctuation():
    result = clean_text("Hello, world! How's it going?")
    assert result == "hello world hows it going"

def test_remove_non_latin_characters():
    result = clean_text("Привет, мир!")
    assert result == ""

def test_combined_changes():
    result = clean_text("Hello, 123 World! Привет, мир!")
    assert result == "hello  world"
