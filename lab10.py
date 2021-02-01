# Write a function add_numbers() that takes as input a list
# containing numbers, and returns the sum of the numbers.

def add_numbers(lst):
	total = sum(lst)
	return total


# Lists can be used to represent mathematical vectors. 
# Write a function add_vectors(u,v) that takes two lists of
# numbers of the same length, and returns a new list containing
# the sums of the corresponding elements of each. If the
# function receives two vectors of different lengths it
# should return None.

def add_vectors(u,v):
	w = []
	if len(u) == len(v):
		for i in range(0, len(u)):
			w.append(u[i]+v[i])
		return w
	else:
		return None


# Write a function word_selector() that takes as input a sentence,
# and returns a list that includes the longest word from that
# sentence as well as any other words with the same length of
# characters.

def word_selector(sentence):
	s_list = sentence.split()
	s_list.sort(key=len)
	word = []
	for i in s_list:
		if len(i) == len(s_list[-1]):
			word.append(i)
	return word
		
