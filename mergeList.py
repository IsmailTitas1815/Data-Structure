from singlyMainFile import Node, LinkedList

def mergeLists(firstList,secondList,mergedList):

    currentFirst = firstList.head
    currentSecond = secondList.head
    while True:
        if currentFirst is None:
            mergedList.insertLast(currentSecond)
            break
        if currentSecond is None:
            mergedList.insertLast(currentFirst)
            break
        if currentFirst.data < currentSecond.data:
            currentFirstNext = currentFirst.next
            currentFirst.next = None
            mergedList.insertLast(currentFirst)
            currentFirst = currentFirstNext
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.insertLast(currentSecond)
            currentSecond = currentSecondNext

node = Node(1)
firstList = LinkedList()
node = Node(1)
firstList.insertLast(node)
node = Node(3)
firstList.insertLast(node)
node = Node(4)
firstList.insertLast(node)


secondList = LinkedList()
node = Node(2)
secondList.insertLast(node)
node = Node(7)
secondList.insertLast(node)
node = Node(9)
secondList.insertLast(node)

print("First List")
firstList.printList()
print("Second List")
secondList.printList()

mergedList = LinkedList()
mergeLists(firstList,secondList,mergedList)
del firstList
del secondList
print("Printing mergeList:")
mergedList.printList()


