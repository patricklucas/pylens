from Tkinter import *
import webbrowser

root = Tk()
root.title("Pyfred")

text = Text(root)
text.config(width=60, height=1)
text.pack(side=LEFT, fill=Y)

def callback(event):
  url = text.get(1.0, END).strip()
  webbrowser.open(url, 2, True)
  root.destroy()

text.bind("<Return>", callback)
text.grab_set()

# center the window
root.withdraw()
root.update_idletasks()  # Update "requested size" from geometry manager
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.deiconify()

root.mainloop()
