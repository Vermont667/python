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
# import os
# name = 'admin'
# print(name)
# import json
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
from itertools import count
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

from car.electro_car import ElectroCar

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

# import os
#
# dir_name = 'work'
# a_name = r'E:\python\work\F1'
# b_name = r'E:\python\work\F2\F21'
#
# objs = os.listdir(dir_name)
# obi = os.listdir(a_name)
# oba = os.listdir(b_name)
# su = obi + objs + oba
# # print(su)
#
# for obj in su:
#     p = os.path.join(dir_name, obj)
#     c = os.path.join(a_name, obj)
#     z = os.path.join(b_name, obj)
#
#     if os.path.isfile(p):
#         if os.path.getsize(p) > 0:
#             print(f'{p} - {os.path.getsize(p)} bytes')
#     if os.path.isfile(c):
#         if os.path.getsize(c) > 0:
#             print(f'{c} - {os.path.getsize(c)} bytes')
#     if os.path.isfile(z):
#         if os.path.getsize(z) > 0:
#             print(f'{z} - {os.path.getsize(z)} bytes')


# import os
#
#
# def info_files(root, folder):
#     for root, dirs, files in os.walk(root):
#         for file in files:
#             file_path = os.path.join(root, file)
#             # print(file_path)
#             file_size = os.path.getsize(file_path)
#             if file_size == 0:
#                 os.renames(file_path, os.path.join(folder, file))
#                 print(f'файл {file} перемещен из папки {root} в папку {folder}')
#             else:
#                 print(f'{file_path} - {file_size} bytes')
#
#
# info_files('work', 'work/empty_files')


# ООП

# class Point:
#     x = 1
#     y = 2
#
#
# p1 = Point()
# Point.x = 100
# print(p1.x)
# print(Point.x)
# print(id(Point))
# print(id(p1))
# p1.x = 100
# p1.y = 50
# print(p1.x, p1.y)
# print(p1.__dict__)
# p2 = Point()
# print(p2.x, p2.y)
# print(p2.__dict__)
# print(Point.__dict__)

# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self):
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.set_coord()
# Point.set_coord(p1)
#
# p2 = Point()
# p2.set_coord()


# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self, x1, y1):
#         self.x = x1
#         self.y = y1
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# Point.set_coord(p1, 10, 20)
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_coord(2, 7)
# print(p2.__dict__)


# class Human:
#     name = 'Name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street house'
#
#     def print_info(self):
#         print(' персональные данные '.center(40, '*'))
#         print(f'имя: {self.name}\nдата рождения: {self.birthday}\nномер телефона: {self.phone}\n'
#               f'страна: {self.country}\nгород: {self.city}\nдомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установили новое имя
#         self.name = name
#
#     def get_name(self):  # получили имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва',
#               'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_name('Юлия')
# h1.print_info()
# print(h1.get_name())


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __del__(self):
#         print('удаление экземпляра\n')
#
#     def print_info(self):
#         print('данные сотрудника:', self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('квалификация сотрудника:', self.skill, '\n')


# p1 = Person('Виктор', 'Резник')
# p1.print_info()
# p1.add_skill(3)
# del p1
#
# p2 = Person('Анна', 'Долгих')
# p2.print_info()
# p2.add_skill(2)


# class Person:
#     count = 0
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         Person.count += 1
#
#     def print_info(self):
#         print('данные сотрудника:', self.name, self.surname)
#
#
# p1 = Person('Виктор', 'Резник')
# p1.print_info()
#
# p2 = Person('Анна', 'Долгих')
# p2.print_info()
#
# print(p1.count)
# print(p2.count)
# print(Person.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('инициализация робота:', self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'выключается!')
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, 'был последним')
#         else:
#             print('работающих роботов осталось:', Robot.k)
#
#     def say_hi(self):
#         print('приветствую! меня зовут:', self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print('численность роботов:', Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print('численность роботов:', Robot.k)
#
# droid3 = Robot('B4-50')
# droid3.say_hi()
# print('численность роботов:', Robot.k)
#
# print('\nздесь роботы могут проделать какую-то работу\n')
# print('роботы проделали свою работу. давайте их выключим\n')
#
# del droid1, droid2, droid3
#
# print('численность роботов:', Robot.k)


# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('координаты должны быть числами')
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print('координат x должна быть числом')
#
#     def set_coord_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print('координат y должна быть числом')
#
#
# p1 = Point(5, 10)
# # p1.z = 20
# # p1.__x = 100
# # p1.__y = 'abc'
# # print(p1.__x, p1.__y)
# p1.set_coord(50, 100)
# print(p1.get_coord())
# p1.set_coord_x(1)
# print(p1.__dict__)
# # p1.__check_value(10)
# # print(Point.__dict__)
# p1._Point__x = 111
# print(p1._Point__x)
# print(p1.__dict__)

# import math
#
#
# class Rectangle:
#
#     def __init__(self, lens=1, wids=1):
#         self.__lens = lens
#         self.__wids = wids
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def get_wids(self):
#         return self.__wids
#
#     def get_lens(self):
#         return self.__lens
#
#     def set_lens(self, lens):
#         if Rectangle.__check_value(lens):
#             self.__lens = lens
#
#     def set_wids(self, wids):
#         if Rectangle.__check_value(wids):
#             self.__wids = wids
#
#     def get_area(self):
#         return self.__lens * self.__wids
#
#     def get_perimetr(self):
#         return (self.__lens + self.__wids) * 2
#
#     def get_hypotenuse(self):
#         return round(math.sqrt(self.__lens ** 2 + self.__wids ** 2), 2)
#
#     def get_draw(self):
#         print(('*' * self.__wids + '\n') * self.__lens)
#
#
# r1 = Rectangle()
# r1.set_wids(9)
# r1.set_lens(3)
# print('длина прямоугольника:', r1.get_lens())
# print('ширина прямоугольника:', r1.get_wids())
# print('площадь прямоугольника:', r1.get_area())
# print('периметр прямоугольника:', r1.get_perimetr())
# print('гипотенуза прямоугольника:', r1.get_hypotenuse())
# r1.get_draw()

# class Point:
#     __slots__ = ['x', 'y']
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# # p1.z = 20
# # print(p1.x, p1.y, p1.z)
# print(p1.x, p1.y)
# # print(p1.__dict__)


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def __set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print('координата х должна быть числом')
#
#     def __get_coord_x(self):
#         return self.__x
#
#     def __del_coord_x(self):
#         print('удаление свойства')
#         del self.__x
#
#     coordX = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# p1 = Point(5, 10)
# p1.coordX = 20.5
# print(p1.coordX)
# del p1.coordX
# print(p1.__dict__)

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     @property    # стоит перед сеттером и делитером
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print('координата х должна быть числом')
#
#     @x.deleter
#     def x(self):
#         print('удаление свойства')
#         del self.__x
#
#     # coordX = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# p1 = Point(5, 10)
# p1.x = 50  # вызов сеттера
# print(p1.x)  # вызов геттера
# del p1.x
# print(p1.__dict__)

# class Person:
#
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.__old = old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person('Irina', 26)
# print(p1.__dict__)
# p1.name = 'Igor'
# p1.old = 31
# print(p1.name)
# print(p1.old)
# del p1.name
# print(p1.__dict__)

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())
# # print(p1.get_count())

# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))
#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a  # 3
#         if b > mx:  # 5 > 3
#             mx = b  # 5
#         if c > mx:  # 7 > 5
#             mx = c  # 7
#         if d > mx:  # 9 > 7
#             mx = d  # 9
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#         return mn
#
#     # @staticmethod
#     # def average(*args):
#     #     return sum(args) / len(args)
#
#     @staticmethod
#     def average(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#
#
# print(Numbers.max(3, 5, 7, 9))
# print(Numbers.min(3, 5, 7, 9))
# print(Numbers.average(3, 5, 7, 9))
# print(Numbers.factorial(5))


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#
# # string_date = '23.10.2025'
# # day, month, year = map(int, string_date.split('.'))  # 23 10 2025
# # date = Date(day, month, year)
# date = Date.from_string('23.10.2025')
# print(date.string_to_db())
#
# date2 = Date.from_string('30.12.2024')
# print(date2.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f'Счёт#{self.num} принадлежащий {self.surname} был открыт!')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счёт#{self.num} принадлежащий {self.surname} был закрыт!')
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, self.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print('Информация о счёте:')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} успешно начислено!')
#         self.print_balance()
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.edit_owner('Дюна')
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()  # ['Волков2', 'Иг@@@орь', 'Николаевич!']
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#         letter = ''.join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             # print(s.strip(letter))
#             if len(s.strip(letter)) != 0:
#                 raise TypeError('В ФИО можно использовать только буквы и дефис')
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError('возраст должен быть числом в диапазоне от 14 до 100 лет')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(year)
#         self.__old = year
#
#
# p1 = UserData('Волков Игорь Николаевич', 26, '1234 4567890', 80.8)
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#         print('инициализатор класса Prop')
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print('переопределенный инициализатор Line')
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f'Рисование линий: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if not isinstance(w, int):
#             raise TypeError('ширина должна быть числом')
#         elif not w > 0:
#             raise ValueError('ширина должна быть положительной')
#         else:
#             self.__width = w
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if isinstance(h, int) and h > 0:
#             self.__height = h
#         else:
#             raise ValueError('высота должна быть положительной')
#
#     def get_area(self):
#         print(f'площадь {self.color} прямоугольника: ', end='')
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.width = 8
# rect.color = 'red'
# print(rect.get_area())


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'прямоугольник:\nширина: {self.width}\nвысота: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print('фон:', self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, r_width, r_type, r_color):
#         super().__init__(width, height)
#         self.r_width = r_width
#         self.r_type = r_type
#         self.r_color = r_color
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'ширина рамки: {self.r_width}\nтип рамки: {self.r_type}\nцвет рамки: {self.r_color}')
#
#
# shape1 = RectFon(400, 200, 'yellow')
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, '1px', 'solid', 'blue')
# shape2.show_rect()

# from math import sqrt
#
#
# class Pair:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def edit_a(self, a):
#         self.a = a
#
#     def edit_b(self, b):
#         self.b = b
#
#     def summ(self):
#         return self.a + self.b
#
#     def mult(self):
#         return self.a * self.b
#
#
# class RightTriangle(Pair):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         self.c = self.hypotenuse()
#
#     def hypotenuse(self):
#         hypo = round(sqrt(self.a ** 2 + self.b ** 2), 2)
#         print(f'гипотенуза: {hypo}')
#         return hypo
#
#     def print_info(self):
#         print(f'прямоугольный треугольник: ({self.a}, {self.b}, {self.c})')
#
#     def square(self):
#         s = 0.5 * self.mult()
#         print(f'площадь: {s}')
#
#     def edit_a(self, a):
#         super().edit_a(a)
#         self.c = self.hypotenuse()
#
#     def edit_b(self, b):
#         super().edit_b(b)
#         self.c = self.hypotenuse()
#
#
# tr = RightTriangle(5, 8)
# tr.print_info()
# tr.square()
# print()
# print(f'сумма: {tr.summ()}')
# print(f'произведение: {tr.mult()}')
# print()
# tr.edit_a(10)
# tr.edit_b(20)
# print(f'сумма: {tr.summ()}')
# print(f'произведение: {tr.mult()}')
# tr.square()


# class Vector(list):
#     def __str__(self):
#         return ' '.join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))


