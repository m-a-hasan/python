from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.maryam = 0
        self.ayah = 0
        self.update_score()

    def ayah_point(self):
        self.ayah += 1
        self.update_score()

    def maryam_point(self):
        self.maryam += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.ayah, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.maryam, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        if self.maryam == 5:
            self.write("Maryam wins!!!", align=ALIGNMENT, font=FONT)
        else:
            self.write("Ayah wins!!!", align=ALIGNMENT, font=FONT)