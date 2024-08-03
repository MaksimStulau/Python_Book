def supersize(num):

    numbers = [int(i) for i in num]
    numbers.sort(reverse=True)
    return numbers


print(supersize(input("number: ")))
