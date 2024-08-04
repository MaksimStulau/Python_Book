def largest_prime_factor(n):
    # Функция для нахождения простых множителей числа n
    def prime_factors(x):
        factors = []
        # Убираем все множители 2
        while x % 2 == 0:
            factors.append(2)
            x //= 2
        # Убираем все множители нечетных чисел начиная с 3
        for i in range(3, int(x ** 0.5) + 1, 2):
            while x % i == 0:
                factors.append(i)
                x //= i
        # Если x стало простым числом больше 2
        if x > 2:
            factors.append(x)
        return factors

    factors = prime_factors(n)
    return max(factors) if factors else None


# Пример использования
number = int(input("Введите число: "))
print("Наибольший простой множитель:", largest_prime_factor(number))
