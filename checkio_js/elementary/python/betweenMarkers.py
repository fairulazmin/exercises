

def betweenMarkers(line, left, right):
    return line[line.index(left) + 1: line.index(right)]

if __name__ == '__main__':
    print('Example:')
    print(betweenMarkers('What is >apple<', '>', '<'))

# These "asserts" are used for self-checking
assert betweenMarkers('What is >apple<', '>', '<') == 'apple'
assert betweenMarkers('What is [apple]', '[', ']') == 'apple'
assert betweenMarkers('What is ><', '>', '<') == ''
assert betweenMarkers('[an apple]', '[', ']') == 'an apple'

print("Coding complete? Click 'Check' to earn cool rewards!")
