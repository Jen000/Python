
# Write a function 'check_e()' that takes as input a 
# string (e.g., a word or a sentence). The function should
# return True if the letter 'e' is in the string, and False
# otherwise. The function should ignore capitalization.
# For example, the function should return True if the input
# is 'hello' or 'HELLO'

def check_e(string):
	yup = string.lower()
	if yup in string:
		return True
	else:
		return False



# Write a function check_letter() that takes as input a
# letter and a string (in this order). The function should
# return True if the letter is in the string, and False 
# otherwise. The function should ignore capitalization.
# For example, the function should return True if the input
# is 'hello' or 'HELLO' and the letter is 'e' or 'E'.


def check_letter(l, s):
	s = s.lower()
	l = l.lower()
	if l in s:
		return True
	else:
		return False




# Write a function check_letter_message() that takes as input a
# letter and a string (in this order). If the letter is in the
# string, the function should return 'The letter LETTER is 
#included in STRING', where LETTER and STRING are the values
# that were provided as input. If the letter is not in the 
# sting, the function should return 'the letter LETTER is not
# included in STRING'. The function should ignore capitalization
# when checking for the occurrence of the letter, but not
# when returning the message. For example, when the inputs are
# 'e' and 'HELLO', the function should return 'The letter e is
# included in HELLO'.



def check_letter_message(LETTER,STRING):
	L1 = LETTER.lower()
	S1 = STRING.lower()
	if L1 in S1:
		return ("The letter " + LETTER + " is included in " + STRING)
	else:
		return ("The letter " + LETTER + " is not included in " + STRING)



# Write a function check_letter_count() that has the same
# functionality as the previous function check_letter_message()
# but that also counts the number of times the letter appears.
# This function should return 'The letter LETTER is included in
# STRING COUNT time' where COUNT is the number of times the letter
# appears. If the letter is not included, the function should 
# return 'The letter LETTER is not included in STRING'
# USE A FOR LOOP TO SOLVE THIS PROBLEM

def check_letter_count(LETTER,STRING):
	L1 = LETTER.lower()
	S1 = STRING.lower()
	count = 0
	if L1 in S1:
		for x in STRING:
			if x == L1:
				count +=1
		return ("The letter " + LETTER + " is included in " + STRING + " " + str(count) + " times.")
	else:
		return ("The letter " + LETTER + " is not included in " + STRING)

