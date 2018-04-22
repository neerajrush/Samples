class point:
	def __init__(self, x, y):
		self.dx = x
		self.dy = y

def is_blocked(i, j):
	for x in range(len(blocked)):
		if i ==  blocked[x].dx and j == blocked[x].dy:
			return True

def path(i, j , M, N, blocked):
	if i == M - 1 and j == N - 1:
		return 1

	if is_blocked(i, j):
		return 0

        # right direction already blocked (i == M -1)
	if j == N-1 and is_blocked(i+1, j):
		return 0

        # down direction already blocked ( j == N -1)
	if i == M-1 and is_blocked(i, j+1):
		return 0

	return 1

if __name__ == "__main__":
	M = 6
	N = 6
	blocked = [ point(2, 3), point(1, 5), point(4, 1), point(4, 3) ]
	grid = [ [0 for j in range(N) ] for i in range(M) ]
	for i in range(M)[::-1]:
		for j in range(N)[::-1]:
			px = path(i, j, M, N, blocked)
			if px:
				if i+1 < M and j+1 < N:
					grid[i][j] = grid[i+1][j] + grid[i][j+1]
				else:
					grid[i][j] = 1
	print("Count: ", grid[0][0])
	print (grid)
