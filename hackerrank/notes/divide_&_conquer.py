def quickSort(ls):
    if len(ls) < 2:
        return ls
    else:
        pivot = ls[0]
        left = [i for i in ls[1:] if i <= ls[0]]
        right = [i for i in ls[1:] if i > ls[0]]
        print(f'left: {left}, \tpivot: {pivot}, \tright: {right}')
        return quickSort(left) + [pivot] + quickSort(right)


print(quickSort([22, 3, 1, 54, 2, 6, 77, 8, 42, 5, 31, 0, 7, 90, 1]))

'''
def max_number(ls):
    # Find the maximum number in a list
    if ls == []:
        return 0
    else:
        return max(ls[0], max_number(ls[1:]))


print(max_number([2, 7, 13, 3, 93, 24, 40, 88, 42, 1]))
'''


'''
def count_num_list(ls):
    # Count number of items in a list
    if ls == []:
        return 0
    else:
        return 1 + count_num_list(ls[1:])


print(count_num_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
'''


'''
def div_conquer(width, length):
    # Divide farm evenly into square plots
    remainder = length % width
    if remainder == 0:
        return width
    else:
        print(length, width)
        return div_conquer(remainder, width)


print(div_conquer(640, 1680))
'''
