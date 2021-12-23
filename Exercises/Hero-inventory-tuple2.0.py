
inventory = ("sword",
"armor",
"shield",
"healing potion")

print("Your items:")

for item in inventory:

	print(item)
input("\nPress the enter key to continue.")

print("You have", len(inventory), "items in your possession.")

input("\nPress the enter key to continue.")

if "healing potion" in inventory:
	print("You will live to fight another day.")

index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\nPress the enter key to continue.")

chest = ("gold", "gems")
print("You find a chest. It contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)
input("\n\nPress the enter key to exit.")