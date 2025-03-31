# name = 'admin'
# print('hello', name)
# age = 20.2
# print(age)
#
# print(type(name))
# print(type(age))
#
# print(id(name))
# print(id(age))
import os
# name = 'admin'
# print(name)

# import keyword
# print(keyword.kwlist)

# a = 5
# b = 20
# print('a:', a)
# print('b:', b)

# print('a:', a)
# print('b:', b)

# print('документ \'file\' находится на пути d:\\folder\\file')

# s1 = 'hello'
# s2 = 'Python'
# s3 = s1 + ' ' + s2 + '\t\t'  # сложение строк
# print(s3)
# s4 = s3 * 3
# print(s4)

# print(6 + 2)
# print(6.2 + 2.4)
# print(6 / 2)
# print(6 // 2)
# print(7 // 2)
#
# print(6 ** 2)
# print(7 % 2)

# a = 5
# b = 7
# c = 3
# print(a + b + c) # 3
# print(a * b * c)
# print((a + b) / c)

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# a = 5
#
# a += 3  # a = a + 3
# print(a)  # 8
#
# a -= 3
# print(a)  # 5

# num = 4321  # 432
# print('исходное число', num)
# a = num % 10
# print('a:', a)
# num = num // 10
# # print(num)
# b = num % 10
# print('b:', b)
# num = num // 10
# # print(num)
# c = num % 10
# print('c:', c)
# num = num // 10
# # print(num)
# d = num % 10
# print('d:', d)
# print('обратное число:', a * 1000 + b * 100 + c * 10 + d)

# num1 = '2'
# num2 = 3
# # res = num1 + str(num2)
# res = int(num1) + num2
# print(res)

# print(int(3.981))
# print(type(round(3.981)))
# print(round(3.981, 2))

# num1 = '2.5'
# num2 = 10
# res = float(num1) + num2
# print(res)

# nan = 'виктор'
# age = 20
# print('меня зовут', nan, '. мне', age, 'лет')
# print('меня зовут ' + nan + '. мне', str(age) + ' лет')
# print('меня зовут ', nan, '. мне ', age, ' лет', sep='', end='')
# print('Hello Python')


# nen = input('введите имя: ')
# print('hello,', nen)

# nun = int(input('введите число: '))
# power = int(input('введите степень: '))
# # nun = int(nun)
# # power = int(power)
# res = nun ** power
# print('число', nun, 'в степени', power, 'равно', res)

# nun = int(input('введите число 1: '))
# non = int(input('введите число 2: '))
# nan = int(input('введите число 3: '))
# nin = int(input('введите число 4: '))
# res = ((nun + non) / (nan + nin))
# print(res, 2)

# b1 = True
# b2 = False
# print(b1)
# print(b2)
# print(type(b1))
# print(type(b2))

# print(5 == 5)
# print(int(b1))
# print(int(b2))
# print(b1 + 5)
# print(b2 + 5)

# print(bool('python'))
# print(bool(''))
# print(bool(' '))
# print(bool(5))
# print(bool(0))
# print(bool(0.02))
# print(bool(0.0))
# print(bool(True))
# print(bool(False))
# print(bool(None))

# test = None
# print(test)
# test = 5
# print(test)

# print(5 == 5)
# print(5 == 3)
# print(5 + 2 == 3 + 4)  # 7 == 7
# print(5 + 2 != 3 + 4)  # 7 != 7
# print(8 > 5)
# print(8 >= 8)
# print(5 < 10)
# print(5 <= 5)
# print('hello' > 'Hello')  # 104 > 72

# print(2 < 4 < 9)  # True : True => True
# print(2 > 4 < 9)  # False : False => False3
#
# print(3 * 3 <= 7 >= 2)  # 9 <= 7 >= 2  False : True => False

# print(5 - 3 == 2 and 1 + 3 == 4)  # 2 == 2 and 4 == 4; True and True => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True and False => False
# print(5 - 3 > 2 and 1 + 3 == 4)  # False and True => False
# print(5 - 3 > 2 and 1 + 3 < 4)  # False and False => False

# print(5 - 3 == 2 or 1 + 3 == 4)  # 2 == 2 or 4 == 4; True or True => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True or False => True
# print(5 - 3 > 2 or 1 + 3 == 4)  # False or True => True
# print(5 - 3 > 2 or 1 + 3 < 4)  # False or False => False

# print(not 9 - 5)  # not True => False
# print(not 7 - 7)  # not False => True

# a = 10
# b = 10
# if a > b:
#     print(a, '>',  b)
# if b > a:
#     print(b, ">", a)
# if b == a:
#     print(b, "==", a)

# a = 40
# b = 50
# if a > b:
#     print(a, '>', b)
# elif b == a:  # else if
#     print(a, '==', b)
# else:
#     print(b, '>', a)

# age = int(input('введите свой возраст: '))
# if age >= 18:
#     print('доступ разрешен')
#     print('приятного просмотра')
# else:
#     print('доступ запрещен')

# a = input('введите первую сторону: ')
# b = input('введите вторую сторону: ')
# c = input('введите третью сторону: ')
#
# if a == b == c:
#     print('треугольник равносторонний')
# elif a == b or a == c or b == c:
#     print('треугольник равнобедренный')
# else:
#     print('треугольник разносторонний')

# day = int(input('введите день недели(цифрой): '))
# if 1 <= day <= 5:   # (day >= 1) and (day <= 5)
#     print('рабочий день - ', end='')
#     if day == 1:
#         print('понедельник')
#     if day == 2:
#         print('вторник')
#     if day == 3:
#         print('среда')
#     if day == 4:
#         print('четверг')
#     if day == 5:
#         print('пятница')
# elif day == 6 or day == 7:
#     print('выходной день - ', end='')
#     if day == 6:
#         print('суббота')
#     if day == 7:
#         print('воскресенье')
# else:
#     print('такого дня недели не существует')

# n = int(input('введите количество ворон: '))
# if 0 <= n <= 9:
#     print('на ветке', end=' ')
#     if n == 1:
#         print(n, 'ворона')
#     elif 2 <= n <= 4:
#         print(n, 'вороны')
#     else:
#         print(n, 'ворон')
# else:
#     print('ошибка ввода данных')

