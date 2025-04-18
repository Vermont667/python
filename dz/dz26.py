class Student:
    def __init__(self, name):
        self.__name = name
        self.nb = self.Notebook()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def print_info(self):
        print(f'{self.__name} => {self.nb.model}, {self.nb.cpu}, {self.nb.ram}')

    class Notebook:
        def __init__(self):
            self.model = 'HP'
            self.cpu = 'i7'
            self.ram = '16'


s = Student('Roman')
s.print_info()
s.name = 'Vladimir'
s.print_info()
