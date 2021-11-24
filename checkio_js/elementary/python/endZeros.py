import re


def endZeros(value):
    return len(re.findall(r'0+', str(value)).pop()) if str(value).endswith('0') else 0

    '''
    if str(value).endswith('0'):
        return len(re.findall(r'0+', str(value)).pop())
    else:
        return 0
    '''


if __name__ == '__main__':
    print("Example:")
    print(endZeros('0'))

# These "asserts" are used for self-checking and not for an auto-testing
assert endZeros(0) == 1
assert endZeros(1) == 0
assert endZeros(10) == 1
assert endZeros(101) == 0
assert endZeros(245) == 0
assert endZeros(100100) == 2
print("Coding complete? Click 'Check' to earn cool rewards!")
