def kaprekarNumbers(p, q):
    # base = [i for i in range(p, q + 1)]
    modified = [i for i in range(p, q + 1) if i == int(
        str(i**2)[:len(str(i**2))//2]) + int(str(i**2)[len(str(i**2))//2:])]

    print(modified)


kaprekarNumbers(1, 2)  # 1, 9, 45, 55, 99
