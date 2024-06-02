'''
Решение системы линейных уравнений
'''

from inverse_of_matrix import inverse_matrix

def multiply_matrix_vector(m: list, v: list):
    ans = [[0] for _ in range(len(v))]
    for i in range(len(m)):
        val = 0
        for j in range(len(v)):
            val += m[i][j] * v[j][0]
        ans[i][0] = val
    return ans


A = [
    [1, 2, 2, -1],
    [2, 1, -1, 1],
    [-1, 3, 1, 2],
    [3, -1, 2, -2]
]

B = [
    [-1],
    [9],
    [6],
    [-3]
]

# 2, 1, -1, 3

[print(*i) for i in multiply_matrix_vector(inverse_matrix(A), B)]

'''
A = [
    [2, 1, -1],
    [1, 2, -1],
    [1, 1, 1]
]

B = [
    [1],
    [2],
    [6]
]

# 1, 2, 3
'''