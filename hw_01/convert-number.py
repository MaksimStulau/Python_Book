arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr[::-1])


def convert(num):

    return [int(i) for i in str(num)[::-1]]


print(convert(123456789))
