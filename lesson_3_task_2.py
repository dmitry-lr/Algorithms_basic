# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа

import random

LENGTH = 6
MIN_VALUE = 0
MAX_VALUE = 50
init_array = [random.randint(MIN_VALUE, MAX_VALUE) for i in range(LENGTH)]
print(f'Начальный массив: {init_array}')
even_index_array = []
for i, item in enumerate(init_array):
    if item % 2 == 0:
        even_index_array.append(i)
print(f'Массив из индексов четных элементов начального массива: {even_index_array}')
