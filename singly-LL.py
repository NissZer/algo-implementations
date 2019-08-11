class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return

        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def delete(self, value):
        currentNode = self.head
        while True:
            last_node = currentNode
            currentNode = currentNode.nextNode
            if currentNode.value == value:
                last_node.nextNode = currentNode.nextNode
                return 

    def printLL(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->", end =" ")
            currentNode = currentNode.nextNode
        print(None)

#testing
l1 = linkedList()
l1.printLL()
l1.insert("3")
l1.printLL()
l1.insert("5")
l1.printLL()
l1.insert("6")
l1.printLL()
l1.delete("5")
l1.printLL()

