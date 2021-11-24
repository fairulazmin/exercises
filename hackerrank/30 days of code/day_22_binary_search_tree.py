class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root is None:
            return -1
        else:
            print(root.data)
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1


data = [9, 20, 50, 35, 44, 9, 15, 62, 11, 13]  # 4
# data = [3, 5, 2, 1, 4, 6, 7]    # 3
myTree = Solution()
root = None
for i in data:
    root = myTree.insert(root, i)
height = myTree.getHeight(root)
print(height)
