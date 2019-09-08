class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

def insert(root, value):
    if not root:
        return Node(value)

    if root.val == value:
        return root

    if value < root.val:
        root.left = insert(root.left, value)
    elif value > root.val:
        root.right = insert(root.right, value)

    return root

def search(root, value):
    if not root:
        return None

    if value == root.val:
        return root

    if value > root.val:
        return search(root.right, value)
    else:
        return search(root.left, value)


def inorder(self):
    if self.left:
        self.left.inorder()
    print(self.val)
    if self.right:
        self.right.inorder()

