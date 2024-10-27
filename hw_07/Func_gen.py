"""Сделать задание 1 как функцию генератор"""


def range_generator(start, stop):
    current = start
    while current < stop:
        yield current
        current += 1


for num in range_generator(1, 5):
    print(num)
