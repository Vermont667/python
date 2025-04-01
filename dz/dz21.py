class Auto:

    def __init__(self, name, year, manuf, power, color, price):
        self.name = name
        self.year = year
        self.manuf = manuf
        self.power = power
        self.color = color
        self.price = price

    def auto_info(self):
        print(' данные автомобиля '.center(40, '*'))
        print(f'название автомобиля: {self.name}\nгод выпуска: {self.year}\nпроизводитель: {self.manuf}\n'
              f'мощность двигателя: {self.power}\nцвет машины: {self.color}\nцена: {self.price}')
        print('=' * 40)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_manuf(self, manuf):
        self.manuf = manuf

    def get_manuf(self):
        return self.manuf

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


p1 = Auto('X7 M50i', 2021, 'BMW', '530 л. с.', 'white', 10790000)
p1.auto_info()