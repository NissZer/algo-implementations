class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

def insert(value):
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

def search(value):
    if not self:
        return None
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
    return self

def inorder(self):
    if self.left:
        self.left.inorder()
    print(self.val)
    if self.right:
        self.right.inorder()

