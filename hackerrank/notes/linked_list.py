class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(data)

    def insertStart(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next

    def getLength(self):
        idx = 0
        curr = self.head
        while curr:
            idx += 1
            curr = curr.next
        return idx


ls = LinkedList()
ls.insertEnd(1)
ls.insertEnd(2)
ls.insertEnd(3)
ls.insertStart(6)
ls.insertStart(5)
ls.insertStart(4)
ls.display()
print(ls.getLength())

'''
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("Error: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length:
            print("Error: 'Erase' Index out of range")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


a = linked_list()
a.append(2)
a.append(4)
a.append(6)
a.display()
# a.erase(1)
# a.display()
'''
