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

    def remove(self,position):
        pos = 1
        currentnode = self.head
        while currentnode is not None:
            if position == pos:
                if position == 1:
                    self.head = currentnode.next
                    # self.tail = currentnode.next
                    # currentnode = None

                    break
                elif currentnode.next is None:
                    self.tail = currentnode.prev
                    # currentnode = None


                    # currentnode = None
                    # self.tail = previousnode
                    break
                else:
                    # nextNode = currentnode.next
                    # previousnode.next = nextNode
                    # nextNode.prev = previousnode
                    previousnode.next = currentnode.next
                    currentnode.next.prev = previousnode
                    break

            else:
                previousnode = currentnode
                currentnode = currentnode.next
                pos+=1



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
# my_list.remove(4)
# print(my_list.size)
my_list.remove(6)
# my_list.remove(4)
# my_list.remove(5)
# my_list.remove(4)
# my_list.remove(4)
# print(my_list.tail.value)
print(my_list)