import kynetx 
from Tkinter import *

app = kynetx.kynetx("a369x122")
data = app.raise_event("desktop", "say_hello")
action = app.directives[0]['action']

if action == "go":
    msg = app.directives[0]['options']['msg']

root = Tk()

if msg is not None:
    w = Label(root, text=msg)
else:
    w = Label(root, text="No msg from Kynetx today!")

w.pack()
root.mainloop()
