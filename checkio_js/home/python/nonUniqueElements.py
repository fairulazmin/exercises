

def nonUniqueElements(data):
    return [x for x in data if data.count(x) > 1]

if __name__ == '__main__':
    print('Example:')
    print(nonUniqueElements([1, 2, 3, 1, 3]))

assert nonUniqueElements([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
assert nonUniqueElements([1, 2, 3, 4, 5]) == []
assert nonUniqueElements([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert nonUniqueElements([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
