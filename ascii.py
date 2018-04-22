def ascii_2_int(string):
	n = len(string) 
	base = n - 1
	signed_char = False
	decimal_val = 0
	if string[0] == '-':
		signed_char = True
	idx = 0
	if signed_char == True:
		idx = 1
	while idx < n:
		if ord(string[idx]) < 48 or ord(string[idx]) > 57:
			return -1, True
		else:
			decimal_val += (ord(string[idx]) - ord('0')) * (10**(base-idx))
		idx += 1
	if signed_char == True:
		decimal_val *= -1

	return decimal_val, False

if __name__ == "__main__":
	x, y = ascii_2_int("123")
	print("123 ==> ", x, y)
	x, y = ascii_2_int("3456789120")
	print("3456789120 ==> ", x, y)
	x, y = ascii_2_int("-1")
	print("-1 ==> ", x, y)
	x, y = ascii_2_int("-12345")
	print("-12345 ==> ", x, y)
	x, y = ascii_2_int("X12345")
	print("X12345 ==> ", x, y)
