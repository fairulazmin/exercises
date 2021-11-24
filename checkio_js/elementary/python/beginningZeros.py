import re

def beginningZeros(text):
    if re.findall(r'^0+', text) == []:
        return 0
    else:
        return len(re.findall(r'^0+', text)[0])

if __name__ == '__main__':
    print('Example:');
    print(beginningZeros('100'));

# These "asserts" are used for self-checking
assert beginningZeros('100') == 0
assert beginningZeros('001') == 2
assert beginningZeros('100100') == 0
assert beginningZeros('001001') == 2
assert beginningZeros('012345679') == 1
assert beginningZeros('0000') == 4

print("Coding complete? Click 'Check' to earn cool rewards!");
