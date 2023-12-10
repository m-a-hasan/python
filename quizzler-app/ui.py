from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.timer = self.window.after(2)

        self.user_score = Label(text="Score: 0", font=(FONT_NAME, 14), bg=THEME_COLOR, fg="white")
        self.user_score.grid(row=0, column=1, pady=(0, 20))

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_label = self.canvas.create_text(150,
                                                      125,
                                                      text="Amazon acquired Twitch in August 2024",
                                                      width=280,
                                                      font=(FONT_NAME, 20, "italic"),
                                                      fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(20, 15))

        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, command=self.true_pressed, highlightthickness=0)
        self.true_btn.grid(row=2, column=0, pady=(20, 0))

        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, command=self.false_pressed, highlightthickness=0)
        self.false_btn.grid(row=2, column=1, pady=(20, 0))

        self.canvas.itemconfig(self.question_label, text=self.quiz.next_question())

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.user_score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_label, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_label, text="You've reached the end of the questions!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, answer_is_right):
        if answer_is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
