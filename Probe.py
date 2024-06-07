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


