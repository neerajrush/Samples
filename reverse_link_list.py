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
	follow_x = head
	while x:
		t = x
		x = x.next
		t.next = follow_x
		follow_x = t
	head = follow_x
	return head

def reverse_link_list(head):
	if not head or not head.next:
		return
	x = head.next
	head.next = None
	fwx = head
	while x:
		t = x
		x = x.next
		t.next = fwx
		fwx = t
	head = fwx
	return head

if __name__ == "__main__":
	head = Node(10)
	for i in range(10)[::-1]:
		head = insert_ll(head, Node(i))
	print_ll(head)
	print("------------")
	head = reverse_link_list(head)
	print_ll(head)
	print("------------")
	head = reverse_ll(head)
	print_ll(head)
	print("------------")
