from random import random as r

N = 100_000_000
sm = 0
for _ in range(N):
    sm += (r() * 9)**2 + (r() * 76)**2

print(sm / N)  # 1952.3159068910343   1951.9855425445724   1952.2920491424766

"""

from math import factorial as f

print(f(12) / f(11) * f(43) / f(28) / f(15) * f(16) * f(39) / f(55))

---------------------

group_1 = [
    [1, 'КТИ', 112],
    [1, 'ВСИ', 105],
    [1, 'МНИ', 109],
    [1, 'АНМ', 90],
    [1, 'УРА', 130],
    [1, 'ВФЫ', 117],
    [1, 'РКИ', 117],
    [1, 'ТРИ', 125],
    [1, 'ТРК', 134],
    [1, 'ТНК', 109]
]

group_2 = [
    [2, 'БРИ', 121],
    [2, 'ДРО', 120],
    [2, 'РНА', 134],
    [2, 'ВРА', 119],
    [2, 'ГРА', 115],
    [2, 'ДЖА', 106],
    [2, 'ВЦК', 107],
    [2, 'ЮЕР', 101],
    [2, 'ЖЕН', 97],
    [2, 'КОР', 117]
]

# 47.5

group = list(group_1)
group.extend(list(group_2))

group.sort(key=lambda x: x[2])

current = group[0][2]
counter = 1

for i in range(1, len(group)):
    if group[i][2] == current:
        counter += 1
    else:
        avg_rang = 3 * i
        for j in range(i - counter, i):
            group.append()

print(*group)


"""