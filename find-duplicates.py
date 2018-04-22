########################
#         1
#       3   5
#          3  4
########################

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def insert_left(self, node):
		self.left = node	

	def insert_right(self, node):
		self.right = node	

def print_tree(root, depth=10):
	if root is None:
		return
	for i in range(depth):
		print(" ", end="")
	print(root.data)
	print_tree(root.left, depth-2)
	print_tree(root.right, depth+2)

def visit_node(node, dupes):
	if node is None:
		return

	if node.data in dupes:
		print("dupes: ", node.data)
	else:
		dupes[node.data] = 1

	visit_node(node.left, dupes)
	visit_node(node.right, dupes)

def find_dupes(root):
	if root is None:
		return
	dupes = {}
	visit_node(root, dupes)

if __name__ == "__main__":
	n1 = Node(1)
	n2 = Node(3)
	n3 = Node(5)
	n4 = Node(3)
	n5 = Node(4)
	n6 = Node(2)
	n7 = Node(5)
	
	n1.insert_left(n2)
	n1.insert_right(n3)
	n3.insert_left(n4)
	n3.insert_right(n5)
	n5.insert_left(n6)
	n5.insert_right(n7)
	
	print_tree(n1)
	find_dupes(n1)
