def fine(date1, date2):
    d1, m1, y1 = map(int, date1.split())
    d2, m2, y2 = map(int, date2.split())

    if y1 > y2:
        return 10000
    elif y1 == y2 and m1 > m2:
        return 500 * (m1 - m2)
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return 15 * (d1 - d2)
    else:
        return 0


#print(fine(input(), input()))
print(fine('9 6 2015', '6 6 2015'))        # 45
print(fine('6 6 2015', '9 6 2016'))        # 0
print(fine('5 5 2014', '23 2 2014'))       # 1500
print(fine('31 5 2014', '1 5 2014'))       # 450
print(fine('1 1 2015', '31 12 2014'))      # 10000
