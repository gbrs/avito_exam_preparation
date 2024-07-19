from math import factorial as f


def calc(n):
    return f(100) / f(100 - n) / f(n) * (1 / 6)**n * (5 / 6)**(100 - n)


p = 0

for i in range(10, 101):
    p += calc(i)

print(calc(11), p)
print(calc(11) / p)
