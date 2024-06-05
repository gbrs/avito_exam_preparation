# dots = ((1, 5), (3, 5), (4, 3), (6, 3), (2, 1), (2, 3))  # 8

dots = ((-3, -3), (-2, 3), (0, 3), (2, 1), (2, -1), (1, -2))  # 21.5

area = 0
for i in range(1, len(dots)):
    area += (dots[i][1] + dots[i - 1][1]) / 2 * (dots[i][0] - dots[i - 1][0])

area += (dots[0][1] + dots[-1][1]) / 2 * (dots[0][0] - dots[-1][0])

print(abs(area))
