from Tkinter import *
import webbrowser
from subprocess import Popen as runCommand
from os.path import expanduser

root = Tk()
root.title("Pylens")

text = Text(root)
text.config(width=60, height=1)
text.pack(side=LEFT, fill=Y)

# custom searches
lenses = []
querySwapToken = "{query}"

# parse the config
try:
	configs = open(expanduser("~") + "/pylens.conf", 'r')
	for lens in configs:
		if not lens.startswith("#") and len(lens.strip()) > 0:
			sep = lens.index(" ")
			lenses += [{"command" : lens[:sep].strip(), "query" : lens[sep:].strip()}]
except IOError:
	print "no config file '~/pylens.conf' found"

# core callback to handle the user query
def handleQuery(event):
	query = text.get(1.0, END).strip()

	# try to match a macro
	bestLens = None
	for lens in lenses:
		if (query + " ").startswith(lens["command"] + " "):
			if bestLens is None or len(lens["command"]) > len(bestLens["command"]):
				bestLens = lens
	if bestLens is not None:
		query = bestLens["query"].replace(querySwapToken, query[len(bestLens["command"]):].strip())

	# 'o' is the lens for running a command
	if query.startswith("o "):
		query = query[2:].strip().replace("~", expanduser("~"))
		runCommand(query, shell=True)
	# no lens means the query is a website or a search
	elif len(query) > 0:
		if "." in query and " " not in query and not query.startswith("http"):
			query = "http://" + query
		elif not query.startswith("http"):
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
