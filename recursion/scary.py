"""
This is your future >:)
"""

class Node:
    """"
    A node in a linked list. Each node has some data and a pointer to the next node.

    This is a linked list: A -> B -> C -> D -> None
    """
    def __init__(self, data="", next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, data):
        self.data = data
    def setNext(self, next):
        self.next = next

def printList(node: Node):
    """"
    Print the data in a linked list starting from the given node.
    """
    if node != None:
        print(node.data)
        printList(node.next)

head = Node("A", Node("B", Node("C", Node("D"))))
printList(head)