def checkio(data: list) -> list:
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.

    # replace this for solution
    return [x for x in data if data.count(x) > 1]

# def checkio(li):
#     f = [x for x in li if li.count(x) > 1]
#     print(f)


print(checkio([1, 2, 3, 1, 3]))        # [1, 3, 1, 3]
print(checkio([1, 2, 3, 4, 5]))        # []
print(checkio([5, 5, 5, 5, 5]))        # [5, 5, 5, 5, 5]
print(checkio([10, 9, 10, 10, 9, 8]))  # [10, 9, 10, 10, 9]
print(checkio([2]))                    # []
