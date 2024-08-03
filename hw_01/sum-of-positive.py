def sum_of_positive(num):

    sum_num = []
    for i in str(num):
        if int(i) % 2 == 0:
            sum_num.append(int(i))

    return sum(sum_num)


print(sum_of_positive(7568))
