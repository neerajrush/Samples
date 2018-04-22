def printMatrics(X, Y):
	for m in range(len(X)):
		print(X[m], end="")
		for n in range(len(Y)):
			print (" ", Y[n], end="")
		print("")

def lcs(X, Y, m, n):
	if m == 0 or n == 0:
		return 0;
	elif X[m-1] == Y[n-1]:
		return 1 + lcs(X, Y, m-1, n-1)
	else:
		return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));

X = "AGGTAB"
Y = "GXTXAYB"

X="AB"
Y="AC"

print( "Length of LCS is ", lcs(X , Y, len(X), len(Y)))
