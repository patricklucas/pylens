from Tkinter import *
import webbrowser

root = Tk()
root.title("Pylens")

text = Text(root)
text.config(width=60, height=1)
text.pack(side=LEFT, fill=Y)

# core callback to handle the user query
def callback(event):
	query = text.get(1.0, END).strip()

	# analyze the query and do something awesome
	if len(query) > 0:
		webbrowser.open(query, 2, True)

	# nicely close down
	root.destroy()

# bind callback and steal focus
text.bind("<Return>", callback)
text.focus_force()

# center the window
root.withdraw()
root.update_idletasks()  # Update "requested size" from geometry manager
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.deiconify()

# go time!
root.mainloop()
