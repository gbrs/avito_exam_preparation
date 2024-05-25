def compute_cosine_distance(x: list, y: list) -> int:
    n = len(x)
    p = lx = ly = 0
    for xx, yy in zip(x,y):
        p += xx * yy
        lx += xx**2
        ly += yy**2
    return 1 - p / lx**0.5 / ly**0.5


vanya = [2, -2, 3, -4, 4]
reavs = [1, 2, 3, 4, 5]
depp = [4, 3, 4, 3, 4]
kerry = [3, 3, 3, 3, 3]

for artist in (reavs, depp, kerry):
    print(compute_cosine_distance(vanya, artist))
