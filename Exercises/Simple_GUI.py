# Demonstrates creating a window

from tkinter import * #tkinter is importet globally

# create root window

root = Tk() # you can have just one root windowd

# modify the window

root.title("Simple GUI")
root.geometry("200x100")

# kick off the window's event loop
root.mainloop()