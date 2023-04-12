import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk

class CoinFlipGame:
    def __init__(self):
        self.root = Tk()
        self.root.title("Coin Flipping Game")
        self.root.geometry('500x500')

        l = Label(self.root, text="Coin Flipping Game")
        l.config(font=("Courier", 14))
        t = Text(self.root, width=52, height=5)
        t.insert(INSERT, "Instructions: Flip the coin and observe the result.")
        l.pack()
        t.pack()

        load = Image.open("coinflip/heads.png")
        load = load.resize((150, 150))
        self.heads = ImageTk.PhotoImage(load)

        load = Image.open("coinflip/tails.png")
        load = load.resize((150, 150))
        self.tails = ImageTk.PhotoImage(load)

        self.i = Label(self.root, image=self.heads)
        self.i.pack()

        b = Button(self.root, text="Flip Coin", bg='lightblue', fg='white', activebackground="lightgray", padx=10, pady=10, command=self.flip)
        b.config(font=("Courier", 8))
        b.pack()

        self.e = Button(self.root, text="Exit Game", bg='gray', fg='white', activebackground="lightgray", padx=40, pady=20, command=self.exit)
        self.e.config(font=("Courier", 14))
        
        self.root.mainloop()

    def flip(self):
        num = random.randint(0,1)
        if num == 0:
            self.i.config(image=self.heads)
        else:
            self.i.config(image=self.tails)

    def exit(self):
        self.root.destroy()
        
CoinFlipGame()
