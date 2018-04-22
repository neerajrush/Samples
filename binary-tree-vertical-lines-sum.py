#Input:
# 1:      
#  -2 -1 0  1  2
#        1
#       /  \
#     2      3
#    /  \   /  \
#   4    5 /    \  
#         /      \
#        6        7

#Output:
#
#-2 : 4
#-1 : 2
# 0 : 12
# 1 : 3
# 2 : 7

#Input:
#
#        1
#       /  \
#     2      3
#    /  \   /  \
#   4    7 /    \  
#         /      \
#        5        6

#Output:
#
#-2 : 4
#-1 : 2
# 0 : 13
# 1 : 3
# 2 : 6
#{0: 13, 1: 3, 2: 6, -2: 4, -1: 2}

#Input:
# 3:      
#  -2 -1 0  1  2
#        10
#       /  \
#     7      8
#    /  \   /  \
#   3    5 /    \  
#         /      \
#        6        4
#
#Output:
#
#-2 : 3
#-1 : 7
# 0 : 21
# 1 : 8
# 2 : 4

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.lArm = 0
		self.rArm = 0

	def printNode(self):
		if self.left is not None:
			self.left.printNode()
		lData = None
		if self.left is not None:
			lData = self.left.data
		rData = None
		if self.right is not None:
			rData = self.right.data
		print("Node: ", self.data, "Left: ", lData, "Right: ", rData, "lArm: ", self.lArm, "rArm: :", self.rArm)
		if self.right is not None:
			self.right.printNode()

	def printTree(self, typeNode = "P:", spaceCount = 20):
		print(typeNode, end="")
		for x in range(spaceCount):
			print(" ", end="")
		print(self.data)
		node = self.left
		if node is not None:
			node.printTree("L:", (spaceCount-2))

		node = self.right
		if node is not None:
			node.printTree("R:", (spaceCount+2))

	def addNode(self, node):
		if self.left is None:
			self.left = node
			self.lArm += 1
			return
		else:
			if self.right is None:
				self.right = node
				self.rArm += 1
				return
		if self.lArm == self.rArm:
			self.lArm += 1
			self.left.addNode(node)
		else:
			self.rArm += 1
			self.right.addNode(node)

def findMinMaxOfBTree(node, minimum, maximum, horizontal_distance):
	if node is None:
		horizontal_distance = 0
	return

	if horizontal_distance < minimum[0]:
		minimum[0] = horizontal_distance
	elif horizontal_distance > maximum[0]:
		maximum[0] = horizontal_distance

	findMinMaxOfBTree(node.left, minimum, maximum, horizontal_distance-1)
	findMinMaxOfBTree(node.right, minimum, maximum, horizontal_distance+1)

def buildBinaryTree(arr):
	root = None
	for x in arr:
		print(x)
		if root is None:
			root = Node(x)
		else:
			root.addNode(Node(x))
	return root

def verticalSum(node, key):
	vSum = 0
	if node is None:
		return vSum
	else:
		if verticals.get(key) is None:
			verticals.update({ key : node.data })
		else:
			verticals[key] += node.data

	if node.left is not None:
		key -= 1
		verticalSum(node.left, key)
		key += 1
	if node.right is not None:
		key += 1
		verticalSum(node.right, key)

if __name__=='__main__':
	verticals = { }
	print ("-------------------")
	arr1 = [1, 2, 3, 4, 5, 7, 6]
	x = buildBinaryTree(arr1)
	x.printNode()
	x.printTree()
	hd = 0
	minx = [0]
	maxx = [0]
	print("HD: ", hd, "Min: ", minx, "Max: ", maxx) 
	findMinMaxOfBTree(x, minx, maxx, hd)
	print("HD: ", hd, "Min: ", minx, "Max: ", maxx) 
	y = verticalSum(x, 0)
	print(verticals, y)
	print ("-------------------")
