#Записать в последний элемент строки матрицы, сумму предыдущих той же строки.

def last_element():
    list_1 = []

    mass = ([
        [1, 2, 3],
        [4, 2, 6, 7]
    ])

    for row in mass:
        for i in row:
            list_1.append(i)
    total = sum(list_1[:-1])
    list_1[-1] = total
    print(list_1)


last_element()

