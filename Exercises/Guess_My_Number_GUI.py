"""
The program you’ll create in this chapter is the classic number guessing game. For those who
missed out on it in their childhood, the game goes like this: the computer chooses a random
number between 1 and 100 and the player tries to guess it in as few attempts as possible. Each
time the player enters a guess, the computer tells the player whether the guess is too high,
too low, or right on the money. Once the player guesses the number, the game is over.
"""

""" make this with GUI ^ """


import random
from tkinter import *

class Application(Frame):


	def __init__(self, master):
		""" Initialize Frame """
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()
		self.computer_number = Application.__generate_computer_number()
		self.attempts = 5
		# Just for testing
		self.comp_message.insert(0.0, "Number: " + str(self.computer_number))
		self.attempts_message.insert(0.0, self.attempts)

	def create_widgets(self):
		#create instruction label
		Label(self, text = " Hello, this is a number guessing game, " 
							"please insert\n"
							" a number between 1-100, "
							"to see if you can guess correctly."
			).grid(row = 0, column = 0, sticky = W)

		#create computer message label and box
		Label(self, text = " Computer says:"
			).grid(row = 1, column = 0, pady = 10, sticky = W)

		self.comp_message = Text(self, width = 60, height = 5, wrap = WORD)
		self.comp_message.grid(row = 2, column = 0, padx = 5)

		#create attemps label and box
		Label(self, text = "Attemps: "
			).grid(row = 1, column = 0)
		self.attempts_message = Text(self, width = 1, height = 1, wrap = WORD)
		self.attempts_message.grid(row = 1, column = 0, padx = (70,0))


		#create label and box for user entry number
		Label(self, text = " Please guess the number: "
			).grid(row = 3, column = 0,pady = 5)

		self.num_ent = Entry(self)
		self.num_ent.grid(row = 4, column = 0)

		#create button for submit
		self.button = Button(self,
			text = "Submit your number",
			command = self.check_number)
		self.button.grid(row = 5, column = 0, pady = 5)


	@staticmethod
	def __generate_computer_number():

		return random.randrange(1,100)


	def check_number(self):

		self.attempts -= 1

		self.attempts_message.insert(0.0, self.attempts)

		self.comp_message.delete(0.0, END)

		if int(self.num_ent.get()) == self.computer_number and self.attempts > 0:
			self.comp_message.insert(0.0, "Congrats, you guessed the number")
			self.button['state'] = ['disabled']
		elif int(self.num_ent.get()) < self.computer_number and self.attempts > 0:
			self.comp_message.insert(0.0, "Higher")
		elif int(self.num_ent.get()) > self.computer_number and self.attempts > 0:
			self.comp_message.insert(0.0, "Lower")
		else:
			self.comp_message.insert(0.0, "You ran out of attemps. ")
			self.button['state'] = ['disabled']
			

			





#main
root = Tk()
root.title("Guess my number GUI")
app = Application(root)
root.mainloop()