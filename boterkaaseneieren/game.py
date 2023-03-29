import tkinter as tk
from tkinter import font

class Speelveld(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Boter-Kaas-En-Eieren")
        self.cells = {}

    def __maak_bordweergave(self):
        weergavescherm = tk.Frame(master=self)
        weergavescherm.pack(fill=tk.X)
        self.weergave = tk.Label(master=weergavescherm,
                                text="Klaar voor?", 
                                font=font.Font(size=28, weight="bold"),
                                )
        self.weergave.pack()

    def __maak_bordraster(self):
        rasterscherm = tk.Frame(master=self)
        rasterscherm.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize= 75)
            for col in range(3):
                knop = tk.Button(master=rasterscherm,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue"
                )
                self._cells[knop] = (row, col)
                knop.grid(row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )


    
        

        