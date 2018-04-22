#
# [ 2, 3 ]   ==> [ 4, 2 ]
# [ 4, 5 ]       [ 5, 3 ]
#
#  2X2
#  (0, 0) ==> (0, 1)
#  (0, 0) ==> (1, 1)
#  (0, 0) ==> (1, 0)
#
#  3X3
#  (0, 0) ==> (0, 2)
#  (0, 0) ==> (2, 2) 
#  (0, 0) ==> (2, 0) 

#  (0, 1) ==> (1, 2)
#  (0, 1) ==> (2, 1) 
#  (0, 1) ==> (1, 2) 

def rotate_2d_array(arr, N):
	for i in range(N-1):
		print(i)
		arr[i][i], arr[i][N-1] = arr[i][N-1], arr[i][i]
		arr[i][i], arr[N-1][N-1] = arr[N-1][N-1], arr[i][i]
		arr[i][i], arr[N-1][i] = arr[N-1][i], arr[i][i]

	return arr

if __name__ == "__main__":
	print("------------------------")

	a = [[2, 3],
	     [4, 5]] 
	N = 2
	print(a, N)
	val = rotate_2d_array(a, N)
	print("Result rotate: ", val)

	a = [[1, 2, 3],
	     [4, 5, 6],
	     [7, 8, 9]] 
	N = 3
	print(a, N)
	val = rotate_2d_array(a, N)
	print("Result rotate: ", val)
	print("------------------------")
