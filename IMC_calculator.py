import math
from tkinter import *

root = Tk()
root.title("calculadora de IMC")
def printName():
    orange = "#ff4814"
    green = "#3bab22"
    red = "#e40508"
    weight = float(entry_weight.get())
    height = float(entry_height.get())
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
            
    label_imc['text'] = "tu IMC es "+str(roundedIMC)
    label_meaning['text'] = message
    label_meaning['fg'] = message_color 
    
head_label = Label(root, text="Calculadora de IMC")
label_weight = Label(root, text="cuanto pesas (kg)")
entry_weight = Entry(root)
label_height = Label(root, text="cuanto mides (cm)")
entry_height = Entry(root)
button_1 = Button(root, text="Calcular", command=printName)
label_imc = Label(root)
label_meaning = Label(root)


head_label.grid(row=0, columnspan=2)
label_weight.grid(row=1, sticky=E)
entry_weight.grid(row=1, column=1)
label_height.grid(row=2, sticky=E)
entry_height.grid(row=2, column=1)
button_1.grid(row=3, columnspan=2)
label_imc.grid(row=4, columnspan=2)
label_meaning.grid(row=5, columnspan=2)




root.mainloop()
