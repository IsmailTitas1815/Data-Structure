class Node:
    def __init__(self,value):
        self.next = None
        self.prev = None
        self.val = value


class DoubleLinkedList:


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val)
        # print(node)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size +=1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def remove(self,value):
        currentnode = self.head
        while currentnode is not None:
            if currentnode.val == value:
                self.__remove_node(currentnode)
            currentnode = currentnode.next

    def __remove_node(self,node):
        if node.prev is None:
            self.head = node.next
            self.size-=1
        else:
            node.prev.next = node.next
            self.size-=1

        if node.next is None:
            self.tail = node.prev
            self.size-=1

        else:
            node.next.prev =  node.prev
            self.size-=1
    def removeLast(self):
        if self.tail.next is None:
            self.__remove_node(self.tail)

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{'. ' .join(str(val) for val in vals)}]"

my_list = DoubleLinkedList()
my_list.add(1)
my_list.add(6)
my_list.add(5)
my_list.add(3)
my_list.add(2)
my_list.add(9)
print(my_list)
my_list.remove(6)
print(my_list)
my_list.removeLast()
print(my_list)