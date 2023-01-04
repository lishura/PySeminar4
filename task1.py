# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
number = math.pi
d = input('Введите число, обозначающее точность выведения числа π: ')

if '.' in d:
    count = len(d) - d.find('.') - 1
else:
    print('Неверный формат числа')

print(round(number, count))
