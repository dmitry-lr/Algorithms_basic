# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

import timeit
import cProfile

# Вариант № 1 через цикл
n = int(input("Введите количество элементов n: "))
el = 1
summa = 0
for i in range(n):
    summa += el
    el *= -0.5

# Вариант № 2 через формулу
summa_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))


# Вариант № 3 через реккурсию
def summa_3(num, start=1.0, step=-0.5):
    if num == 1:
        return start
    # if num > 55:
    #     return 2/3
    return start + summa_3(num - 1, start * step)


sum_ = summa_3(n)


print(timeit.timeit('summa', number=100000, globals=globals()))                          #0.004790199999999967
print(timeit.timeit('summa', number=1000000, globals=globals()))                         #0.019846199999999925
print(timeit.timeit('summa', number=10000000, globals=globals()))                        #0.21017609999999998
print('_'*100)
print(timeit.timeit('summa_2 = 1 * (1 - (-0.5) ** 10) / (1 - (-0.5))', number=100000))   #0.0011597000000000968
print(timeit.timeit('summa_2 = 1 * (1 - (-0.5) ** 10) / (1 - (-0.5))', number=1000000))  #0.012180400000000091
print(timeit.timeit('summa_2 = 1 * (1 - (-0.5) ** 10) / (1 - (-0.5))', number=10000000)) #0.12471690000000013
print('_'*100)
print(timeit.timeit('summa_3(10)', number=100000, globals=globals()))                    #0.20312419999999998
print(timeit.timeit('summa_3(10)', number=1000000, globals=globals()))                   #1.9691387000000002
print(timeit.timeit('summa_3(10)', number=10000000, globals=globals()))                  #20.1556998


cProfile.run('summa')
#          3 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('summa_2')
#   3 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('summa_3(990)')
#          993 function calls (4 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     990/1    0.001    0.000    0.001    0.001 lesson_4_task_1.py:20(summa_3)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#Вывод: лучше всего использовать простую формулу из алгебры для подсчета геометрической прогрессии,
# он примерно в 2 раза быстрее алгоритма с циклом for и на несколько порядков быстрее реккурсии.
# Реккурсия в целом очень затратный алгоритм, одиночный цикл for (без дополнительно вложенных циклов)
# значительно оптимальнее, обычная формула без перебора последовательности и реккурсии - самый простой и быстрый вариант




