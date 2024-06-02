from scipy.integrate import dblquad


foo = lambda y, x: x**2 / y**2
low = lambda x: 1 / x
high = lambda x: x


print(dblquad(foo, 1, 2, low, high))