# перегрузка методов


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x=None, y=None):
#         if y is None:
#             self.x = x
#         elif x is None:
#             self.y = y
#         else:
#             self.x = x
#             self.y = y
#
#
# p1 = Point(5, 7)
# print(p1.__dict__)
# p1.set_coord(20, 30)
# print(p1.__dict__)
# p1.set_coord(50)
# print(p1.__dict__)
# p1.set_coord(y=100)
# print(p1.__dict__)


# абстрактные методы


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError('в дочернем классе должен быть определен метод draw()')
#
#
# class Line(Prop):
#
#     def draw(self):
#         print(f'Рисование линий: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Rect(Prop):
#
#     def draw(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Ellipse(Prop):
#     ...
#
#     # def draw(self):
#     #     print(f'Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 20)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(70, 70), Point(90, 90)))
#
# for f in figs:
#     f.draw()

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print('нарисовал шахматную доску')
#
#     @abstractmethod
#     def move(self):
#         print('метод move() в базовом классе')
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print('ферзь перемещен на e2e4')
#
#
# q = Queen()
# q.draw()
# q.move()

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self.width = self.length = width
#             else:
#                 self.width = width
#                 self.length = length
#         else:
#             self.radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError('в дочернем классе должен быть определен метод calc_area()')
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self.width * self.length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self.radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = 'RUB'
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=' ')
#
#     def print_info(self):
#         self.print_value()
#         print(f' = {self.convert_to_rub():.2f} {Currency.suffix}')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end='')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end='')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print('*' * 50)
# for elem in d:
#     elem.print_info()
# print('*' * 50)
# for elem in e:
#     elem.print_info()

# интерфейс

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('Child Class')
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('GrandChild Class')
#
#
# gc = GrandChild()
# gc.display1()
# gc.display2()


# вложенные классы

# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print('Name', self.name)
#
#
# outer = Color()
# outer.show()
# print(outer.name)
# # print(outer.lg.name)
# # outer.lg.display()
# g = outer.lg
# g.display()

# class Intern:
#     def __init__(self):
#         self.name = 'Дмитрий'
#
#     def display(self):
#         print('name', self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = Intern()
#         # self.head = self.Head()
#
#     def show(self):
#         print('Name', self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Александр'
#
#         def display(self):
#             print('name', self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# # d2 = outer.head
# d2 = Employee().Head()
# d1.display()
# d2.display()

# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('наружный класс')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print('промежуточный класс')
#
#         class InnerClass:
#             def show(self):
#                 print('вложенный класс')
#
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = 'PC001'
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i9'
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('in base class')
#
#     class Inner:
#         def display1(self):
#             print('inner of base class')
#
#
# class SubClass(Base):
#     def __init__(self):
#         print('in SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('inner of SubClass')
#
#
# a = SubClass()
# # a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is barking')
#
#
# dog = Dog('Buddy')
# dog.sleep()
# dog.play()
# dog.bark()

# class A:
#     def __init__(self):
#         print('инициализатор класса A')
#
#
# class AA:
#     def __init__(self):
#         print('инициализатор класса AA')
#
#
# class B(A):
#     def __init__(self):
#         print('инициализатор класса B')
#
#
# class C(AA):
#     def __init__(self):
#         print('инициализатор класса C')
#
#
# class D(B, C):
#     def __init__(self):
#         print('инициализатор класса D')
#
#
# d = D()
# print(D.mro())
# # print(D.__mro__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Styles:
#     def __init__(self, color='red', width=1):
#         print('инициализатор Styles')
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print('инициализатор Pos')
#         self.sp = sp
#         self.ep = ep
#         # Styles.__init__(self, *args)
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f'рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()


# Миксины

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='log_file.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='log.txt')
#
#
# subclass = MySubClass()
# subclass.display('эта строка будет печататься и записываться в файл')

# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print('init Goods')
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('init MixinLog')
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар был продан в 15:20')
#
#
# class Notebook(Goods, MixinLog):
#     ...
#
#
# n = Notebook('HP', 1.5, 35000)
# n.print_info()
# n.save_sell_log()


# Перегрузка операторов

