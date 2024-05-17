'''
a = 1
b = 2
c = 3
d = 4
k = 0
m = 2
N = 1_000
'''

a, b, c, d = map(int, input().split())
k, m = map(int, input().split())
N = int(input())

step = (m - k) / N
integral = 0

for i in range(N):
    x = k + step * i
    integral += (a * x**3 + b * x**2 + c * x + d) * step

print(round(integral, 3))

'''
1 2 3 4
0 2
1000
'''