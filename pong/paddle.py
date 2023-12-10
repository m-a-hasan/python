from turtle import Turtle

WIDTH = 5
LENGTH = 1
INIT_Y_POS = 0
STEP_LENGTH = 20


class Paddle(Turtle):

    def __init__(self, init_x_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.penup()
        self.color("white")
        self.speed("slow")
        self.goto(x=init_x_position, y=INIT_Y_POS)

    def move_up(self):
        new_y_cor = self.ycor() + STEP_LENGTH
        self.goto(x=self.xcor(), y=new_y_cor)

    def move_down(self):
        new_y_cor = self.ycor() - STEP_LENGTH
        self.goto(x=self.xcor(), y=new_y_cor)
