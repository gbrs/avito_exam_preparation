a = [
    [1]
]

c = [
    [3]
]

if len(a[0]) == len(c):
    ans = [[0] * len(c[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(c[0])):
            val = 0
            for k in range(len(c)):
                val += a[i][k] * c[k][j]
            ans[i][j] = val
    [print(*i) for i in ans]
else:
    print('невозможно перемножить')


'''
a = [
    [1, 2, 3],
    [1, 0, -1]
]

c = [
    [3, 4, 5],
    [6, 0, -2],
    [7, 1, 8]
]
36 7 25
-4 3 -3

a = [
    [1, 3],
    [2, 1],
    [4, -3]
]

c = [
    [3, 2, 1],
    [-2, 1, 4]
]
-3 5 13
4 5 6
18 5 -8
'''