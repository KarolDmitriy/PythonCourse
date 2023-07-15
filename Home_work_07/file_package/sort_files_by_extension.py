# Функция для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке остаются только те файлы, которые не подошли для сортировки.

import os
import shutil


def sort_files_by_extension(source_directory, target_directory):
    file_types = {
        "Videos": [".mp4", ".avi", ".mov"],
        "Images": [".jpg", ".jpeg", ".png"],
        "Text": [".txt", ".doc", ".pdf"],
        # Добавьте другие группы и расширения по необходимости
    }

    for file in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file)

        if os.path.isfile(file_path):
            for file_type, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    target_dir = os.path.join(target_directory, file_type)

                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)

                    shutil.move(file_path, target_dir)
                    break