# password = 'qwerty'
#
# match password:
#     case 'admin':
#         print('администратор')
#     case 'user':
#         print('пользователь')
#     case _:
#         print('пароль неверный')

# day = 'понедельник'
# time = 13
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print('рабочий день')
#     case 'суббота' | 'воскресенье':
#         print('выходной день')
#     case _:
#         print('такого дня недели не существует или не рабочее время')

# a, b = 30, 20
#
# print(a if a < b else b)

# a, b = 20, 20
# print('a == b' if a == b else 'a > b' if a > b else 'b > a')

# try:   # попытаться выполнить
#     n = int(input('введите целое число: '))
#     print(n * 2)
# except ValueError:
#     print('не то')

# try:
#     n = int(input('введите делимое: '))
#     m = int(input('введите делитель: '))
#     print(n / m)
# except ValueError:
#     print('нельзя вводить строки')
# except ZeroDivisionError:
#     print('нельзя делить на ноль')


# try:
#     n = int(input('введите делимое: '))
#     m = int(input('введите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print('нельзя вводить строки или нельзя делить на ноль')
# else:
#     print('всё ок, ты ввел', n, 'и', m)
# finally:   # работает в любом случае
#     print('конец')

# n = input('введите число: ')   #
# m = input('введите число: ')   #
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# циклы

# while условие:
#     блок_инструкций

# i = 0 # Счетчик
# while i < 5: # условие
#     print('i =', i)
#     i += 1  # изменение счетчика

# итерация - один шаг цикла


# i = 2
# while i <= 20:
#     if i % 2:  # i % 2 == 1, i % 2 != 0 - нечетные числа, i % 2 == 0 - четные числа
#         print(i, end=' ')
#     i += 1

# i = 2
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=' ')
#     i += 2

# n = int(input('количество символов: '))
# # print('*' * n)
# i = 0
# while i < n:
#     print('*', end='')
#     i += 1

# +-+-+-+

# n = int(input('количество символов: '))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print('+', end='')
#     else:
#         print('-', end='')
#     i += 1


# n = int(input('количество символов: '))
# while n > 0:
#     print('*', end='')
#     n -= 1

# a = int(input('введите начало диапазона: '))
# b = int(input('введите конец диапазона: '))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a, end=' ')
#         res += a  # res = res + a
#     a += 1
# print('\nсумма:', res)

# n = input('введите целое число: ')
#
# while type(n) is not int:  # is not - !=
#     try:
#         n = int(n)
#     except ValueError:
#         print('число не целое')
#         n = input('введите целое число: ')
#
# if n % 2 == 0:
#     print('четное')
# else:
#     print('нечетное')

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершен')

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input('введите положительное число: '))
#     if n < 0:
#         breaK
#
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print('цикл окончен, i =', i)

# i = 1
# while i < 5:
#     print('внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print('\tвнутренний цикл: j =', j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# for element in collection:
#   print(element)

# for i in 'hello', 'world':
#     print(i)

# range(start=0, stop, step=1)
#
# print(range(0, 8, 2))

# a = 10
# for i in range(0, 10, 1):  # i = 0, i < 10, i += 1  # i = 0, i > 0, i -= 1
#     print(i, end=' ')
#
# print()
#
# i = 1
# while i < 10:
#     print(i, end=' ')
#     i *= 2


# a = int(input('введите целое число: '))
#
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=' ')

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=' ')
#
# print()
#
# for i in range(11, 100, 11):
#     print(i, end=' ')
#
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('цикл закончен')

# for i in range(3):
#     print('+++')
#     for j in range(2):
#         print('-----')

# w = int(input('введите ширину прямоугольника: '))
# h = int(input('введите высоту прямоугольника: '))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# letter = [i * 2 for i in 'hello']
# print(letter)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)


# список (list)
# nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[1])
# print(nums[10])
# print(nums[-1])
# print('кол-во', len(nums))
# nums[1] = 256
# nums[3] += 100
# print(nums)

# s = []
# print(s)
# print(type(s))
#
# t = list('python')
# print(t)
# print(type(t))
#
# print(range(0, 8, 2))
# print(list(range(1, 18, 2)))

# a = [1, 5, 7, 9]
# b = [1, 6, 7, 8, 9]
# print(a + b)
# print(a * 3)

# a = [1, 5, 7, 9]
#
# for i in a:
#     print(i)

# a = [0 for _ in range(5)]
# print(a)  # [0, 0, 0, 0, 0]

# a = [i for i in range(5)]
# print(a)  # [1, 2, 3, 4]

# n = 15
# a = [i ** 2 for i in range(2, n)]
# print(a)

# a = [0] * int(input('введите кол-во элементов списка: '))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('-> '))
# print(a)

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# print(a)

# lst = [9, 8, 7, 6]
#
# for i in range(len(lst)):  # 0 1 2 3
#     print(lst[i], end=' ')
#
# print()
#
# for v in lst:  # 9 8 7 6
#     print(v, end=' ')

# n = list(range(21, 41))
# print(n)
# c = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         c += 1
#     else:
#         s += n[i]
# print('кол-во четных элементов:', c)
# print('кол-во нечетных элементов:', s)

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=' ')
# print()
#
# for i in range(0, len(a), 2):
#     print(a[i], end=' ')

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')

# a = [9, 7, 8, 4, 2]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# срез

# список[start:stop:step]
# a = [9, 7, 8, 4, 2, 1, 3]
# print(a)
# print(a[1:4])
# print(a[5:])
# print(a[1:4:2])
# print(a[::-2])
# print(a[-1:0:-1])
# print(a[10:20])

# a = [9, 7, 8, 4, 2, 1, 3]
# print(a)
# a[1:2] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]
# print(a)
# a[100:111] = [100]
# print(a)
# print(a[10])
# print(len(a))

# методы списков
# s = [9, 7, 8, 4, 2, 1, 3]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([11, 12, 13])  # добавляет другой список элементов в конец списка
# print(s)
# s.insert(2, 100)   # добавляет элемент (второй параметр) по заданному индексу (первый параметр)
# print(s)

