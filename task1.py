import tkinter as tk
from tkinter import *
from tkinter import ttk
##TK settings
window = tk.Tk()
window.title("fake calculator")
window.resizable(False,False)
##create TK widgets
space = tk.Label(window, text=" ")
space2 = tk.Label(window, text=" ")
enterbox1 = tk.Entry(width=10)
enterbox2 = tk.Entry(width=10)
enterbox3 = tk.Entry(width=10)
eq = tk.Label(window, text="=")
x = tk.Label(window, text="x")
##pack TK widgets
space.pack(side=LEFT)
enterbox1.pack(side=LEFT)
x.pack(side=LEFT)
enterbox2.pack(side=LEFT)
eq.pack(side=LEFT)
enterbox3.pack(side=LEFT)
space2.pack(side=LEFT)


window.mainloop()