class Pair:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self.a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self.b

    @b.setter
    def b(self, b):
        self._b = b

    def summ(self):
        print(f'сумма: {self._a + self._b}')

    def work(self):
        print(f'произведение: {self._a * self._b}')


class RightTriangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def show_triangle(self):
        self.hypotenuse_right()
        self.summ()
        self.work()
        self.square()

    def hypotenuse_right(self):
        g = pow(self._a, 2) + pow(self._b, 2)
        c = pow(g, 0.5)
        print('Гипотенуза:', round(c, 2))

    def square(self):
        print(f'площадь: {self._a * self._b / 2}')


p2 = RightTriangle(5, 8)
p2.show_triangle()
print()
p2.a = 10
p2.b = 20
p2.show_triangle()


# from math import sqrt
#
#
# class Pair:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def edit_a(self, a):
#         self.a = a
#
#     def edit_b(self, b):
#         self.b = b
#
#     def summ(self):
#         return self.a + self.b
#
#     def mult(self):
#         return self.a * self.b
#
#
# class RightTriangle(Pair):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         self.c = self.hypotenuse()
#
#     def hypotenuse(self):
#         hypo = round(sqrt(self.a ** 2 + self.b ** 2), 2)
#         print(f'гипотенуза: {hypo}')
#         return hypo
#
#     def print_info(self):
#         print(f'прямоугольный треугольник: ({self.a}, {self.b}, {self.c})')
#
#     def square(self):
#         s = 0.5 * self.mult()
#         print(f'площадь: {s}')
#
#     def edit_a(self, a):
#         super().edit_a(a)
#         self.c = self.hypotenuse()
#
#     def edit_b(self, b):
#         super().edit_b(b)
#         self.c = self.hypotenuse()
#
#
# tr = RightTriangle(5, 8)
# tr.print_info()
# tr.square()
# print()
# print(f'сумма: {tr.summ()}')
# print(f'произведение: {tr.mult()}')
# print()
# tr.edit_a(10)
# tr.edit_b(20)
# print(f'сумма: {tr.summ()}')
# print(f'произведение: {tr.mult()}')
# tr.square()