# s = []
# n = int(input('кол-во элементов списка: '))
# for num in range(n):
#     x = int(input('введите число: '))
#     # s.append(x)
#     s.insert(0, x)  # [7, 8, 9] (развернул)
# print(s)

# a = [5, 9, 2, 1, 4, 3, 3, 4]
# b = [4, 2, 1, 3, 7, 2]
# c = []
#
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
#
# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 3, 7, 2]
# c = []
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):  # 0, 1, 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0, 1, 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
#
# print(c)

# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):  # 0, 1, 2
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# s = [9, 7, 8, 4, 3, 8, 2, 1, 3]
# print(s)
# item = 8
# if item in s:
#     s.remove(item)  # удаляет первое вхождение элемента по значению
# print(s)
#
# last = s.pop()  # удаляет последний элемент из списка
# print(last)
# print(s)
#
# try:
#     second = s.pop(10)  # удаляет элемент по заданному индексу
# except IndexError:
#     second = 'такого индекса нет'
# print(second)
# print(s)
#
# s.clear()  # удаляет элементы из списка
# print(s)

# s = [9, 7, 8, 4, 3, 8, 1, 3]
# print(s)
#
# s[5:] = []
# print(s)
#
# del s[:]
# print(s)

# s = [9, 7, 8, 4, 3, 8, 1, 3, 8]
# print(s)
#
# # num = s.count(8)  # кол-во вхождений заданного элемента
# # print(num)
#
# ind = s.index(8, 3, 7)  # ищет первое вхождение заданного элемента, возвращает индекс на котором
# # нашел элемент, можно задать диапазон поиска
# print(ind)

# a = [1, 2, 3]
# b = a.copy()
# print('a=', a, id(a))
# print('b=', b, id(b))
# b.append(20)
# print('a=', a)
# print('b=', b)
# a.append(100)
# print('a=', a)
# print('b=', b)

# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# # s.reverse()
# # print(s)
# s.sort(reverse=True)
# print(s)

# s = ['виталий', 'сергей', 'аня', 'саня']
# s.sort(key=len, reverse=True)
# print(s)

# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# lst = sorted(s, reverse=True)
# print('lst:', lst)
# print(s)

# import random

# print(random.random())
# print(random.randint(5, 10))
# print(random.randrange(5, 10, 2))
# print(round(random.uniform(10.5, 25.5), 2))

# c = ['москва', 'питер', 'сочи', 'новосибирск']
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(random.choice(c))
# print(random.choice(s))
# print(random.choices(c, k=3))
# print(random.choices(s, k=3))
# random.shuffle(s)
# print(s)

# import random

# m = [random.randint(50, 100) for i in range(10)]
# print(m)
# print(len(m))
# print(max(m))
# print(min(m))
# print(sum(m))

# m = [random.randint(0, 100) for i in range(10)]
# print(m)
# n = max(m)
# print(n)
# m.remove(max(m))
# m.insert(0, n)
# print(m)

# import random
#
# m = [random.randint(0, 100) for i in range(10)]
# print(m)
# min_ = min(m)
# print('min:', min_)
# ind = m.index(min_)
# print('index min:', ind)
# del m[:ind]
# print(m)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 9],
#     [3, 5, 6, 10]
# ]
# print(m)

# print(len(m))
# print(m[1][2])
# print(m[2][1])

# print('вариант 1')
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()
# print('вариант 2')
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()

# m = ['hello', 'world', [44, [55, 2, 66], 77, ['python']]]
# print(m)
# print(m[1][0])
# print(m[2][1][1])
# print(m[2][3][0][3])

# import math
#
# print(math.sqrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.8))

# import math as m
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import *
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))

# from math import sqrt, ceil, floor
# #
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))

# print(dir(list))

# from math import pi
#
# # print(pi)
# radius = int(input('введите радиус окружности: '))
# print('длина окружности:', round(2 * radius * pi, 2))

import time
import locale
from os import write
from sys import base_prefix

# print(time.time())
# print(time.ctime())
# res = time.localtime()
# print(res)
# print(res.tm_year, '-', res.tm_mon, '-', res.tm_mday, sep='')
# print(time.strftime('today is %B %d, %Y'))
# print(time.strftime('%m/%d/%Y, %H:%M:%S', time.localtime(46592486)))
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime('сегодня: %B %d, %Y'))

# start = time.time()
# print('запуск')
# time.sleep(5)
# res = time.time() - start
# print('программа выполнена за', res, 'секунд')


# функции

# def hello(name, age):  # аргументы
#     print('меня зовут', name, 'мой возраст', age)
#
#
# hello('Irina', 28)  # параметры
# hello('Ivan', 25)


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum('abc', 'def')

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', '0')


# def get_sum(a, b):
#     print('сумма:', end=' ')
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 5))
# print(maximum(5, 15))


# def raz(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# x = int(input('a = '))
# y = int(input('b = '))
# print(raz(x, y))


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, 'в кубе =', cube(i))


# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def one_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = int(input('введите первое число: '))
# b = int(input('введите второе число: '))
# if one_big(a, b):
#     print('первое число больше второго')
# else:
#     print('второе число больше первого')


# print(one_big(10, 5))
# print(one_big(5, 10))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input('введите пароль: ')
# if check_password(p):
#     print('это надежный пароль')
# else:
#     print('это ненадежный пароль')

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2, c=5))
# print(get_sum('h', 'e', d='p', c='l'))


# def set_param(count=20, symbol='-'):
#     print(symbol * count)
#
#
# set_param(10, '+')
# set_param(5, '*')
# set_param(15, '#')
# set_param(7)
# set_param()


# def display_info(name, age):
#     print('name:', name, '\nage:', age)
#
#
# display_info('irina', 23)
# display_info(23, 'irina')
# display_info(age=23, name='irina')


# lt1 = 'hello'
# lt2 = 'hello'
# print(lt1, id(lt1))
# print(lt2, id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)

#
# lt1 = [1, 2, 3]
# print(lt1, id(lt1))
# lt1.append(4)
# print(lt1, id(lt1))
# lt1.pop(1)
# print(lt1, id(lt1))

