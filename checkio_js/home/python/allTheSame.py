

def allTheSame(elements):
    return all([x == elements[0] for x in elements])


if __name__ == '__main__':
    print('Example:')
    print(allTheSame([1, 1, 1]))

# These "asserts" are used for self-checking and not for an auto-testing

assert allTheSame([1, 1, 1]) == True
assert allTheSame([1, 2, 1]) == False
assert allTheSame(['a', 'a', 'a']) == True
assert allTheSame([]) == True
assert allTheSame([1]) == True
print("Coding complete? Click 'Check' to earn cool rewards!")
