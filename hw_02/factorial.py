#Посчитать факториал указанного числа

#import math
#print(math.factorial(5))


def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    print(fac)


factorial(3)
