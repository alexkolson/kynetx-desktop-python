import kynetx 
from Tkinter import *

app = kynetx.kynetx("a369x122")
app.raise_event("desktop", "say_hello")
print app.directives
"""root = Tk()
w = Label(root, text=text)
w.pack()
root.mainloop()"""
