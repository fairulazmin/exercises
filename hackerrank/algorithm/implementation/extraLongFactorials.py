def extraLongFactorials(n):
    if n == 1:
        return 1
    else:
        return n * extraLongFactorials(n-1)


print(extraLongFactorials(25))  # 1551121004330985984000000
