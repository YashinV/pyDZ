
# 1. Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$



from math import pi
d = int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')


# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input('Введите число N: '))
list = []
a = n
if n > 1:
    restart = True
    while restart:
        restart = False
        for i in range (2, n+1):
            if n%i == 0:
                list.append(i)
                n = int(n/i)
                restart = True
                break

    print(f'Простые множители числа {a} - {list}')
elif n == 1:
    print(f'Простые множители числа {a} - [1]')
else:
    print(f'Вы ввели не правильное число')

# 3 Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


import random

def fill_number_list(n=20, min=10, max=99) -> list:
    number_list = [random.randint(min, max)]
    for i in range (1, n):
        number_list.append(random.randint(min, max)) 
    return number_list

def unique_values_list(user_list) -> list:
    new_list = [user_list[0]]
    for i in range(1, len(user_list)):
        for j in range(len(new_list)):
            if user_list[i] == new_list[j]:
                break
            elif j == len(new_list)-1:
                new_list.append(user_list[i])
    return new_list

source_list = fill_number_list(20, 10, 50)
unique_list = unique_values_list(source_list)
print(f'{source_list} ->')
print(unique_list)

# 4 Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


k = int(input('Задайте натуральную степень многочлена k: '))
import Func_coeff_polinom as cp 
coeff_polynom = cp.fill_coefficients_polynomial_list(k)
my_file = 'f_polinom4_4.txt'
import Func_call_record_func as fc
fc.call_record_func(k, coeff_polynom, my_file)



# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')




# def transform_polinom(user_polynom: str, user_file: str):
#     polyn = user_polynom.replace('$', '')
#     polyn = polyn.replace('**', '^')
#     polyn = polyn.replace(' ', '')
#     polyn = polyn[:-2]
#     return polyn

# my_file1='f_polinom4_5_1.md' # Файл c записью 1-го многочлена
# my_file2='f_polinom4_5_2.md' # Файл c записью 2-го многочлена

# import Func_read_file as r
# polynom1 = r.read_file(my_file1)
# polynom2 = r.read_file(my_file2)

# p1 = transform_polinom(polynom1, my_file1)
# p2 = transform_polinom(polynom2, my_file2)
# print(type(p1))
# import Func_fill_missing_coeff as fm
# tp1 = fm.fill_missing_coeff(p1)
# tp2 = fm.fill_missing_coeff(p2)

# import Func_sum_polinom as fs
# result = fs.sum_polinom(tp1, tp2)

# my_file_result='f_polinom4_5_result.txt' 
# import Func_call_record_func as fc
# fc.call_record_func(len(result)-1, result, my_file_result)