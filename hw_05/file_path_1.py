"""1. Написать программу, которая читает файл,
путь у которому передается аргументом, и выводит содержимое в консоль.
Добавить обработку возможных исключений."""

import os

base_path = os.path.dirname(__file__)
print(base_path)
file_path = os.path.dirname(base_path)
print(file_path)
new_file_path = os.path.join(file_path, 'text_file.txt')
print(new_file_path)

#file_path = os.path.join(os.getcwd(), 'text_file.txt')


def read_file(*args):

    try:
        with open(file_path, 'r') as file:
            return file.read()

    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except PermissionError:
        return f"Error: Permission denied for file '{file_path}'."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


print(read_file(file_path))