# a = 5
# print(a, id(a))
# a = 7
# print(a, id(a))


# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# lst[1] = 100
# print(lst)
# print(tpl)

# a = ()
# print(a, type(a))
# b = tuple()
# print(b, type(b))

# a = (1, 2, 3)
# print(a, type(a))
#
# b = tuple('hello')
# print(b, type(b))
#
# b = tuple('hello')
# print(b)
#
# print(b[1])
# print(b[1:3])

# s1 = tuple(input('->') for i in range(5))
# print(s1)

# s1 = tuple(i for i in range(5))
# print(s1)


# from random import randint
#
# s1 = tuple(randint(50, 100) for i in range(5))
# print(s1)

# t1 = tuple('hello')
# t2 = tuple('world')
# # print(t1)
# # print(t2)
# t3 = t1 + t2
# # print(t3 * 2)
# print(t3)
# print(t3.count('l'))


# множество (set)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)  # a | b
# c = a | b
# a |= b
# c = a & b  # {1, 2, 3, 4)
# a &= b
# print(a)
# c = a - b  # {0}
# a -= b
# print(c)
# c = a ^ b
# a ^= b
# print(c)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a <= b
# print(c)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = {6, 2}
# e = {8, 2}
# # d = b ^ c ^ a ^ e  # { 4, 6}  ^ {0, 2}
# d = a.symmetric_difference(b).symmetric_difference(c).symmetric_difference(e)  #
# print(d)

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# j = {9, 8}
# n = a | b | c | d | e | f | j
# print(n)
# print('unic elem count:', (len(n)))
# print('min elem:',  min(n))
# print('max elem:',  max(n))

# a = 'hello'
# b = 'how are you'
# c = set(a) & set(b)
# for i in c:
#     print(i, end=' ')

# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)
# s1 = frozenset('hello')
# print(s1)


#  словарь (dict)

# lst = ['one', 'two']
# b = {'first': 'one', 'second': 'two'}
# print(lst[1])
# print(b['second'])

# d = {0: 'text', 'one': 45, (1, 2): 'кортеж', True: [5, 6, 4, 3], False: 'один', 1: 'список'}
# print(d)


# d = {1: 'one', 'second': 'two'}
# print(d)
# print(type(d))
#
# d1 = dict(first='one', second='two')
# print(d1)
# print(type(d1))

# lst = [
#     ['one', 1],
#     ['two', 2],
#     ['three', 3]
# ]
#
# print(lst)
# d = dict(lst)
# print(d)

# d = {i: i ** 2 for i in range(1, 7)}
# print(d)
#
# for i in d:
#     print('key =', i, 'value =', d[i])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)
#
# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
# del d['x2']
# print(d)

# d = dict()
# d[1] = input('->')
# d[2] = input('->')
# d[3] = input('->')
# d[4] = input('->')
# print(d)

# d = {i: input('->') for i in range(1, 5)}
# print(d)
# dis = int(input('какой элемент исключить: '))
# del d[dis]
# print(d)

# goods = {
#     '1': ['core-i3-4330', 9, 4500],
#     '2': ['core-i5-4670K', 3, 8500],
#     '3': ['AMD ZX-6300', 6, 3700],
#     '4': ['pentium 03220', 8, 2100],
#     '5': ['core i7 4350', 5, 6500],
# }
#
# for i in goods:
#     print(i, ')', goods[i][0],  ' - ', goods[i][1], ' шт. по ', goods[i][2], sep='')
#
# while True:
#     n = input('N: ')
#     if n == '0':
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input('количество: '))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print('некорректно. введите число')
#         else:
#             print('такого ключа не существует')
#
# for i in goods:
#     print(i, ')', goods[i][0],  ' - ', goods[i][1], ' шт. по ', goods[i][2], sep='')

# print(dir(dict))

# d = {1: 'one', 2: 'two'}
# print(d.keys())
# print(d.values())
# print(d.items())
#
# for i, j in d.items():
#     print(i, ':', j)

# d = {1: 'one', 2: 'two', 3: 'three'}
# d2 = d.copy()
# print('d =', d)
# print('d2 =', d2)
#
# d2[2] = 'four'
# print('d =', d)
# print('d2 =', d2)

# d = {1: 'one', 2: 'two', 3: 'three'}
# print(d)
# d.clear()
# item = d.pop(6, 'нет')
# item = d.popitem()
# print(d)
# print(item)

# d = {1: 'one', 2: 'two', 3: 'three'}
# value = d[6]
# value = d.get(6, 'такого ключа нет')
# print(value)
# item = d.setdefault(4, 'four')
# print(d)
# print(item)
# a = {10: 'A', 20: 'B', 2: 'C'}
# a = [(10, 'A'), (20, 'B'), (2, 'C')]
# c= d | a
# print(c)
# d.update(a)
# print(d)

# d = {'name': 'kelly', 'age': 25, 'salary': 8800, 'city': 'new york'}
#
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# new_d['name'], new_d['salary'] = d.pop('name'), d.pop('salary')
#
# print(d)
# print(new_d)

# d = {'name': 'kelly', 'age': 25, 'salary': 8800, 'city': 'new york'}
#
# d['location'] = d.pop('city')
# print(d)


# reg = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 4737, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451},
# }
#
#
# for x, y in reg.items():
#     print(x)
#     for i, j in y.items():
#         print('\t', i, ':', j)

# c = {'один': 1, 'Два': 2, 'три': 3, 'четыре': 4}
# new_c = {value: key for key, value in c.items()}
# print(c)
# print(new_c)

# c = {'один': 1, 'Два': 2, 'три': 3, 'четыре': 4}
# new_c = {key: value for key, value in c.items() if value <= 2}
# print(new_c)

# c = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(c)
#
# s = 'hello'
# c1 = {key: key * 3 for key in s}
# print(c1)

# c = {'один': 1, 'Два': 2, 'три': 3, 'четыре': 4}
#
# print(list(c.values()))
# print(list(c.keys()))
# print(list(c.items()))

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) is str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)


# zip

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)

