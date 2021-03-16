#Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

BASE = 16

HEX_ITEMS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

DECIMAL_ITEMS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def sum_hex(num1, num2):
    num1 = num1.copy()
    num2 = num2.copy()
    if len(num2) > len(num1):
        num1, num2 = num2, num1
    num2.extendleft('0' * (len(num1) - len(num2)))
    res = deque()
    excessive = 0
    while len(num1) != 0:
        first_digit = DECIMAL_ITEMS[num1.pop()]
        second_digit = DECIMAL_ITEMS[num2.pop()]
        result_digit = first_digit + second_digit + excessive
        if result_digit >= BASE:
            excessive = 1
            result_digit -= BASE
        else:
            excessive = 0
        res.appendleft(HEX_ITEMS[result_digit])
    if excessive == 1:
        res.appendleft('1')
    return res


def product_hex(num1, num2):
    num1 = num1.copy()
    num2 = num2.copy()
    if len(num2) > len(num1):
        num1, num2 = num2, num1
    num2.extendleft('0' * (len(num1) - len(num2)))
    res = deque('0')
    while len(num2) != 0:
        second_digit = DECIMAL_ITEMS[num2.pop()]
        eggs = deque('0')
        for i in range(second_digit):
            eggs = sum_hex(eggs, num1)
        eggs.extend('0' * (len(num1) - len(num2) - 1))
        res = sum_hex(res, eggs)
    return res


a = deque(input('Введите первое шестнадцатеричное число: ').upper())
b = deque(input('Введите второе шестнадцатеричное число: ').upper())
print(f'{list(a)} + {list(b)} = {list(sum_hex(a,b))}')
print(f'{a} * {b} = {product_hex(a,b)}')
