# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует,
# то определить, является ли он разносторонним, равнобедренным или равносторонним.

a = float(input("Введите длину первого отрезка: "))
b = float(input("Введите длину второго отрезка: "))
c = float(input("Введите длину третьего отрезка: "))
if a + b <= c or a + c <= b or b+c <= a:
    print("Составить треугольник из данных отрезков нельзя")
elif a != b and b != c and a != c:
    print("Из этих отрезков можно составить разносторонний треугольник")
elif a == b == c:
    print("Из этих отрезков можно составить равносторонний треугольник")
else:
    print("Из этих отрезков можно составить равнобедренный треугольник")
