import math
from tkinter import *


class IMC_calculator:
    def __init__(self, master):
    
        self.head_label = Label(master, text="Calculadora de IMC")
        self.label_weight = Label(master, text="cuanto pesas (kg)")
        self.entry_weight = Entry(master)
        self.label_height = Label(master, text="cuanto mides (cm)")
        self.entry_height = Entry(master)
        self.button_1 = Button(master, text="Calcular")
        self.button_1.bind("<Button-1>", self.calcIMC )
        self.label_imc = Label(master)
        self.label_meaning = Label(master)

        self.head_label.grid(row=0, columnspan=2)
        self.label_weight.grid(row=1, sticky=E)
        self.entry_weight.grid(row=1, column=1)
        self.label_height.grid(row=2, sticky=E)
        self.entry_height.grid(row=2, column=1)
        self.button_1.grid(row=3, columnspan=2)
        self.label_imc.grid(row=4, columnspan=2)
        self.label_meaning.grid(row=5, columnspan=2)


    def calcIMC(self, event):
        orange = "#ff4814"
        green = "#3bab22"
        red = "#e40508"
        weight = float(self.entry_weight.get())
        height = float(self.entry_height.get())
        IMC = (weight/(height*height))*10000
        roundedIMC = math.ceil(IMC*100)/100 
        print(IMC)
        if IMC < 25 and IMC >= 18.5:
            message = "Normal"
            message_color = green
        elif IMC >= 25 and IMC < 30:
            message = "Soprepeso"
            message_color = orange
        elif IMC >= 30:
            message = "Obesidad"
            message_color = red
        elif IMC >= 40:
            message = "Obesidad morbida"
            message_color = red
        elif IMC < 18.5:
            message = "Bajo peso"
            message_color = orange
                
        self.label_imc['text'] = "tu IMC es "+str(roundedIMC)
        self.label_meaning['text'] = message
        self.label_meaning['fg'] = message_color 
    
root = Tk()
b = IMC_calculator(root)
root.title("calculadora de IMC")
root.mainloop()
