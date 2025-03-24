from math import pi, pow


def plo(x):
    if m == 1:
        a = int(input('введите длину: '))
        b = int(input('введите ширину: '))
        return a * b
    if m == 2:
        n = int(input('введите основание: '))
        s = int(input('введите высоту: '))
        return n * s / 2
    if m == 3:
        c = int(input('введите радиус: '))
        return pi * (pow(c, 2))


m = int(input('1 - прямоугольник, 2 - треугольник, 3 - круг :'))
print(round(plo(m), 2))
