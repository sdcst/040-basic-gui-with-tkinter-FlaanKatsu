import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("「T-Town」獣医データベース")
window.resizable(False,False)

imgimg = PhotoImage(file="dog.png")

##Create GUI elements  (i tried tanslating it into japanese for fun)

img = tk.Label(window, image=imgimg, borderwidth=3)
namelb = tk.Label(window, text="名前")
typelb = tk.Label(window, text="タイプ")
breedlb = tk.Label(window, text="犬種")
ownerlb = tk.Label(window, text="飼い主")
bdlb = tk.Label(window, text="誕生日")
CD = tk.Label(window, text="クライアント\nデータベース")
bx1 = tk.Entry(window, width=12)
bx2 = tk.Entry(window, width=12)
bx3 = tk.Entry(window, width=12)
bx4 = tk.Entry(window, width=12)
bx5 = tk.Entry(window, width=12)
bx6 = tk.Entry(window, width=16)
btnsearch = tk.Button(window,text="名前で検索")
btnbk = tk.Button(window,text="< 前へ")
btnfwd = tk.Button(window,text="次へ >")
btnhz = tk.Button(window,text="保存する")

##format GUI

img.grid(row = 1, column = 1, rowspan = 3)
btnsearch.grid(row = 1, column = 4)
bx6.grid(row = 1, column = 5)
CD.grid(row = 2, column = 3)

namelb.grid(row = 4, column = 1)
typelb.grid(row = 4, column = 2)
breedlb.grid(row = 4, column = 3)
ownerlb.grid(row = 4, column = 4)
bdlb.grid(row = 4, column = 5)

bx1.grid(row = 5, column = 1)
bx2.grid(row = 5, column = 2)
bx3.grid(row = 5, column = 3)
bx4.grid(row = 5, column = 4)
bx5.grid(row = 5, column = 5)

btnbk.grid(row = 6, column=1,)
btnfwd.grid(row = 6, column = 5)
btnhz.grid(row = 6, column = 3)

##sustain window
window.mainloop()