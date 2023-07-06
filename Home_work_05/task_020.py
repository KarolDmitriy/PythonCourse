# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a # использую ключевое слово для упрощения
        a, b = b, a + b

# Создаем объект-генератор для чисел Фибоначчи
fib_gen = fibonacci_generator()

# Генерируем первые 10 чисел Фибоначчи и выводим их
for _ in range(10):
    fib_num = next(fib_gen)
    print(fib_num)
