from re import findall

def countDigits(text):
    return len(findall(r'\d', text))

if __name__ == '__main__':
    print('Example:')
    print(countDigits('hi'))

#  These "asserts" are used for self-checking
assert countDigits('hi') == 0
assert countDigits('who is 1st here') == 1
assert countDigits('my numbers is 2') == 1
assert countDigits('This picture is an oil on canvas '
 + 'painting by Danish artist Anna '
 + 'Petersen between 1845 and 1910 year') == 8
assert countDigits('5 plus 6 is') == 2
assert countDigits('') == 0

print("Coding complete? Click 'Check' to earn cool rewards!")
