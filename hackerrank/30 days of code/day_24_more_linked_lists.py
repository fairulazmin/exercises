class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while(start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    # def removeDuplicates(self, head):
    #     unique = set()
    #     h = head
    #     unique.add(head.data)
    #     while head.next != None:
    #         if head.next.data in unique:
    #             head.next = head.next.next
    #         else:
    #             head = head.next
    #             unique.add(head.data)
    #     return h

    def removeDuplicates(self, head):
        unique = set()
        h = head
        unique.add(h.data)
        while h.next != None:
            if h.next.data in unique:
                h.next = h.next.next
            else:
                h = h.next
                unique.add(h.data)
        return head

    # def removeDuplicates(self, head):
    #     unique = set()
    #     curr = head
    #     while curr:
    #         unique.add(curr.data)
    #         curr = curr.next
    #     no_duplicate = Solution()
    #     head = None
    #     for i in unique:
    #         data = i
    #         head = no_duplicate.insert(head, data)
    #     return head


mylist = Solution()
head = None
for i in [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 2, 2, 3, 3, 3]:
    data = i
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
