# На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

import json
import logging
from functools import wraps

# Настройка логгирования
logging.basicConfig(filename='param_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def save_params_to_log(func):
    @wraps(func)
    def wrapper(target_number, num_attempts):
        # Вызываем декорируемую функцию и получаем результат
        result = func(target_number, num_attempts)

        # Подготавливаем данные для логирования
        params = {
            'target_number': target_number,
            'num_attempts': num_attempts,
            'result': result
        }

        # Записываем данные в лог
        logging.info("Game parameters: %s", json.dumps(params, indent=4))

    return wrapper

# Пример использования
@save_params_to_log
def game_function(target_number, num_attempts):
    # Логика игры
    pass

if __name__ == "__main__":
    game_function(42, 10)


