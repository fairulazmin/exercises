

def isAscending(values):
    return False if len(values) > 1 and len(set(values)) == 1 else values == sorted(values)

if __name__ == '__main__':
    print('Example:')
    print(isAscending([-5, 10, 99, 123456]))

# These "asserts" are used for self-checking
assert isAscending([-5, 10, 99, 123456]) == True
assert isAscending([99]) == True
assert isAscending([4, 5, 6, 7, 3, 7, 9]) == False
assert isAscending([]) == True
assert isAscending([1, 1, 1, 1]) == False

print("Coding complete? Click 'Check' to earn cool rewards!")