# Число секунд в одном дне: 24 * 60 * 60 = 86400

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError('секунды должны быть целым числом')
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('правый операнд должен быть типом данных Clock')
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('правый операнд должен быть типом данных Clock')
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#         return self.sec == other.sec
#
#
# c1 = Clock(100)
# c2 = Clock(100)
# # c4 = Clock(300)
# # c3 = c1 + c2 + c4
# # c1 += c2
# print(c1.get_format_time())
# print(c2.get_format_time())
# # print(c4.get_format_time())
# # print(c3.get_format_time())
# if c1 == c2:
#     print('время одинаковое')
# else:
#     print('время разное')


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError('неверный индекс')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('индекс должен быть целым положительным числом')
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError('индекс должен быть целым числом')
#         del self.marks[key]
#
#
# s1 = Student('Сергей', 5, 5, 3, 4, 5)
# print(s1[1])
# s1[10] = 4
# del s1[2]
# print(s1.marks)


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError('секунды должны быть целым числом')
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('ключ должен быть строкой')
#         if item == 'hour':
#             return (self.sec // 3600) % 24
#         if item == 'min':
#             return (self.sec // 60) % 60
#         if item == 'sec':
#             return self.sec % 60
#         return 'неверный ключ'
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError('ключ должен быть строкой')
#         if not isinstance(value, int):
#             raise ValueError('значение должно быть целым числом')
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == 'hour':
#             self.sec = s + 60 * m + value * 3600
#         if key == 'min':
#             self.sec = s + 60 * value + h * 3600
#         if key == 'sec':
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(8000)
# print(c1.get_format_time())
# print(c1['hour'], c1['min'], c1['sec'])
# c1['hour'] = 10
# print(c1.get_format_time())
# c1['min'] = 62
# print(c1.get_format_time())
# c1['sec'] = 30
# print(c1.get_format_time())


# class Point:
#     def __init__(self, x):
#         self.x = x
#
#     # def __str__(self):
#     #     return f'{self.x}'
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.x}'
#
#
# p1 = Point(5)
# print(p1)

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == 'M':
#             return f'{self.name} is good boy!!!'
#         elif self.pol == 'F':
#             return f'{self.name} is good girl!!!'
#         else:
#             return f'{self.name} is good kitty!!!'
#
#     def __repr__(self):
#         return f'Cat(name="{self.name}", age={self.age}, pol="{self.pol}"'
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat('No name', 0, choice(['M', 'F'])) for _ in range(1, randint(2, 6))]
#         else:
#             raise TypeError('Types are not supported!')
#
#
# cat1 = Cat('Tom', 4, 'M')
# cat2 = Cat('Elsa', 5, 'F')
# # cat3 = Cat('Murzik', 5, 'M')
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)


# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(1, 2, 3)
# print(len(p))

# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(1, 2)
# print(p1.length)
# p1.length = 10
# print(p1.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2D(1, 2)
# print('pt1 =', pt1.__sizeof__())
# print('pt2 =', pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# p = Point(1, 2)
# p3 = Point3D(10, 20, 30)
# p3.z = 30
# print(p3.z)


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text('python')
# print(t1.total(35))
# print(t2.total(35))

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cat(Animal):
#     def info(self):
#         print(f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}')
#
#     def make_sound(self):
#         print(f'{self.name} мяукает.')
#
#
# class Dog(Animal):
#     def info(self):
#         print(f'Я собака. Меня зовут {self.name}. Мой возраст {self.age}')
#
#     def make_sound(self):
#         print(f'{self.name} гавкает.')
#
#
# cat = Cat('Пушок', 2.5)
# dog = Dog('Мухтар', 4)
#
# for animal in cat, dog:
#     animal.info()
#     animal.make_sound()


# Функторы

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()

# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError('аргумент должен быть строкой')
#
#         return string.strip(chars)
#     return wrap
#
#
# s1 = string_strip('?:!.; ')
# print(s1('   Hello World!   '))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('аргумент должен быть строкой')
#
#         return args[0].strip(self.chars)
#
#
# s1 = string_strip('?:!.; ')
# print(s1('   Hello World!   '))


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self):
#         print('перед вызовом функции')
#         self.func()
#         print('после вызова функции')
#
#
# @MyDecorator
# def func():
#     print('text')
#
#
# func()


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         # print('перед вызовом функции')
#         res = self.func(a, b)
#         # print('после вызова функции')
#         return f'перед вызовом функции\n{res}\nпосле вызова функции'
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# class Power:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def mult(a, b):
#     return a * b
#
#
# print(mult(2, 3))


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, *args, **kwargs):
#         res = self.func(*args, **kwargs)
#         return f'перед вызовом функции\n{res}\nпосле вызова функции'
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func1(2, 5, 2))


# class MyDecorator:
#     def __init__(self, arg):  # 'test2'
#         self.name = arg
#
#     def __call__(self, fn):  # func
#         def wrap(*args, **kwargs):  # 2, 5
#             res = fn(*args, **kwargs)
#
#             return f'перед вызовом функции\n{self.name}\n{res}\nпосле вызова функции'
#         return wrap
#
#
# @MyDecorator('test2')
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             res = fn(*args, **kwargs)
#
#             return f'result : {res ** self.arg}'
#
#         return wrap
#
#
# @Power(2)
# def func(a, b):
#     return a * b
#
#
# print(func(2, 2))


# Декоратор методов

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print('*' * 20)
#         fn(*args, **kwargs)
#         print('*' * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person('Виталий', 'Карасев')
# p1.info()


# декораторы классов

# def decorator(cls):
#     class Wrapper(cls):
#         def sample(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print('init ActualClass')
#
#     def method_in_class(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.method_in_class(4))
# print(obj.sample(4))


# метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# print(lst, lst.get_length())


# Создание модулей

# import geometry.rect
# import geometry.sq
# import geometry.trian

# from geometry import *

# from geometry import rect, sq, trian


# if __name__ == '__main__':
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())


# def ran():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     ran()

# from car.electro_car import ElectroCar
#
#
# if __name__ == '__main__':
#     e_car = ElectroCar('Tesla', 'T', 2018, 99000, 100)
#     e_car.show_car()
#     e_car.description_battery()


# упаковка (Сериализация) и распаковка (Десериализация) данных

import pickle


# filename = 'basket.txt'
#
# shop = {
#     'фрукты': ['яблоко', 'груша'],
#     'овощи': ('морковь', 'лук'),
#     'бюджет': 1000
# }
#
# with open(filename, 'wb') as fh:
#     pickle.dump(shop, fh)
#
# with open(filename, 'rb') as fh:
#     shop_list = pickle.load(fh)
#
# print(shop_list)


# class Test:
#     num = 25
#     string = 'Привет'
#     lst = [1, 2, 3]
#     dictionary = {'first': 1, 'second': 2}
#
#     def __str__(self):
#         return f'Число: {Test.num}\nстрока: {Test.string}\nсписок: {Test.lst}\nсловарь: {Test.dictionary}'
#
#
# obj = Test()
# # print(obj)
#
# obj1 = pickle.dumps(obj)
# print(f'Сериализация в строку:\n{obj1}\n')
#
# obj2 = pickle.loads(obj1)
# print(f'Десериализация из строки:\n{obj2}\n')


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(2)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# print(item1)
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3)
# print(item3.__dict__)

# import json
#
#
# data = {
#     'name': 'Olga',
#     'age': 35,
#     '20': None,
#     'True': False,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'firstname': 'Alice',
#             'age': 6
#         }
#     ]
# }
#
# # with open('data_file.json', 'w') as fw:
# #     json.dump(data, fw, indent=4)
# #
# #
# # with open('data_file.json', 'r') as fw:
# #     data1 = json.load(fw)
# #
# # print(data1)
#
# json_string = json.dumps(data, sort_keys=True)
# print(json_string)
# print(type(json_string))
# data2 = json.loads(json_string)
# print(data2)
# print(type(data2))


