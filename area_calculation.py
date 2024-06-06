from cross_product_2d import cross_product

# dots = ((1, 5), (3, 5), (4, 3), (6, 3), (2, 1), (2, 3))  # 8

dots = ((-3, -3), (-2, 3), (0, 3), (2, 1), (2, -1), (1, -2))  # 21.5


# нахождение площади через векторные произведения

area = 0
for i in range(1, len(dots)):
    area += cross_product(dots[i], dots[i - 1])

area += cross_product(dots[0], dots[-1])

print(abs(area / 2))


# нахождение площади через трапеции

area = 0
for i in range(1, len(dots)):
    area += (dots[i][1] + dots[i - 1][1]) / 2 * (dots[i][0] - dots[i - 1][0])

area += (dots[0][1] + dots[-1][1]) / 2 * (dots[0][0] - dots[-1][0])

print(abs(area))



