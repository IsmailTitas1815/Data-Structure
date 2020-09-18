from LinkedList.doubly import DoubleLinkedList

class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList


    def push(self,value):
        print(value)
        self.__list.add(value)

    def pop(self):
        val = self.__list.back()
        self.__list.removeLast()
        return val

    def is_empty(self):
        return self.__list.size == 0

    def peek(self):
        return self.__list.back()

    def __len__(self):
        return self.__list.size

    # def __str__(self):
    #     val = []
    #     currentNode = self.__list.head
    #     while currentNode is not None:
    #         val.append(currentNode)
    #         currentNode = currentNode.next



mystack_list = Stack()
mystack_list.push("titas")
print(len(mystack_list))


