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

""" 
TO TEST : 


test_array = [100, 45, 12, 34, 60, 3, 4, 5, 20]
print("initial array : ", test_array)
print("sorted array : ", bubble_sort(test_array))


output:

'initial array : [100, 45, 12, 34, 60, 3, 4, 5, 20]
 sorted array : [3, 4, 5, 12, 20, 34, 45, 60, 100]'
"""