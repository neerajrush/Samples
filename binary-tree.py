#----------------------------------------------------
def bubbleSort(arr):
	for i in range (1, len(arr)):
		j = i-1 
		k = i
		while j >= 0 and arr[j] > arr[k]:
			arr[k], arr[j] = arr[j], arr[k]
			j -= 1
			k -= 1
	return arr
#----------------------------------------------------
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 1

	def calcHeight(self):
		if self is None:
			return 0
		h1 = 0
		h2 = 0
		if self.left is not None:
			h1 += self.left.calcHeight()
		if self.right is not None:
			h2 += self.right.calcHeight()

		if abs(h1 - h2) > 1:
			return -1

		if h1 > h2:
			return h1 + 1
		else:
			return h2 + 1

	def isBalanced(self):
		if self is None:
			return True

		h = self.calcHeight()

		if h < 0:
			return False

		return True

	def getHeight(self):
		if self is None:
			return 0
		h1 = 0
		h2 = 0
		if self.left is not None:
			h1 = 1 + self.left.getHeight()
			print("Left Height: ", h1)

		if self.right is not None:
			h2 = 1 + self.right.getHeight()
			print("Right Height: ", h2)

		return max(h1, h2)

	def insert(self, data):
		print("self data: ", self.data, data)
		if data < self.data:
			if self.left is None:
				self.left = Node(data)
			else:
				self.left.insert(data)
		else:
			if self.right is None:
				self.right = Node(data)
			else:
				self.right.insert(data)

		self.height += self.getHeight()

		flag = self.isBalanced()

		print("isBalanced: ", flag, " Height: ", self.height)

	def printInOrder(self):
		if self is None:
			return

		if self.left is not None:
			self.left.printInOrder()

		print(self.data)

		if self.right is not None:
			self.right.printInOrder()

	def printPreOrder(self):
		if self is None:
			return
		print(self.data)

		if self.left is not None:
			self.left.printPreOrder()

		if self.right is not None:
			self.right.printPreOrder()

	def printPostOrder(self):
		if self is None:
			return

		if self.left is not None:
			self.left.printPostOrder()

		if self.right is not None:
			self.right.printPostOrder()

		print(self.data)

	def printTree(self, depth = 0):
		if self is None:
			return

		if self.left is not None:
			self.left.printTree(depth+2)
		for i in range(depth+1):
			print("....",  end="")

		print(self.data)

		if self.right is not None:
			self.right.printTree(depth+2)

def binaryTree(arr):
	root = None
	for i in range(len(arr)):
		if root is None:
			root = Node(arr[i])
		else:
			root.insert(arr[i])
	return root

data_arr = []
def print_all_paths(root):
	if not root:
		return False

	data_arr.append(root.data)

	if not root.left and not root.right:
		print(data_arr)
		data_arr.pop()
		return True

	l = print_all_paths(root.left)
	r = print_all_paths(root.right)

	if l or r:
		data_arr.pop()

	return l and r
		
if __name__ == "__main__":
	arr = [ 3, 5, 1, 7, 8, 4, 9, 6, 2 ]
	arr = bubbleSort(arr)
	print("Given list: ", arr)
	print("----------------------")
	arr = [ 7, 5, 1, 3, 8, 4, 9, 6, 2 ]
	tree = binaryTree(arr)
	print("----------------------")
	print("Binary Tree (InOrder): ")
	tree.printInOrder()
	print("----------------------")
	print("Binary Tree (PreOrder): ")
	tree.printPreOrder()
	print("----------------------")
	print("Binary Tree (PostOrder): ")
	tree.printPostOrder()
	print("----------------------")
	print("Binary Tree (isBalanced): ", tree.isBalanced(), " Height: ", tree.height)
	print("----------------------")
	print("Binary Tree (root): ", tree.data)
	tree.printTree()
	print("----------------------")
	print("Print All Paths: ", tree.data)
	print_all_paths(tree)
	print("----------------------")
