# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# - имя файла без расширения или название каталога,
# - расширение, если это файл,
# - флаг каталога,
# - название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.


import os
import logging
from collections import namedtuple

# Настройка логгирования
logging.basicConfig(filename='directory_info_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_directory_info(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise ValueError(f"Directory '{directory_path}' does not exist.")

        items = os.listdir(directory_path)
        directory_info = []

        for item in items:
            item_path = os.path.join(directory_path, item)
            is_directory = os.path.isdir(item_path)
            parent_directory = os.path.basename(directory_path)

            if is_directory:
                directory_info.append(FileInfo(item, None, True, parent_directory))
            else:
                name, extension = os.path.splitext(item)
                directory_info.append(FileInfo(name, extension, False, parent_directory))

        return directory_info
    except Exception as e:
        logging.error("Error while getting directory info: %s", e)
        return []

def main():
    try:
        directory_path = input("Enter the directory path: ")
        directory_info = get_directory_info(directory_path)

        with open('directory_info.txt', 'w') as file:
            for file_info in directory_info:
                if file_info.is_directory:
                    file_type = "Directory"
                else:
                    file_type = f"File ({file_info.extension})"
                log_message = f"Name: {file_info.name}, Type: {file_type}, Parent: {file_info.parent_directory}"
                logging.info(log_message)
                file.write(log_message + '\n')

        print("Directory info saved to 'directory_info.txt'")
    except KeyboardInterrupt:
        print("Operation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
