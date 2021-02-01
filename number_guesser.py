#import random module

import random

rand_num = (random.randint(1,10))
#guess counter
count = 1
#ask user to guess, respond with directions
#if guessed provide with the number and guesses.
while True:
	answer = int(input("Guess the random number\n"))
	if answer == rand_num:
		print ("You guessed it, the number was ", rand_num, "It only took", count, " guesses.")
		break
	elif answer < rand_num:
		print ("Larger, guess again")
	elif answer > rand_num:
		print ("Samller, guess again")
	count+=1
