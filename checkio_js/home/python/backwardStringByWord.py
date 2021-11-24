

def backwardStringByWord(text):
    return  ' '.join(map(lambda x: x[::-1], text.split(' ')))

if __name__ == '__main__':
    print('Example:')
    print(backwardStringByWord(''))

#  These "asserts" are used for self-checking
assert backwardStringByWord('') == ''
assert backwardStringByWord('world') == 'dlrow'
assert backwardStringByWord('hello world') == 'olleh dlrow'
assert backwardStringByWord('hello   world') == 'olleh   dlrow'
assert backwardStringByWord('welcome to a game') == 'emoclew ot a emag'

print("Coding complete? Click 'Check' to earn cool rewards!")
