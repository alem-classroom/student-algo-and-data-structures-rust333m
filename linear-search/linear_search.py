def linear_search(lst, to_find):
	num = -1
	for i in range(len(lst)):
		if to_find == lst[i]:
			num = lst[i]
			return num
	return num
