# Определить, какое число в массиве встречается чаще всего.

import random

LENGTH = 20
MIN_VALUE = 0
MAX_VALUE = 1000
array = [random.randint(MIN_VALUE, MAX_VALUE) for i in range(LENGTH)]
print(f'Начальный массив: {array}')
num = array[0]
freq = 1
for i in range(len(array)):
    egg = 1
    for j in range(i+1, len(array)):
        if array[i] == array[j]:
            egg += 1
    if egg > freq:
        freq = egg
        num = array[i]
if freq > 1:
    print(f'Число {num} встречается в массиве {freq} раз')
else:
    print("Все элементы массива уникальны")
