W = [1, 2, 4, 2, 5]
V = [5, 3, 5, 3, 2]

# n = 4 Y: w=5, C=5, v=2
C = 10
N = len(W)
class CX:
	def __init__(self):
		self.countX = 0
	def incr(self):
		self.countX += 1
cX = CX()

MX = [ [0x7FFF for j in range(C+1) ] for i in range(N+1) ] 
def knapsack(n, C):
	#print(n, C)
	cX.incr()
	if n < 0 or C == 0:
		return 0
	if MX[n][C] != 0x7FFF:
		return MX[n][C]
	elif W[n] > C:
		result = knapsack(n-1, C)
	else:
		t1 = knapsack(n-1, C)
		t2 = V[n] + knapsack(n-1, C - W[n])
		result = max(t1, t2)
	MX[n][C] = result
	return result

if __name__ == "__main__":
	print("------------------------")
	n = len(W) - 1
	print(W, V, "Cap: ", C)
	x = knapsack(n, C)
	print(x)
	print("Count: ", cX.countX)
	print("------------------------")
