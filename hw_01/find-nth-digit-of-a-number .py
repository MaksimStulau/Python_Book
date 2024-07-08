arr = [0, -3, 7, 4, 0, 3, 7, 9]
print(len(arr[2:9]))

num_1 = 10
print(len(str(num_1)))


def find_nth(num, ind):

    if ind < 0 or ind >= len(num):
        return "invalid input index"
    return num[ind]


number = input("number: ")
index = int(input("index: "))
result = find_nth(number, index)

print(f"the digit of index {index} is: {result}")
