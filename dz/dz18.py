file = 'text2.txt'
with open(file, 'w') as f:
    f.write('замена строки в текстовом файле;\n'
            'изменить строку в списке;\n'
            'записать список в файл;\n')


with open(file) as f:
    re = f.readlines()

pos1 = int(input('pos1 = ')) - 1
pos2 = int(input('pos2 = ')) - 1

if 0 <= pos1 < len(re) and 0 <= pos2 < len(re):
    re[pos1], re[pos2] = re[pos2], re[pos1]
else:
    print('такой строки нет')
print(re)

with open(file, 'w') as f:
    f.writelines(re)




