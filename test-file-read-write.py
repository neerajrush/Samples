def read_file(file_name):
	words_map = {}
	fx = open(file_name, "r")
	if fx.mode == "r":
		lines = fx.readlines()
		for aline in lines: 
			print(aline)
			word = ""
			for a_char in aline:
				if a_char == " " or a_char == "\t" or a_char == "\n":
					if words_map.__contains__(word):
						words_map[word] += 1
					else:
						words_map[word] = 1
					word = ""
				else:
					word += a_char
	fx.close()
	print("words_map: ", words_map)
	return words_map

def words_count(words_map):
	count = 0
	for x in words_map:
		print(x, words_map[x])
		count += words_map[x]
	return count

def write_file(file_name, data):
	print(data)
	fx = open(file_name, "a+")
	if fx.mode == "a+":
		fx.write(data)
	fx.close()

if __name__ ==  "__main__":
	file_name = "test_file"
	write_file(file_name, "This is a test write.\n")
	words_map = read_file(file_name)
	c = words_count(words_map)
	print("Words count: ", c)
