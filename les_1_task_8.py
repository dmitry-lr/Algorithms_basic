# Определить, является ли год, который ввел пользователь, високосным или не високосным.

year_number = int(input("Введите номер года: "))
if year_number % 4 != 0:
    print("Год не високосный")
elif year_number % 100 == 0:
    if year_number % 400 != 0:
        print("Год не високосный")
    else:
        print("Год високосный")
else:
    print("Год високосный")