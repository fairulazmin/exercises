class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    return self.left.insert(data)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data)
                else:
                    return self.right.insert(data)


bt = BinaryTree()
bt.insert(4)
bt.insert(2)
bt.insert(7)
bt.insert(5)
