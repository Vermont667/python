s = 0


def para(a, b, c):
    def inner(i, j):
        return i * j
    global s
    s = 2 * (inner(a, b) + (inner(a, c) + (inner(b, c))))
    return s


para(2, 4, 6)
print(s)
para(5, 8, 2)
print(s)
para(1, 6, 8)
print(s)


def para2(a, b, c):
    s = 0

    def inner2(i, j):
        nonlocal s
        s += i * j

    inner2(a, b)
    inner2(a, c)
    inner2(b, c)

    return 2 * s


print(para2(2, 4, 6))
print(para2(5, 8, 2))
print(para2(1, 6, 8))
