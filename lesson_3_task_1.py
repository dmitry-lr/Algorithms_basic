# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# каждому из чисел в диапазоне от 2 до 9.

from_range = 2
to_range = 9
from_num = 2
to_num = 99
for i in range(from_range, to_range + 1):
    count = 0
    for j in range(from_num, to_num + 1):
        if j % i == 0:
            count += 1
    print(f'Числу {i} кратны {count} чисел')
