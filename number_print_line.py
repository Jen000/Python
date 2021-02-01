# a function that counts up to integer on diff lines


# define counting function
def count_up(num):
	i = 1
	while i <= num:
		print(i)
		i += 1


#ask user for input integer greater than zero
number = int(input("Enter a number greater than 0\n"))
num = number
count_up(num)

#prints numbers up to num on diff lines