def linear_search(lst, to_find):
	num = -1
	for i in range(len(lst)):
		if to_find == lst[i]:
			num = lst[i]
			return num
	return num
print(linear_search([1,2,3,4],5))
