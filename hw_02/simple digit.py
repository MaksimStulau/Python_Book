#Проверить является ли указанное число простым.

def simple_digit():
    num = int(input('digit: '))

    if num <= 1:
        print("The digit is not simple")
        return

    for i in range(2, num):
        if num % i == 0:
            print("The digit is not simple")
            return

    print("The digit is simple")


simple_digit()

