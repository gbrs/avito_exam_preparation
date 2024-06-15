import sys

lst = [[float(x) for x in line.split()] for line in sys.stdin]


# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [print(*i) for i in lst]

n = len(lst)

answer = [[0] * n for _ in range(n)]
# [print(*i) for i in answer]


for i in range(n):
    for j in range(n):
        answer[j][n - 1 - i] = lst[i][j]

[print(*i) for i in answer]



