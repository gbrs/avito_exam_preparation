lst = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

# lst = [
#     [1, 2, 3, 4, 5],
#     [16, 17, 18, 19, 6],
#     [15, 24, 25, 20, 7],
#     [14, 23, 22, 21, 8],
#     [13, 12, 11, 10, 9]
# ]

N = len(lst)

for k in range(N // 2 + N % 2):
    y = k
    for x in range(k, N - k):
        print(lst[y][x], end=' ')
    x = N - k - 1
    for y in range(k + 1, N - k):
        print(lst[y][x], end=' ')
    y = N - k - 1
    for x in range(N - k - 2, k - 1, -1):
        print(lst[y][x], end=' ')
    x = k
    for y in range(N - k - 2, k, -1):
        print(lst[y][x], end=' ')

