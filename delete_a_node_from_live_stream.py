class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def insert_ll(head, node):
	if not head:
		head = node	
		return
	node.next = head
	head = node
	return head

def print_ll(head):
	tmp = head
	while tmp:
		print(tmp.data, ' ', end="")
		tmp = tmp.next
	print("")

def delete_a_node(node):
	if not node:
		return
	print("Node to be deleted: ", node.data)
	tmp = node.next
	if tmp:
		node.data = tmp.data
		node.next = tmp.next
	else:
		print("last node in the list. Can't be deleted")

if __name__ == "__main__":
	head = Node(10)
	for i in range(10)[::-1]:
		head = insert_ll(head, Node(i))
	print_ll(head)
	print("------------")
	node = head.next
	node = node.next
	node = node.next
	node = node.next
	node = node.next
	node = node.next
	node = node.next
	node = node.next
	node = node.next
	node = node.next
	delete_a_node(node)
	print_ll(head)
	print("------------")
