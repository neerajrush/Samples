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

def reverse_ll(head):
	if not head or not head.next:
		return
	x = head.next
	head.next = 0
	fx = head
	while x:
		t = x
		x = x.next
		t.next = fx
		fx = t
	head = fx
	return head

if __name__ == "__main__":
	head = Node(10)
	for i in range(10)[::-1]:
		head = insert_ll(head, Node(i))
	print_ll(head)
	print("------------")
	head = reverse_ll(head)
	print_ll(head)
	print("------------")
