def rotateImage(a):
	n = len(a)
	last = n -1
	nlevels = int(n/2)
	level = 0
	while level < nlevels:
		for i in range(level, last):
        		a[level][i], a[i][last]               = a[i][last],             a[level][i]
        		a[level][i], a[last][last-i+level]    = a[last][last-i+level],   a[level][i]
        		a[level][i], a[last-i+level][level]   = a[last-i+level][level], a[level][i]
		level += 1
		last -= 1
	return a

def print_image(a):
	for x in range(len(a)):
		print(a[x])

if __name__ == "__main__":
	print("-----------------")
	a = [[0, 1], [2, 3]]
	print_image(a)
	print("")
	print_image(rotateImage(a))
	print("-----------------")

	b = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
	print_image(b)
	print("")
	print_image(rotateImage(b))
	print("-----------------")

	c = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15] ]
	print_image(c)
	print("")
	print_image(rotateImage(c))
	print("-----------------")
