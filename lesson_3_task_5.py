# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

LENGTH = 10
MIN_VALUE = -200
MAX_VALUE = -100
array = [random.randint(MIN_VALUE, MAX_VALUE) for i in range(LENGTH)]
print(f'Массив: {array}')
i = 0
index = -5
for i in range(len(array)):
    if array[i] < 0 and index == -5:
        index = i
    elif (array[i] < 0 and array[i] > array[index]):
        index = i
    i += 1
if index != -5:
    print(f'Максимальное отрицательное число = {array[index]} находится в ячейке {index}')
