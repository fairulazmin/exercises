def split_pairs(text):
    arr = []

    if text == '':
        return arr

    for i in range(0, len(text), 2):
        arr.append(text[i:i+2])

    if len(arr[-1]) == 1:
        arr[-1] = arr[-1] + '_'

    return arr


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
