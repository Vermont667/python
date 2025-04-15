from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, old, dire, bal, grad=None):
        self.grad = grad
        self.name = name
        self.old = old
        self.dire = dire
        self.bal = bal

    @abstractmethod
    def print_info(self):
        pass


class Student(Human):

    def print_info(self):
        return print(f'{self.name} {self.old} {self.dire} {self.bal}')


class Teacher(Human):
    def print_info(self):
        return print(f'{self.name} {self.old} {self.dire} {self.bal}')


class Graduate(Student):
    def print_info(self):
        print(f'{self.name} {self.old} {self.dire} {self.bal} {self.grad}')


s = [Student('Батодалаев Даши', '16', 'ГК Web_011', '5'),
     Student('Загидуллин Линар', '32', 'РПО PD_011', '5'),
     Student('Маркин Даниил', '17', 'ГК Python_011', '5')]
t = [Teacher('Даньшин Андрей', '38', 'Астрофизика', '110'),
     Teacher('Башкиров Алексей', '45', 'Разработка приложений', '20')]
g = Graduate('Шугани Сергей', '15', 'РПО PD_011', '5', 'защита персональных данных')

for elem in s:
    elem.print_info()

g.print_info()

for elem in t:
    elem.print_info()

