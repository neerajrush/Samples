def heapifyMax(heap):
	for k in range(len(heap))[::-1]:
		if k > 0 and heap[k] > heap[k-1]:
			heap[k], heap[k-1] = heap[k-1], heap[k]

def heapifyMin(heap):
	#print("INPUT: ", heap)
	for k in range(len(heap))[::-1]:
		if k > 0 and heap[k] < heap[k-1]:
			heap[k], heap[k-1] = heap[k-1], heap[k]
	#print("OUTPUT: ", heap)

def longest_path(xlist, k):
	if k < 1 or len(xlist) < 1:
		return None

	heap = [0] * k
	idx = 0
	heap_set = False
	while idx < len(xlist):
		if heap_set is False:
			for i in range(k):
				heap[i] = xlist[idx]
				idx += 1
			heap_set = True
		else:
			heap[0] = xlist[idx]
			idx += 1
		heapifyMin(heap)
	return heap[1:]


def shortest_path(xlist, k):
	if k < 1 or len(xlist) < 1:
		return None

	heap = [0] * k
	idx = 0
	heap_set = False
	while idx < len(xlist):
		if heap_set is False:
			for i in range(k):
				heap[i] = xlist[idx]
				idx += 1
			heap_set = True
		else:
			heap[0] = xlist[idx]
			idx += 1
		heapifyMax(heap)
	return heap[1:]

if __name__ == "__main__":
	print("---------------------")
	xlist = [ 1, 12, 5, 6, 3, 7, 9, 2, 11, 18, 8]
	k = 5
	print("List: ", xlist, " k: ", k)
	slist = shortest_path(xlist, k+1)
	print("Shorted path k-items: ", slist)
	print("---------------------")
	xlist = [ 1, 12, 5, 6, 3, 7, 9, 2, 11, 18, 8]
	slist = longest_path(xlist, k+1)
	print("Longest path k-items: ", slist)
	print("---------------------")
