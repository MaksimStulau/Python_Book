#Определить процент букв, цифр и специальных символов в заданной строке


def calculate_character_percentages(input_string):
    letter_count = 0
    digit_count = 0
    special_count = 0

    total_length = len(input_string)

    for i in input_string:
        if i.isalpha():
            letter_count += 1
        elif i.isdigit():
            digit_count += 1
        else:
            special_count += 1

    letter_percentage = (letter_count / total_length) * 100
    digit_percentage = (digit_count / total_length) * 100
    special_percentage = (special_count / total_length) * 100

    return letter_percentage, digit_percentage, special_percentage


input_string = "Hello, World! 888"
letter_percentage, digit_percentage, special_percentage = calculate_character_percentages(input_string)

print(f"Letters:{letter_percentage:.2f}%")
print(f"Digits: {digit_percentage:.2f}%")
print(f"Special characters: {special_percentage:.2f}%")
