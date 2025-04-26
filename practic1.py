class Point3D:
    def __init__(self, x, y, z):
        self.__x = x
        self.z = z
        self.y = y

    def __add__(self, other):
        return Point3D(self.__x + other.__x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.__x - other.__x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point3D(self.__x * other.__x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Point3D(self.__x / other.__x, self.y / other.y, self.z / other.z)

    def __eq__(self, other):
        return Point3D(self.__x == other.__x, self.y == other.y, self.z == other.z)

    def print_info1(self):
        print(f'координаты 1-й точки: {self.__x}, {self.y}, {self.z}')

    def print_info2(self):
        print(f'координаты 2-й точки: {self.__x}, {self.y}, {self.z}')

    def get_info(self):
        return f'({self.__x}, {self.y}, {self.z})'

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x


p1 = Point3D(12, 15, 18)
p2 = Point3D(6, 3, 9)
p1.print_info1()
p2.print_info2()
p3 = p1 + p2
print('сложение координат: ', p3.get_info())
p3 = p1 - p2
print('вычитание координат: ', p3.get_info())
p3 = p1 * p2
print('умножение: ', p3.get_info())
p3 = p1 / p2
print('деление: ', p3.get_info())
if p1.x == p2.x and p1.y == p2.y and p1.z == p2.z:
    print('равенство координат: True')
else:
    print('равенство координат: False')
print(f'x = {p1.x} x1 = {p2.x}')
print(f'y = {p1.y} y1 = {p2.y}')
print(f'z = {p1.z} z1 = {p2.z}')
p1.x = 20
p2.x = 20
print('запись значения в координату x: 20')
p1.print_info1()
p2.print_info2()
