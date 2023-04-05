import tkinter as tk
import random
#import tkinter ("as tk" zorgt ervoor dat ik niet over "tkinter" hoef in te vullen)

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Getallen raden")
        
        #de titel

        self.number_to_guess = random.randint(1, 20)
        self.guesses_remaining = 3
        #wordt een random getal aangemaakt en de guesses kunnen hier gewijzigd worden

        self.label = tk.Label(master, text="Raad het getal tussen 1 en 20:")
        self.label.pack()
        #hier vraagt het om te raden

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
        

        self.remaining_label = tk.Label(master, text="Je hebt nog {} pogingen over".format(self.guesses_remaining))
        self.remaining_label.pack()
        #hier staat het hoeveel guesses je nog hebt

        self.guess_button = tk.Button(master, text="Raad", command=self.check_guess)
        self.guess_button.pack()
        #de button voor raden

    def check_guess(self):
        guess = int(self.guess_entry.get())
        self.guess_entry.delete(0, 'end')

        self.guesses_remaining -= 1
        self.remaining_label.config(text="Je hebt nog {} pogingen over".format(self.guesses_remaining))

        if guess == self.number_to_guess:
            self.result_label.config(text="Gefeliciteerd, je hebt het juiste getal geraden!")
            self.guess_button.config(state="disabled")
            self.guess_entry.config(state="disabled")
        elif self.guesses_remaining == 0:
            self.result_label.config(text="Je hebt geen pogingen meer over. Het juiste getal was {}.".format(self.number_to_guess))
            self.guess_button.config(state="disabled")
            self.guess_entry.config(state="disabled")
        elif guess < self.number_to_guess:
            self.result_label.config(text="Het gezochte getal is hoger.")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Het gezochte getal is lager.")
            #hier checkt die wat de gebruiker heeft ingevuld en geeft daarop antwoord