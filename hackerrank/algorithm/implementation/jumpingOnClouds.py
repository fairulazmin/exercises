def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    i = k % n
    while i != 0:
        if c[i] == 1:
            energy -= 3
        elif c[i] == 0:
            energy -= 1
        i = (i+k) % n

    if c[0] == 0:
        return energy-1
    else:
        return energy-3


print(jumpingOnClouds([0, 0, 1, 0], 2))                    # 96
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))        # 92
print(jumpingOnClouds([1, 1, 1, 0], 3))                    # 90
print(jumpingOnClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3))  # 80
