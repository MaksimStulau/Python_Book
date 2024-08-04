# Посчитать сумму и произведение цифр заданного числа

def calculate_digits(number):
    sum_of_digits = 0
    multip_of_digits = 1
    for i in str(number):
        int_digit = int(i)
        sum_of_digits += int_digit
        multip_of_digits *= int_digit
    return sum_of_digits, multip_of_digits


number = 1234
result = calculate_digits(number)
print("Сумма цифр:", result[0])
print("Произведение цифр:", result[1])
