# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

def repeat_times(num_repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_repeats):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Пример использования декоратора с параметром
@repeat_times(num_repeats=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

