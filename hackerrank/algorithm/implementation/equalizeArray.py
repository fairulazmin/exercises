def equalizeArray(arr):
    mx = 0
    for i in set(arr):
        if arr.count(i) > mx:
            mx = arr.count(i)
    return len(arr) - mx


print(equalizeArray([1, 2, 2, 3]))         # 2
print(equalizeArray([3, 3, 2, 1, 3]))      # 2
