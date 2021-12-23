import random

player_number = int(input("Please type the number to be guessed: "))
computer_number = random.randint(1,100)
print(computer_number)
tries = 1
limited_tries = 6

while computer_number != player_number:
	if computer_number < player_number:
		computer_number = random.randint(1,player_number)
	else:
		computer_number = random.randint(player_number,100)

	print(computer_number)

	tries += 1


	if tries == limited_tries:
		break

if tries == limited_tries:
	print("Computer ran out of tries")
	print("The number was", player_number)
else:
	print("Computer guessed it! The number was", computer_number)
	print("And it only took", tries, "tries!\n")



	input("\n\nPress the enter key to exit.")
