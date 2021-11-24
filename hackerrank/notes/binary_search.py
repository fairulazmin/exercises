def binarySearch(my_list, val, idx=0):
    ''' Recursive binary search'''
    mid = len(my_list) // 2

    if my_list[mid] == val:
        return idx + mid
    elif len(my_list) == 1:
        return None
    elif my_list[mid] < val:
        if my_list[mid + 1:] == []:
            return None
        else:
            return binarySearch(my_list[mid + 1:], val, idx + mid + 1)
    else:
        return binarySearch(my_list[:mid], val, idx)


my_list = [1, 3, 5, 7, 9, 11, 13, 15, 18, 22, 56]
not_my_list = [0, 2, 4, 6, 8, 10, 12, 14, 17, 20, 55, 66]
for i in not_my_list:
    print(binarySearch(my_list, i))  # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
# print(binarySearch(my_list, -1))  # => None


'''
def binarySearch(my_list, val, idx=0):
    mid = len(my_list) // 2

    if my_list[mid] == val:
        # print(f'{"if my_list[mid] == val":<30}{idx:<5}{my_list}{"":<15}')
        return idx + mid
    elif len(my_list) == 1:
        # print(f'{"elif len(my_list) == 1":<30}{idx:<5}{my_list}{"":<15}')
        return None
    elif my_list[mid] < val:
        if my_list[mid + 1:] == []:
            # print(f'{"my_list[mid + 1:] == []"}')
            return None
        else:
            # print(f'{"elif my_list[{mid}] < {val}":<30}{idx:<5}{my_list}{"":<15}')
            return binarySearch(my_list[mid + 1:], val, idx + mid + 1)
    else:
        # print(f'{"else":<30}{idx:<5}{my_list}{"":<15}')
        return binarySearch(my_list[:mid], val, idx)


my_list = [1, 3, 5, 7, 9, 11, 13, 15, 18, 22, 56]
not_my_list = [0, 2, 4, 6, 8, 10, 12, 14, 17, 20, 55, 66]
for i in not_my_list:
    print(binarySearch(my_list, i))  # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
# print(binarySearch(my_list, -1))  # => None
'''
