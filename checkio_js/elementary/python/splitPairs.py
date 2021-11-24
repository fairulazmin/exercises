

def splitPairs(text):
    arr = []
    for i in range(0, len(text), 2):
        if len(text[i:i+2]) == 1:
            arr.append(text[i:i+2] + '_')
        else:
            arr.append(text[i:i+2])
    return arr

if __name__ == '__main__':
    print('Example:')
    print(splitPairs('abcd'))

# These "asserts" are used for self-checking
assert splitPairs('abcd') == ['ab', 'cd']
assert splitPairs('abc') == ['ab', 'c_']
assert splitPairs('abcdf') == ['ab', 'cd', 'f_']
assert splitPairs('a') == ['a_']
assert splitPairs('') == []

print ("Coding complete? Click 'Check' to earn cool rewards!")
