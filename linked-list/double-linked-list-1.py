

from curses import noecho


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        if temp is None:
            print("Empty !")
        while temp:
            print(temp.data, end="--->")
            temp = temp.next
        print("\n")


d = DoubleLinkList()
n0 = Node(0)
d.head = n0
n1 = Node(1)
n0.next = n1
n1.prev = n0

print(n1.prev.data)
d.display()
