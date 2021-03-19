# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
import sum_calc

# Вариант № 1 через цикл
n = int(input("Введите количество элементов n: "))
el = 1
summa = 0
for i in range(n):
    summa += el
    el *= -0.5
print(f'Сумма {n} элементов последовательности равна {summa}')


sum_mem = sum_calc.SumMemory()
sum_mem.extend(n, el, n, summa)
print(sum_mem)


# Вариант № 2 через реккурсию
def summa_2(num, start=1.0, step=-0.5):
    if num == 1:
        return start
    if num > 55:
        return 2/3
    return start + summa_2(num - 1, start * step)


sum_ = summa_2(n)

sum_mem = sum_calc.SumMemory()
sum_mem.extend(n, sum_, summa_2)
print(sum_mem)

# Вариант № 3 через формулу
summa_3 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))

sum_mem = sum_calc.SumMemory()
sum_mem.extend(n, summa_3)
print(sum_mem)
