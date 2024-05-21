from math import sin, cos

def dist(x, a):
    ans = (
        2 * (cos(x) - a * sin(x))**2 +
        (sin(x) - a * cos(x))**2
    )
    return ans

K, N = 0.001, 4
R, M, T = 2, 2000, 1000

for i in range(1, N):
    r, m, t = map(int, input().split())
    if (0.9*R <= r <= 1.1*R) and (0.95*M <= m <= 1.05*M) and (0.98*T <= t <= 1.02*T):
        left = 0.0
        right = 26.0
        for _ in range(100):
            middle = (left + right) / 2
            if dist(middle, i) > 0:
                left = middle
            else:
                right = middle
        print(middle)
        break
else:
    print(-1)



'''
2 2000 1010
3 2100 950
4 2200 1100
'''
