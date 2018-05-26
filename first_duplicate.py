def firstDuplicate(a):
	min_idx = len(a)
	occur_map = {}
	for i in range(0, len(a)):
		if i == min_idx:
			break
		if min_idx < len(a) and a[i] == a[min_idx]:
			continue
		if occur_map.__contains__(a[i]):
			occur_map[a[i]] += 1
			if min_idx > i:
				min_idx = i
		else:
			occur_map[a[i]] = 1
	
	if min_idx < len(a):
		return a[min_idx]

	return -1

if __name__ == "__main__":
	a = [ 2, 4, 5, 6, 1, 3, 1, 3, 3, 4, 5, 2]
	print(firstDuplicate(a))
