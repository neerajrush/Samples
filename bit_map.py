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
	n = r
	if l%2 == 1 and r%2 == 1:
		n = r + 1
	elif l%2 == 1:
		n = r
	else:
		m = l + 1
	i = m
	for i in range(m, n, 2):
		arr.append(i)

	return arr
#
# n = 5: 0101
# ANS: 30, 32
#

def bit_map(n):
	x = 1
	for i in range(32):
		if x & n:
			print(i, bin(n))
		x = x << 1

if __name__ == "__main__":
	arr = [ 2, 3, 4, 5]
	k = 5
	print (findNumber(arr, k))

	print(odd_N(3, 15))
	print(odd_N(2, 6))
	print(odd_N(2, 7))
	print(odd_N(3, 12))

	bit_map(0xF0000000)
