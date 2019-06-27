# Count Sort is a sort which can sort integers in Linear time. 
# array will be the integer array to be sorted and range will be a 2-tuple with the 
# upper and lower bound of the range. Inclusive range.
def countsort(arr, integer_range):
	if arr is None:
		return None
	lower_bound, upper_bound = integer_range
	m = upper_bound - lower_bound + 1
	sort_array = []
	for i in range(0, m):
		sort_array.append([])
	for element in arr:
		sort_array[element - lower_bound].append(element)
	index = 0
	for num_list in sort_array:
		for element in num_list:
			arr[index] = element
			index += 1
	return arr

def countsort_int(arr, integer_range):
	if arr is None:
		return None
	lower_bound, upper_bound = integer_range
	m = upper_bound - lower_bound + 1
	sort_array = []
	for i in range(0, m):
		sort_array.append(0)
	for element in arr:
		sort_array[element - lower_bound]+=1
	index = 0
	for n in range(0, len(sort_array)):
		for number in range(0, sort_array[n]):
			arr[index]=n+lower_bound
			index+=1
	return arr


if __name__ == "__main__":
	import random
	import cProfile

	def random_int_list_generator(number_of_elements, integer_range):
		lower_bound, upper_bound = integer_range
		return_list = []
		for i in range(0, number_of_elements):
			return_list.append(random.randint(lower_bound, upper_bound))
		return return_list

	def python_sort(arr):
		arr.sort()
		return arr



	integer_range = (1, 100)
	unsorted_array = random_int_list_generator(10000000, integer_range)
	unsorted_array_2 = unsorted_array.copy()
	# new_array = countsort_int(unsorted_array_2, integer_range)
	# python_sort(unsorted_array)
	# for i in range(0,len(new_array)):
	# 	assert new_array[i] == unsorted_array[i]
	cProfile.run('countsort_int(unsorted_array_2, integer_range)')
	cProfile.run('python_sort(unsorted_array)')











