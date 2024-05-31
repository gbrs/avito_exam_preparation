"""
minimum search
"""

def calculate_foo(x: float) -> float:
    return x / 3 - x**(2/3)
    # max - 0, min - 8


left = 0.00001
right = 1000000

for _ in range(300):
    ml = 2 * left / 3 + right /3
    mr = left / 3 + 2 * right / 3
    if calculate_foo(mr) > calculate_foo(ml):
        right = mr
    else:
        left = ml

print(left)

