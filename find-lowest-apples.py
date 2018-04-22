def find_lowest_apples(arr, rows, cols):
	sumX = [ [ 0 for i in range(cols) ] for j in range(rows) ]
	print(sumX)
	for i in range(rows):
		for j in range(cols):
			sumX[i][j] = arr[i][j] + min(sumX[i][j-1], sumX[i-1][j])

	print(sumX)
	return sumX[rows-1][cols-1]

if __name__ == "__main__":
	print("---------------------------")
	arr = [ [ 1, 2, 3, 1 ], [ 0, 1, 2, 3 ], [ 3, 2, 0, 1 ] ]
	print(arr)
	result = find_lowest_apples(arr, 3, 4)
	print("lowest apples: ", result)
	print("---------------------------")
