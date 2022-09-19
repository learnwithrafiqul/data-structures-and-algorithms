# Deleting on Begining
# Deleting on End
# Deleting on gaven Position


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
        len = 0
        data = []
        if temp is None:
            return "Empty !"
        while temp:
            data.append(temp.data)
            len += 1
            temp = temp.next
        return (data, len)

    def deletingHead(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = Node

    def deletingBottom(self):
        next = self.head.next
        prev = self.head
        while next.next is not None:
            next = next.next
            prev = prev.next
        print(prev.data)
        print(next.data)
        next.prev = None
        prev.next = None

    def deletingOnPosition(self, position):
        if self.display()[1] < position:
            return "False Position"
        else:
            prev = self.head
            next = self.head.next
            for _ in range(position-1):
                prev = prev.next
                next = next.next
            prev.next = next.next
            next.next.prev = prev
            next.prev = None
            next.next = None


d = DoubleLinkList()
n0 = Node(0)
d.head = n0
n1 = Node(1)
n0.next = n1
n1.prev = n0
n2 = Node(2)
n1.next = n2
n2.prev = n1
n3 = Node(3)
n2.next = n3
n3.prev = n2
n4 = Node(4)
n3.next = n4
n4.prev = n3
n5 = Node(5)
n4.next = n5
n5.prev = n4

# d.deletingHead()
# d.deletingBottom()
d.deletingOnPosition(3)

print(d.display())
