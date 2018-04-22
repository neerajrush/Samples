def find_occrances(arr, val):
	count = 0
	complexity = 0
	idx = int(len(arr)/2)
	while idx < len(arr):
		complexity +=1
		if val < arr[idx]:
			idx = int(idx/2)
		elif val > arr[idx]:
			idx += int((len(arr) - idx)/2)
		else:
			while idx > 0 and val == arr[idx]:
				idx -= 1
			idx += 1
			while idx < len(arr) and val == arr[idx]:
				count += 1
				idx += 1
			break
	print(complexity)
	return count

if __name__ == "__main__":
	print("------------------------")
	arr = [2,3,4,5,6,7,7,7,9,9,9,9,10]
	val = 7
	print(arr, "len: ", len(arr))
	x = find_occrances(arr, val)
	print("val: ", val, "occrances: ", x)
	print("------------------------")
	val = 9
	print(arr, "len: ", len(arr))
	x = find_occrances(arr, val)
	print("val: ", val, "occrances: ", x)
	print("------------------------")
	val = 10 
	print(arr, "len: ", len(arr))
	x = find_occrances(arr, val)
	print("val: ", val, "occrances: ", x)
	print("------------------------")
