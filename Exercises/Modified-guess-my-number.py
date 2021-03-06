import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 5 attemps.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1
limited_tries = 5

# guessing loop
while guess != the_number:
	if guess > the_number:
		print("Lower...")
	else:
		print("Higher...")
	guess = int(input("Take a guess: "))
	tries += 1
	if tries == limited_tries:
		break

if tries == limited_tries:
	print("You ran out of tries")
	print("The number was", the_number)
else:
	print("You guessed it! The number was", the_number)
	print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")