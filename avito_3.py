from math import sin, cos, pi
from scipy import integrate

n = 2
ans_a = []
ans_b = []

for i in range(n + 1):
    ans_a.append(
        round(
            integrate.quad(
                lambda x: sin(x) * cos(i * x) / (sin(x) + 2),
                -pi,
                pi)[0]
            / pi,
            3
        )
    )

    if i > 0:
        ans_b.append(
            round(
                integrate.quad(
                    lambda x: sin(x) * sin(i * x) / (sin(x) + 2),
                    -pi,
                    pi)[0]
                / pi,
                3
            )
        )

print(*ans_a)
print(*ans_b)


