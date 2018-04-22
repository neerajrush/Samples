def binomialCoef(n, k):
	C = [[0 for x in range(k+1)] for x in range(n+1)]
	for i in range(n+1):
		for j in range(min(i, k)+1):
			if j == 0 or j == i:
				C[i][j] = 1
			else:
				C[i][j] = C[i-1][j-1] + C[i-1][j]
		print(C[i])
	return C[n][k]

def binCoef(n, k):
	if n == k:
		return 1
	if k <= 1:
		return n
	if n < k:
		return 0
	return binCoef(n-1, k-1) + binCoef(n-1, k)

def min_partition(arr, l1, l2):
	n = len(arr)
	if n == 0:
		return abs(l1 - l2) 
	#case1 : include current item in l1 and recurse for remaining n-1.
	incl = min_partition(arr[0:n-1], l1+arr[n-1], l2)

	#case1 : exclude current item in l1 and recurse for remaining n-1.
	excl = min_partition(arr[0:n-1], l1, l2+arr[n-1])

	return min(incl, excl)

def min_partition_dp(arr, dp_ll, l1, l2):
	n = len(arr)
	if n == 0:
		return abs(l1 - l2) 
	#case1 : include current item in l1 and recurse for remaining n-1.
	incl = min_partition_dp(arr[0:n-1], dp_ll, l1+arr[n-1], l2)

	#case1 : exclude current item in l1 and recurse for remaining n-1.
	excl = min_partition_dp(arr[0:n-1], dp_ll, l1, l2+arr[n-1])

	return min(incl, excl)

if __name__ == "__main__":
	print("------------------------")
	m = binCoef(7, 4)
	n = binomialCoef(7, 4)
	print(m, n)
	print("------------------------")
	arr = [ 1, 2, 3, 4, 2, 5 ]
	print(arr)
	dp_ll = [ [ 0 for j in range(len(arr)) ] for i in range(len(arr)) ]
	m = min_partition_dp(arr, dp_ll, 0, 0)
	print(m)
	print("------------------------")
	arr = [ 10, 20, 15, 5, 25 ]
	print(arr)
	m = min_partition(arr, 0, 0)
	print(m)
	print("------------------------")
