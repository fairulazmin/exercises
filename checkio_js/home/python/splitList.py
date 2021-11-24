from math import ceil

def splitList(values):
    return [values[:ceil(len(values)/2)], values[ceil(len(values)/2):]]

if __name__ == '__main__':
    print('Example:')
    print(splitList([1, 2, 3, 4, 5, 6]))

# These "asserts" are used for self-checking
assert splitList([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
assert splitList([1, 2, 3]) == [[1, 2], [3]]
assert splitList([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
assert splitList([1]) == [[1], []]
assert splitList([]) == [[], []]

print("Coding complete? Click 'Check' to earn cool rewards!")