# x = {'name': 'Виктор'}
#
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))
#
# a = json.dumps(x)
# print(json.loads(a))
#
#
# with open('data_file.json', 'w') as fw:
#     json.dump(x, fw)
#
# with open('data_file.json', 'r') as fw:
#     data2 = json.load(fw)
#
# print(data2)


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())

# persons = []
# for i in range(5):
#     persons.append(gen_person())
# print(persons)

# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # st = ''
#         # for i in self.marks:
#         #     st += str(i) + ', '
#         # return f'Студент => {self.name}: {st[:-2]}'
#         st = ', '.join(map(str, self.marks))
#         return f'Студент => {self.name}: {st}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def del_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_marks(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def dump_to_json(self):
#         data = {'name': self.name, 'marks': self.marks}
#         with open(self.get_file_name(), 'w') as f:
#             json.dump(data, f)
#
#     def get_file_name(self):
#         return self.name + '.json'
#
#     def load_from_file(self):
#         with open(self.get_file_name(), 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         st = '\n'.join(map(str, self.students))
#         return f'\nГруппа: {self.group}\n{st}'
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(gr1, gr2, index):
#         return gr2.add_student(gr1.remove_student(index))
#
#     def get_file_name(self):
#         return self.group.lower().replace(' ', '-') + '.json'
#
#     def dump_to_json(self):
#         data = [{'name': student.name, 'marks': student.marks} for student in self.students]
#         with open(self.get_file_name(), 'w') as f:
#             json.dump(data, f, indent=2)
#
#     def load_for_file(self):
#         with open(self.get_file_name()) as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.del_mark(3)
# # print(st1)
# # st1.edit_marks(2, 4)
# # print(st1)
# # print(st1.average_mark())
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# # st1.dump_to_json()
# # st1.load_from_file()
#
# sts1 = [st1, st2]
# group1 = Group(sts1, 'ГК Python')
# # # print(group1)
# # # print()
# # group1.add_student(st3)
# # # print(group1)
# # # print()
# # group1.remove_student(1)
# # # print(group1)
# sts2 = [st2]
# group2 = Group(sts2, 'ГК Web')
# # print(group1)
# # print(group2)
# Group.change_group(group1, group2, 0)
# print(group1)
# print(group2)
# group2.dump_to_json()
# group2.load_for_file()


# import requests
# import json
#
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
# # print(todos)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
#
# max_users = ' and '.join(users)
# print(max_users)
#
# e = 's' if len(users) > 1 else ''
# print(f'user{e} {max_users} completed {max_complete} TODOs')

# import json
#
#
# class Country:
#     country = {}
#     file_name = 'country.json'
#
#     def add_country(self, count):
#         Country.country.update(count)
#
#     def del_all(self):
#         Country.country.clear()
#
#     def get_country(self, ind):
#         print('-' * 20)
#         print('Страна: ', ind)
#         print('Столица: ', Country.country.get(ind))
#
#     def edit_country(self, index, new_country):
#         self.country[index] = new_country
#
#     def dump_to_json(self):
#         with open(Country.file_name, 'w') as f:
#             json.dump(Country.country, f, indent=2)
#
#     def load_from_file(self):
#         with open(Country.file_name, 'r') as f:
#             print(json.load(f))
#
#     def print_info(self):
#         while True:
#             print('*' * 30)
#             n = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n'
#                           '4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: '))
#             if n == 1:
#                 a = input('Введите название станы: ')
#                 b = input('Введите название столицы страны: ')
#                 self.add_country({a: b})
#                 self.dump_to_json()
#                 print('Файл сохранен')
#             if n == 2:
#                 self.del_all()
#                 c.dump_to_json()
#                 print('Файл сохранен')
#             if n == 3:
#                 g = input('Введите страну: ')
#                 self.get_country(g)
#             if n == 4:
#                 h = input('Введите страну: ')
#                 j = input('Введите новую столицу: ')
#                 self.edit_country(h, j)
#                 self.dump_to_json()
#                 print('Файл сохранен')
#             if n == 5:
#                 print(f'{self.country}')
#             elif n == 6:
#                 print('Завершение работы')
#                 break
#
#
# c = Country()
#
# c.print_info()

