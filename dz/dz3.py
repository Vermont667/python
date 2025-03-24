n = int(input('введите количество копеек от 1 до 99: '))
c = n
if 11 <= n <= 14:
    print(n, 'копеек')
elif 1 <= n <= 99:
    c = c % 10
    if c == 1:
        print(n, 'копейка')
    elif 2 <= c <= 4:
        print(n, 'копейки')
    else:
        print(n, 'копеек')
else:
    print('неверное значение')
