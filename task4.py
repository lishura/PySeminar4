# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# *Пример:*

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
from sympy import symbols 

k = int(input('Введите степень k: '))

x = symbols('x')
polynomial = 0
while k >= 1:
    polynomial += random.randint(0, 100)*x**k
    k -= 1
polynomial = polynomial + random.randint(0, 100)

with open('file.txt','a') as data:
    data.writelines([f'{polynomial}\n'])



