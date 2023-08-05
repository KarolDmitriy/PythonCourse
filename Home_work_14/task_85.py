# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# 1. doctest,
# 2. unittest,
# 3. pytest.

import pytest
from Home_work_14.rectangle import Rectangle


@pytest.fixture
def rectangle():
    return Rectangle(4, 5)

def test_area(rectangle):
    assert rectangle.area() == 20

def test_perimeter(rectangle):
    assert rectangle.perimeter() == 18

def test_addition(rectangle):
    other_rectangle = Rectangle(2, 3)
    result = rectangle + other_rectangle
    assert result.length == rectangle.length + other_rectangle.length
    assert result.width == rectangle.width + other_rectangle.width

def test_subtraction(rectangle):
    other_rectangle = Rectangle(2, 2)
    result = rectangle - other_rectangle
    assert result.length == max(rectangle.length - other_rectangle.length, 0)
    assert result.width == max(rectangle.width - other_rectangle.width, 0)

def test_comparison(rectangle):
    smaller_rectangle = Rectangle(3, 4)
    larger_rectangle = Rectangle(5, 6)
    assert rectangle < larger_rectangle
    assert rectangle > smaller_rectangle
    assert rectangle == Rectangle(4, 5)
    assert rectangle != smaller_rectangle

# Добавьте здесь другие тесты

if __name__ == '__main__':
    pytest.main()
