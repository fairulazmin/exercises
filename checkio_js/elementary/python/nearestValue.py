

def nearestValue(values, search):
    values.append(search)
    values.sort()
    idx = values.index(search)
    if idx == 0:
        return values[1]
    elif (len(values) == idx + 1):
        return values[len(values) - 2]
    elif ((values[idx + 1] - search) < (search - values[idx - 1])):
        return values[idx + 1]
    else:
        return values[idx - 1]

if __name__ == '__main__':
    print('Example:')
    print(nearestValue([4, 7, 10, 11, 12, 17], 9))

# These "asserts" are used for self-checking
assert nearestValue([4, 7, 10, 11, 12, 17], 9) == 10
assert nearestValue([4, 7, 10, 11, 12, 17], 8) == 7
assert nearestValue([4, 8, 10, 11, 12, 17], 9) == 8
assert nearestValue([4, 9, 10, 11, 12, 17], 9) == 9
assert nearestValue([4, 7, 10, 11, 12, 17], 0) == 4
assert nearestValue([4, 7, 10, 11, 12, 17], 100) == 17
assert nearestValue([5, 10, 8, 12, 89, 100], 7) == 8
assert nearestValue([-1, 2, 3], 0) == -1

print("Coding complete? Click 'Check' to earn cool rewards!")
