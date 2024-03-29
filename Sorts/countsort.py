# Count Sort is a sort which can sort integers in Linear time. 
# array will be the integer array to be sorted and range will be a 2-tuple with the 
# upper and lower bound of the range. Inclusive range.

def default_key(obj):
	return obj

def countsort(arr, reverse=False, key_function=default_key):
	if arr is None:
		return None
	m = list(map(key_function, arr))
	integer_range = (min(m), max(m))
	lower_bound, upper_bound = integer_range
	m = upper_bound - lower_bound + 1
	sort_array = []
	for i in range(0, m):
		sort_array.append([])
	for element in arr:
		key = key_function(element)
		sort_array[key - lower_bound].append(element)
	index = 0
	for num_list in sort_array:
		for element in num_list:
			arr[index] = element
			index += 1
	if reverse:
		arr.reverse()
	return arr

def countsort_int(arr, integer_range=None):
	if arr is None:
		return None
	if integer_range is None:
		integer_range = (min(arr), max(arr))
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

	def first_digit(num):
		return num%10



	# integer_range = (1, 1000)
	# unsorted_array = random_int_list_generator(10, integer_range)
	# unsorted_array_2 = unsorted_array.copy()
	# print(unsorted_array)
	# countsort(unsorted_array_2, key_function=first_digit)
	# print(unsorted_array_2)
	# python_sort(unsorted_array)
	# for i in range(0,len(unsorted_array_2)):
	# 	assert unsorted_array_2[i] == unsorted_array[i]
	# cProfile.run('countsort_int(unsorted_array_2, integer_range)')
	# cProfile.run('python_sort(unsorted_array)')











