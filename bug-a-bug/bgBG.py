#
#  ___________
#  |  |  |    |
#  -----------
#  |  |  |     |
#  -----------
#  |  |  |     |
#  -----------
#  |  |  |	     |
#  -----------

class bg:
	def __init__(self, i, j):
		self.color = "Blue"
		self.x = i
		self.y = j
	def move(self, i, j):
		print("Move bg to:", i, j)

class BG:
	def __init__(self, i, j):
		self.color = "Red"
		self.x = i
		self.y = j

	def move(self, i, j):
		print("Move BG to:", i, j)

	def jump(self, i, j):
		print("Jump BG to:", i, j)

class bgBGGame:
	def __init__(self):
		self.pos = [ [None for j in range(5)] for i in range(5) ]
		self.BG  = [BG(0, 0), BG(0, 4), BG(4, 0), BG(4, 4)]
		self.bg  = [ [ 0 for j in range(5)] for i in range(4) ]
		x = 0
		y = 0
		for i in range(4):
			if i == 0:
				x, y = 1, 1
			elif i == 1:
				x, y = 1, 3
			elif i == 2:
				x, y = 3, 1
			else:
				x, y = 3, 3
			for j in range(5):
				self.bg[i][j] = bg(x, y)
		print(self.pos)

	def play(self):
		print("Start Playing:")


if __name__ == "__main__":
	x = bgBGGame()
	x.play()
