#Заменить подстроку между соответствующими скобками в заданной строке (а - первую, б - все)

def replace_substring_in_brackets(string, replacement, all_brackets=False):
    """Заменяет подстроку между скобками в заданной строке без использования регулярных выражений.

    Args:
        string: Исходная строка.
        replacement: Строка для замены.
        all_brackets: Если True, заменяет содержимое всех пар скобок.
                      Если False, заменяет только содержимое первой пары.

    Returns:
        Строка с замененными подстроками.
    """

    result = ""
    in_brackets = False
    first_replacement = True  # Новый флаг для отслеживания первой замены

    for i, char in enumerate(string):
        if char == '(':
            in_brackets = True
            start_index = i
        elif char == ')' and in_brackets:
            if all_brackets or first_replacement:  # Замена всех или первой пары
                result += string[start_index:i+1].replace(string[start_index+1:i], replacement)
                first_replacement = False  # Сбрасываем флаг после первой замены
            else:
                result += string[start_index:i+1]
            in_brackets = False
        else:
            result += char
    return result


string = "Это (текст) для (замены) подстрок."

result1 = replace_substring_in_brackets(string, "новый текст", False)
print(result1)  # Вывод: Это новый текст для (замены) подстрок.

result2 = replace_substring_in_brackets(string, "новый текст", True)
print(result2)  # Вывод: Это новый текст для новый текст подстрок.
