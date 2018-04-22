class point:
	def __init__(self, x, y):
		self.dx = x
		self.dy = y

def is_blocked(i, j):
	for x in range(len(blocked)):
		if i ==  blocked[x].dx and j == blocked[x].dy:
			return True

def is_path(i, j , M, N, blocked):
	if i == M - 1 and j == N - 1:
		return True

	if is_blocked(i, j):
		return False

        # right direction already blocked (i == M -1)
	if j == N-1 and is_blocked(i+1, j):
		return False

        # down direction already blocked ( j == N -1)
	if i == M-1 and is_blocked(i, j+1):
		return False

	return True

#
# Input: number of paths from (0, 0) to (5, 5):
# [[0, 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, X],   blocked: (1, 5)
#  [0, 0, 0, X, 0, 0],   blocked: (2, 3)
#  [0, 0, 0, 0, 0, 0], 
#  [0, X, 0, X, 0, 0],   blocked: (4, 1), (4, 3)
#  [0, 0, 0, 0, 0, 0]]
#
#
# Result:
# Count:  61
# [[61, 32, 16, 8, 4, 0], 
#  [29, 16,  8, 4, 4, 0], 
#  [13,  8,  4, 0, 4, 1], 
#  [ 5,  4,  4, 3, 3, 1], 
#  [ 1,  0,  1, 0, 2, 1], 
#  [ 1,  1,  1, 1, 1, 1]]

if __name__ == "__main__":
	M = 6
	N = 6
	blocked = [ point(1, 5), point(2, 3), point(4, 1), point(4, 3) ]
	grid = [ [0 for j in range(N) ] for i in range(M) ]
	for i in range(M)[::-1]:
		for j in range(N)[::-1]:
			if is_path(i, j, M, N, blocked):
				if i+1 < M and j+1 < N:
					grid[i][j] = grid[i+1][j] + grid[i][j+1]
				else:
					grid[i][j] = 1
	print("Count: ", grid[0][0])
	print (grid)
