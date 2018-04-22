
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def inOrder(root):
	if not root:
		return
	stack = []
	current = root
	while True:
		if current:
			stack.append(current)
			current = current.left
		else:
			if len(stack):
				node = stack.pop()
				print(node.data, " ", end="")
				current = node.right
			else:
				break
	print("")

def preOrder(root):
	if not root:
		return
	stack = []
	current = root
	while True:
		if current:
			print(current.data, " ", end="")
			stack.append(current)
			current = current.left
		else:
			if len(stack):
				node = stack.pop()
				current = node.right
			else:
				break
	print("")

def postOrder(root):
	if not root:
		return
	stack = []
	stack_post = []
	current = root
	stack_post.append(current)
	while True:
		if current:
			stack.append(current)
			current = current.right
			stack_post.append(current)
		else:
			if len(stack):
				node = stack.pop()
				current = node.left
				stack_post.append(current)
			else:
				break
	while len(stack_post):
		node = stack_post.pop()
		if node:
			print(node.data, " ", end="")
	print("")

def inOrder_r(root):
	if not root:
		return
	inOrder_r(root.left)
	print(root.data, " ", end="")
	inOrder_r(root.right)

def preOrder_r(root):
	if not root:
		return
	print(root.data, " ", end="")
	preOrder_r(root.left)
	preOrder_r(root.right)

def postOrder_r(root):
	if not root:
		return
	postOrder_r(root.left)
	postOrder_r(root.right)
	print(root.data, " ", end="")

# Driver program to test above function
 
""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#root = Node(10)
#root.left = Node(8)
#root.right = Node(2)
#root.left.left = Node(3)
#root.left.right = Node(5)
#root.right.left = Node(2)
#preOrder(root)
 
print("InOrder: ", end="")
inOrder(root)
print("InOrder_r: ", end="")
inOrder_r(root)
print("")
print("PreOrder: ", end="")
preOrder(root)
print("PreOrder_r: ", end="")
preOrder_r(root)
print("")

print("PostOrder: ", end="")
postOrder(root)
print("PostOrder_r: ", end="")
postOrder_r(root)
print("")
