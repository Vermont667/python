from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, a):
        self.a = a

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def plosh(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class Square(Shape):

    def perimetr(self):
        return 4 * self.a

    def plosh(self):
        return self.a * self.a

    def print_info(self):
        print('===Квадрат===')
        print(f'сторона: {self.a}\nцвет: red\nплощадь: {self.plosh()}\nпериметр: {self.perimetr()}')

    def print(self):
        for j in range(self.a):
            print('*' * self.a)


class Rectangle(Shape):
    def __init__(self, a, w):
        super().__init__(a)
        self.w = w

    def perimetr(self):
        return 2 * (self.w + self.a)

    def plosh(self):
        return self.w * self.a

    def print(self):
        for j in range(self.a):
            print('*' * self.w)

    def print_info(self):
        print('===Прямоугольник===')
        print(f'длина: {self.a}\nширина: {self.w}\nцвет: green\nплощадь: {self.plosh()}\nпериметр: {self.perimetr()}')


class Triangle(Shape):
    def __init__(self, a, w, h):
        super().__init__(a)
        self.w = w
        self.h = h

    def perimetr(self):
        return self.a + self.w + self.h

    def plosh(self):
        n = self.perimetr() / 2
        s = round((n * (n - self.a) * (n - self.w) * (n - self.h)) ** 0.5, 2)
        return s

    def print(self):
        for j in range(self.w):
            print(' ' * self.h + '*' * (j+j+1))
            self.h -= 1

    def print_info(self):
        print('===Треугольник===')
        print(f'сторона1: {self.a}\nсторона2: {self.w}\nсторона3: {self.h}\nцвет: green\nплощадь: {self.plosh()}\n'
              f'периметр: {self.perimetr()}')


s = Square(3)
r = Rectangle(3, 7)
t = Triangle(11, 6, 6)
for i in s, r, t:
    i.print_info()
    i.print()