"""Написать программу, которая вычисляет все члены чисел Фибоначчи
до указанного n-ого включительно и пишет их в файл.
Путь к файлу передается аргументом."""


import os

file_path = os.path.join(os.getcwd(), 'fibonacci.txt')


def fibonacci_sequence(n):
    sequence = []

    a, b = 0, 1
    for i in range(n + 1):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def write_fibonacci_to_file(sequence, file_path):
    try:
        with open(file_path, 'w') as file:
            for number in sequence:
                file.write(f"{number}\n")
        print(f"Числа Фибоначчи успешно записаны в файл: {file_path}")
    except Exception as e:
        print(f"Ошибка при записи в файл: {str(e)}")


def main(n, file_path):

    fib_sequence = fibonacci_sequence(n)

    write_fibonacci_to_file(fib_sequence, file_path)


n = 10

main(n, file_path)
