""" Implementation of merge sort algorithm """

def merge_sort(in_list):
	"""
	parameter in_list: mutable list to be sorted
	returns sorted in_list
	"""
	if len(in_list) > 1:
		mid = len(in_list) // 2
		left_half = in_list[:mid]
		right_half = in_list[mid:]

		merge_sort(left_half)
		merge_sort(right_half)

		i, j, k = 0, 0, 0

		left_len = len(left_half)
		right_len = len(right_half)

		while i < left_len and j < right_len:
			if left_half[i] < right_half[j]:
				in_list[k] = left_half[i]
				i += 1
			else:
				in_list[k] = right_half[j]
				j += 1
			k += 1


		while i < left_len:
			in_list[k] = left_half[i]
			i += 1
			k += 1

		while j < right_len:
			in_list[k] = right_half[j]
			j += 1
			k += 1

	return in_list		


user_input = input('type list of numbers to be sorted \nseparate with a comma: ')
the_list = [int(i) for i in user_input.split(',')]
print(merge_sort(the_list))
