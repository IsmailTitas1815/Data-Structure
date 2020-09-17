class Node:
    def __init__(self,node):
        self.node = node
        self.next = None
        # self.prev = None

class ReverseList:
    def __init__(self):
        self.head = None
        self.tail = None
        # self.size = 0

    def add_value(self,node):
        node = Node(node)

        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def rev_list(self):
        prev = None
        currentNode = self.head
        while currentNode is not None:
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next
        self.head = prev

    def __str__(self):
        vals=[]
        node = self.head
        while node is not None:
            vals.append(node.node)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


mylist = ReverseList()
mylist.add_value(1)
mylist.add_value(2)
mylist.add_value(3)
mylist.add_value(4)

mylist.rev_list()
print(mylist)
mylist.rev_list()
print(mylist)