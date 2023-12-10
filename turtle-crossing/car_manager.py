import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_COR = 260
CAR_WIDTH = 1
CAR_LENGTH = 2


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=CAR_WIDTH, stretch_len=CAR_LENGTH)

    def place_car(self, start_screen, end_screen):
        x_pos = random.randint(start_screen, end_screen)
        y_pos = random.randint(-Y_COR, Y_COR)
        self.goto(x_pos, y_pos)

    def move(self, speed):
        self.goto(x=self.xcor() - speed, y=self.ycor())
