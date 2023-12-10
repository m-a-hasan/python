from tkinter import *


def add(*args):
    result = 0
    for n in args:
        result += n
    return result


def change_label():
    label["text"] = text_input.get()


print(add(5, 6, 2))

root = Tk()
root.geometry("600x400")

label = Label(text="Not clicked yet", font=("Arial", 20))
button = Button(text="Click me", command=change_label)
new_button = Button(text="Click me too", command=change_label)
text_input = Entry(width=10)

label.grid(row=0, column=0)
button.grid(row=1, column=1)
new_button.grid(row=0, column=2)
text_input.grid(row=2, column=3)

root.mainloop()
