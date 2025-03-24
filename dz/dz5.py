a = [int(input('-> ')) for i in range(int(input('n = ')))]
print(a)
res = 0
for i in range(len(a)):
    if a[i] < 0:
        res += a[i]
print(res)