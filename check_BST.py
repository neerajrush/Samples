class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data, label="+"):
    if not root:
        root = Node(data)
        print(label, data)
        return
    if root.data == data:
        print(label, data)
        return
    if root.data > data:
        if root.left:
            insert(root.left, data, label+"L")
        else:
            print(label+"L:", data)
            root.left = Node(data)
    elif root.data < data:
        if root.right:
            insert(root.right, data, label+"R")
        else:
            print(label+"R:", data)
            root.right = Node(data)

def print_tree(root, depth):
    if not root:
        return
    for x in range(depth): 
        print(" ", end="")
    print(root.data)
    if root.left:
        print_tree(root.left, depth-2)
    if root.right:
        print_tree(root.right, depth+2)

min_x = 0
max_x = 0

def checkBST(root):
    if not root:
        return True
    if root.left:
       if root.left.data >= root.data:
           return False
    if root.right:
       if root.right.data <= root.data:
           return False
    return checkBST(root.left) and checkBST(root.right)

if __name__ == "__main__":
    root = Node(8)
    insert(root, 2)
    insert(root, 9)
    insert(root, 15)
    insert(root, 1)
    insert(root, 3)
    insert(root, 5)
    insert(root, 7)
    insert(root, 4)
    insert(root, 10)

    print_tree(root, 20)

    if root:
        min_x = root.data
        max_x = root.data

    x = checkBST(root)
    print(x)
