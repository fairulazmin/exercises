def permutationEquation(p):
    size = len(p)
    x = {}
    for i in range(size):
        x[p[i]] = i+1

    return [x[x[i]] for i in range(1, size + 1)]


print(permutationEquation([5, 2, 1, 3, 4]))    # 4, 2, 5, 1, 3
print(permutationEquation([4, 3, 5, 1, 2]))    # 1 3 5 4 2
print(permutationEquation([2, 3, 1]))          # 2 3 1
# [2,5,11,13,1,14,7,3,4,18,8,6,16,12,15,10,9,17]
print(permutationEquation([2, 5, 11, 10, 1, 14, 7, 3, 16, 9, 8, 6, 18, 12, 15, 17, 13, 4]))
