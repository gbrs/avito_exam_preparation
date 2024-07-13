import sys

# A = input().split()
# B = input().split()
# C = input().split()

A = ['VERNITE_MOI', '2007', '07', '07']
B = ['TEST', '2000', '01', '01']
C = ['POKEMON_GO', '2023', '04', '30']


# print(A, B, C)

# lst = [line for line in sys.stdin]

lst = [
        'IMG_20070707_001311111.jpg',
        'IMG_20070707_001412000.jpg',
        'IMG_20070707_001617235.jpg',
        'IMG_20070707_002424603.jpg',
        'DCIM-2000-01-01-1.jpg',
        'DCIM-2000-01-01-2.jpg',
        '202304300924-1.jpg',
        '202304301001-2.jpg',
        '202304301012-3.jpg'
]

lst = [''.join([x for x in foto if x in '0123456789']) + '.jpg' for foto in lst]

lst.sort()

months = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

a = b = c = 1

for foto in lst:
    foto = ''.join([x for x in foto if x in '0123456789']) + '.jpg'
    year = foto[:4]
    month = foto[4:6]
    day = foto[6:8]
    if year == A[1] and month == A[2] and day == A[3]:
        conf = A[0]
        idx = a
        a += 1
    elif year == B[1] and month == B[2] and day == B[3]:
        conf = B[0]
        idx = b
        b += 1
    elif year == C[1] and month == C[2] and day == C[3]:
        conf = C[0]
        idx = c
        c += 1
    print(f'{year}_{months[int(month)]}_{day}_{conf}_{idx}.jpg')





