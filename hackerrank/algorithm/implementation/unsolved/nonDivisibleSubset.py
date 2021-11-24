def nonDivisibleSubset(k, s):
    print([i % k for i in s])


print(nonDivisibleSubset(4, [19, 10, 12, 10, 24, 25, 22]))     # 3 [10, 12, 25] [19, 22, 24]
print(nonDivisibleSubset(3, [1, 7, 2, 4]))
print(nonDivisibleSubset(5, [770528134, 663501748, 384261537, 800309024,
                             103668401, 538539662, 385488901, 101262949, 557792122, 46058493]))  # 6


'''
def recursion(k, arr):
    parent = [arr[0]]
    child = [i for i in arr[1:] if (i + parent[0]) % k != 0]
    # print(f'parent = {parent}, \tchild = {child}')
    if child == []:
        return parent
    else:
        return parent + recursion(k, child)


def nonDivisibleSubset(k, s):
    ls = []
    for i in range(len(s)):
        ls.append(recursion(k, s[i:]))
    print(ls)
    return max([len(i) for i in ls])


print(nonDivisibleSubset(4, [19, 10, 12, 10, 24, 25, 22]))     # 3 [10, 12, 25] [19, 22, 24]
print(nonDivisibleSubset(3, [1, 7, 2, 4]))                     # 3 [1, 7, 4]
'''

'''
from itertools import combinations

for i in range(len(s), 1, -1):
a = list(combinations(s, i))
# print(f'list(a) = {a}')
for x in a:
    # print(all([True if sum(m) % k != 0 else False for m in list(combinations(x, 2))]))
    if all([True if sum(m) % k != 0 else False for m in list(combinations(x, 2))]):
        return len(x)
print([True if sum(m) % k != 0 else False for m in x])
for x in a:
print(list(combinations(x, 2)))
print([True if sum(m) % k != 0 else False for x in a for m in list(combinations(x, 2))])
print(set([(s[i], s[j]) for i in range(len(s))
           for j in range(i+1, len(s)) if (s[i] + s[j]) % k != 0]))


print(nonDivisibleSubset(4, [19, 10, 12, 10, 24, 25, 22]))     # 3 [10, 12, 25] [19, 22, 24]
print(nonDivisibleSubset(3, [1, 7, 2, 4]))                     # 3 [1, 7, 4]
'''
