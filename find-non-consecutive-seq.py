def lcs(X, n):
	i = 0
	ll = []
	max_ll = ll
	while i < n:
		ll.append(X[i])
		j = i + 1
		last_pushed = X[i]
		while j < n:
			if X[j] > last_pushed:
				ll.append(X[j])
				last_pushed = X[j]
			j += 1
		i += 1

		if len(max_ll) < len(ll):
			max_ll = ll
		print(ll)
		ll = []
	print("Found MaxSq: ", max_ll)
	return len(max_ll)

def leastCommonSequence(X, n):
	lcs = [1] * n
	ll = []
	i = 1
	while i < n:
		j = 0
		while j <= i: 
			if X[j] < X[i]:
				lcs[i] = max(lcs[i], lcs[j]+1)
			j += 1
		i += 1
	maxSq = 0
	print(lcs, ll)
	for i in range(n):
		if maxSq < lcs[i]:
			maxSq = lcs[i]
	return maxSq

if __name__ == "__main__":
	X = "GXTXAYB"
	X = "PTXGYABZ"
	#X = "GTXAYBP"
	z = leastCommonSequence(X, len(X))
	print(X, " len: ", z)

	z = lcs(X, len(X))
	print(X, " len: ", z)
