def foo(x):
    return x**2 + 3 * x - 4


a = -5
b = 2
flag = True

foo_a = foo(a)
foo_b = foo(b)

if foo_b <= 0 <= foo_a:
    low = b
    high = a
elif foo_b >= 0 >= foo_a:
    low = a
    high = b
else:
    flag = False
    print('Не могу найти корней в указанном диапазоне')

if flag:
    for _ in range(100):
        middle = (low + high) / 2
        if foo(middle) < 0:
            low = middle
        else:
            high = middle

        print(high)
