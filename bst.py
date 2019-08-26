class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, value):
        if self.val == value:
            return False
        elif value < self.val:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        elif value > self.val:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
    
    def search(self, value):
        if value > self.val:
            if self.right:
                return self.right.search(value)
            else:
                return "Not found!"
        elif value < self.val:
            if self.left:
                return self.left.search(value)
            else:
                return "Not found!"
        else:
            return self

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()

