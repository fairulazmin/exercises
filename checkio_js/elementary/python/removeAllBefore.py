def removeAllBefore(values, b):
    try:
        return values[values.index(b):]
    except:
        return values


if __name__ == '__main__':
    print('Example:')
    print(removeAllBefore([1, 2, 3, 4, 5], 3))

# These "asserts" are used for self-checking and not for an auto-testing
assert removeAllBefore([1, 2, 3, 4, 5], 3) == [3, 4, 5]
assert removeAllBefore([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]
assert removeAllBefore([1, 1, 2, 4, 2, 3, 4], 2) == [2, 4, 2, 3, 4]
assert removeAllBefore([1, 1, 5, 6, 7], 2) == [1, 1, 5, 6, 7]
assert removeAllBefore([], 0) == []
assert removeAllBefore([7, 7, 7, 7, 7, 7, 7, 7, 7], 7) == [7, 7, 7, 7, 7, 7, 7, 7, 7]

print("Coding complete? Click 'Check' to earn cool rewards!")
