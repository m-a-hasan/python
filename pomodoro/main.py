from tkinter import *
from time import strftime
from time import gmtime

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60

repeat_process = 0
tick = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    if timer is None:
        pass
    else:
        window.after_cancel(timer)
        canvas.itemconfig(timer_label, text="00:00")
        title.config(text="Timer", fg=GREEN)
        global tick
        tick = ""
        check_label.config(text=tick)
        global repeat_process
        repeat_process = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repeat_process
    repeat_process += 1

    if repeat_process % 8 == 0:
        title.config(text="Break", fg=RED)
        time_counter(LONG_BREAK_MIN)
    elif repeat_process % 2 == 0:
        title.config(text="Break", fg=PINK)
        time_counter(SHORT_BREAK_MIN)
    else:
        title.config(text="Work", fg=GREEN)
        time_counter(WORK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def time_counter(count):
    if count >= 0:
        time_display = strftime("%M:%S", gmtime(count))
        canvas.itemconfig(timer_label, text=time_display)
        global timer
        timer = window.after(1000, time_counter, count - 1)
    else:
        start_timer()
        if repeat_process % 2 == 0:
            global tick
            tick = tick + " ✔ "
            check_label.config(text=tick)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img_file = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img_file)
timer_label = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title = Label(text="Timer", font=(FONT_NAME, 60), bg=YELLOW, fg=GREEN)
title.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)

window.mainloop()
