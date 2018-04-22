from math import *

class Heap:
	def __init__(self, size, heap_type="min"):
		self.arr = [0] * size
		self.size = size
		self.count = 0
		self.heap_type = heap_type 

	def heapCount(self):
		return self.count

	def heapSize(self):
		return self.size

	def root(self):
		if self.size > 0:
			return self.arr[0]

	def parentIndex(self, idx):
		p = floor((idx - 1)/2)
		if p < 0:
			return 0
		else:
			return p

	def leftChildIndex(self, idx):
		return idx*2 + 1

	def rightChildIndex(self, idx):
		return idx*2 + 2

	def hasParent(self, idx):
		p = self.parentIndex(idx)
		if p >= 0 and p < self.size:
			return p
		else:
			return None

	def hasLeftChild(self, idx):
		l = self.leftChildIndex(idx)
		if l >= 1 and l < self.size:
			return l
		else:
			return None

	def hasRightChild(self, idx):
		r = self.leftChildIndex(idx)
		if r >= 2 and r < self.size:
			return r
		else:
			return None

	def getParent(self, idx):
		p = self.hasParent(idx)
		if p is not None:
			return self.arr[p]

	def getLeftChild(self, idx):
		l = self.hasLeftChild(idx)
		if l is not None:
			return self.arr[l]
		else:
			return None

	def getRightChild(self, idx):
		r = self.hasRightChild(idx)
		if r is not None:
			return self.arr[r]
		else:
			return None

	def add(self, data):
		if self.count <= self.size:
			self.arr[self.count] = data
			self.count += 1
			self.heapifyUp()
		else:
			print("error: heap full.")

	def remove(self):
		if self.count > 0:
			self.arr[0], self.arr[self.count-1] = self.arr[self.count-1], self.arr[0]
			self.heapifyDown()
			self.count -= 1
		else:
			print("error: heap empty.")

	def heapifyUp(self):
		if self.heap_type == "min":
			idx = self.count - 1
			while idx >= 0:
				if self.arr[idx] < self.getParent(idx):
					p = self.parentIndex(idx)
					self.arr[idx], self.arr[p] = self.arr[p], self.arr[idx]
				idx -= 1
		else:
			idx = self.count - 1
			while idx >= 0:
				if self.arr[idx] > self.getParent(idx):
					p = self.parentIndex(idx)
					self.arr[idx], self.arr[p] = self.arr[p], self.arr[idx]
				idx -= 1

	def heapifyDown(self):
		if self.heap_type == "min":
			idx = 0
			while idx < self.count - 1:
				l = self.leftChildIndex(idx)
				if l is not None and l < self.count-1 and self.arr[idx] > self.arr[l]:
					self.arr[idx], self.arr[l] = self.arr[l], self.arr[idx]

				r = self.rightChildIndex(idx)
				if r is not None and r < self.count-1 and self.arr[idx] > self.arr[r]:
					self.arr[idx], self.arr[r] = self.arr[r], self.arr[idx]

				idx += 1
		else:
			idx = 0
			while idx < self.count - 1:
				l = self.leftChildIndex(idx)
				if l is not None and l < self.count-1 and self.arr[idx] < self.arr[l]:
					self.arr[idx], self.arr[l] = self.arr[l], self.arr[idx]

				r = self.rightChildIndex(idx)
				if r is not None and r < self.count-1 and self.arr[idx] < self.arr[r]:
					self.arr[idx], self.arr[r] = self.arr[r], self.arr[idx]

				idx += 1

	def printNode(self, idx, depth=2):
		if idx < 0 or idx >= self.size:
			return

		lIdx = self.leftChildIndex(idx);
		rIdx = self.rightChildIndex(idx);
		if lIdx is not None:
			self.printNode(lIdx, depth+2)
		for i in range(depth):
			print("....", end="")
		print(self.arr[idx])
		if rIdx is not None:
			self.printNode(rIdx, depth+2)

	def printInOrder(self):
		if self.count == 0:
			return
		self.printNode(0)
		print("")

def heap_sort(arr):
	hx = Heap(len(arr), "min")
	for i in range(len(arr)):
		hx.add(arr[i])

	print("Top: ", hx.root(), " Count: ", hx.heapCount(), " InOrder: ")
	hx.printInOrder()

	print("....... sorted array.. ")
	for i in range(len(arr)):
		print(hx.root(), " ", end="")
		hx.remove()
	print("....... sorted array ..done. ")

	#print("Top: ", hx.root(), " Count: ", hx.heapCount(), " InOrder: ", end="")
	#hx.printInOrder()

	#hx.add(1)

	#print("Top: ", hx.root(), " Count: ", hx.heapCount(), " InOrder: ", end="")
	#hx.printInOrder()
		
	return hx.arr

if __name__ == "__main__":
	arr = [ 3, 6, 14, 1, 12, 9, 15, 7, 5, 10, 2, 13, 4, 11, 8]
	print("Input: ", arr, " size: ", len(arr))
	arr = heap_sort(arr)
	print("Output: ", arr, " size: ", len(arr))
