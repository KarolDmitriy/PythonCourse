# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# - уровень логирования,
# - дату события,
# - имя функции (не декоратора),
# - аргументы вызова,
# - результат.

import json
import logging
from functools import wraps

# Настройка логгирования
logging.basicConfig(filename='param_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def save_params_to_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Записываем информацию о вызове функции в лог
        logging.info("Function: %s", func.__name__)
        logging.info("Arguments: %s, %s", args, kwargs)

        # Вызываем декорируемую функцию и получаем результат
        result = func(*args, **kwargs)

        # Подготавливаем данные для логирования
        params = {
            'target_number': args[0],
            'num_attempts': args[1],
            'result': result
        }

        # Записываем данные в лог
        logging.info("Game parameters: %s", json.dumps(params, indent=4))

        return result

    return wrapper

# Пример использования
@save_params_to_log
def game_function(target_number, num_attempts):
    # Логика игры
    pass

if __name__ == "__main__":
    game_function(42, 10)
