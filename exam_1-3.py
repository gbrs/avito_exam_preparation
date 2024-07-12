# lst = [[x for x in line.split()] for line in sys.stdin]


lst = [
    ['P', 'S'],
    ['S', 'P'],
    ['P', 'P'],
    ['P', 'S'],
    ['R', 'S'],
    ['P', 'R'],
    ['P', 'P'],
    ['S', 'S'],
    ['P', 'P'],
    ['P', 'S']
]
n = len(lst)

m = 0
w = 0
d = 0

for i in lst:
    if i[0] == i[1]:
        d += 1
    elif i in (['R', 'S'], ['S', 'P'], ['P', 'R']):
        m += 1
    else:
        w += 1

if m > w:
    print('Костя')
    print(f'W: {m / n:.2%}')
    print(f'D: {d / n:.2%}')
    print(f'L: {w / n:.2%}')

elif w > m:
    print('Ксюша')
    print(f'W: {w / n:.2%}')
    print(f'D: {d / n:.2%}')
    print(f'L: {m / n:.2%}')

else:
    print('Ничья')
    print(f'W: {m / n:.2%}')
    print(f'D: {d / n:.2%}')
    print(f'L: {w / n:.2%}')

'''
# можно ж было подсократить
if m > w:
    print('Костя')

elif w > m:
    print('Ксюша')
    m, w = w, m

else:
    print('Ничья')

print(f'W: {m / n:.2%}')
print(f'D: {d / n:.2%}')
print(f'L: {w / n:.2%}')
'''



