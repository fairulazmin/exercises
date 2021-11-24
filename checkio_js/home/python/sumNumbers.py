import re

def sumNumbers(test):
    return sum(map(int, re.findall(r'\b[0-9]+\b', test)))


if __name__ == '__main__':
    print('Example:')
    print(sumNumbers('hi'))

#  These "asserts" are used for self-checking
assert sumNumbers('hi') == 0
assert sumNumbers('who is 1st here') == 0
assert sumNumbers('my numbers is 2') == 2
assert sumNumbers('This picture is an oil on canvas '
  + 'painting by Danish artist Anna '
  + 'Petersen between 1845 and 1910 year') == 3755
assert sumNumbers('5 plus 6 is') == 11
assert sumNumbers('') == 0

print("Coding complete? Click 'Check' to earn cool rewards!")
