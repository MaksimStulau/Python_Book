"""Написать программу, которая читает файл, сортирует строки по возрастанию длины
и пишет результат в тот же файл."""

import os

base_path = os.path.dirname(__file__)
print(base_path)
file_path = os.path.dirname(base_path)
print(file_path)
new_file_path = os.path.join(file_path, 'text_file.txt')
print(new_file_path)


def sort_lines_by_length(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        sorted_lines = sorted(lines, key=len)

        with open(file_path, 'w') as file:
            file.writelines(sorted_lines)

        print(f"Строки файла '{file_path}' успешно отсортированы по длине.")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


sort_lines_by_length(file_path)
