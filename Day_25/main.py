from tkinter import *

window = Tk()
window.title('Conversor de Milhas para Quilômetros')
window.minsize(width=200, height=100)

#Rótulos
label_miles = Label(text='Milhas', font=('Arial'))
label_miles.grid(column=2, row=0)

label_equal = Label(text='é igual a', font=('Arial'))
label_equal.grid(column=0, row=1)

label_result = Label(text=0, font=('Arial'))
label_result.grid(column=1, row=1)

label_km = Label(text='Km', font=('Arial'))
label_km.grid(column=2, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

#Botão
def miles_to_km():
    input_value = float(input.get())
    result = input_value * 1.609
    label_result.config(text=float(round(result, 2)))

button = Button(text='Calcular', command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()