# a = [1, 2, 3, 4]
# b = ['one', 'two', 'three']
# d = {k: v for k, v in zip(a, b)}
# print(d)

# one = {'name': 'igor', 'surname': 'pavlov', 'job': 'consultant'}
# two = {'name': 'irina', 'surname': 'vetrova', 'job': 'manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# s = [(1, 'a'), (2, 'b'), (3, 'c')]
# a, b = zip(*s)
# print(a)
# print(b)

# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 1, 3, 2]
# d = dict(zip(letters, numbers))
# print(d)
#
# data1 = list(zip(letters, numbers))
# print(data1)
# data1.sort()
# print(data1)
# d2 = dict(data1)
# print(d2)
#
# data2 = list(zip(numbers, letters))
# print(data2)
# data2.sort()
# print(data2)
# d3 = {v: k for k, v in data2}
# print(d3)

# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 1, 3, 2]
#
# data = sorted(zip(letters, numbers))
# print(dict(data))

# one = {'один': 1, 'два': 2}
# two = {'три': 3, 'четыре': 4}
#
# print({**one, **two})
# print(one | two)
#
# for k, v in {**one, **two}.items():
#     print(k, '->', v)

# colors = ['red', 'green', 'blue']
# ind = 1
# for color in colors:
#     print(str(ind) + '-й цвет: ' + color)
#     ind += 1
#
# print()
# for index, color in enumerate(colors, 10):
#     print(str(index) + '-й цвет: ' + color)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
#
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ') ', k, ': ', v, sep='')

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(1, 2, 3, 'abc'))
# print(func())

# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(7, 8, 9))


# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(1, 2, 3, 4, 5))


# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='bob', age=31, weiht=61, eyes_color='grey')
# print(my_dict)


# def func(a, *args, b=100, ** kwargs):
#     return a, args, kwargs, b
#
#
# print(func(1, 2, 3, 4, 5, 6, c=55, d=56, e=77))


# области видимости (score)

# name = 'tom'  # глобальная область видимости
#
#
# def hi():
#     global name
#     name = 'sam'
#     surname = 'jonson'  # локальная область видимости
#     print('hello', name, surname)
#
#
# def bye():
#     print('good bye', name)
#
#
# print(name)
# hi()
# bye()
# print(name)


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()


# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)


# max = 5
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(max(lst))


# def add_two(a):
#     x = 2  # 2
#
#     def add_some():
#         x = 3
#         print('x =', x)  # 4
#         return a + x  # 5
#     print('x в наружной функции =', x)
#     return add_some()  # 3  6
#
#
# print(add_two(3))  # 1  7


#  вложенные функции

# def outer(who):
#     def inner():
#         print('Hello,', who)
#
#     inner()
#
#
# outer('world')


# def outer():
#     a = 6
#
#     def inner(b):
#         a = 4
#         print('сумма:', a + b)
#
#     print('a =', a)
#     inner(5)
#
#
# outer()


# def para(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + (inner(a, c) + (inner(b, c))))
#     return s
#
#
# print(para(2, 4, 6))
# print(para(5, 8, 2))
# print(para(1, 6, 8))


#  замыкание


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# a = outer(5)
# print(a(10))
#
# b = outer(6)
# print(b(10))
#
# print(outer(5)(10))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a
#         c.append(4)
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# анонимные функции (lambda)

# def func(x, y):
#     return x + y
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))

# func1 = lambda x, y: x + y
#
# print(func1(1, 2))
# print(func1(5, 2))

# print((lambda n: lambda x: lambda y: x + n + y)(1)(2)(3))


# map()


# t = (2.88, -1.78, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# areas = [3.454212, 5.546357, 4.123456, 56.754638, 9.356923765, 32.6387563]
#
# print(list(map(round, areas, range(1, 7))))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))


# filter()

# t = ('abcd', 'qwe', 'zxcvb', 'def', 'hjk')
#
# print(tuple(filter(lambda s: len(s) == 3, t)))

# import random
#
# t = [random.randint(0, 40) for i in range(10)]
# print(t)
# print(list(filter(lambda s: s in range(10, 21), t)))


# nums = [45, 55, 60, 37, 100, 105, 220]
#
# print(list(filter(lambda x: x % 15 == 0, nums)))
# print(list(filter(lambda x: not x % 15, nums)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))
#
# print([x ** 2 for x in range(10) if x % 2])


#  декораторы

# def hello():
#     return 'hello, im func "hello"'
#
#
# def super_func(func):
#     print('hello, i im func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'hello, im func "hello"'
#
#
# text = hello
# print(text())


# def my_decorator(func):
#     def inner():
#         print('до кода')
#         func()
#         print('после кода')
#     return inner
#
#
# def func_test():
#     print('hello, i am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):
#     def inner():
#         print('до кода')
#         func()
#         print('после кода')
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('hello, i am func "func_test"')
#
#
# func_test()

# from math import pi
#
# l1 = [2 * 2]
# l2 = [10]
# l3 = [13]
# l4 = [7]
# l5 = [5]
# l6 = [3/2]
#
# print(list(map(lambda x: pi * x, l1)))
# print(list(map(lambda x, y: x * y, l2, l3)))
# print(list(map(lambda a, b, h: (a + b) * h, l4, l5, l6)))


# def ci(fn):
#     def wrap():
#         return '(' + fn() + ')'
#
#     return wrap
#
#
# def angel(fn):
#     def wrap():
#         return '<' + fn() + '>'
#
#     return wrap
#
#
# @angel
# @ci
# def ex():
#     return '5 + 2'
#
#
# print(ex())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print('вызов функции:', count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('hello')
#
#
# hello()
# hello()
# hello()
# hello()


# def decor(arg):
#     def pl(fn):
#         def fo(*args, **kwargs):
#             return arg * fn(*args, **kwargs)
#
#         return fo
#     return pl
#
#
# @decor(3)
# def st(num):
#     return num
#
#
# print(st(5))

# def typ(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:
#                     raise TypeError('неверный тип данных')
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return wrapper
#
#
# @typ(int, int, int)
# def typed(x, y, z):
#     return x * y * z
#
#
# print(typed(3, 4, 5))
# print(typed(3, 4, 'hello'))


