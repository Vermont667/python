def decor(fn):
    def inner(*args):
        print('сумма чисел', end=' '), print(*args, sep=', ', end=' '), print('=', fn(*args))
        print('среднее арифметическое чисел', end=' '), print(*args, sep=', ', end=' ')
        print('=', fn(*args) / len(args))

    return inner


@decor
def summ(*args):
    return sum(args)


summ(2, 3, 3, 4)
