class Node:
        def __init__(self, data:int = None):
            self.data = data
            self.next = None

def insert(data:int):
    pass

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data:int):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, data:int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def printData(self):
        temp = self.head

        while temp is not None:
            print(temp.data)
            temp = temp.next

linkedlist = LinkedList()
linkedlist.push(20)

linkedlist.push(30)
linkedlist.push(40)

linkedlist.printData()