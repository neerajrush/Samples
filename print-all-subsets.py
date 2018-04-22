#              []
#          [] { 
#              [2]
# [1, 2] []      
#               ]1]
#          [1] {
#               [1, 2]

def printIt(subsets):
	print("{", end="")
	for x in range(len(subsets)):
		if subsets[x]:
			print(subsets[x], ", ", end="")
	print("}")

def printSubsets(arr, subsets, i, total):
	if len(arr) == i:
		if sum(subsets) == total:
			printIt(subsets)
		return
	subsets[i] = 0
	printSubsets(arr, subsets, i+1, total)
	subsets[i] = arr[i]
	printSubsets(arr, subsets, i+1, total)

if __name__ == "__main__":
	print("------------------")
	arr = [ 2, 3, 4, 6, 7, 10 ]
	print(arr)
	total = 20
	subsets = [0] * len(arr)
	printSubsets(arr, subsets, 0, total)
	print("------------------")
