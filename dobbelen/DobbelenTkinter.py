#DobbelenTkinter Serkan

#importeert tkinter, "tk" zorgt ervoor dat je "tkinter" niet de hele tijd hoeft in te vullen
import tkinter as tk
#dit heb ik later nodig zodat er een random getal word gekozen
import random

#maakt een window aan met de naam "Dobbelen"
window = tk.Tk()
window.title("Dobbelen")

#voegt text toe dat ook de achtergrond is voor de window
Label1 = tk.Label(
    height=5,
    width=50,
    text='Klik op "Random getal" om een random getal te maken!',
    font=("Arial", 30),
    background='#aa00ff'
)
#dit zorgt ervoor dat de achtergrond volledig word gevuld
Label1.pack(fill=tk.BOTH, expand=True)

#dit heb ik later nodig voor de random nummer
Label2 = tk.Label(
    height=5,
    width=30,
    text='',
    font=("Arial", 40),
    background='#aa00ff'
)
Label2.pack(fill=tk.BOTH, expand=True)

#als je hier op klikt dan maakt hi een random getal aan
submit = tk.Button(
    text="Random getal",
    background='white',
    font=("Arial", 18)   
)
submit.pack()

#lijst van random getallen
dobbelen = list(('1','2','3','4','5','6'))

#hier veranderd de label2 stukje zodat er een random getal komt
def submitten(event):
    Label2['text'] = 'Het getal is: ' + random.choice(dobbelen) + '!'

#linkermuisknop word gebind met de functie "submitten" en de knop "submit"
submit.bind('<Button-1>', submitten)


#lijst van kleuren
kleuren = list(('#aa00ff', '#ff3c00', '#00e1ff', '#0dff00', '#2600ff', '#fffb00', '#ff0000'))

#achtergrond veranderen met rechermuisknop
def veranderAchtergrond(event):
    Label1['background'] = random.choice(kleuren)
    Label2['background'] = random.choice(kleuren)

#bind de rechtermuisknop met submit en functie die de achtergrond evranderd
submit.bind('<Button-3>', veranderAchtergrond)



#dit zorgt ervoor dat de nummer word verwijderd
clear = tk.Button(
    text="Clear",
    background='white',
    font=("Arial", 18)   
)
clear.pack(side='bottom')

#veranderd de text naar "" (niks)
def clearen(event):
    Label2['text'] = ''

#bind de knop met de funtie    
clear.bind('<Button-1>', clearen)


window.mainloop()