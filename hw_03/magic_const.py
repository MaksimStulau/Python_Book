# Определить является ли квадрат магическим.

def is_magic_square(square):
    n = len(square)
    magic_const = (n * (n * n + 1)) / 2

    # Проверка строк
    for row in square:
        if sum(row) != magic_const:
            return False

    # Проверка столбцов
    for col in range(n):
        if sum(row[col] for row in square) != magic_const:
            return False

    # Проверка главной диагонали
    if sum(square[i][i] for i in range(n)) != magic_const:
        return False

    # Проверка побочной диагонали
    if sum(square[i][n - i - 1] for i in range(n)) != magic_const:
        return False

    return True


# Пример использования
square = [[2, 7, 6],
          [9, 5, 1],
          [4, 3, 8]]

if is_magic_square(square):
    print("Это магический квадрат!")
else:
    print("Это не магический квадрат.")
