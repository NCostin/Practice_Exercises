import random

WORDS = ("tigaie","tigan","foame","mustar","snitel", "katalin")

secret_word = random.choice(WORDS)

correct = secret_word

word_lenght = len(secret_word)

print(f"The choosen word has {word_lenght} characters")

chances = 5

guess = None


while guess != correct and guess != '':

	guess = input("Please guess the word: ")
	print("Sorry, wrong guess")


	while chances != 0 and guess and guess != '' :

		ask_computer = input("Ask the computer if a letter is in word: ")

		if ask_computer in secret_word:
			print("yes")
			chances -= 1
			print(f"You have more {chances} chances!")
		else:
			print("no")
			chances -= 1
			print(f"You have more {chances} chances!")

		guess = input("Please guess the word: ")
		if guess == correct:
			break
		else:

			print("Sorry, wrong guess")




print("\nCongrats, you guessed the word!")

print("Thanks for playing. ")

input("\n\nPress the enter key to exit.")