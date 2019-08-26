class LinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

class DLL:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = LinkedListNode(value)
        current_node = self.head
        new_node.next_node = None
        
        if self.head is None:
            new_node.prev_node = None
            self.head = new_node
            return
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        new_node.prev_node = current_node   

    def printDLL(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, "->", end=" ")
            current_node = current_node.next_node
        print(None)
        
