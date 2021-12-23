# Demonstrates check buttons

from tkinter import *

class Application(Frame):
	""" GUI Application for favorite movie types. """
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		""" Create widgets for movie type choices. """

		# create description label
		Label(self, text = "Choose your favorite movie types").grid(row = 0, column = 0, 
			sticky = W) #Label object is not assigned to a variable because Label object is
						#connected to the program by it's master, in short, because I don't
						#need to directly access a widget, then I don't need to assign the
						#object to a variable

		# create instruction label

		Label(self, text= "Select all that apply: ").grid(row = 1, column = 0, sticky = W)

		# create Comedy check button
		self.likes_comedy = BooleanVar() # a special object, instance of the BooleanVar() class from tkinter module

		Checkbutton(self, text = "Comedy",
		 				  variable = self.likes_comedy, #associating the check button status(selected or unchecked) with the likes_comedy attribute 
		 				  command = self.update_text).grid(row = 2, column = 0, sticky = W) #binding the activation of checkbutton with update_text() method

		# create Drama check button
		self.likes_drama = BooleanVar()

		Checkbutton(self, text = "Drama", variable = self.likes_drama, command = self.update_text).grid(row = 3, column = 0, sticky = W)

		#create Romance check button
		self.likes_romance = BooleanVar()
		Checkbutton(self, text = "Romance", variable = self.likes_romance, command = self.update_text).grid(row = 4, column = 0, sticky = W)

		# create text field to display results
		self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
		self.results_txt.grid(row = 5, column = 0, columnspan = 3)

	def update_text(self):
		""" Update text widget and display user's favorite movie types. """
		likes = ""

		if self.likes_comedy.get():					#you can't acces the value of BooleanVar obect directly, you must invoke object's get() method
			likes += "You like comedic movies.\n"

		if self.likes_drama.get():
			likes += "You like dramatic movies.\n"

		if self.likes_romance.get():
			likes += "You like romantic movies.\n"

		self.results_txt.delete(0.0, END)
		self.results_txt.insert(0.0, likes)

#main
root = Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()


