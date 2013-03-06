from Tkinter import *
import webbrowser
from subprocess import Popen as runCommand

root = Tk()
root.title("Pylens")

text = Text(root)
text.config(width=60, height=1)
text.pack(side=LEFT, fill=Y)

# core callback to handle the user query
def handleQuery(event):
	query = text.get(1.0, END).strip()

	# 'o' is the lens for running a command
	if query.startswith("o "):
		runCommand(query[2:].strip())
	# no lens means the query is a website or a search
	elif len(query) > 0:
		if "." in query and " " not in query:
			if not query.startswith("http"):
				query = "http://" + query
		else:
			query = "https://www.google.com/search?q=" + query
		webbrowser.open(query, 2, True)

	close(event)

# close down nicely
def close(event):
	root.destroy()

root.bind("<FocusOut>", close)
root.bind("<Escape>", close)

text.bind("<Return>", handleQuery)
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
