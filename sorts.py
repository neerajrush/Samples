def insertionSort(arr):
	for i in range (1, len(arr)):
		value = arr[i]
		k = i
		while k > 0 and arr[k-1] > value:
			arr[k] = arr[k-1]
			k = k-1
		arr[k] = value

def insertionSort2(arr, n):
	for i in range (1, n):
		for j in range(i):
			if arr[i] < arr[j]:
				tmp = arr[i]
				k = i
				while k > j:
					arr[k] = arr[k-1]
					k -= 1
				arr[j] = tmp
		print("Y arr: ", arr)

def bubbleSort(arr, n):
	for i in range (1, n):
		j = i-1 
		k = i
		while j >= 0 and arr[j] > arr[k]:
			arr[k], arr[j] = arr[j], arr[k]
			j -= 1
			k -= 1

def selectionSort(arr, n):
	for i in range (0, n):
		print("X arr: ", arr)
		least = i
		for j in range (i+1, n):
			if arr[j] < arr[least]:
				least = j
		if least != i:
			arr[least], arr[i] = arr[i], arr[least]
		print("Y arr: ", arr)

def swap( A, x, y ):
	tmp = A[x]
	A[x] = A[y]
	A[y] = tmp

def selectionSortX( arr, n ):
	for i in range( n ):
		least = i
		print("X arr: ", arr)
		for k in range( i + 1 , n ):
			if arr[k] < arr[least]:
				least = k

		swap( arr, least, i )
		print("Y arr: ", arr)

def merge(left, right):
	result = [0] * (len(left) + len(right))
	l = 0
	r = 0
	s = 0
	while l < len(left) and r < len(right):
		if left[l] <= right[r]:
			result[s] = left[l]
			l += 1
		else:
			result[s] = right[r]
			r += 1
		s += 1

	while l < len(left):
		result[s] = left[l]
		l += 1
		s += 1

	while r < len(right):
		result[s] = right[r]
		r += 1
		s += 1

	return result

def mergeSort(arr):
	if len(arr) <= 1:
		return arr

	middle = int (len(arr)/2)

	l_size = middle
	r_size = len(arr) - middle

	left = [0] * l_size
	right = [0] * r_size

	for i in range(l_size):
		left[i] = arr[i]

	for i in range(r_size):
		right[i] = arr[i+middle]

	left  = mergeSort(left)
	right = mergeSort(right)

	return merge(left, right)

def heapSort(arr, n):
	for i in range (0, n):
		for j in range(i,n):
			if arr[i] < arr[j]:
				tmp = arr[i]
				arr[i] = arr[j]
				arr[j] = tmp 

def divide(arr, begin, end):
	pivot = arr[end]
	i = begin - 1
	for j in range(begin, end):
		if arr[j] <= pivot:
			i += 1	
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[end] = arr[end], arr[i+1]
	print(arr, i+1)
	return i + 1

def quick_sort(arr, begin, end):
	if begin >= end:
		return

	partition = divide(arr, begin, end);
	quick_sort(arr, begin, partition - 1)
	quick_sort(arr, partition + 1, end)

def qSort(arr):
	if len(arr) <= 1:
		return
	quick_sort(arr, 0, len(arr)-1)

if __name__ == "__main__":
	print("----------------------")
	arr1 = [ 3, 4, 6, 2, 5, 7, 1]
	print("arr: ", arr1)
	qSort(arr1)
	print("Quick: arr: ", arr1)
	print("----------------------")
	arr1 = [ 3, 4, 6, 2, 5, 7, 1]
	print("arr: ", arr1)
	insertionSort(arr1)
	print("InsertionSort: arr: ", arr1)
	print("----------------------")
	arr1 = [ 3, 4, 6, 2, 5, 7, 1]
	print("arr: ", arr1)
	insertionSort2(arr1, len(arr1))
	print("InsertionSort2: arr: ", arr1)
	print("----------------------")
	arr1 = [ 3, 4, 6, 2, 5, 7, 1]
	print("arr: ", arr1)
	bubbleSort(arr1, len(arr1))
	print("BubbleSort: arr: ", arr1)
	print("----------------------")
	arr1 = [ 3, 4, 6, 2, 5, 7, 1]
	print("arr: ", arr1)
	selectionSort(arr1, len(arr1))
	print("SelectionSort: arr: ", arr1)
	print("----------------------")
	arr1 = [ 3, 4, 6, 2, 5, 7, 1]
	print("arr: ", arr1)
	selectionSortX(arr1, len(arr1))
	print("SelectionSortX: arr: ", arr1)
	print("----------------------")
	arr1 = [ 3, 4, 6, 2, 5, 7, 1]
	print("arr: ", arr1)
	arr1 = mergeSort(arr1)
	print("mergeSort: arr: ", arr1)
