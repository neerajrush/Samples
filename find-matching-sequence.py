def leastCommonSequence(X, Y, m, n):
	if m == 0 or n == 0:
		return 0
	elif X[m-1] == Y[n-1]:
		return 1 + leastCommonSequence(X, Y, m-1, n-1)
	else:
		return max(leastCommonSequence(X, Y, m, n-1), leastCommonSequence(X, Y, m-1, n))

def leastCommonSequence2(X, Y, m, n):
	max_ll = []
	idx = n
	while idx >= 0:
		ll = lCS2(X, Y, m, idx)
		if len(ll) > len(max_ll):
			max_ll = ll
		idx -= 1
	print("Found Max Seq: ", max_ll)
	return len(max_ll)

def lCS2(X, Y, m, n):
	ll = []
	iEnd = m
	jEnd = n
	j = jEnd - 1
	while j >= 0:
		i = iEnd - 1
		while i >= 0:
			if X[i] == Y[j]:
				ll.append(X[i])
				iEnd = i
				break
			i -= 1
		j -= 1
	print("Seq: ", ll)
	return ll

if __name__ == "__main__":
	X = "AGGTAB"
	Y = "GXTXAYB"
	X = "PTXAGGTYTABXZ"
	Y = "GXTXAYBP"
	z = leastCommonSequence(X, Y, len(X), len(Y))
	print(X, Y, " lcs: ", z)

	z = leastCommonSequence2(X, Y, len(X), len(Y))
	print(X, Y, " lcs: ", z)
