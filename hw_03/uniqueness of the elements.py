# Проверить уникальность элементов двухмерного списка.

#import numpy as np


def uniqe():
    list_1 = []

    mass = ([
        [1, 2, 3],
        [4, 2, 6, 7]
    ])

    for row in mass:
        for num in row:
            list_1.append(num)

    if len(list_1) == len(set(list_1)):
        print("list is unique")
    else:
        print("list is not unique")
    print(list_1)


uniqe()
