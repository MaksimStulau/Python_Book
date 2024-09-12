import time
from functools import reduce
"""Написать фунцию декоратор для измерения скорости работы других функций.
   Измерить с помощью декоратора скорость работы своей реализации факториала, 
   версия с reduce и с рекурсией. Сравнить результаты."""


def time_colc(func):
    def wrapper(*args, _is_recursive=False):
        if not _is_recursive:
            start_time = time.perf_counter()
            result = func(*args, _is_recursive=True)
            end_time = time.perf_counter()
            speed_time = end_time - start_time
            print(f"Время выполнения {func.__name__}: {speed_time:.10f} секунд")
            return result
        else:
            return func(*args, _is_recursive=True)
    return wrapper


@time_colc
def factorial(n, _is_recursive=False):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


@time_colc
def factorial_reduce(n, _is_recursive=False):
    return reduce(lambda x, y: x * y, range(1, n + 1))


@time_colc
def factorial_recursive(n, _is_recursive=False):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1, _is_recursive=True)


n = 10
print(f"Факториал {n} с использованием цикла: {factorial(n)}")
print(f"Факториал {n} с использованием reduce: {factorial_reduce(n)}")
print(f"Факториал {n} с использованием рекурсии: {factorial_recursive(n)}")
