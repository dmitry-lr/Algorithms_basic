# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def sum_digits(num):
    if num < 10:
        return num
    return num % 10 + sum_digits(num // 10)


n = int(input("Введите натуральное число (0 - для окончания ввода): "))
max_sum = 0
max_n = 0
while n != 0:
    egg_n = n
    egg_sum = sum_digits(n)
    if egg_sum > max_sum:
        max_sum = egg_sum
        max_n = egg_n
    n = int(input("Введите натуральное число (0 - для окончания ввода): "))
print(f"Число {max_n} имеет максимальную сумму цифр, которая равна: {max_sum} ")
