
def max_list_iter(int_list):
	x = 0
	if int_list == None:
		raise ValueError
	if int_list == []:
		return None
	for i in range(0, len(int_list)):
		if i == 0:
			x = int_list[i]
		elif int_list[i] > x:
			x = int_list[i]
	return x

def reverse_rec(int_list):
    if int_list == None:
        raise ValueError
    elif len(int_list) > 0:
        x = [int_list[len(int_list) - 1]]
        int_list.remove(int_list[len(int_list) - 1])
        y = reverse_rec(int_list)
        return x + y
    else:
        return []

def bin_search(target, low, high, int_list):
	spot = (low + high) // 2
	if int_list == None:
		raise ValueError
	if int_list == [] or (high == low and int_list[spot] != target):
		return None
	if int_list[spot] == target:
		return spot
	if target < int_list[spot]:
		return bin_search(target, low, spot - 1 , int_list)
	if target > int_list[spot]:
		return bin_search(target, spot + 1, high, int_list)
