from math import cos

def dist(x):
    print(cos(x))
    return cos(x)

left = 0
right = 1.5
for _ in range(10):
    middle = (left + right) / 2
    if dist(middle) > 0:
        right = middle
    else:
        left = middle

print(middle)
