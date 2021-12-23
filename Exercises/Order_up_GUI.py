"""
Create a GUI program, Order Up!, that presents the user with
a simple restaurant menu, which lists items and prices. Let the
user select different items and then show the user the total
bill.
"""

from tkinter import *
import random

class Application(Frame):
	
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		#product label generator

		Label(self, text = "Products: "
			).grid(row = 0, column = 0, sticky = W, pady = 20, padx = (10,0))

		#products list generator
		products = ["Ciorba de vaca", "Ciorba de fasole",
					"Cascaval pane", "Cartofi pai", "Legume sote",
					"Chiftele", "Ardei copti", "Salata de varza",
					"Friptura de poroc", "Friptura de vita"]		
		row = 1

		for product in products:
			Label(self, text = product
					).grid(row = row, column = 0, sticky = W, padx = (10,0))
			row += 1


		#item prices label
		Label(self, text = "Prices: "
					).grid(row = 0, column = 1)

		#prices list generator and checkbuttons

		row = 1
		t = 0
		self.selected_list = []
		self.prices_list = []

		for x in products:

			prices = random.randrange(10,90)

			self.selected_list.append(BooleanVar())

			self.prices_list.append(prices)
			
			Label(self, text = str(prices)
				).grid(row = row, column = 1)

			#checkbuttons
			Checkbutton(self, text = '', 
							  variable = self.selected_list[t]
							  ).grid(row = row, column = 2, padx = 4 )

			row += 1
			t += 1


		#total sum label
		Label(self, text = "Total: "
			).grid(row = 11, column = 1,pady = 5)

		#total sum
		self.sum_txt = Text(self, width = 5, height = 1, wrap = WORD)
		self.sum_txt.grid(row = 12, column = 1)

		#calculate sum button
		Button(self,
				text = "Calculate total",
				command = self.calculate_sum
				).grid(row = 12, column = 0, padx = (10,0))


	#calculate function
	def calculate_sum(self):
		total = 0
		for i in self.selected_list:
			if i.get():
				total += self.prices_list[self.selected_list.index(i)] 
		self.sum_txt.delete(0.0, END)
		self.sum_txt.insert(0.0, total)


#main
root = Tk()
root.title("Order_up")
app = Application(root)
root.mainloop()