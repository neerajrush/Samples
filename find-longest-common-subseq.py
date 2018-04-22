#################
#    A B B
# A  1 0 0
# B  0 1 1 
#
#
#################

def lcs(arr1, arr2):
	r_arr = [ [ 0 for j in range(len(arr2)+1) ] for i in range(len(arr1)+1) ]
	for i in range(len(arr1)+1):
		for j in range(len(arr2)+1):
			if i == 0 or j == 0:
				r_arr[i][j] = 0
			elif arr1[i-1] == arr2[j-1]:
				r_arr[i][j] = 1 + r_arr[i-1][j-1]
			else:
				r_arr[i][j] = max(r_arr[i-1][j], r_arr[i][j-1])
	for x in range(len(arr1)+1):
		print(r_arr[x])
	return r_arr[len(arr1)][len(arr2)]

if __name__ == "__main__":
	print("-----------------------")
	arr1 = "ABB"
	arr2 = "AB"
	arr = lcs(arr1, arr2)
	print(arr1, arr2, "LCS: ", arr)
	print("-----------------------")
	arr1 = "ABCDGDH"
	arr2 = "ADEFHR"
	arr = lcs(arr1, arr2)
	print(arr1, arr2, "LCS: ", arr)
	print("-----------------------")
	arr1 = "AGGTAB"
	arr2 = "GXTXAYB"
	arr = lcs(arr1, arr2)
	print(arr1, arr2, "LCS: ", arr)
	print("-----------------------")
	arr1 = "XYZAB"
	arr2 = "A"
	arr = lcs(arr1, arr2)
	print(arr1, arr2, "LCS: ", arr)
	print("-----------------------")
