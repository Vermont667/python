class Weight:

    def __init__(self, kg=12):
        self.__kg = kg

    def __check_value(c):
        if isinstance(c, int) or isinstance(c, float):
            return True
        return False

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, kg):
        if Weight.__check_value(kg):
            self.__kg = kg
        else:
            print('килограммы задаются только числами')

    @kg.deleter
    def kg(self):
        del self.__kg


w1 = Weight()
print(w1.kg, 'кг =>', round(w1.kg * 2.2046, 2), 'фунтов')
w1.kg = 41
print(w1.kg, 'кг =>', round(w1.kg * 2.2046, 2), 'фунтов')