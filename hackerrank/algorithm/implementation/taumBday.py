def taumBday(b, w, bc, wc, z):
    if bc > wc + z:
        return b*(wc + z) + w*wc
    elif wc > bc + z:
        return b*bc + w*(bc + z)
    else:
        return b*bc + w*wc


print(taumBday(10, 10, 1, 1, 1))    # 20
print(taumBday(5, 9, 2, 3, 4))      # 37
print(taumBday(3, 6, 9, 1, 1))      # 12
print(taumBday(7, 7, 4, 2, 1))      # 35
print(taumBday(3, 3, 1, 9, 2))      # 12
