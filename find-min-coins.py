def find_min_coins(arr, xSum):
	min_arr = [0xFFFF] * (xSum + 1)
	min_arr[0] = 0
	for i in range(1, xSum+1):
		for j in range(len(arr)):
			if arr[j] <= i and min_arr[i - arr[j]] + 1 < min_arr[i]:
				min_arr[i] = min_arr[i - arr[j]] + 1
	print(min_arr)
	return min_arr[xSum]

def find_max_apples(arrX, n, m):
	sumX = [[0 for i in range(n)] for j in range(m)]
	print(sumX)
	for i in range(n):
		for j in range(m):
			sumX[i][j] = arrX[i][j] + max(sumX[i][j-1], sumX[i-1][j])
	print(sumX)
	return sumX[n-1][m-1]

if __name__ == "__main__":
	arr = [ 1, 3, 5]
	print("arr: ", arr)
	xSum = 11
	x = find_min_coins(arr, xSum)
	print("Min coins: ", x, "Sum :" , xSum, " Coins: ", arr)
	print("----------------------")
	arrX = [ [ 1, 2 ,3],
                 [ 1, 2, 3],
                 [ 1, 2, 3]
               ]
	print("arrX: ", arrX)
	maxApples = find_max_apples(arrX, 3, 3)
	print(maxApples)
	print("----------------------")
