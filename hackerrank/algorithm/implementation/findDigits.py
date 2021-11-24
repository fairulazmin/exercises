def findDigits(n):
    str_n = str(n)
    count = 0

    for i in set(str_n):
        if i != '0':
            if n % int(i) == 0:
                count += str_n.count(i)
    return count


print(findDigits(12))    # 2
print(findDigits(1012))  # 3
print(findDigits(12034))  # 2
