from turtle import Turtle

FONT = ("Courier", 24, "normal")
X_POS = -250
Y_POS = 250


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(X_POS, Y_POS)
        self.hideturtle()
        self.level_up()

    def level_up(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(-50, 0)
        self.write(arg=f"Game Over!!!", font=FONT)