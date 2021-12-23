import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

word = random.choice(WORDS)

correct = word

jumble = ""


while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position + 1):]

print(
"""
Welcome to Word Jumble!
Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
hint = ''
reward = 0
while guess != correct and guess != "":
	print("Sorry, that's not it.")
	hint = input("Do you need a hint? (yes/no) ")

	if hint.lower() == "yes" and correct == "python":
		while guess != correct and guess != "":

			print("\nHint: Think about your favorite programming language")
			guess = input("Your guess: ")

	elif hint.lower() == "yes" and correct == "jumble":
		while guess != correct and guess != "":

			print("\nHint: Think about the game")
			guess = input("Your guess: ")
	elif hint.lower() == "yes" and correct == "easy":
		while guess != correct and guess != "":

			print("\nHint: Think about games difficulties")
			guess = input("Your guess: ")
	elif hint.lower() == "yes" and correct == "difficult":
		while guess != correct and guess != "":

			print("\nHint: Think about how the word feels now")
			guess = input("Your guess: ")
	elif hint.lower() == "yes" and correct == "answer":
		while guess != correct and guess != "":

			print("\nHint: Think about when someone asks a question")
			guess = input("Your guess: ")
	elif hint.lower() == "yes" and correct == "xylophone":
		while guess != correct and guess != "":

			print("\nHint: Think about a musical instrument")
			guess = input("Your guess: ")

	else:

		guess = input("Your guess: ")
		reward = 1



if guess == correct and reward:
	print("That's it! You guessed it! Without any help! \n")

else:
	print("That's it! You guessed it! But with some help.... \n")

print("Thanks for playing. ")

input("\n\nPress the enter key to exit.")