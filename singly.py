class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, node):
        temp = self.head
        self.head = node
        self.head.next = temp
        del temp
    def listLength(self):
        currentNode = self.head
        count = 1
        while currentNode.next is not None:
            count+=1
            currentNode = currentNode.next
        return count
    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def middleinsertion(self,node,position):
        if position == 1:
            self.insertHead(node)
            return
        elif 0 < position > self.listLength():
             # return f"Invalid Position inserted"
            print("invalid position")
            return
        count = 1
        temp = self.head
        while True:
            if count is not position:
                count+=1
                prev = temp
                temp = temp.next
            else:
                prev.next = node
                node.next = temp
                break

    def insertLast(self, node):
        if self.head is None:
            self.head = node
        else:
            last = self.head
            while True:
                if last.next is None:
                    break
                else:
                    last = last.next
            last.next = node

    def delete(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def deleteMiddle(self,position):
        if 0 < position > self.listLength():
            print("Invalid position")
            return
        # if self.isListEmpty() is False:
        #     if position is 1:


        currentNode = self.head
        currentPosition = 1
        while True:
            if currentPosition is position:
                previousNode.next = currentNode.next
                currentNode= None
                break

            else:
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition+=1

    def print(self):
        if self.head is None:
            print("Nothing is in the list")
            return
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next

obj = LinkedList()
node = Node(1)
obj.insertLast(node)
node = Node(2)
obj.insertLast(node)
node = Node(3)
obj.insertLast(node)
node = Node(4)
obj.insertLast(node)
node = Node(5)
obj.insertLast(node)
node = Node("Titas")
obj.insertLast(node)
node = Node("Ismail")
obj.middleinsertion(node,2)
headnode = Node("Head")
obj.insertHead(headnode)
obj.delete()
obj.deleteMiddle(3)
node = Node("Ok")
obj.middleinsertion(node,1)
node = Node("Ok")
obj.middleinsertion(node,10)
obj.print()
print(f"List length is {obj.listLength()}")