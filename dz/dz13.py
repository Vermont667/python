from math import pi

plo = {
     1: (lambda x: pi * x)(2 * 2),
     2: (lambda x, y: x * y)(10, 13),
     3: (lambda a, b, h: (a + b) * h)(7, 5, 3/2)
}

print('площадь окружности радиуса 2:', plo.get(1))
print('площадь прямоугольника размером 10*13:', plo.get(2))
print('площадь трапеции для a=7 b=5 h=3:', plo.get(3))


