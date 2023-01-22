# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
# Формат: Объясняет преподаватель Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce


# 1- Определить, присутствует ли в заданном списке строк, некоторое число

import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def ask_number():
    number = input(f'Введите число: ')
    if(not number.isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return ask_number()
    return int(number)

clear()
ls = ['aaa','aaa1', 'bbb2', 'ccc3', 'ddd4', 'eee5', '67']
print(f'Список строк: {ls}')
n = ask_number()
fl = list(filter(lambda s: str(n) in s, ls))
res = 'есть' if len(fl) != 0 else 'отсутствует'
print(f'В заданном списке строк число {n} {res}')


# 2- Найти сумму чисел списка стоящих на нечетной позиции


from functools import reduce
import os
import random

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()
ls = random.sample(range(100), 10)
print(list(ls))
sum = str(reduce(lambda x,y: x + y,\
    map(lambda x: x[1],\
        filter(lambda x: x[0]%2 != 0, enumerate(ls)))))
print(f'Сумма чисел списка стоящих на нечетной позиции: {sum}')




# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import os
import math

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def askCoordinates():
    coordinates = list(map(lambda s: int(s),\
    filter(lambda s: s.isdigit(),\
        input('Введите координаты через пробел: ').split(' '))))
    if(len(coordinates) != 4):
        print('Ошибка: координат должно быть четыре! Повторите ввод')
        return askCoordinates()
    return coordinates

clear()
ls = askCoordinates()
distance =round(math.sqrt(math.pow(ls[2]-ls[0],2) + math.pow(ls[3]-ls[1],2)),2)
print(f'A ({ls[0]},{ls[1]}); B({ls[2]},{ls[3]}) -> {distance}')



# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет. Примеры список:
# ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe",
# ответ: 3 список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"],
# ищем: "йцу", ответ: 5 список: ["йцу", "фыв", "ячс", "цук", "йцукен"],
# ищем: "йцу", ответ: -1 список: ["123", "234", 123, "567"], 
# ищем: "123", ответ: -1 список: [], ищем: "123", ответ: -1

import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()
ls = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(f'Список строк: {ls}')
str = input('Введите строку для поиска: ')
ls = list(filter(lambda t: t[1] == str, enumerate(ls)))
print(ls[1][0] if len(ls)>1 else -1)



# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import os
import math
import random

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()
ls = random.sample(range(50), random.randint(4,8))
center = math.ceil(len(ls)/2)
left = ls[:center]
right = ls[center:]
right.reverse()

result = list(map(lambda tuple: tuple[0]*tuple[1], zip(left,right)))
print(f'{ls} => {result}')



# 6-Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
# Полезная информация

import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def ask_number():
    number = input(f'Введите число: ')
    if(not number.isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return ask_number()
    return int(number)

clear()

n = ask_number()
ls = [(-3 if i % 2 == 0 else 3)**(i - 1) for i in range(1, n+1)]
print(ls)


# Допустим, у вас есть функция. def is_int(input_number:str): 
#     ''' Проверяет аргумент на принадлежность к int params:
# input_number - введенное значение return: int или False ''' try: 
# input_number = int(input_number) return input_number except ValueError: 
# return False Вы можете использовать эту функцию в лямбде.
# Делается это, примерно, вот так: ┌────────────────────────────┐ │lambda input_number: is_int(input_number) │
# └────────────────────────────┘ или даже необязательно называть это input_number:
# ┌────────────────┐ │lambda char: is_int(char)│ └────────────────┘ 

