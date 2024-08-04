#Найти n-ый член последовательности фибоначчи.


def fibonacci_iterative(n):
    a = 0
    b = 1
    for i in range(n):
        a = b
        b = a + b
    return a


n = int(input("введи номер числа Фибоначчи: "))
print(f"{n} это число: {fibonacci_iterative(n)}")
