import tkinter as tk
import tkinter.ttk as ttk

class Master(tk.Tk):
    pass

class JanelaMenuInicial(tk.Frame):
    def __init__(self, master) -> None:
        self.master = master
        tk.Button(self).pack()
        pass

mstr = Master()
JanelaMenuInicial(mstr)
mstr.mainloop()