"""
DP text justificaiton using the following recurrence
* text is a sequence of words in the following format [word1, word2, word3, ...]

* min_text_error(i) where i can be any number from 0, n, where n is the number of words
* is defined as the best text error for text[i:n].
* BASE CASE : min_text_error(n) = 0, since there is no word in text[n:n].

* Error function is called badness and is defined as the error score for a given sequence of words. text[i:j]
* badness(sequence of words) = how bad it is for all those words to be on a line.

* recurrence: min_text_error(i) = min([badness(i, j) + min_text_error(j)]) for range of j in [i+1, n]
"""

# defining badness

# raw text
TEXT = "I gave a specific solution below, but more generally, think of it as two tasks: you figure out what's a lexeme first, and then make your token second. So once you have a substring that matches your rule for an int, then you convert it to one, or if it matches your rule for a float, you convert it to one of those, and so on. The rest you want to return as is, so making your token means just returning the substring."

NUMBER_OF_CHAR_PER_LINE = 80

def badness(list_of_words):
	total_length = 0
	for word in list_of_words:
		total_length += len(word)
	total_length += len(list_of_words) - 1
	error = NUMBER_OF_CHAR_PER_LINE - total_length
	if error < 0:
		return float("inf")
	return error

def text_justification(text, i,  break_points, min_text_error_memo=None):
	if min_text_error_memo is None:
		min_text_error_memo = {}
	if i == len(text):
		min_text_error_memo[i]=0
		return min_text_error_memo[i]
	if min_text_error_memo.get(i) is not None:
		return min_text_error_memo[i]
	# do computation
	min_text_error = float("inf")
	break_point = i+1
	for j in range(i+1, len(text)+1): # can optimize
		temp_error = badness(text[i:j]) + text_justification(text, j, break_points, min_text_error_memo)
		if temp_error < min_text_error:
			min_text_error = temp_error
			break_point = j
	if len(break_points) == 0 or break_point != break_points[-1]:
		break_points.append(break_point)
	min_text_error_memo[i] = min_text_error
	return min_text_error_memo[i]

# entire string formating excluding text justificaiton calculation is O(n)
memo = {}
bp = []
text = TEXT.split() # O(n)
text.reverse()
print(len(text))
text_justification(text, 0, bp, memo)
print(bp)
i = len(text)
for j in bp:
	t = text[j:i].copy() #O(n)
	t.reverse()
	print(" ".join(t))
	i = j 
t = text[0:i].copy()
t.reverse()
print(" ".join(t))













