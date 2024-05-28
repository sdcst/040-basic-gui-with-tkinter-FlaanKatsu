import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("「T-Town」獣医データベース")
window.resizable(False,False)

imgimg = PhotoImage(file="dog.png")

pochakko = tk.Label(window, text="ポチャッコーちゃん！")
pochakkoChan = tk.Label(window, image=imgimg, borderwidth=3)
body = tk.Label(window, text="BTW, you noted that \"an app built on a\n mac will look like a mac app\", this\nis techically incorrect, an app RUNNING on\na mac will look like a mac app, build machine\ndoes not matter.", bg="#9effd0")

pochakko.grid(row=1, column=4)
pochakkoChan.grid(row=1, column=3)
body.grid(row=2,column=1,columnspan=5)

window.mainloop()