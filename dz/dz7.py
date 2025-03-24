from math import pi, pow

s = None
m = int(input('выберите фигуру:\n1-треугольник\n2-прямоугольник\n3-круг\n: '))
if m == 1:
    a = int(input('введите высоту: '))
    b = int(input('введите основание: '))
    s = b * a / 2
elif m == 2:
    a = int(input('введите длину: '))
    b = int(input('введите ширину: '))
    s = a * b
elif m == 3:
    a = int(input('введите радиус окружности: '))
    s = pi * (pow(a, 2))
else:
    print('такой фигуры нет')

print(round(s, 2))