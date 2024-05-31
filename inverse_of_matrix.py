from determinant import compute_determinant

def adjoint(m: list):
    adj_matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            lst = []
            for ii in range(size):
                line = []
                if ii != i:
                    for jj in range(size):
                        if jj != j:
                            line.append(m[ii][jj])
                    lst.append(line)
            # print(lst)
            adj_matrix[i][j] = (-1)**(i + j) * compute_determinant(lst)
    return list(zip(*adj_matrix))


def inverse_matrix(m: list):
    det = compute_determinant(m)
    if det != 0:
        inv_matrix = [[0] * size for _ in range(size)]
        adj_matrix = adjoint(m)
        for i in range(size):
            for j in range(size):
                inv_matrix[i][j] = adj_matrix[i][j] / det
        return inv_matrix






matrix = [
    [0, 42],
    [0, 54]
]

size = len(matrix)

im = inverse_matrix(matrix)
if im:
    [print(*i) for i in inverse_matrix(matrix)]
else:
    print('Обратной матрицы не существует')

'''
matrix = [
    [2, 1],
    [4, 3]
]

1.5 -0.5
-2.0 1.0

matrix = [
    [1, 1, 1],
    [2, 1, 2],
    [2, 1, 1]
]

-1 0 1
2 -1 0
0 1 -1
'''
