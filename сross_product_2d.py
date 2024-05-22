def cross_product(a, b):
    return a[0]*b[1] - a[1]*b[0]


v1 = tuple(map(int, input().split()))
v2 = tuple(map(int, input().split()))
print(cross_product(v1, v2))

'''
2 -1
1 3
7

1 3
2 -1
-7

2 16
3 19
-10

2 -16
3 19
86

2 -16
-3 -19
-86
'''

