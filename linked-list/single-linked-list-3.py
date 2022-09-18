# Deleting on Begining
# Deleting on End
# Deleting on gaven Position

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

    def deletingStart(self) -> None:
        temp = self.head
        self.head = temp.next
        temp.next = None
        print("Start value is deleted !")

    def deletingEnd(self) -> None:
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        print("End value is deleted")

    def deletingOnPosition(self, position: int) -> None:
        temp = self.head.next
        prev = self.head
        for i in range(position-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None


s = SingleLinkedList()
n0 = Node(0)
s.head = n0
n1 = Node(1)
n0.next = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n5 = Node(5)
n4.next = n5

# s.deletingStart()
# s.deletingEnd()
s.deletingOnPosition(2)

s.display()
print("List length----->")
s.length
