class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        # head is node because current has .data and .next
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head == None:
            head = Node(data)
            return head
        current = head
        while current.next != None:
            current = current.next
        current.next = Node(data)
        return head


mylist = Solution()
T = [2, 3, 4, 1]
head = None
for i in T:
    data = i
    head = mylist.insert(head, data)
mylist.display(head)  # 2 3 4 1
