

def isAllUpper(text):
    if text == '':
        return True
    else:
        return text.isupper()

if __name__ == '__main__':
    print('Example:')
    print(isAllUpper('ALL UPPER'))

# These "asserts" are used for self-checking
assert isAllUpper('ALL UPPER') == True
assert isAllUpper('all lower') == False
assert isAllUpper('mixed UPPER and lower') == False
assert isAllUpper('') == True

print("Coding complete? Click 'Check' to earn cool rewards!")
