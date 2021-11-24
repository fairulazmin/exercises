import re

def isAllUpper(text):
    return text == text.upper() if re.findall(r'[a-zA-Z]', text) != [] else False

if __name__ == '__main__':
    print('Example:');
    print(isAllUpper('ALL UPPER'));

# These "asserts" are used for self-checking
assert isAllUpper('ALL UPPER') == True
assert isAllUpper('all lower') == False
assert isAllUpper('mixed UPPER and lower') == False
assert isAllUpper('') == False
assert isAllUpper("     ") == False

print("Coding complete? Click 'Check' to earn cool rewards!")
