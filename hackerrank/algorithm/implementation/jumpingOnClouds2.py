def jumpingOnClouds(c):
    jump = 0
    while c != [0]:
        if c[:3] == [0, 0, 0]:
            c = c[2:]
        elif c[:3] == [0, 0, 1]:
            c = c[1:]
        elif c[:2] == [0, 1]:
            c = c[2:]
        elif c[:2] == [0, 0]:
            c = c[1:]
        jump += 1
    return jump


print(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]))  # 3
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))  # 4
print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))     # 3
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))     # 3
