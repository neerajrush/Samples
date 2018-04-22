def isSubsetSum(arr, gSum):
    n = len(arr) 
    subset=[[True] * (gSum+1)] * (n+1)

    for j in range(1, gSum + 1) :
        subset[0][j] = False
   
    # Fill the subset table in botton 
    # up manner
    for i in range(1, n+1) :
        for j in range(1, gSum+1) :
            if(j < arr[i-1]) :
                subset[i][j] = subset[i-1][j]
            if (j >= arr[i-1]) :
                subset[i][j] = subset[i-1][j] or subset[i - 1][j-arr[i-1]]
   
    return subset[n][gSum];

if __name__ == "__main__":
	print("------------------------")
	arr = [2, 2, 3]
	gSum = 7
	print(arr, "Sum: ", gSum)
	if (isSubsetSum(arr, gSum) == True) :
    		print("Found a subset with given sum")
	else :
    		print("No subset with given sum")
	print("------------------------")
