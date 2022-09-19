# Insertion on Begining
# Insertion on End
# Insertion on gaven Position


from operator import ne


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

    def insertHead(self, data):
        node = Node(data)
        temp = self.head
        temp.prev = node
        node.next = temp
        self.head = node

    def insertBottom(self, data):
        node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        node.prev = temp

    def insertOnPosition(self, position, data):
        if self.display()[1] < position:
            return "False Position"
        else:
            node = Node(data)
            temp = self.head
            for _ in range(position-1):
                temp = temp.next
            node.prev = temp
            node.next = temp.next
            temp.next = node
            temp.next.prev = node


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

d.insertHead(10)
d.insertBottom(50)
d.insertOnPosition(5, 660)

print(d.display())
