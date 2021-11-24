from math import sqrt, ceil, floor


def squares(a, b):
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1


print(squares(3, 9))        # 2
print(squares(24, 49))      # 3
print(squares(25, 49))      # 3
