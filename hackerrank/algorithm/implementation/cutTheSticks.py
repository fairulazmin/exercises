def cutTheSticks(arr):
    cut = [len(arr)]
    while len(arr) != 0:
        arr = [i-min(arr) for i in arr if i-min(arr) != 0]
        cut.append(len(arr))
    return cut[:-1]


print(cutTheSticks([1, 2, 3]))                     # 3 2 1
print(cutTheSticks([5, 4, 4, 2, 2, 8]))            # 6 4 2 1
print(cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]))      # 8 6 4 1
