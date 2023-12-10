from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Maryam ate {self.score} candies | Highest she ate: "
                       f"{self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.clear()
        self.update_scoreboard()

