# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

while True:
    input_number = input('Введите день недели:')
    if input_number.isdigit():
        day_number = int(input_number)
        if 1 <= day_number <= 7:
            break
    print('Ошибка! Введите число от 1 до 7!')

if 1 <= day_number <= 5:
    print('Сегодня рабочий день!')
elif 6 <= day_number <= 7:
    print('Сегодня выходной!')






# 2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.




print('Проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат')

claim_1 = False
claim_2 = False
for x in range(2):
    for y in range(2):
        for z in range(2):
            claim_1 = not (bool(x) or bool(y) or bool(z))
            claim_2 = not bool(x) and not bool(y) and not bool(z)
            print(f'При значении предикат X, Y, Z = [{bool(x)}, {bool(y)}, {bool(z)}]', end=', ')
            print(f'утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z = {claim_1 == claim_2}')



# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("input coordinates of the point x: "))
y = int(input("input coordinates of the point y: "))
if x > 0 and y > 0:
    print("I")
if x < 0 and y > 0:
    print("II")
if x < 0 and y < 0:
    print("III")
if x > 0 and y < 0:
    print("IV")



# 4 Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y) from math import sqrt.

number_quarter = int(input("input number quarter: "))
if number_quarter < 1 or number_quarter > 4:
    print("repeat input number quarter: ")
elif number_quarter == 1:
    print("x > 0; y > 0")
elif number_quarter == 2:
    print("x < 0; y > 0")
elif number_quarter == 3:
    print("x < 0; y < 0")
elif number_quarter == 4:
    print("x > 0; y < 0")



# 5 Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt

print("input x and y Point a")
x_a = float(input("X: "))
y_a = float(input("y: "))
print("input x and y Point b")
x_b = float(input("X: "))
y_b = float(input("y: "))
interval = sqrt(((x_b - x_a) ** 2) + ((y_b - y_a) ** 2))
print(interval)
