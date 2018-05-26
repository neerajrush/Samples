#
# [ 2, 3 ]   ==> [ 4, 2 ]
# [ 4, 5 ]       [ 5, 3 ]
#
#  2X2: last = N-1, level = 0, i = 0
#  (0, 0) ==> (0, 1)       swap((0, 0), (0, 1))  ==> swap((level, i), (i, last))
#  (0, 0) ==> (1, 1)       swap((0, 0), (1, 1))  ==> swap((level, i), (last, last-i))
#  (0, 0) ==> (1, 0)       swap((0, 0), (1, 0))  ==> swap((level, i), (last-i, level))
#
#  3X3
#  [1, 2, 3]          [7, 4, 1]
#  [4, 5, 6]    <==>  [8, 5, 2]
#  [7, 8, 9]          [9, 6, 3]
#                          level = 0, last = N-1, i = 0:
#  (0, 0) ==> (0, 2)       swap((0, 0), (0, 2))  ==> swap((level, i), (i, last))
#  (0, 0) ==> (2, 2)       swap((0, 0), (2, 2))  ==> swap((level, i), (last, last-i))
#  (0, 0) ==> (2, 0)       swap((0, 0), (2, 0))  ==> swap((level, i), (last-i, level))

#  [7, 2, 1]
#  [4, 5, 6]
#  [9, 8, 3]
#                         last = N-1, i = 1:
#  (0, 1) ==> (1, 2)      swap((0, 1), (1, 2))   ==> swap((level, i), (i, last))
#  (0, 1) ==> (2, 1)      swap((0, 1), (2, 1))   ==> swap((level, i), (last, last-i))
#  (0, 1) ==> (1, 0)      swap((0, 1), (1, 0))   ==> swap((level, i), (last-ii, level)

# 4X4:
# [ 11, 12, 13, 14]
# [ 15, 16, 17, 18]
# [ 19, 20, 21, 22]
# [ 23, 24, 25, 26]
#
# [ 23, 19, 15, 11]
# [ 24, 20, 16, 12]
# [ 25, 21, 17, 13]
# [ 26, 22, 18, 14]

def print_matrix(arr):
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			print(arr[i][j], "  ", end="")
		print("")


def rotate_2d_array(arr, N):
	last = N - 1
	level = 0
	n_levels = int(N/2)
	while level < n_levels:
		for i in range(level, last):
			arr[level][i], arr[i][last]    = arr[i][last], arr[level][i]
			arr[level][i], arr[last][last-i+level] = arr[last][last-i+level], arr[level][i]
			arr[level][i], arr[last-i+level][level]    = arr[last-i+level][level], arr[level][i]
		level += 1
		last -= 1

	return arr

if __name__ == "__main__":
	print("------------------------")
	print("Input::")

	a = [[0, 1],
	     [2, 3]] 
	N = 2
	print("Size: :",  N)
	print_matrix(a)
	val = rotate_2d_array(a, N)
	print("Expected result:")
	print_matrix([[2, 0], [3, 1]])
	print("Result  rotated:")
	print_matrix(val)
	print("------------------------")
	print("Input::")

	a = [[0, 1, 2],
	     [3, 4, 5],
	     [6, 7, 8]] 
	N = 3
	print("Size: :",  N)
	print_matrix(a)
	val = rotate_2d_array(a, N)
	print("Expected result:")
	print_matrix([[6, 3, 0], [7, 4, 1], [8, 5, 2]])
	print("Result  rotated:")
	print_matrix(val)
	print("------------------------")
	print("Input::")

	a = [[ 0, 1, 2, 3],
	     [ 4, 5, 6, 7],
	     [ 8, 9, 10, 11],
	     [ 12, 13, 14, 15]]
	N = 4
	print("Size: :",  N)
	print_matrix(a)
	val = rotate_2d_array(a, N)
	print("Expected result:")
	print_matrix([[ 12, 8, 4, 0], [ 13, 9, 5, 1], [ 14, 10, 6, 2], [ 15, 11, 7, 3]])
	print("Result  rotated:")
	print_matrix(val)
	print("------------------------")
