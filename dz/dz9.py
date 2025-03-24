from random import randint


def kort(x, y):
    return tuple(randint(x, y) for i in range(10))


t1 = kort(0, 5)
print(t1)
t2 = kort(-5, 0)
print(t2)
t3 = t1 + t2
print(t3)
print('0 =', t3.count(0))