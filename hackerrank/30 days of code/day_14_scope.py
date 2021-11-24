class Difference:
    maximumDifference = None

    def __init__(self, a):
        self.__elements = a

        # Add your code here
    def computeDifference(self):
        self.maximumDifference = max([abs(self.__elements[i] - j)
                                      for i in range(len(self.__elements)-1) for j in self.__elements[i+1:]])


# End of Difference class
a = [1, 2, 5]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
