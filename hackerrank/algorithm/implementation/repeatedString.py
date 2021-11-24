def repeatedString(s, n):
    x, y = divmod(n, len(s))
    num_a = s.count('a')
    num_mod_a = s[:y].count('a')
    return num_a*x + num_mod_a


print(repeatedString('abcac', 10))            # 4
print(repeatedString('aba', 10))              # 7
print(repeatedString('a', 1000000000000))     # 1000000000000
