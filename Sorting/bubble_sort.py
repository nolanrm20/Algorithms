""" Implementation of bubble sort algorithm """

def bubble_sort(in_list):
	"""
	parameter in_list: unsorted mutable list to be sorted

	returns sorted in_list
	"""
	switch = True
	passes = len(in_list) - 1

	while passes > 0 and switch:
		switch = False
		for i in range(passes):
			if in_list[i] > in_list[i + 1]:
				switch = True
				temp = in_list[i]
				in_list[i] = in_list[i + 1]
				in_list[i + 1] = temp
		passes = passes - 1

	return in_list

user_input = input('type list of numbers separated by a comma: ')
the_list = [int(i) for i in user_input.split(',')]
print(bubble_sort(the_list))