# строки


# print(bin(18))  # 0b10010 - двоичная система счисления
# print(oct(18))  # 0o22 - восьмеричная система счисления
# print(hex(18))  # 0x12 - шестнадцатеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12 + 0b10010 + 4)


# q = 'pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print('y' in e)
# print(e[1])
# print(e[::-1])


# def chat_str(s, old, new):
#     s2 = ''
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#
#         i += 1
#
#     return s2
#
#
# str1 = 'Я изучаю Python. Мне нравится Python. Python очень интересный язык программирования'
# str2 = chat_str(str1, 'P', 'N')
# print(str1)
# print(str2)


# print(u'привет')
# print('привет')

# print('C:\\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + '\\')
# print('C:\\file.txt\\')

# print(b'1e2b3c')

# name = 'дмитрий'
# age = 25
# print(f'Меня зовут {name}, мне {age} лет.')

# x = 10
# y = 5
# print(f'{x=}, {y=}')
# print(f'{round(10/7, 2)}')
# print(f'{10/7:.2f}')
# num = 74
# print(f'{{{num}}}')

# dir_name = 'folder'
# file_name = 'file.txt'
# print(fr'home\{dir_name}\{file_name}')
# print('home\\' + dir_name + '\\' + file_name)

# s = '''многостр  очный
# текст'''
# print(s)


# def sq(n):
#     '''принимает число n, возвращает квадрат числа n'''
#     res = n ** 2
#     return res
#
#
# print(sq(5))
# print(sq.__doc__)
# print(sum.__doc__)
# print(len.__doc__)


# from math import pi
#
#
# def cil(r, h):
#     """
#     вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания.
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cil(2, 4))
# print(cil.__doc__)


# print(ord('b'))
# print(ord('П'))


# while True:
#     n = input('->')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# st = 'Test string for me '
# arr = [ord(x) for x in st]
# print('ASCII коды', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print('среднее арифметическое:', arr)
# arr += [ord(x) for x in input('-> ')[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
#
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=' ')
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=' ')


# print('apple' == 'Apple')
# print(ord('a'))
# print(ord('A'))


# from random import randint
#
#
# short = 8
# long = 16
# min_ASCII = 33
# max_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(short, long)
#     result = ''
#     for i in range(rand_len):
#         result += chr(randint(min_ASCII, max_ASCII))
#     return result
#
#
# print('случайный пароль:', random_password())


# s = 'hello, WORLD! I am learning Python'
# print(s.capitalize())  # первый символ в строке в верхнем регистре, остальные в нижнем
# print(s.lower())  # все символы в нижнем регистре
# print(s.upper())  # все символы в верхнем регистре
# print(s.swapcase())  # инверсия регистров символов
# print(s.title())  # первая буква каждого слова в верхнем регистре
# print(s.count('h', 1, -4))  # подсчет кол-ва заданных символов
# print(s.lower().count('i'))
# print(s.find('Python'))  # возвращает первый индекс подстроки
# print(s.find('h', 1, -4))  # если вхождений не найдено, то возвращается '-1'
# print(s.rfind('h', 1, -4))  # возвращает последний индекс подстроки. если вхождений не найдено возвращает '-1'
# print(s.index('Python'))  # возвращает индекс подстроки
# print(s.index('h', 1, -4))  # если вхождений не найдено, возвращает исключение ValueError
# print(s.startswith('he'))  # возвращает True если строка начинается с заданной подстроки
# print(s.startswith('I am', 14))
# print(s.endswith('n'))  # возвращает True если строка заканчивается заданной подстрокой
# print('abc123'.isalnum())  # проверяет, состоит ли строка из букв и/или цифр
# print('ABCsvg'.isalpha())  # проверяет, состоит ли строка только из букв
# print('5634'.isdigit())  # проверяет, состоит ли строка только из цифр
# print('abc'.islower())  # проверяет, состоит ли строка из букв в нижнем регистре, допуск наличия любых других символов
# print('Abc'.isupper())  # проверяет, состоит ли строка из букв в верхнем регистре, допуск наличия других символов
# print('py'.center(10))  # выравнивает строку по центру
# print('py'.center(10, '-'))
# print('   py'.lstrip())  # удаляет пробелы слева
# print('py   '.rsplit())  # удаляет пробелы справа
# print('  py   '.strip())  # удаляет пробелы и слева и справа
# print('https://www.python.org'.lstrip('htps:/'))
# print(str1.replase('N', 'P'))  # поиск и замена

# st = '-'
# se = ('a', 'b', 'c')
# print(st.join(se))  # объединяет итерируемую последовательность в строку
# print('..'.join(['1', '99']))
# print(':'.join('abc'))

# print('строка разделенная пробелами'.split())  # строку преобразовывает в список по символу разделителю
# print('www.python.org.ru'.split('.', 2))
# print('www.python.org.ru'.rsplit('.'))
# print('www.python.org.ru'.rsplit('.', 2))

# st = 'один два'
# st = 'hello world'
# one = st[:st.find(' ')]
# two = st[st.find(' ') + 1:]
# print(two + ' ' + one)

# st = 'Ников Валерий Анатольевич'
# st = input('введите ФИО: ').split()
# print(st)
# print(f'{st[0]} {st[1][0]}. {st[2][0]}.')

# num = input('введите числа через пробел: ').split()
# print(num)
# num = list(map(int, num))
# print(num)
# print(sum(num))


#  регулярные выражения

import re

# s = 'Я ищу совпадения в 2025 году. И я их найду в 2 счёта.'
# reg = r'\.'
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения
# print(re.search(reg, s))  # месторасположение первого совпадения объекта
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.match(reg, s))  # поиск совпадения только с начала строки
# print(re.split(reg, s))  # список, в котором строка разбита по заданному шаблону
# print(re.sub(reg, '!', s))  # поиск и замена

# print(dir(re))
# reg = r"[205]"
# reg = r"[0-9]"
# reg = r"[6-9]"
# reg = r"[12][0-9][0-9][0-9]"
# reg = r"[А-яЁё]"
# reg = r"[а-яА-ЯЁё]"

