import queue
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def insert_node(root, data, label = "T"):
	if not root:
		return
	if data < root.data:
		if root.left:
			insert_node(root.left, data, label+"L")
		else:
			root.left = Node(data)
	elif data > root.data:
		if root.right:
			insert_node(root.right, data, label+"R")
		else:
			root.right = Node(data)
	print(label, root.data)

def build_tree(arr):
	if len(arr) == 0:
		return
	root = Node(arr[0])
	for i in range(1, len(arr)):
		insert_node(root, arr[i])
	return root

def print_inorder_r(root):
	if root:
		print_inorder_r(root.left)
		print(root.data, " ", end="")
		print_inorder_r(root.right)

def print_preorder_r(root):
	if root:
		print(root.data, " ", end="")
		print_preorder_r(root.left)
		print_preorder_r(root.right)

def print_postorder_r(root):
	if root:
		print_postorder_r(root.left)
		print_postorder_r(root.right)
		print(root.data, " ", end="")

def print_ancesters(root, data):
	if not root:
		return False
	if root.data == data:
		return True
	if print_ancesters(root.left, data) or print_ancesters(root.right, data):
		print(root.data)
		return True

def print_all_paths(root):
	if not root:
		return
	y_arr = []
	arr = [] 
	arr.append(root)
	while len(arr):
		node = arr.pop()
		y_arr.append(node.data)
		leaf_found = False
		if not node.left and not node.right:
			print(y_arr)
			y_arr.pop()
			leaf_found = True

		if node.left:
			arr.append(node.left)

		if node.right:
			arr.append(node.right)

x_arr = []
def print_all_paths_r(root):
	if not root:
		return False

	x_arr.append(root.data)

	if not root.left and not root.right:
		print(x_arr)
		x_arr.pop()
		return True

	l = print_all_paths_r(root.left)
	r = print_all_paths_r(root.right)

	if l or r:
		x_arr.pop()
	
	return l and r

def height(root):
	if not root:
		return 0
	if not root.left and not root.right:
		return 1
	l = height(root.left) + 1
	r = height(root.right) + 1
	return max(l, r)

def width(root, level = 0):
	if not root:
		return 0
	if level == 0 or level == 1:
		return 1
	elif level > 1:
		return width(root.left, level-1) + width(root.right, level-1)

def getMaxWidth(root):
	h = height(root)
	print("height: ", h)
	w = 0
	for l in range(1, h+1):
		x = width(root, l)
		w = max(w, x)
	return w

def width_q(root):
	if not root:
		return 0
	result = 0
	z_arr = queue.Queue() 
	z_arr.put(root)
	while not z_arr.empty():
		count = z_arr.qsize()
		result = max(count, result)
		while count:
			node = z_arr.get()
			if node.left:
				z_arr.put(node.left)
			if node.right:
				z_arr.put(node.right)
			count = count - 1
	return result

##########################
#           6
#         /   \ 
#        4     8
#      /  \   /  \
#     3    5 7    9
#   /  \
#  1    2
#########################

if __name__ == "__main__":
	arr = [6, 8, 7, 9, 4, 2, 5, 1, 3]
	root = build_tree(arr)
	print_preorder_r(root)
	print("")
	print_inorder_r(root)
	print("")
	print_postorder_r(root)
	print("")
	print("Ancesters of 5:")
	print_ancesters(root, 5)
	print("Ancesters of 7:")
	print_ancesters(root, 7)
	print("----- all paths to leaves ----")
	print_all_paths(root)
	print("----- all paths to leaves_r ----")
	print_all_paths_r(root)

	print("----- width ----")
	w = width(root, 4)
	print(w)

	print("----- width_q ----")
	w = width_q(root)
	print(w)

	print("----- height ----")
	h = height(root)
	print(h)

	print("----- MaxWidth ----")
	w = getMaxWidth(root)
	print(w)
