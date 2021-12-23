import random

flips = 0
heads= 0
tails = 0

while flips != 100:

	coin_number = random.randint(1,2)

	flips += 1

	if coin_number == 1:

		heads += 1

	else:
		tails += 1

print(f"Total number of heads are: {heads}")
print(f"Total number of tails are: {tails}")

input("\n Please press enter to exit ")

