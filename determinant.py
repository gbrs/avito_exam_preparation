def compute_determinant(x: list) -> int:
    n = len(x)
    answer = 0
    if n == 1:
        answer = x[0][0]
    else:
        for i in range(n):
            answer += (-1)**i * x[i][0] * compute_determinant([x[j][1:] for j in range(n) if j != i])
    return answer


if __name__ == '__main__':
    lst = [
        [1, -2, 3],
        [4, 0, 6],
        [-7, 8, 9]
    ]
    # 204

    print(compute_determinant(lst))

'''
lst = [
    [1, -2, 3],
    [4, 0, 6],
    [-7, 8, 9]
]
# 204
'''

'''
lst = [
    [2, 4, 8, 16],
    [3, 9, 27, 81],
    [4, 16, 64, 256],
    [5, 25, 125, 625]
]
# 1440
'''

'''
lst = [
    [1, 1, 1, 1],
    [2, 1, 3, 1],
    [1, 2, 3, 0],
    [-1, 2, 0, 1]
]
# -5

lst = [
    [11, -3],
    [-15, -2]
]
# -67
'''
