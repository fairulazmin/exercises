
def replaceFirst(values):
    try:
        return values[1:] + [values[0]]
    except:
        return []

if __name__ == '__main__':
    print('Example:')
    print(replaceFirst([1, 2, 3, 4]))

# These "asserts" are used for self-checking
assert replaceFirst([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replaceFirst([1]) == [1]
assert replaceFirst([]) == []

print("Coding complete? Click 'Check' to earn cool rewards!")
