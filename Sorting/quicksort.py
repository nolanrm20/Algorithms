""" Implementation of the quicksort algorithm """

def quicksort(in_list):
	""" 
	parameter in_list: an unsorted and mutable list to be sorted

	returns sorted in_list
	"""
	if len(in_list) <= 1:
		return in_list

	smaller = []
	larger = []
	equal = []
	pivot = in_list[len(in_list) // 2]

	for item in in_list:
		if item < pivot:
			smaller.append(item)
		elif item > pivot:
			larger.append(item)
		else:
			equal.append(item)
	return quicksort(smaller) + equal + quicksort(larger)

user_input = input('type list of numbers to be sorted \nseparate with a comma: ')
the_list = [int(i) for i in user_input.split(',')]
print(quicksort(the_list))

