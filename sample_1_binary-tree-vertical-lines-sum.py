#Input:
# 1:      
#  -2 -1 0  1  2
#        1
#       /  \
#     2      3
#    /  \   /  \
#   4    5 /    \  
#         /      \
#        7        6
#
#Output:
#
#-2 : 4
#-1 : 2
# 0 : 13
# 1 : 3
# 2 : 6

#Input:
# 2:      
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

	def printNode(self, typeNode = "P", spCount = 20):
		if self is None:
			return
		print(typeNode, ": ", end= "")
		for x in range(spCount):
			print(" ", end = "")
		print(self.data)

	def printConnections(self):
		if self.left is not None:
			self.left.printConnections()
		lData = None
		if self.left is not None:
			lData = self.left.data
		rData = None
		if self.right is not None:
			rData = self.right.data
		print("Node: ", self.data, "Left: ", lData, "Right: ", rData)
		if self.right is not None:
			self.right.printConnections()

class BTree:
	def __init__(self, data):
		self.root = data
		self.lArm = 0
		self.rArm = 0

	def addNode(self, data):
		if self.root is None:
			self.root = Node(data)
			return

		node = self.root
		if (self.lArm == self.rArm):
			while node.left is not None:
				node = node.left
			node.left = Node(data)
			self.lArm += 1
		else:
			while node.right is not None:
				node = node.right
			node.right = Node(data)
			self.rArm += 1

	def printTree(self, typeNode = "P", spCount = 20):
		node = self.root
		node.printNode()
		while node.left is not None:
			node = node.left
			spCount -= 2
			node.printNode("L", spCount)

		node = self.root
		spCount = 20
		while node.right is not None:
			node = node.right
			spCount += 2
			node.printNode("R", spCount)

def buildBinaryTree(arr):
	btree = BTree(None)
	for i in arr:
		print(i)
		btree.addNode(i)
	return btree

def verticalSum(btree):
	vSum = 0
	node = btree.root	
	key = 0
	verticals = { key : node.data }
	while node.left is not None:
		key -= 1
		if verticals.get(key) is not None:
			verticals[key] += node.data
		else:
			verticals.update({ key: node.data })
		if node.right is not None:
			key += 1
			if verticals.get(key) is not None:
				verticals[key] += node.data
			else:
				verticals.update({ key: node.data })
		node = node.left

	node = btree.root	
	while node.right is not None:
		key += 1
		if verticals.get(key) is not None:
			verticals[key] += node.data
		else:
			verticals.update({ key: node.data })
		if node.left is not None:
			key -= 1
			if verticals.get(key) is not None:
				verticals[key] += node.data
			else:
				verticals.update({ key: node.data })
		node = node.right

	for k, v in verticals.items():
		print(k, "==>", v)
		vSum = max(vSum, v)

	return vSum

if __name__=='__main__':
    print ("-------------------")
    arr1 = [1, 2, 3, 4, 5, 7, 6]
    x = buildBinaryTree(arr1)
    x.root.printConnections()
    x.printTree()
    verticalSum(x)
    print ("-------------------")
