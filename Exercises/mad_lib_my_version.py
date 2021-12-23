# Create my custom story

from tkinter import *

class Application(Frame):

	def __init__(self, master):
		 """ Initialize Frame. """
		 super(Application, self).__init__(master)
		 self.grid()
		 self.create_widgets()

	def create_widgets(self):
		#create instruction label
		Label(self, text = "Enter information for a new story\n"
					).grid(row = 0, column = 1, columnspan = 2)

		#create a label and text entry for the name of a person
		Label(self, text = "Person: "
					).grid(row = 1, column = 1, sticky = W)
		self.person_ent = Entry(self)
		self.person_ent.grid(row = 1, column = 2, padx = (0, 10))

		#create a label and text entry for a plural noun
		Label(self, text = "Plural Noun: "
			).grid(row = 2, column = 1, sticky = W)
		self.nount_ent = Entry(self)
		self.nount_ent.grid(row = 2, column = 2, padx = (0, 10))

		#create a label and text entry for a verb
		Label(self, text = "Verb: "
					).grid(row = 3, column = 1, sticky = W)
		self.verb_ent = Entry(self)
		self.verb_ent.grid(row = 3, column = 2, padx = (0, 10))

		#create a label and text entry for a location
		Label(self, text = "Location: "
					).grid(row = 4, column = 1, sticky = W)
		self.loc_ent = Entry(self)
		self.loc_ent.grid(row = 4, column = 2, padx = (0, 10))

		#create a label and text entry for a weapon
		Label(self, text = "Weapon: "
					).grid(row = 5, column = 1, sticky = W)
		self.wep_ent = Entry(self)
		self.wep_ent.grid(row = 5, column = 2, padx = (0, 10))

		#create a label for adjectives check buttons
		Label(self, text = "Adjective(s)"
					).grid(row = 6, column = 1, pady = (10,0), padx = (10,0))

		#create itchy check button
		self.is_itchy = BooleanVar()
		Checkbutton(self,
					text = "itchy",
					variable = self.is_itchy
					).grid(row = 7, column = 1, pady = (0,10), sticky = W, padx = (10,0))
		
		#create joyous check button
		self.is_joyous = BooleanVar()
		Checkbutton(self,
					text = "joyous",
					variable = self.is_joyous
					).grid(row = 8, column = 1, pady = (0,10), sticky = W, padx = (10,0))

		#create electric check button
		self.is_electric = BooleanVar()
		Checkbutton(self,
					text = "electric",
					variable = self.is_electric
					).grid(row = 9, column = 1, pady = (0,10), sticky = W, padx = (10,0))

		#create sticky check button
		self.is_sticky = BooleanVar()
		Checkbutton(self,
					text = "sticky",
					variable = self.is_sticky
					).grid(row = 10, column = 1, pady = (0,10), sticky = W, padx = (10,0))

		#create a label for body parts radio buttons
		Label(self,
			  text = "Body part",
			  ).grid(row = 6, column = 2, pady = (10,0))

		#create variable for single body part
		self.body_part = StringVar()
		self.body_part.set(None)

		#create body part radio buttons
		body_parts = ["bellybutton", "spline", "stomach", "eye"]
		row = 7
		for part in body_parts:
			Radiobutton(self,
						text = part,
						variable = self.body_part,
						value = part
						).grid(row = row, column = 2, pady = (0,10), padx = (30,0), sticky = W)
			row += 1

		#create a submit button
		Button(self,
			text = "Click for story",
			command = self.tell_story
			).grid(row = 9, column = 0)

		self.story_txt = Text(self, width = 30, height = 25, wrap = WORD)
		self.story_txt.grid(row = 0, column = 0, rowspan = 9)

	
	def tell_story(self):
		""" Fill text box with new story on user input. """
		# get values from GUI

		person = self.person_ent.get()
		noun = self.nount_ent.get()
		verb = self.verb_ent.get()
		loc = self.loc_ent.get()
		wep = self.wep_ent.get()

		adjectives = ""
		if self.is_itchy.get():
			adjectives += "itchy, "
		if self.is_joyous.get():
			adjectives += "joyous, "
		if self.is_electric.get():
			adjectives += "electric, "
		if self.is_sticky.get():
			adjectives += "sticky, "


		body_part = self.body_part.get()

				#create the story
		story = "The famous explorer "
		story += person
		story += " had nearly given up a life-long quest to find The Lost City of "
		story += noun.title()
		story += " when one day, the "
		story += noun
		story += " found "
		story += person + "."
		story += " at the "
		story += loc + "."
		story += " A strong, "
		story += adjectives
		story += "peculiar feeling overwhelmed the explorer. "
		story += "With his "
		story += wep
		story += " in his hands, he was relieved."
		story += "After all this time, the quest was finally over. A tear came to "
		story += person + "'s "
		story += body_part + ". "
		story += "And then, the "
		story += noun
		story += " promptly devoured "
		story += person + "."
		story += "The moral of the story? Be careful what you "
		story += verb
		story += " for."



		#display the story
		self.story_txt.delete(0.0, END)
		self.story_txt.insert(0.0, story)




#main
root = Tk()
root.title("Mad lib my version (Costi)")
#root.geometry("1000x1000")
app = Application(root)
root.mainloop()