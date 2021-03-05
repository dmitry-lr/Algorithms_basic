while True:
    sign = input("Введите знак операции (+, -, *, /, 0): ")
    if sign == '0':
        break
    if sign == "+" or sign == "-" or sign == "*" or sign == "/":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if sign == "+":
            print(f"Сумма чисел равна: {a+b:.2f}")
        elif sign == "-":
            print(f"Разность чисел равна: {a-b:.2f}")
        elif sign == "*":
            print(f"Произведение чисел равно: {a*b:.2f}")
        elif b != 0:
            print(f"Частное чисел равно {a/b:.2f}")
        else:
            print("Невозможно разделить на ноль!")
    else:
        print("Ошибка ввода!")
