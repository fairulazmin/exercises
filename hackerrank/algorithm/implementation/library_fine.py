def libraryFine(d1, m1, y1, d2, m2, y2):

    if y1 > y2:
        return 10000
    elif y1 == y2 and m1 > m2:
        return 500 * (m1 - m2)
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return 15 * (d1 - d2)
    else:
        return 0


print(libraryFine(9, 6, 2015, 6, 6, 2015))        # 45
print(libraryFine(6, 6, 2015, 9, 6, 2016))        # 0
print(libraryFine(5, 5, 2014, 23, 2, 2014))       # 1500
print(libraryFine(31, 5, 2014, 1, 5, 2014))       # 450
print(libraryFine(1, 1, 2015, 31, 12, 2014))      # 10000
