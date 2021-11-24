def appendAndDelete(s, t, k):
    temp = ''
    for i in range(len(s), 0, -1):
        if s[:i] == t[:i]:
            temp = s[:i]
            adjust = len(s) - len(temp)
            break
        adjust = len(s)

    adjust += len(t) - len(temp)

    if k >= adjust and (k-adjust) % 2 == 0 or len(s) + len(t) < k:
        return 'Yes'
    else:
        return 'No'


print(appendAndDelete('abc', 'def', 6))                 # Yes
print(appendAndDelete('hackerhappy', 'hackerrank', 9))  # Yes
print(appendAndDelete('aba', 'aba', 7))                 # Yes
print(appendAndDelete('y', 'yu', 3))                    # Yes
print(appendAndDelete('y', 'yu', 4))                    # Yes
print(appendAndDelete('ashley', 'ash', 2))              # No
print(appendAndDelete('qwerasdf', 'qwerbsdf', 6))       # No
print(appendAndDelete('y', 'yu', 2))                    # No
print(appendAndDelete('asdasd', 'bsdasd', 6))           # No
print(appendAndDelete('abcd', 'abcdert', 10))           # No
