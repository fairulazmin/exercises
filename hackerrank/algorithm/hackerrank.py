

# =============================================================================
# class Difference:
#     maximumDifference = None
#
#     def __init__(self, a):
#         self.__elements = a
#
#     def computeDifference(self):
#         self.maximumDifference = max([abs(self.__elements[i] - j) for i in range(len(self.__elements)-1) for j in self.__elements[i+1:]])
#
# a = [1,2,3,4,5]
# d = Difference(a)
# d.computeDifference()
#
# print(d.maximumDifference)
# =============================================================================


# =============================================================================
# def formingMagicSquare(s):
#     combi = [[8,1,6,3,5,7,4,9,2], [6,1,8,7,5,3,2,9,4], [2,7,6,9,5,1,4,3,8], [4,3,8,9,5,1,2,7,6], [2,9,4,7,5,3,6,1,8], [4,9,2,3,5,7,8,1,6], [6,7,2,1,5,9,8,3,4], [8,3,4,1,5,9,6,7,2]]
#     s = [j for i in s for j in i]
#     minimum = 100
#     for x in combi:
#         add = 0
#         for y,z in zip(s,x):
#             add += abs(y - z)
#         if add < minimum:
#             minimum = add
#     print(minimum)
#
# formingMagicSquare([[2, 7, 6], [8, 5, 1], [4, 4, 6]])  # 4
# formingMagicSquare([[6, 4, 4], [1, 5, 8], [6, 7, 2]])  # 4 fail
# formingMagicSquare([[6, 1, 6], [7, 5, 4], [2, 8, 4]])  # 4
# formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])  # 4 fail
# formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]])  # 1
# formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]])  # 7
# =============================================================================


# =============================================================================
# from time import strptime, strftime
# def dayOfProgrammer(year):
#     # day = 256
#     # if 1700 <= year <= 1917 and year%4 == 0:
#     #     day -= 1
#     # day = strptime(str(year) + ' ' + str(day), '%Y %j')
#     # return strftime('%d.%m.%Y', day)
#     if 1700 <= year <= 1917 and year%4 == 0:
#         day = 12 # Leap
#     elif year == 1918:
#         day = 26
#     elif year > 1918 and year%4 == 0:
#         if year%100 == 0 and year%400 != 0:
#             day = 13 # Not leap
#         else:
#             day = 12 # Leap
#     else:
#         day = 13
#     return f'{day}.09.{year}'
#
# print(dayOfProgrammer(1918))        # 26.09.1918
# print(dayOfProgrammer(1800))        # 12.09.1800
# print(dayOfProgrammer(1916))        # 12.09.1916
# print(dayOfProgrammer(1917))        # 13.09.1917
# print(dayOfProgrammer(1984))        # 12.09.1984 leap
# print(dayOfProgrammer(2016))        # 12.09.2016 Leap
# print(dayOfProgrammer(2017))        # 13.09.2017 Not leap
# print(dayOfProgrammer(2000))        # 12.09.2000 Leap
# print(dayOfProgrammer(2100))        # 13.09.2100 Not leap
# =============================================================================


# =============================================================================
# def getMoneySpent(keyboards, drives, b):
#     try:
#         return max([i+j for i in keyboards for j in drives if i+j <= b])
#     except:
#         return -1
#
# print(getMoneySpent([40, 50, 60], [5, 8, 12], 60))      # 58
# print(getMoneySpent([3, 1], [5, 2, 8], 10))             # 9
# print(getMoneySpent([4], [5], 5))                       # -1
# =============================================================================

# =============================================================================
# def bonAppetit(bill, k, b):
#     x = (sum(bill) - sum([bill[i] for i in [k]]))/2
#     if  x == b:
#         print('Bon Appetit')
#     else:
#         print(int(abs(b - x)))
#
#
# bonAppetit([3, 10, 2, 9], 1, 12)     # 5
# bonAppetit([3, 10, 2, 9], 1, 7)      # Bon Appetit
# =============================================================================


# =============================================================================
# from collections import Counter
# def migratoryBirds(arr):
#     return Counter(sorted(arr)).most_common(1)[0][0]
#
#
# print(migratoryBirds([1, 4, 4, 4, 5, 3]))                  # 4
# print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))   # 3
# =============================================================================

# =============================================================================
# def divisibleSumPairs(n, k, ar):
#     li = [[ar[i],j] for i in range(len(ar) - 1) for j in ar[i+1:] if (ar[i]+j) % k == 0]
#     return len(li)
#
#
# print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))   # 5
# print(divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]))   # 5
# =============================================================================

# =============================================================================
# from time import strptime, strftime
#
# s = '07:05:45PM'
# t = strptime(s, '%I:%M:%S%p')
# print(strftime('%H:%M:%S', t))
# =============================================================================

# =============================================================================
# Print a staircase of size  using # symbols and spaces.
# n = 6
#
# for i in range(1, n+1):
#     print(f'{"#"*i:>{n}}')
# =============================================================================
