def linear_search(lst, to_find):
	
	for i in range(len(lst)):
		if to_find == lst[i]:
			return i
	return -1
