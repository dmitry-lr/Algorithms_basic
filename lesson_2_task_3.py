# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

number = int(input("Введите натуральное число: "))
res = 0
while number > 0:
    last_digit = number % 10
    number = number // 10
    res = res * 10
    res = res + last_digit
print(f"Перевернутое число: {res}")