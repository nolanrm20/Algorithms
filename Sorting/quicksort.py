""" Implementation of the quicksort algorithm """

def quicksort(in_list):
	""" 
	:parameter in_list: an unsorted and mutable list to be sorted

	will return sorted in_list
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

""" 
TO TEST : 


test_array = [100, 45, 12, 34, 60, 3, 4, 5, 20]
print("initial array : ", test_array)
print("sorted array : ", quicksort(test_array))


output:

'initial array : [100, 45, 12, 34, 60, 3, 4, 5, 20]
 sorted array : [3, 4, 5, 12, 20, 34, 45, 60, 100]'
"""

