import queue
q = queue

color_l = ['white'] * 10
depth_l = [0] * 10
parent_l = [None] * 10

def BSF(graph):
	root_node = 0
	color_l[root_node] = 'gray'
	depth_l[root_node] = 1 
	parent_l[root_node] = None 
	child_nodes = graph[root_node]
	q.push(root_node)
	while len(q) > 0:
		print(q)


#########################################
# Graph: 1->(2,3) 2->(1, 4, 5), 3->(1, 5), 4->(2, 5, 6), 5->(3, 4, 6), 6->(4, 5)
#       1 
#     /   \
#    2     3
#    | \   |
#    |  \  |
#    |   \ | 
#    4 --- 5
#     \   /
#       6 
#########################################

if __name__== "__main__":
	print("--------------------------------")
	arr = [{}] * 10
	arr[0] = { }
	arr[1] = { 2, 3 }
	arr[2] = { 1, 4, 5 }
	arr[3] = { 1, 5 }
	arr[4] = { 2, 5, 6 }
	arr[5] = { 2, 3, 4, 6 }
	arr[6] = { 4, 5 }
	print(arr)
	print("--------------------------------")
