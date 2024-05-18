from math import acos, radians

v = list(map(int, input().split()))
dim = len(v)
n, t = map(int, input().split())
answer = []

for i in range(n):
    u = list(map(int, input().split()))
    vl = ul = sp = 0
    for uu, vv in zip(u, v):
        sp += uu * vv
        vl += vv**2
        ul += uu**2
    # print(acos(sp / vl**0.5 / ul**0.5))
    if acos(sp / vl**0.5 / ul**0.5) <= radians(t):
        answer.append(i)

if answer:
    print(*answer)
else:
    print(-1)


'''
1 0
2 90
-1 1
0 1
ответ: 1
'''

'''
1 1 1 1
4 30
0 0 0 1
1 0 1 0
1 1 1 1
1 1 1 0
ответ: 2 3
'''

'''
1 1 1
2 0
0 0 1
3 0 3
ответ: -1
'''