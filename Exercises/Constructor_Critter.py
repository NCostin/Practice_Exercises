
class Critter(object):
	"""A virtual pet"""
	def __init__(self):
		print("A new critter has been born!")

	def talk(self):
		print("\nHi. I'm an instance of classs Critter.")

#main
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("\n\nPress the enter key to exit.")