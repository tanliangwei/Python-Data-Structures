from countsort import countsort
from math import log, floor, pow

def get_number_of_digits(number, base):
	return floor(log(number, base)) + 1

def default_key(num):
	return num

def radixsort(arr, base=None, reverse=False, key_function=default_key):
	if arr is None:
		return None
	m = list(map(key_function, arr))
	if base is None:
		base = 10
	max_number_of_digits = get_number_of_digits(max(m), base)
	for i in range(0, max_number_of_digits):
		countsort(arr, integer_range=(0, base-1), key_function=key_function_generator(i+1, base, key_function))
	return arr


# number % base to the power of digit poistion, then, the number divided by base to power of digit position - 1
def key_function_generator(digit_position, base, key_function):
	def return_function(num):
		number = key_function(num)
		number = number % (base ** digit_position)
		number = number // (base ** (digit_position-1))
		return number
	return return_function



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
		return num%100

	integer_range = (1, 1000)
	unsorted_array = random_int_list_generator(10, integer_range)
	unsorted_array_2 = unsorted_array.copy()
	print(unsorted_array_2)
	radixsort(unsorted_array_2, base = 8, key_function=first_digit)
	print(unsorted_array_2)
	# python_sort(unsorted_array)
	# for i in range(0,len(unsorted_array_2)):
	# 	assert unsorted_array_2[i] == unsorted_array[i]