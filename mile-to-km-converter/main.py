from tkinter import *

FONT = ("Arial", 14)
window = Tk()
window.title("Mile to Km Converter")
window.geometry("400x250")
window.config(padx=80, pady=80)


def calculation():
    mile = float(text_box.get())
    km = int(mile * 1.61)
    number_label.config(text=str(km))


text_box= Entry(width=10)
text_box.grid(row=0, column=1)

mile_label = Label(text="Miles", font=FONT)
mile_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(row=1, column=0)

number_label = Label(text="0", font=FONT)
number_label.grid(row=1, column=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

calculator = Button(text ="Calculate", command=calculation)
calculator.grid(row=2, column=1)

window.mainloop()
