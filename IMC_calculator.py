import math
from tkinter import *


class IMC_calculator:
    def __init__(self, master):
        
        self.head_label = Label(master, text="Calculadora de IMC")
        self.gender_list = Listbox(master, width=6, height=2)
        self.label_weight = Label(master, text="cuanto pesas (kg)")
        self.entry_weight = Entry(master)
        self.label_height = Label(master, text="cuanto mides (cm)")
        self.entry_height = Entry(master)
        self.button_1 = Button(master, text="Calcular")
        self.button_1.bind("<Button-1>", self.calcIMC )
        self.label_imc = Label(master)
        self.label_meaning = Label(master)
        self.labe_ideal = Label(master)

        self.head_label.grid(row=0, columnspan=2)
        self.gender_list.insert(1, "Hombre")
        self.gender_list.insert(2, "Mujer")
        self.gender_list.grid(row=1, column=1, sticky=E)
        self.gender_list.select_set(0)
        self.gender_list.event_generate("<<ListboxSelect>>")
        self.label_weight.grid(row=2, sticky=E)
        self.entry_weight.grid(row=2, column=1)
        self.label_height.grid(row=3, sticky=E)
        self.entry_height.grid(row=3, column=1)
        self.button_1.grid(row=4, columnspan=2)
        self.label_imc.grid(row=5, columnspan=2)
        self.label_meaning.grid(row=6, columnspan=2)
        self.labe_ideal.grid(row=7, columnspan=2)


    def calcIMC(self, event):
        orange = "#ff4814"
        green = "#3bab22"
        red = "#e40508"
        weight = float(self.entry_weight.get())
        height = float(self.entry_height.get())
        IMC = (weight/(height*height))*10000
        roundedIMC = math.ceil(IMC*100)/100
        gender =  self.gender_list.get(ACTIVE)
        if gender == "Hombre":
            idealIMC = 23
        else:
            idealIMC = 22
        idealWeight = math.ceil(((idealIMC*weight)/IMC)*100)/100
        if IMC < 25 and IMC >= 18.5:
            message = "Normal"
            message_color = green
        elif IMC >= 25 and IMC < 30:
            message = "Soprepeso"
            message_color = orange
        elif IMC >= 30 and IMC < 40:
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
        self.labe_ideal['text'] = "tu peso ideal es "+str(idealWeight)
    
root = Tk()
b = IMC_calculator(root)
root.title("calculadora de IMC")
root.mainloop()
