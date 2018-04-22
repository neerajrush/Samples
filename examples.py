def bubble_sort(arr, n):
        for i in range (1, n):
                j = i-1
                k = i
                while j >= 0 and arr[j] > arr[k]:
                        arr[k], arr[j] = arr[j], arr[k]
                        j -= 1
                        k -= 1
def insertion_sort(arr):
	for i in range (1, len(arr)):
		value = arr[i]
		k = i
		while k > 0 and arr[k-1] > value:
			arr[k] = arr[k-1]
			k = k-1
		arr[k] = value
    
def selection_sort(arr):
	for i in range(len(arr)):
		minIdx = i
		for j in range(i, len(arr)):
			if arr[minIdx] > arr[j]:
				minIdx = j
		if minIdx != i:
			arr[i], arr[minIdx] = arr[minIdx], arr[i]
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

def binomial_coefficient(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]

def find_seq_no_matching_index(arr):
	m = len(arr)
	sx = [[0 for i in range(m+1)] for j in range(m+1)]
	for i in range(1, m+1):
		for j in range(1, m+1):
			if (arr[i-1] == arr[j-1] and i != j):
				sx[i][j] = 1 + sx[i-1][j-1]
			else:
                		sx[i][j] = max(sx[i][j-1], sx[i-1][j])
	result = ""
	i = m
	j = m
	while i > 0 and j > 0:
		if sx[i][j] == sx[i-1][j-1] + 1:
			result += arr[i-1]
			i -= 1
			j -= 1
		elif sx[i-1][j] == sx[i][j]:
			i -= 1
		else:
			j -= 1
	return "".join(reversed(result))
