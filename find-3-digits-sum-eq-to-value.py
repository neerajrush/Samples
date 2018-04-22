import copy

def find_sub_seq(seq, oVal, sub_seq, rVal, i):
	if len(seq) == 0 or oVal <= 0 or i >= len(seq):
		return False 
	if len(sub_seq) == 3 and sum(sub_seq) == oVal:
		return True 

	x = seq[i]
	sub_seq.append(x)
	rVal += x

	if rVal == oVal:
		return True
	elif rVal < oVal:
		find_sub_seq(seq, oVal, sub_seq, rVal, i+1)
	else:
		x = seq[i]
		sub_seq.remove(x)
		rVal -= x
		return find_sub_seq(seq, oVal, sub_seq, rVal, i+1)

def find_sum_eq_val(seq, oVal):
	if len(seq) == 0 or oVal <= 0 or sum(seq) < oVal:
		return []
	if len(seq) == 3 and sum(seq) == oVal:
		return seq 

	sub_seq = []
	rVal = 0

	find_sub_seq(seq, oVal, sub_seq, rVal, 0)

	return sub_seq

def find_sum_eq_val_dp(seq, oVal):
	if len(seq) == 0 or oVal <= 0 or sum(seq) < oVal:
		return []
	if len(seq) == 3 and sum(seq) == oVal:
		return seq 
	sub_seq = []
	rVal = 0
	x = 0
	for i in range(len(seq)):
		for j in range(i+1, len(seq)):
			if len(sub_seq) == 3 and sum(sub_seq) == oVal:
				return sub_seq
			elif rVal < oVal:
				x = seq[i]
				sub_seq.append(x)
				rVal += x
			else:
				sub_seq.remove(x)
				rVal -= x
	print(all_sub_seqs)
	return sub_seq

if __name__ == "__main__":
	print("-----------------------")
	seq = [12, 3, 4, 1, 6, 9]
	value = 16
	print(seq, "val: ", 16)
	s_seq = find_sum_eq_val(seq, value)
	print(s_seq)
	print("-----------------------")
	s_seq = find_sum_eq_val_dp(seq, value)
	print(s_seq)
	print("-----------------------")
