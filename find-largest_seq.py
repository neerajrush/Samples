def find_largest_seq(arr):
	l_seq = [1] * len(arr)
	result = 0
	for i in range(1, len(arr)):
		for j in range(i+1):
			if arr[j] < arr[i]:
				l_seq[i] = max(l_seq[i], l_seq[j]+1)
	print(l_seq)

	for x in range(len(l_seq)):
		if l_seq[x] > result:
			result = l_seq[x]

	r_seq = []
	idx = 1
	for x in range(len(l_seq)):
		if l_seq[x] == idx:
			r_seq.append(arr[x])
			idx += 1

	return result, "".join(r_seq)

if __name__ == "__main__":
	print("---------------------------")
	#arr = [ 'a', 'c', 'e', 'b', 'd', 's', 't', 'j', 'f', 'k', 'x' ]
	arr = "ACAGSHTB"
	print(arr)
	result, r_seq = find_largest_seq(arr)
	print("largets seq: ", r_seq, " size: ", result)
	print("---------------------------")
