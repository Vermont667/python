n = int(input('введите число: '))
res = 1
while n:
    n = int(input('введите число: '))
    if n == 0:
        break
    res *= n
print('произведение:', res)