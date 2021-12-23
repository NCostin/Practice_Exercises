#Demonstrates inheritance - overriding methods

class Card(object):
	"""A playing card"""
	RANKS = ["A", "2", "3", "4", "5", "6", "7", 
						"8", "9", "10", "J", "Q", "K"]
	SUITS = ["c", "d", "h", "s"]

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit 

	def __str__(self):
		rep = self.rank + self.suit
		return rep


class Unprintable_Card(Card):
	"""A Card won't reveal its rank or suit when printed. """

	def __str__(self):
		return "<unprintable>"


class Positionable_Card(Card):
	"""A Card that can be face up or face down. """

	def __init__(self, rank, suit, face_up = True):
		super(Positionable_Card, self).__init__(rank, suit) # invoca metoda __init__() din clasa de baza Card()
															# Positionable_Card se refera la faptul ca vreau sa invoc o metoda
																# a clasei de baza a lui Positionable_Card, care este clasa Card()
															# self are rol de referinta pentru obiectul Positionable_Card, astfel ca codul
																# din clasa Card() poate ajunge la obiect pentru ai adauga atributele rank si suit
															# __init__(rank, suit) ii spune Python-ului ca vreau sa invoc metoda constructor
																# a clasi Card() si vreau sa parsez valorile lui rank si suit
		self.is_face_up = face_up

	def __str__(self):
		if self.is_face_up:									# verifica daca atributul face_up este True, daca da, reprezentarea
																# stringului pt carte se face cu metoda __str__() din clasa de baza Card()
			rep = super(Positionable_Card, self).__str__()
		else:
			rep = "XX"
		return rep

	def flip(self):
		self.is_face_up = not self.is_face_up



#main
card1 = Card("A", "c")
card2 = Unprintable_Card("A", "d")
card3 = Positionable_Card("A", "h")

print("Printing a Card object:")
print(card1)

print("\nPrinting an Unprintable_Card object:")
print(card2)

print("\nPrinting a Positionable_Card object: ")
print(card3)

print("Flipping the Positionable_Card object.")
card3.flip()

print("Printing the Positionable_Card object:")
print(card3)

input("\n\nPress the enter key to exit.")