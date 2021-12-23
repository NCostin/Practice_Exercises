#Demonstrates radio buttons

from tkinter import *

class Application(Frame):
	""" GUI Application for favorite movie type. """
	def __init__(self, master):
		""" Initialize Frame. """
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		""" Create widgets for movie type choices. """
		#create description label
		Label(self, text = "Choose your favorite type of movie").grid(row =0, column = 0, sticky = W)

		#create instruction label
		Label(self, text = "Select one:").grid(row = 1, column = 0, sticky = W)

		#create variable for single, facorite type of movie
		self.favorite = StringVar() #allows a string to be stored and retrieved
		self.favorite.set(None)

		#create Comedy radio button 

		#by setting radio button variable option to self.favorite and its value option
		#to "comedy". I'm saying that when the Comedy radio button is selected,
		#the StringVar referenced by self.favorite should store the string "comedy".

		Radiobutton(self, text= "Comedy",
						  variable = self.favorite, #defines the special variable associated with
						  							#the radio button

						  value = "comedy.",		#defines the value to be stored by the special
						  							#variable when the radio button is selected 
						  command = self.update_text
						  ).grid(row = 2, column = 0, sticky = W)


		#create Drama radio button
		Radiobutton(self, text = "Drama", variable = self.favorite, value = "drama.", command = self.update_text).grid(row = 3, column = 0, sticky = W)

		#create Romance radio button
		Radiobutton(self, text = "Romance", variable = self.favorite, value = "romance.", command = self.update_text).grid(row = 4, column = 0, sticky = W)


		#create text field to display result
		self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
		self.results_txt.grid(row = 5, column = 0, columnspan = 3)

	def update_text(self):
		""" Update text area and display user's favorite movie type. """
		message = "Your favorite type of movie is "
		message += self.favorite.get()

		self.results_txt.delete(0.0, END)
		self.results_txt.insert(0.0, message)

#main
root = Tk()
root.title("Movie Chooser 2")
app = Application(root)
root.mainloop()