# reg = r"[A-Za-z\]\[-]"
# reg = r"[^0-9]"
# reg = r"[0-9]."
# reg = r"[0-9]..."
# reg = r"\d"
# reg = r"\D"
# reg = r"\s"
# reg = r"\S"
# reg = r"\S"
# reg = r"\w"
# reg = r"\W"
# reg = r"\AЯ ищу"
# reg = r"Wor_ld\Z"
# reg = r"сов\B"
# reg = r"\w+"
# reg = r"\d+"
# reg = r"20*"
# print(re.findall(reg, s))

# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1 повторения


# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T18:55. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))

# d = "Цифры: 7, +17, -24, 0013, 0.3"
# reg = r"[+-]?[\d.]+"
# print(re.findall(reg, d))

# d = "05-03-1987  # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s\s#.+", "", d))
#
# print(re.sub("-", ".", d))
#
# print("Дата рождения:", re.sub(r"\s\s#.+", "", re.sub("-", ".", d)))

# st = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w+\s*\w+\.?\w?\.?"
# # reg = r"\w+\s*=[\w\s.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))
#
# reg1 = r";\s"
# print(re.split(reg1, st))

# st = "12 сентября 2025 года  456789456"
# # reg = r"\d{4}"
# reg = r"\d{2,4}"
# # reg = r"\d{4,}"
# print(re.findall(reg, st))

# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))


# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel-lo] Wor_ld 2000000000000000000"
# # reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))


# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9_-]{3,16}$", login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("P0012yt"))


# text = "<body>Примет жадного совпадения соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?


# st = "Петр, Ольга и Виталий отлично учатся!"
# reg = r"Петр|Ольга|Виталий|Наталья"
# print(re.findall(reg, st))

# st = "int = 4, float = 4.0f, double = 8.0, int"
# # reg = r"\w+\s*=\s*\d[.\w+]*"
# # reg = r"int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*"
# # reg = r"(?:int|float)\s*=\s*\d[.\w+]*"
# reg = r"((int|float)\s*=\s*(\d[.\w+]*))"
# print(re.findall(reg, st))

# d = "Word2016, PS6, AI5"
# # reg = r"([A-Za-z]+)\d+"
# reg = r"[A-Za-z]+(\d+)"
# print(re.findall(reg, d))
# print(re.search(reg, d))


# st = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, st))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта"
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group(1))
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])

# s = 'Самолет прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025.'
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = 'yandex.com and yandex.ry'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))


# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = 'hello world'
# print(re.findall(r'\w+', text, re.DEBUG))

# text = 'helLo worLd'
# reg = 'l'
# print(re.findall(reg, text, re.IGNORECASE))

# text = '''
# one
# two
# '''
#
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, re.DOTALL))
#
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))

# print(re.findall('''
# [a-z.-]+  # part 1
# @     # @
# [a-z.]+   # part 2
# ''', 'test@mail.ru', re.VERBOSE))

# text = '''Python,
# python,
# PYTHON'''
# reg = '(?im)^python'
# print(re.findall(reg, text))


# рекурсия

# def elevator(n):
#     if n == 0:  # базовый случай
#         print('вы в подвале')
#         return
#     print('=>', n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input('на каком этаже вы находитесь: '))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, '=> lst[0]:', lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, '=> lst[0]:', lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):  # 2, 10
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]  # '2'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # to_str(25 // 10, 10) + '4' + '5'
#
#
# print(to_str(254, 10))

# def to_str(n, base):  # 15, 16
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]  # 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 'F' + 'E'
#
#
# print(to_str(254, 16))


# names = ['Adam', ['Bob', ['Chet', 'cat'], 'Bard', 'berd'], 'Alex', ['bea', 'Bill'], 'Ann']
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))


# names = ['Adam', ['Bob', ['Chet', 'cat'], 'Bard', 'berd'], 'Alex', ['bea', 'Bill'], 'Ann']
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


#  файлы

# f = open('text.txt', 'r')
# print(f)
# print(*f)
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)


# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()


# f = open('xyz.txt', 'w')
# f.write('This is line1.\nThis is line2.\nThis is line3.\n')
# f.close()


# f = open('xyz.txt')
# # print(f.read())
#
# # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
#
# print(f.readlines())
# f.close()


# f = open('xyz.txt')
# # for line in f:
# #     print(line)
# #
# # f.close()

# count = 0
# f = open('xyz.txt')
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print(count)

# f = open('xyz.txt')
# print(len(f.readlines()))
# f.close()


# f = open('test.txt', 'w')
# f.write('Hello\nWorld\n')
# f.close()
#
# f = open('test.txt', 'a')
# f.write('New text')
# f.close()

# lines = ['This is line1.', 'This is line2.', 'This is line3.']
#
# f = open('test1.txt', 'a')
# f.writelines(lines)
# f.close()


# file = 'text2.txt'
# f = open(file, 'w')
# f.write('Замените строку в текстовом файле;\n'
#         'изменить строку в списке;\n'
#         'записать список в файл;\n')
# f.close()
#
# f = open(file)
# data = f.readlines()
# print(data)
# data[1] = 'hello world!\n'
# print(data)
# f.close()
#
# f = open(file, 'w')
# f.writelines(data)
# f.close()


# f = open('text3.txt', 'w')
# lst = [str(i) for i in range(1, 100, 3)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open('text.txt')
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию условного курсора в файле
# print(f.seek(1))  # перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()


# f = open('text.txt', 'w+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()

# f = open('text.txt', 'a+')
# print(f.read())
# f.close()


# with open('text.txt', 'w') as f:
#     print(f.write('0123456789'))
# print(f.closed)


# lst = [4.5, 6.4, 7.8, 3.99, 2.71]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# with open('res.txt', 'w') as f:
#     f.write(get_line(lst))
#
# print('файл записан')


# with open('res.txt') as f:
#     nums = f.read()
#
# print(nums)
#
# lst = list(map(float, nums.split()))
# print(lst)
# print(sum(lst)


