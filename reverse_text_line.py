def reverseWord(Xll, start, stop):
	i = start
	j = stop
	while i < stop and j > 0 and i < j:
		Xll[i], Xll[j] = Xll[j], Xll[i]
		i += 1
		j -= 1
	return Xll

def reverse(X):
	i = 1
	n = len(X)
	wStart = 0
	Xll = list(X)
	while i < n:
		if Xll[i] == ' ' or Xll[i] == '\0':
			Xll = reverseWord(Xll, wStart, i-1)
			wStart = i + 1
		i += 1
	Xll = reverseWord(Xll, 0, n-1)
	return "".join(Xll)
			
if __name__ == "__main__":
	X = "[ This is a sample text message. ]"
	print(X, " len: ", len(X))
	X = reverse(X)
	print(X, " len: ", len(X))
