# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('file_1.txt', 'r') as data_1,\
        open('file_2.txt', 'r') as data_2,\
            open('file_sum.txt', 'w') as data_sum:
            first_poly = data_1.readlines()            
            second_poly = data_2.readlines()            
            data_sum.write(f'{first_poly[0]} + {second_poly[0]}')

