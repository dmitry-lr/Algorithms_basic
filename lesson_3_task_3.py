# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

LENGTH = 6
MIN_VALUE = 0
MAX_VALUE = 50
array = [random.randint(MIN_VALUE, MAX_VALUE) for i in range(LENGTH)]
print(f'Начальный массив: {array}')
index_min = 0
index_max = 0
for i in range(len(array)):
    if array[i] < array[index_min]:
        index_min = i
    elif array[i] > array[index_max]:
        index_max = i
array[index_min], array[index_max] = array[index_max], array[index_min]
print(f'Максимальный и минимальный элементы поменяли местами: {array}')