# file_name = 'long.txt'
#
# with open(file_name, 'w') as f:
#     f.write('файл - именованная область данных на носите информации, используемая как базовый объект'
#             ' с данными в операционных системах.')
#
#
# def longest_world(file):
#     with open(file) as text:
#         lst = text.read().split()
#         print(lst)
#         max_length = len(max(lst, key=len))
#         print(max_length)
#         res = [word for word in lst if len(word) == max_length]
#
#         return res[0] if len(res) == 1 else res
#
#
# print(longest_world(file_name))


# t = 'Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n'
# with open('one.txt', 'w') as f:
#     f.write(t)
#
# with open('one.txt') as fr, open('two.txt', 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)


# модули OS и OS.PATH

# import os

# print(os.getcwd())  # путь к текущей директории
# print(os.listdir())  # список директорий и файлов
# print(os.listdir('.venv'))
# os.mkdir('folder')  # создание папки
# os.rmdir('folder')  # удаление папки
# os.makedirs('nested1/nested2/nested3')  # создание папки с промежуточными директориями
# os.remove('xyz.txt')  # удалить файл
# os.rename('file_name', 'file_name.txt')  # переименование файла или перемещение в существующую директорию
# os.rename('file_name.txt', 'new_file.txt')
# os.rename('new_file.txt', 'nested1/new_file.txt')
# os.renames('two.txt', 'test/two.txt')  # переименование файла, может создать директории, которых не существует

# for root, dirs, files in os.walk('nested1', topdown=False):
#     print('root:', root)
#     print('\tdirs:', dirs)
#     print('\t\tfiles:', files)


# def remove(root):
#     for root, dirs, files in os.walk(root):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена.')
#
#
# remove('nested1')


# import os.path  # import os
#
# print(os.path.split(r'E:\python\nested1\nested2\nested3\text3.txt'))  # разбивает путь на 2 элемента по последнему '\'
# print(os.path.join(r'E:\python', 'nested1', 'nested2', 'nested3', 'text3.txt'))  # собирает путь из элементов
# print(os.path.exists(r'E:\python\nested1\nested2\nested3\text3.txt'))  # проверяет существование пути (папка, файл)
# print(os.path.isfile(r'E:\python\nested1\nested2\nested3\text3.txt'))  # является ли документ файлом
# print(os.path.isdir(r'E:\python\nested1\nested2\nested3\text3.txt'))  # является ли документ папкой


# with open('text1.txt', 'w+') as f:
#     print(f.write('hello'))
#     f.seek(0)
#     data = f.read()
#     data += '!'
#     f.seek(0)
#     f.write(data)

# s = 'hello\nworld'
# print(len(s))

# print('данные в локальном репозитории')

# print('код созданный на новом устройстве')

# import os
#
# dirs = [r'work\F1', r'work\F2\F21']
#
# # for d in dirs:
# #     os.makedirs(d)
#
# files = {
#     'work': ['w.txt'],
#     r'work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# # for key, value in files.items():
# #     for file in value:
# #         file_path = os.path.join(key, file)
# #         open(file_path, 'w').close()
#
# file_with_text = [r'work\w.txt', r'work\F1\f12.txt', r'work\F2\f21\f211.txt']
#
#
# # for file in file_with_text:
# #     with open(file, 'w') as f:
# #         f.write(f'Некоторый текст для файла {file}')
#
#
# def print_tree(topdown):
#     print(f'обход work {'сверху вниз' if topdown else 'снизу вверх'}')
#     for root, directory, file in os.walk('work', topdown):
#         print(root)
#         print(directory)
#         print(file)
#     print('-' * 50)
#
#
# print_tree(False)
# print_tree(True)

# import os
# import time
#
# path = 'main.py'
# print(os.path.getsize(path))  # размер файла
# print(os.path.getatime(path))  # время последнего доступа к файлу (в секундах)
# print(os.path.getmtime(path))  # время последнего изменения файла
# print(os.path.getctime(path))  # время создания файла
#
# size = os.path.getsize(path)
# a_time = os.path.getatime(path)
# m_time = os.path.getmtime(path)
# c_time = os.path.getctime(path)
#
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(a_time)))
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(m_time)))
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(c_time)))
# print(size // 1024)

# import os
#
# file_path = r'C:\python\nested1\new_file.txt'
#
# if os.path.exists(file_path):
#     dih, name = os.path.split(file_path)
#     time = os.path.getatime(file_path)
#     print(f'{name} ({dih}) - {time}')
# else:
#     print(f'файл {file_path} не существует')

# import os
#
# dir_name = 'work'
#
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     # print(p)
#     if os.path.isfile(p):
#         print(f'{obj} - file - {os.path.getsize(p)} bytes')
#     if os.path.isdir(p):
#         print(f'{obj} - dir')

import os
#
# dir_name = r'E:work\F1'
#
# for file in os.listdir(dir_name):
#     dir_file = dir_name + '\\' + file
#     if os.path.isfile(dir_file):
#         with open(dir_file) as fil:
#             test = fil.readlines()
#             print(test)

# import os

# file_path = 'work'
#
#
# obj = os.listdir(file_path)
# print(obj)


# if os.path.exists(file_path):
#     dih, name = os.path.split(file_path)
#     time = os.path.getatime(file_path)
#     print(f'{name} ({dih}) - {time}')
# else:
#     print(f'файл {file_path} не существует')

import os

dir_name = 'work'
a_name = r'E:\python\work\F1'
b_name = r'E:\python\work\F2\F21'

objs = os.listdir(dir_name)
obi = os.listdir(a_name)
oba = os.listdir(b_name)
su = obi + objs + oba
# print(su)

for obj in su:
    p = os.path.join(dir_name, obj)
    c = os.path.join(a_name, obj)
    z = os.path.join(b_name, obj)

    if os.path.isfile(p):
        if os.path.getsize(p) > 0:
            print(f'{p} - {os.path.getsize(p)} bytes')
    if os.path.isfile(c):
        if os.path.getsize(c) > 0:
            print(f'{c} - {os.path.getsize(c)} bytes')
    if os.path.isfile(z):
        if os.path.getsize(z) > 0:
            print(f'{z} - {os.path.getsize(z)} bytes')
































































































