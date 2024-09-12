"""Написать фунцию декоратор для задачи по строкам (4),
 которая бы проверяла корректность передаваемых аргументов:
   1 - входная строка,
   2 - строка на которую надо заменить,
   3 - тип скобки,
   4 - число (1 - все менять, 0 - первое вхождение).
   Необходимо вывести сообщение какие аргументы не корректны и прервать выполнение."""

from typing import Callable, Any


def validate_args(func: Callable[[str, str, str, int], Any]) -> Callable[[str, str, str, int], Any]:
    def wrapper(input_str: str, replace_str: str, bracket_type: str, change_all: int) -> Any:
        # Проверка входной строки
        if not isinstance(input_str, str):
            raise ValueError("Входная строка должна быть строкой.")

        # Проверка строки на замену
        if not isinstance(replace_str, str):
            raise ValueError("Строка на замену должна быть строкой.")

        # Проверка типа скобки
        if bracket_type not in ('()', '[]', '{}'):
            raise ValueError("Тип скобок должен быть одним из следующих: '()', '[]', '{}'.")

        # Проверка числа
        if not isinstance(change_all, int) or change_all not in (0, 1):
            raise ValueError("Число должно быть 0 или 1.")

        return func(input_str, replace_str, bracket_type, change_all)

    return wrapper


@validate_args
def replace_in_string(input_str: str, replace_str: str, bracket_type: str, change_all: int) -> str:

    if bracket_type == '()':
        open_bracket, close_bracket = '(', ')'
    elif bracket_type == '[]':
        open_bracket, close_bracket = '[', ']'
    elif bracket_type == '{}':
        open_bracket, close_bracket = '{', '}'

    if change_all == 1:
        return input_str.replace(open_bracket, replace_str).replace(close_bracket, replace_str)
    else:
        return input_str.replace(open_bracket, replace_str, 1).replace(close_bracket, replace_str, 1)


try:
    result = replace_in_string("Hello (world)!", "{}", '()', 1)
    print(result)
except ValueError as e:
    print(e)
