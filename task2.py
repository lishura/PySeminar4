# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def factorize(n):
    multipliers = []
    i = 2
    while i <= n*0.5:
        while n % i == 0:
            n //= i
            multipliers.append(i)
        i += 1

    if n > 1:
        multipliers.append(n)
    return multipliers


N = int(input('Введите натуральное число: '))

print(factorize(N))
