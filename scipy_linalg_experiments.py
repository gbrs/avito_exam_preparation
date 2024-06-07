from scipy.linalg import inv, solve, det, cosm

matrix = [
    [2, 1],
    [4, 3]
]

print('Обратная матрица:')
print(inv(matrix))
print('----------')

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

print('Вектор X:')
print(*solve(A, B))
print('----------')

lst = [
    [1, -2, 3],
    [4, 0, 6],
    [-7, 8, 9]
]
# 204

print(f'Детерминант: {det(lst)}')
print('----------')

print('Косинус: ')
print(cosm(matrix))
print('----------')



