from turtle import Turtle, Screen


def move_forward():
    tim.forward(2)


def move_backward():
    tim.backward(2)


def move_clockwise():
    tim.right(2)


def move_counter_clockwise():
    tim.left(2)


tim = Turtle()

screen = Screen()
screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_clockwise, "d")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(screen.resetscreen, "c")

screen.exitonclick()
