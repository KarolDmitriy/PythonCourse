# Напишите для задачи 1 тесты unittest.
# Проверьте следующие варианты:
# 1. возврат строки без изменений
# 2. возврат строки с преобразованием регистра без потери символов
# 3. возврат строки с удалением знаков пунктуации
# 4. возврат строки с удалением букв других алфавитов
# 5. возврат строки с учётом всех вышеперечисленных пунктов(кроме п. 1)

import unittest
import re

def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower().strip()

class TestCleanText(unittest.TestCase):
    def test_no_changes(self):
        result = clean_text("This is a simple test")
        self.assertEqual(result, "this is a simple test")

    def test_change_case(self):
        result = clean_text("UPPERCASE and lowercase")
        self.assertEqual(result, "uppercase and lowercase")

    def test_remove_punctuation(self):
        result = clean_text("Hello, world! How's it going?")
        self.assertEqual(result, "hello world hows it going")

    def test_remove_non_latin_characters(self):
        result = clean_text("Привет, мир!")
        self.assertEqual(result, "")

    def test_combined_changes(self):
        result = clean_text("Hello, 123 World! Привет, мир!")
        self.assertEqual(result, "hello  world")

if __name__ == "__main__":
    unittest.main()
