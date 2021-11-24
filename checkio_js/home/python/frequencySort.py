

def frequencySort(items):
    d = {}
    for i in items:
        d[i] = 1 if i not in d else d[i] + 1

    '''
    for i in items:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    '''

    '''
    for i in items:
        if i not in d:
            d[i] = items.count(i)
    '''

    dsort = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return [a for x in [[y]*z for y, z in dsort] for a in x]


if __name__ =='__main__':
    print('Example:');
    print(frequencySort([4, 6, 2, 2, 6, 4, 4, 4]));

# These "asserts" are used for self-checking and not for an auto-testing
assert frequencySort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
assert frequencySort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
assert frequencySort([17, 99, 42]) == [17, 99, 42]
assert frequencySort([]) == []
assert frequencySort([1]) == [1]
assert frequencySort([4,6,2,2,2,6,4,4,4]) == [4,4,4,4,2,2,2,6,6]

print("Coding complete? Click 'Check' to earn cool rewards!");
