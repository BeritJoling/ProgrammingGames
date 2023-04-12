import tkinter as tk
from tkinter import ttk
from snake import snake_menu
from getallenraden import rohaneindopdracht
from dobbelen import DobbelenTkinter
from coinflip import eindopdr

class window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Main Menu")
        
        self.main_label = tk.Label(self, text="This is the main menu, select the game you'd like to play from the buttons below.")
        self.main_label.grid(row=1, columnspan=3, padx=5, pady=10)
        
        # Credit to Serkan
        self.game1_start = ttk.Button(self, text="Dobbelen", command=self.Dobbelen)
        self.game1_start.grid(row=2, column=1, padx=5, pady=5)
        
        # Credit to Berit
        self.game2_start = ttk.Button(self, text="Snake", command=self.Snake)
        self.game2_start.grid(row=3, column=1, padx=5, pady=5)
        
        # Credit to Rohan
        self.game3_start = ttk.Button(self, text="Number Guessing", command=self.NumberGuessing)
        self.game3_start.grid(row=4, column=1, padx=5, pady=5)
        
        # Credit to Peter
        self.game4_start = ttk.Button(self, text="Coinflip", command=self.Coinflip)
        self.game4_start.grid(row=5, column=1, padx=5, pady=5)
        
        # Credit to Stefan
        self.game5_start = ttk.Button(self, text="Game5", command=self.game5)
        self.game5_start.grid(row=6, column=1, padx=5, pady=5)
        
    def Dobbelen(self):
        DobbelenTkinter.Dobbelen()
        
        self.destroy()
    
    def Snake(self):
        snake_menu.snake_diff_window()
        
        self.destroy()
        
    def NumberGuessing(self):
        rohaneindopdracht.GuessingGame()
        
        self.destroy
    
    def Coinflip(self):
        eindopdr.CoinFlipGame()
        
        self.destroy()
    
    def game5(self):
        pass
    

root = window()
root.mainloop()
