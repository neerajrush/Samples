##############################
#LISP - > LUMP -> LIMP -> LIKE 
#
#        (null)
#        /
#       L
#      / \
#     I   U
#    / \ / 
#   K   M 
#  /   /
# E   P
#
##############################

ALPHA_SIZE = 26

class Node:
	def __init__(self, data = ""):
		self.data = data
		self.children = [None] * ALPHA_SIZE
		self.isEOW = False

def insert(node, key):
	pCrawl = node
	for i in range(len(key)):
		index = ord(key[i]) - ord('A')
		if not pCrawl.children[index]: 
			pCrawl.children[index] = Node(key[i])
		pCrawl = pCrawl.children[index]
	pCrawl.isEOW = True

def search(node, key):
	pCrawl = node
	for i in range(len(key)):
		index = ord(key[i]) - ord('A')
		if not pCrawl.children[index]: 
			return False
		pCrawl = pCrawl.children[index]

	if pCrawl and pCrawl.isEOW:
		return True

def print_trie(node, depth = 0):
	if not node:
		return
	idx = 0
	while idx < depth:
		print(" ", end="")
		idx += 1
	print(node.data)
	if node.isEOW:
		return
	for i in range(ALPHA_SIZE):
		if node.children[i]:
			print_trie(node.children[i], depth+2)

def traverse_BFS(node):
	words_list = list() 
	if not node: 
		return words_list
	node_q = [node]	
	while node_q:
		curr_node = node_q.pop()
		words_list.append(curr_node.data)
		if curr_node.isEOW:
			words_list.append('*')
		for i in range(ALPHA_SIZE):
			if curr_node.children[i]:
				node_q.append(curr_node.children[i])
	return  words_list

def print_path(node, start_word, end_word):
	if not node or node.isEOW:
		return
	idx = 0
	prefix = ""
	words_list = [] 
	top_node = node
	while idx < len(start_word):
		if start_word[idx] != end_word[idx]:
			break 
		node = node.children[ord(start_word[idx]) - ord('A')]
		prefix += start_word[idx]
		idx += 1
	words_list = traverse_BFS(top_node)
	print(words_list)

if __name__ == "__main__":
	root = Node()
	insert(root, "LISP")
	insert(root, "LIMP")
	insert(root, "LIST")
	insert(root, "LUMP")
	insert(root, "LIKE")
	print_trie(root)
	print("-----------------")
	print(search(root, "LISP"))
	print(search(root, "LIMP"))
	print(search(root, "LIST"))
	print(search(root, "LUMP"))
	print(search(root, "LIKE"))
	print(search(root, "LIKES"))
	print("-----------------")
	start_word = "LISP"
	end_word = "LIKE"
	print_path(root, start_word, end_word)
	print("-----------------")
