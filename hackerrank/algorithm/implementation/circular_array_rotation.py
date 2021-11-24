'''
John Watson knows of an operation called a right circular rotation on an array of integers. One rotation
operation moves the last array element to the first position and shifts all remaining elements right one.
To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform
the rotation operation a number of times then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the value of the element at a
given index.
'''


def circularArrayRotation(a, k, queries):
    if k % len(a) == 0:
        k = 0
    else:
        k = len(a) - k % len(a)
    new_a = a[k:] + a[:k]
    return [new_a[i] for i in queries]


print(circularArrayRotation([1, 2, 3], 6, [0, 1, 2]))  # [1,2,3]
print(circularArrayRotation([1, 2, 3], 4, [0, 1, 2]))  # [3,1,2]
print(circularArrayRotation([1, 2, 3], 3, [0, 1, 2]))  # [1,2,3]
print(circularArrayRotation([1, 2, 3], 2, [0, 1, 2]))  # [2,3,1]
print(circularArrayRotation([3, 4, 5], 2, [0, 1, 2]))  # [4,5,3]
