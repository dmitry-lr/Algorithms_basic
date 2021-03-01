# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input("Введите натуральное трехзначное число: "))
hundreds = number//100
tens = number // 10 % 10
units = number % 10
summa = hundreds + tens + units
product = hundreds * tens * units
print(f'Сумма цифр равна: {summa}')
print(f'Произведение цифр равно: {product}')




