def evil_or_odious(num):

    if num % 2 == 0:
        return f'{num} in binary format is {num:b} is evil' #when the 'binary' number is even

    else:
        return f'{num} in binary format is {num:b} is odious' #when the binary number is odd


print(evil_or_odious(10))


