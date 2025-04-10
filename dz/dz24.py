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


