points_pool = 30
choice = None
Strenght = 0
Health = 0
Wisdom = 0
Dexterity = 0

while choice != "0":

	print(
		f"""
		Hello, you have a total of {points_pool}, please invest them in your skills:

		0 - Exit
		1 - Strenght {Strenght}
		2 - Health {Health}
		3 - Wisdom {Wisdom}
		4 - Dexterity {Dexterity}
		"""
		)

	choice = input("Please select the skill: ")

	if choice == "0":
		print("Good-bye. ")

	elif choice == "1":
		option = input("Do you want to add or rmv points? ")
		if option == "rmv":
			sub = int(input("How many points do you want to take back? "))
			if sub > Strenght:
				print("Sorry, not enough points")
			else:
				Strenght -= sub
				points_pool += sub
		else:

			add = int(input("How many points do you want to add? : "))
			if add > points_pool:
				print("Sorry, you don't have enough points. ")
			else:
				Strenght += add
				points_pool -= add


	
	elif choice == "2":
		option = input("Do you want to add or rmv points? ")
		if option == "rmv":
			sub = int(input("How many points do you want to take back? "))
			if sub > Health:
				print("Sorry, not enough points")
			else:
				Health -= sub
				points_pool += sub
		else:

			add = int(input("How many points do you want to add? : "))
			if add > points_pool:
				print("Sorry, you don't have enough points. ")
			else:
				Health += add
				points_pool -= add

	elif choice == "3":
		option = input("Do you want to add or rmv points? ")
		if option == "rmv":
			sub = int(input("How many points do you want to take back? "))
			if sub > Wisdom:
				print("Sorry, not enough points")
			else:
				Wisdom -= sub
				points_pool += sub
		else:

			add = int(input("How many points do you want to add? : "))
			if add > points_pool:
				print("Sorry, you don't have enough points. ")
			else:
				Wisdom += add
				points_pool -= add

	elif choice == "4":
		option = input("Do you want to add or rmv points? ")
		if option == "rmv":
			sub = int(input("How many points do you want to take back? "))
			if sub > Dexterity:
				print("Sorry, not enough points")
			else:
				Dexterity -= sub
				points_pool += sub
		else:

			add = int(input("How many points do you want to add? : "))
			if add > points_pool:
				print("Sorry, you don't have enough points. ")
			else:
				Dexterity += add
				points_pool -= add

	else:
		print(f"\nSorry, but {choice} isn't a valid choice")



