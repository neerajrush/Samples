def merge(l_xlist, r_xlist, depth):
	for d in range(depth):
		print("....", end="")
	print("INPUT: " , l_xlist, r_xlist)
	
	s_xlist = [0] * (len(l_xlist) + len(r_xlist)) 
	s = 0
	i = 0
	j = 0
	while i < len(l_xlist) and j < len(r_xlist):
		if l_xlist[i] <= r_xlist[j]:
			s_xlist[s] = l_xlist[i]
			i += 1
		else:
			s_xlist[s] = r_xlist[j]
			j += 1
		s += 1

	while i < len(l_xlist):
		s_xlist[s] = l_xlist[i]
		i += 1
		s += 1

	while j < len(r_xlist):
		s_xlist[s] = r_xlist[j]
		j += 1
		s += 1

	for d in range(depth):
		print("....", end="")
	print("OUTPUT: ", s_xlist)
	return s_xlist

def mergeSort(xlist, depth = 0):
	if len(xlist) <= 1:
		return xlist

	middle = int(len(xlist)/2)

	l_size = middle
	r_size = len(xlist) - middle

	l_list = [0] * l_size
	r_list = [0] * r_size

	for i in range(l_size):
		l_list[i] = xlist[i]

	for i in range(r_size):
		r_list[i] = xlist[i+middle]

	l_list = mergeSort(l_list, depth+1)
	r_list = mergeSort(r_list, depth+1)

	return merge(l_list, r_list, depth)

if __name__ == "__main__":
	print("----------------------")
	xlist = [ 6, 4, 3, 2, 5, 7, 1 ]
	print("Given list: ", xlist)
	print("----------------------")
	mlist = mergeSort(xlist)
	print("----------------------")
	print("Merged list: ", mlist)
	print("----------------------")
