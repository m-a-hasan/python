import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
FILE_NAME = "data/words_to_learn.csv"

current_word = None

# ---------------------------- Load CSV ----------------------- #
try:
    df = pd.read_csv(FILE_NAME)
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
finally:
    to_learn = df.to_dict(orient="records")


# -------------------- Save Words to Learn -------------------- #
def save_words():
    pd.DataFrame(to_learn).to_csv(FILE_NAME, index=False)


# -------------------------- Change Word ---------------------- #
def remove_word():
    to_learn.remove(current_word)
    next_word()


def next_word():
    global timer, current_word
    window.after_cancel(timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(lang_label, text="French", fill="black")
    canvas.itemconfig(word, text=current_word["French"], fill="black")
    timer = window.after(3000, show_translation)


# ---------------------- Show Translation --------------------- #
def show_translation():
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(lang_label, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")


# ------------------------ UI Setup --------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=show_translation)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front)
lang_label = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

retry_img = PhotoImage(file="images/wrong.png")
retry_btn = Button(image=retry_img, command=next_word, highlightthickness=0)
retry_btn.grid(row=1, column=0)

completed_img = PhotoImage(file="images/right.png")
completed_btn = Button(image=completed_img, command=remove_word, highlightthickness=0)
completed_btn.grid(row=1, column=1)

next_word()

window.mainloop()

save_words()
