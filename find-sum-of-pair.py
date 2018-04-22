########################
#         10
#       8   12
#     6  9 13 14
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

def find_pair_sum(root, given_num):
	if not root or not root.left or not root.right:
		return
	l = root.left.data
	r = root.right.data
	if l + r == given_num:
		print("Given sum: ", given_num, " pair: ", root.left.data, root.right.data)
	else:
		find_pair_sum(root.left, given_num)
		find_pair_sum(root.right, given_num)

if __name__ == "__main__":
	n1 = Node(10)
	n2 = Node(8)
	n3 = Node(12)
	n4 = Node(6)
	n5 = Node(9)
	n6 = Node(13)
	n7 = Node(14)
	
	root = n1
	
	root.insert_left(n2)
	root.insert_right(n3)
	n2.insert_left(n4)
	n2.insert_right(n5)
	n3.insert_left(n6)
	n3.insert_right(n7)
	
	print_tree(root)
	find_pair_sum(root, 15)
	find_pair_sum(root, 20)
