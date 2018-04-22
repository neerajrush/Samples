def find_pos(st):
	pos = 0
	ch_map = [0 for x in range(26)]
	count = 0
	idx = 0
	for ch in range(len(st)):
		pos += 1
		if ord(st[ch]) < ord('a') or ord(st[ch]) > ord('z'):
			continue
		idx = ord(st[ch]) - ord('a')
		if ch_map[idx] == 0:
			ch_map[idx] = 1
			count += 1
		if count == 26:
			break
	return pos - 1

if __name__ == "__main__":
	st = 'abc d ef ghijklmnopqrstuvwxyyyyyyyyz'
	print(st, "len: ", len(st))
	pos = find_pos(st)
	print(pos)
