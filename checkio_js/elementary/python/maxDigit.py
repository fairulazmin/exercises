

def maxDigit(value):
    return max(map(int, list(str(value))))

if __name__ == '__main__':
    print('Example:')
    print(maxDigit(0))

# These "asserts" are used for self-checking
assert maxDigit(0) == 0
assert maxDigit(52) == 5
assert maxDigit(634) == 6
assert maxDigit(1) == 1
assert maxDigit(10000) == 1

print("Coding complete? Click 'Check' to earn cool rewards!")
