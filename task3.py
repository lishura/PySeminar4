# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
length = int(input('Введите количество чисел в последовательности: '))
my_list = []
for i in range(length):
    my_list.append(random.randint(0, 10))

list2 = []
for i in range(length):
    if my_list.count(my_list[i])==1:
        list2.append(my_list[i])

print(my_list)
print(list2)