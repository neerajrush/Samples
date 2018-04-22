class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def insert_node(root, data):
	if not root:
		root = Node(data)
	if data < root.data:
		if not root.left:
			root.left = Node(data)
		else:
			insert_node(root.left, data)
	elif data > root.data:
		if not root.right:
			root.right = Node(data)
		else:
			insert_node(root.right, data)
	else:
		return root

def add_node_to_right(root, data):
	if not root:
		return
	node = root
	while node.right:
		node = node.right
	node.right = Node(data)

def build_tree(arr):
	if len(arr) == 0:
		return None
		
	root = Node(arr[0])

	for i in range(1, len(arr)):
		insert_node(root, arr[i])

	return root

def print_tree(root, depth = 10, sx = "T"):
	if not root:
		return
	print(sx, end="")
	for i in range(depth):
		print(" ", end="")
	print(root.data)
		
	if root.left:
		print_tree(root.left, depth-2, sx+"L")
	if root.right:
		print_tree(root.right, depth+2, sx+"R")

def find_min_height(root):
	if not root:
		return 0
	if not root.left and not root.right:
		return 1
	if not root.left:
		return find_min_height(root.right) + 1
	if not root.right:
		return find_min_height(root.left) + 1
	return min(find_min_height(root.left), find_min_height(root.right)) + 1

def find_max_height(root):
	if not root:
		return 0
	if not root.left and not root.right:
		return 1
	if not root.left:
		return find_max_height(root.right) + 1
	if not root.right:
		return find_max_height(root.left) + 1
	return max(find_max_height(root.left), find_max_height(root.right)) + 1

def isLeftSubTreeLesser(root, pData):
	if not root:
		return True
	if root.data < pData and isLeftSubTreeLesser(root.left, root.data):
		return True
	return False

def isRightSubTreeGreater(root, pData):
	if not root:
		return True
	if root.data > pData and isRightSubTreeGreater(root.right, root.data):
		return True
	return False

def isBST(root):
	if not root:
		return True
	if isLeftSubTreeLesser(root.left, root.data) and isRightSubTreeGreater(root.right, root.data) and isBST(root.left) and isBST(root.right):
		return True

	return False

if __name__ == "__main__":
	print("------------------")
	arr = [ 5, 3, 7, 6, 2, 4, 8, 9, 11]
	root = build_tree(arr)
	print_tree(root)
	minH = find_min_height(root)
	print("Min Height: ", minH)
	maxH = find_max_height(root)
	print("Max Height: ", maxH)
	bstTest = isBST(root)
	print("isBST: :", bstTest)
	print("----- Messing up BST ------------")
	add_node_to_right(root, 1)
	print_tree(root)
	minH = find_min_height(root)
	print("Min Height: ", minH)
	maxH = find_max_height(root)
	print("Max Height: ", maxH)
	bstTest = isBST(root)
	print("isBST: :", bstTest)
	print("------------------")
