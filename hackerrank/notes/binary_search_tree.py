class Node:
    def __init__(self, val):
        self.value = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left.insert(data)
                return True
        else:
            self.right.insert(data)
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

        def find(self, data):
            if (self.value == data):
                return True


class BinaryTree:
    def __init__(self, root):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
