# Insertion on Begining
# Insertion on End
# Insertion on gaven Position


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        if temp == None:
            print("LinkList length is leas then 0")
        else:
            while temp:
                print(temp.data)
                temp = temp.next

    @property
    def length(self):
        temp = self.head
        i = 0
        if temp == None:
            print(i)
        else:
            while temp:
                i += 1
                temp = temp.next
            print(i)

    def insertStart(self, data: int) -> None:
        node = Node(data)
        node.next = self.head
        self.head = node
        print("New node added on Start")

    def insertEnd(self, data: int) -> None:
        temp = self.head
        while temp.next:
            temp = temp.next
        node = Node(data)
        temp.next = node
        print("New node added on End !")

    def insertOnPosition(self, position: int, data: int) -> None:
        temp = self.head
        for i in range(position-1):
            temp = temp.next
        pre = temp
        next = pre.next
        new = Node(data)
        pre.next = new
        new.next = next
        print("Inserted on position !")


s = SingleLinkedList()
n0 = Node(0)
s.head = n0

n1 = Node(1)
n0.next = n1

n2 = Node(2)
n1.next = n2

s.insertStart(10)
s.insertEnd(11)
s.insertOnPosition(2, 22)

s.display()
print("List length----->")
s.length
