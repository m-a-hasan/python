"""
Classes
    1. Player
    2. Ball
    3. Score

Steps
    1. Create pong screen
    2. Create 2 players
    3. Move 2 players up & down
    4. Move the ball with angle
    5. Return the ball with angle
    6. Detect collision with ball and player
    7. Detect collision with ball and wall
    8. Keep score by detecting collision with player side walls
"""
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Maryam VS Ayah - The Pong")
screen.tracer(0)

maryam = Paddle(init_x_position=350)
ayah = Paddle(init_x_position=-350)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(fun=maryam.move_up, key="Up")
screen.onkey(fun=maryam.move_down, key="Down")
screen.onkey(fun=ayah.move_up, key="w")
screen.onkey(fun=ayah.move_down, key="s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_collision()

    # Paddle collision
    if (ball.distance(maryam) < 50 and ball.xcor() > 330) or (ball.distance(ayah) < 50 and ball.xcor() < -330):
        ball.paddle_collision()

    # Game point
    if ball.xcor() > 390:
        score.ayah_point()
        ball.restart_game()

    elif ball.xcor() < -390:
        score.maryam_point()
        ball.restart_game()

    if score.maryam == 5 or score.ayah == 5:
        score.game_over()
        game_is_on = False

screen.exitonclick()
