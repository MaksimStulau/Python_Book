# Найти среднее арифметическое отрицательных элементов двухмерного массива.

import numpy as np


def arithmetic_average():

    total_sum = 0
    count = 0

    mass = np.array([
        [1, -2, 3],
        [4, -5, 6]
    ])

    for row in mass:
        for num in row:
            if num < 0:
                total_sum += num
                count += 1
    average = total_sum / count
    print(average)


arithmetic_average()
