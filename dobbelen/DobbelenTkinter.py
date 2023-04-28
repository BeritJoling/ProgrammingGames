#DobbelenTkinter Serkan
#importeert tkinter, "tk" zorgt ervoor dat je "tkinter" niet de hele tijd hoeft in te vullen
import tkinter as tk
#dit heb ik later nodig zodat er een random getal word gekozen
import random
class Dobbelen:
        def __init__(self, master):
            #maakt een window aan met de naam "Dobbelen"
            self.master = master
            master.title("Dobbelen")
            #voegt text toe dat ook de achtergrond is voor de window
            self.Label1 = tk.Label(
                height=5,
                width=50,
                text='Klik op "Random getal" om een random getal te maken! \n Rechtermuisknop op "Random Getal" Veranderd de achtergrond',
                font=("Arial", 30),
                background='#aa00ff'
            )
            #dit zorgt ervoor dat de achtergrond volledig word gevuld
            self.Label1.pack(fill=tk.BOTH, expand=True)
            #dit heb ik later nodig voor de random nummer
            self.Label2 = tk.Label(
                height=5,
                width=30,
                text='',
                font=("Arial", 40),
                background='#aa00ff'
            )
            self.Label2.pack(fill=tk.BOTH, expand=True)
            #als je hier op klikt dan maakt hi een random getal aan
            self.submit = tk.Button(
                text="Random getal",
                background='white',
                font=("Arial", 18)   
            )
            self.submit.pack()
            #lijst van random getallen
            self.dobbelen = list(('1','2','3','4','5','6'))
            #hier veranderd de label2 stukje zodat er een random getal komt
            def submitten(event):
                self.Label2['text'] = 'Het getal is: ' + random.choice(self.dobbelen) + '!'
            #linkermuisknop word gebind met de functie "submitten" en de knop "submit"
            self.submit.bind('<Button-1>', submitten)
            #lijst van kleuren
            self.kleuren = list(('#aa00ff', '#ff3c00', '#00e1ff', '#0dff00', '#2600ff', '#fffb00', '#ff0000', '#ffffff'))
            #achtergrond veranderen met rechermuisknop
            def veranderAchtergrond(event):
                self.Label1['background'] = random.choice(self.kleuren)
                self.Label2['background'] = random.choice(self.kleuren)
            #bind de rechtermuisknop met submit en functie die de achtergrond evranderd
            self.submit.bind('<Button-3>', veranderAchtergrond)
            #dit zorgt ervoor dat de nummer word verwijderd
            self.clear = tk.Button(
                text="Clear",
                background='white',
                font=("Arial", 18)   
            )
            self.clear.pack(side='bottom')
            #veranderd de text naar "" (niks)
            def clearen(event):
                self.Label2['text'] = ''
            #bind de knop met de funtie    
            self.clear.bind('<Button-1>', clearen)


# if __name__ == '__main__':
#     root = tk.Tk()
#     app = Dobbelen(root)
#     root.mainloop()