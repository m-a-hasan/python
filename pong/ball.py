from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball_speed = 1
        self.y_direction = self.ball_speed
        self.x_direction = self.ball_speed
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.goto(self.xcor() + self.x_direction, self.ycor() + self.y_direction)

    def wall_collision(self):
        if self.ycor() < 0:
            self.y_direction = self.ball_speed
        else:
            self.y_direction = -self.ball_speed

    def paddle_collision(self):
        self.ball_speed += 0.5
        if self.xcor() < 0:
            self.x_direction = self.ball_speed
        else:
            self.x_direction = -self.ball_speed

    def restart_game(self):
        self.ball_speed = 1
        if self.xcor() > 0:
            self.x_direction = -self.ball_speed
            self.y_direction = -self.ball_speed
        else:
            self.x_direction = self.ball_speed
            self.y_direction = self.ball_speed
        self.goto(0, 0)
