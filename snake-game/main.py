import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Maryam's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
keep_score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if food.distance(snake.head) < 15:
        food.move_random()
        snake.extend()
        keep_score.increase_score()

    # Check collision with the wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        keep_score.reset_score()
        snake.reset_snake()

    # Check collision with the body
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            keep_score.reset_score()
            snake.reset_snake()


screen.exitonclick()
