import math
from tkinter import *

root = Tk()

def printName():
    weight = float(entry_weight.get())
    height = float(entry_height.get())
    IMC = (weight/(height*height))*10000
    roundedIMC = math.ceil(IMC*100)/100 
    print(IMC)
    label_imc['text'] = "tu IMC es "+str(roundedIMC)
    
head_label = Label(root, text="Calculadora de IMC")
label_weight = Label(root, text="cuanto pesas (kg)")
entry_weight = Entry(root)
label_height = Label(root, text="cuanto mides (cm)")
entry_height = Entry(root)
button_1 = Button(root, text="Calcular", command=printName)
label_imc = Label(root)


head_label.grid(row=0, columnspan=2)
label_weight.grid(row=1, sticky=E)
entry_weight.grid(row=1, column=1)
label_height.grid(row=2, sticky=E)
entry_height.grid(row=2, column=1)
button_1.grid(row=3, columnspan=2)
label_imc.grid(row=4, columnspan=2)




root.mainloop()

#http://stackoverflow.com/questions/17125842/python-3-tkinter-change-label-text
