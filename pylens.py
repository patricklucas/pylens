import os
from Tkinter import END, LEFT, Tk, Text, Y
import subprocess
import webbrowser

QUERY_SWAP_TOKEN = "{query}"
CONFIG_PATH = os.path.expanduser("~/.pylens.conf")


class PyLens(object):

    def __init__(self):
        self.root, self.text = self._init_ui()
        self.lenses = self._init_lenses()

    def _init_ui(self):
        root = Tk()
        root.title("pylens")
        root.bind("<FocusOut>", self.close)
        root.bind("<Escape>", self.close)

        # center the window
        root.withdraw()
        root.update_idletasks() # Update "requested size" from geometry manager
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry("+%d+%d" % (x, y))
        root.deiconify()

        text = Text(root)
        text.config(width=60, height=1)
        text.pack(side=LEFT, fill=Y)
        text.bind("<Return>", self.handle_query)
        text.focus_force()

        return root, text

    def _init_lenses(self):
        lenses = [] # Custom searches

        # Parse the config file
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH) as f:
                for line in f:
                    line = line.strip()

                    if not line or line.startswith('#'):
                        continue

                    command, query = line.split(' ', 1)
                    self.lenses.append(dict(command=command, query=query))

        return lenses

    def run(self):
        self.root.mainloop()

    def handle_query(self, event):
        query = self.text.get(1.0, END).strip()

        # try to match a macro
        best_lens = None
        for lens in self.lenses:
            if (query + " ").startswith(lens['command']):
                if (not best_lens or
                      len(lens['command']) > len(best_lens['command'])):
                    best_lens = lens

        if best_lens is not None:
            query = best_lens["query"].replace(QUERY_SWAP_TOKEN,
                query[len(best_lens["command"]):].strip())

        if query.startswith("o "):
            # 'o' is the lens for running a command
            query = query[2:].strip().replace("~", os.path.expanduser("~"))
            subprocess.call(query, shell=True)
        elif len(query) > 0:
            # no lens means the query is a website or a search
            if not query.startswith("http"):
                if '.' in query and ' ' not in query:
                    query = "http://" + query
                else:
                    query = "https://www.google.com/search?q=" + query

            webbrowser.open(query, 2, True)

        self.close(event)

    def close(self, event):
        self.root.destroy()


if __name__ == '__main__':
    PyLens().run()
