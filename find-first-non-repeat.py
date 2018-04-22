def first_non_repeat(arr):
	lx = [0] * len(s)
	for i in range(len(s)):
		if lx[i] == 1:
			continue
		for j in range(i+1, len(s)):
			if lx[j] == 1:
				continue
			if s[i] == s[j]:
				lx[i] = 1
				lx[j] = 1
		if lx[i] == 0:
			return s[i]
	return '_'

if __name__ == "__main__":
	print("------------------------")
	s = "abacab"
	print(s)
	val = first_non_repeat(s)
	print("First non repeat char: ", val)
	s = "abacabc"
	print(s)
	val = first_non_repeat(s)
	print("First non repeat char: ", val)
	s = "z"
	print(s)
	val = first_non_repeat(s)
	print("First non repeat char: ", val)
	print("------------------------")
