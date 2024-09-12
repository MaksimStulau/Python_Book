"""Написать фунцию декоратор, которая будет писать в лог файл сведения о вызовах функций,
которые ей декорированы.
Функция деоратор имеет опциональный аргумент - путь к файлу.
В файл пишется название функции, а также дата и время вызова.
* Добавить аргумент в декоратор, который будет передавать количесво дней, которые файл будет хранится.
При истечении срока декоратор удаляет старый файл и создает новый."""


import os
from datetime import datetime

"""base_path = os.path.dirname(__file__)
print(base_path)
file_path = os.path.join(base_path, 'logs.txt')
print(file_path)"""


def log(file_path, days_to_store=7):

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Получаем текущую дату и время
            current_time = datetime.now()

            # Проверяем существование файла и его возраст
            if os.path.exists(file_path):
                file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                # Если файл старше заданного срока, удаляем его и создаем новый
                if (current_time - file_creation_time).days >= days_to_store:
                    os.remove(file_path)

            # Открываем файл для добавления записи
            with open(file_path, "a") as log_file:
                log_file.write(f"Function '{func.__name__}' was called at {current_time}\n")

            # Вызываем исходную функцию
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@log(file_path='function_log.txt', days_to_store=3)
def example_function():
    print("Shchyry dzyakyi Gena!")


example_function()