# import csv

# with open('data.csv') as f:
#     file_reader = csv.reader(f, delimiter=';')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {', '.join(row)}')
#         else:
#             print(f'\t{row[0]} - {row[1]}. Родился в {row[2]} году.')
#         count += 1
#     print(f'Всего в файле {count} строки.')

# with open('data.csv') as f:
#     fields = ['Имя', "Профессия", "Год рождения"]
#     file_reader = csv.DictReader(f, delimiter=';', fieldnames=fields)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {', '.join(row)}')
#         print(f'\t{row['Имя']} - {row["Профессия"]}. Родился в {row["Год рождения"]} году.')
#         count += 1
#     print(f'Всего в файле {count} строки.')

# import csv

# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open('sw_data.csv', 'r') as f:
#     print(f.read())

# import csv

# with open('stud.csv', 'w') as f:
#     names = ['Имя', "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": 6})
#     file_writer.writerow({"Имя": "Маша", "Возраст": 15})
#     file_writer.writerow({"Имя": "Вова", "Возраст": 14})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict_writer.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=data[0].keys())
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# import sqlite3


# con = sqlite3.connect('profile.db')
# cur = con.cursor()
#
# cur.execute('''''')
# con.close()

# with sqlite3.connect('profile.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date BLOB
#     )''')
#     cur.execute('DROP TABLE users')


# import sqlite3
#
#
# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
# cur.execute('''
# CREATE TABLE IF NOT EXISTS person(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# phone BLOB NOT NULL DEFAULT '+79090000000',
# age INTEGER CHECK(age > 0 AND age < 100),
# email TEXT UNIQUE
# )
# ''')

# cur.execute('''
# ALTER TABLE person
# RENAME TO person_table;
# ''')

# cur.execute('''
# ALTER TABLE person_table
# ADD COLUMN address TEXT
# ''')

# cur.execute('''
# ALTER TABLE person_table
# RENAME COLUMN address TO home_address
# ''')

# cur.execute('''
# ALTER TABLE person_table  # изменения в существующей таблице
# DROP COLUMN home_address   # удаление столбца
# ''')

# cur.execute('''
# DROP TABLE person_table  # удаление таблицы
# ''')


# import sqlite3
#
#
# with sqlite3.connect('db_3.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     SELECT *
#     FROM T1
#     LIMIT 2, 5
#     ''')
#
#     # for res in cur:
#     #     print(res)
#
#     # res = cur.fetchall()  # вернет всё []
#     # print(res)
#
#     res2 = cur.fetchmany(2)  # вернет указанное кол-во значений []
#     print(res2)
#
#     res1 = cur.fetchone()  # вернет одно значение ()
#     print(res1)


# import sqlite3
#
# list_cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000)
# ]
#
# with sqlite3.connect('car.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     )''')
#
#     # for car in list_cars:
#     #     cur.execute('INSERT INTO cars VALUES(NULL, ?, ?)', car)
#
#     # cur.executemany('INSERT INTO cars VALUES(NULL, ?, ?)', list_cars)
#
#     cur.executescript('''
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100
#     ''')

    # cur.execute('INSERT INTO cars VALUES(1, "Renault", 22000)')
    # cur.execute('INSERT INTO cars VALUES(2, "Volvo", 29000)')
    # cur.execute('INSERT INTO cars VALUES(3, "Mercedes", 57000)')
    # cur.execute('INSERT INTO cars VALUES(4, "Bentley", 35000)')
    # cur.execute('INSERT INTO cars VALUES(5, "Audio", 52000)')

# con.commit()
# con.close()
