# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# 1. doctest,
# 2. unittest,
# 3. pytest.

import doctest
import math

def run_doctests():
    failures, _ = doctest.testmod(math)
    if failures == 0:
        print("All doctests passed.")
    else:
        print(f"{failures} doctest(s) failed.")
def area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.

    >>> area(4, 5)
    20
    >>> area(3, 7)
    21
    >>> area(0, 0)
    0
    """
    return length * width

if __name__ == "__main__":
    run_doctests()

