def  findNumber(arr, k):
        if len(arr) == 0:
                return "NO"
        
        for i in range(len(arr)):
            if arr[i] == k:
                return "YES"
        return "NO"

def odd_N(l, r):
	arr = []
	m = l
	n = r + 1
	if m%2 == 0:
		m += 1
	if n%2 == 0:
		n += 1
	for i in range(m, n, 2):
		arr.append(i)

	return arr

if __name__ == "__main__":
	arr = [ 2, 3, 4, 5]
	k = 5
	print (findNumber(arr, k))

	print(3, 15, "==> ", odd_N(3, 15))
	print(2,  6, "==> ", odd_N(2, 6))
	print(2,  7, "==> ", odd_N(2, 7))
	print(3, 12, "==> ", odd_N(3, 12))

	print("%.3f" %(123.51))
