class linkedListNode:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode

class DLL:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = linkedListNode(value)
        currentNode = self.head
        new_node.nextNode = None
        
        if self.head is None:
            new_node.prevNode = None
            self.head = new_node
            return
        while currentNode.nextNode:
            currentNode = currentNode.nextNode
        currentNode.nextNode = new_node
        new_node.prevNode = currentNode   

    def printDLL(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->", end=" ")
            currentNode = currentNode.nextNode
        print(None)

l1 = DLL()
l1.insert("5")
l1.insert("6")
l1.printDLL()
