from random import *

def devide(arr, begin, end):
	pivot = arr[end]
	i = begin - 1

	for j in range(begin, end):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[end] = arr[end], arr[i+1]
	return i + 1

def quick_sort(arr, begin, end):
	if len(arr) <= 1:
		return arr

	if begin >= end:
		return None

	pivot = devide(arr, begin, end)

	quick_sort(arr, begin, pivot - 1)
	quick_sort(arr, pivot + 1, end)

	return arr

def partition(arr, low, high):
	pivot = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1

def quick_sort_r(arr, low, high):
	if low >= high:
		return
	pivot = partition(arr, low, high)
	quick_sort_r(arr, low, pivot-1)
	quick_sort_r(arr, pivot+1, high)

def quick_sort_2(arr):
	if len(arr) <= 1:
		return arr

	quick_sort_r(arr, 0, len(arr)-1)
		
	return arr

if __name__ == "__main__":
	print("----------------------------------------")
	arr = [ 3, 6, 14, 1, 12, 9, 15, 7, 5, 10, 2, 13, 4, 11, 8]
	print("Input: ", arr, " size: ", len(arr))
	arr = quick_sort(arr, 0, len(arr)-1)
	print("Output: ", arr, " size: ", len(arr))
	print("----------------------------------------")
	arr = [ 3, 6, 14, 1, 12, 9, 15, 7, 5, 10, 2, 13, 4, 11, 8]
	print("Input: ", arr, " size: ", len(arr))
	arr = quick_sort_2(arr)
	print("Recursive: Output: ", arr, " size: ", len(arr))
	print("----------------------------------------")
