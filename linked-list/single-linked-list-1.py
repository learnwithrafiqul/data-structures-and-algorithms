

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is Empty !")
        temp = self.head
        while temp:
            print(temp.data, end=" ---> ")
            print('\n')
            temp = temp.next


s = SingleLinkedList()
n0 = Node(0)
s.head = n0
n1 = Node(1)
n0.next = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
s.display()
