def sum_and_multip(number):
    # Проверяем, что число не отрицательное
    if number < 0:
        print("Number must be non-negative")

    # Инициализируем сумму и произведение цифр
    digit_sum = 0
    digit_multip = 1

    # Копия числа для обработки
    n = number

    while n > 0:
        # Извлекаем последнюю цифру
        digit = n % 10

        # Добавляем цифру к сумме
        digit_sum += digit

        # Умножаем цифру на произведение
        digit_multip *= digit

        # Убираем последнюю цифру
        n //= 10

    return digit_sum, digit_multip


# Пример использования
number = 1234
result_sum, result_multip = sum_and_multip(number)
print(f"Сумма цифр: {result_sum}")
print(f"Произведение цифр: {result_multip}")
