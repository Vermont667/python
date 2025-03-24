c = int(input('количество студентов: '))
a = {input('введите имя: '): int(input('балл: ')) for i in range(c)}
sr = round(sum(a.values()) / c)
print('средний балл: ', sr, '\nстуденты с балом выше среднего: ')
for i in a:
    if a[i] > sr:
        print(i)





