from countsort import countsort
from math import log, floor

def get_number_of_digits(number, base):
	return floor(log(number, base)) + 1

def get_first_digit(number, base):
	return number%base

def radixsort(arr, base=None, reverse=False):
	if base is None:
		base = 10

	max_number_of_digits = get_number_of_digits(max(arr), base)
	for i in range(0, max_number_of_digits):
		temp_list = 
		for number in arr:




