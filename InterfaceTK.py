import tkinter as tk
import tkinter.ttk as ttk

class Master(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('')
        self.geometry('300x120')
        self.resizable(False, False)

class JanelaMenuInicial(tk.Frame):
    def __init__(self, master) -> None:
        self.master = master
        tk.Button(self).pack()

print(__name__)
mstr = Master()
JanelaMenuInicial(mstr)
mstr.mainloop()