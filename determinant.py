def compute_determinant(x: list) -> int:
    n = len(x)
    answer = 0
    if n == 1:
        answer = x[0][0]
    else:
        for i in range(n):
            answer += (-1)**i * compute_determinant([x[j][1:] for j in range(n) if j != i])
    print(answer)
    return answer


lst = [
    [1, 1, 1, 1],
    [2, 1, 3, 1],
    [1, 2, 3, 0],
    [-1, 2, 0, 1]
]
# -6

print(compute_determinant(lst))



