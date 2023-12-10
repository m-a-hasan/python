from turtle import Turtle, Screen
from random import random, randrange, randint


def change_color(change_turtle):
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)

    change_turtle.color((r, g, b))


tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)
change_color(tim)
tim.speed("fastest")

### Makes a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

### Makes a multicolor dotted line
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     change_color(tim)

### Making triangle to 10-agon
# for number_of_sides in range(3, 11):
#     change_color(tim)
#     for _ in range(number_of_sides):
#         tim.forward(100)
#         tim.right(360 / number_of_sides)

# for _ in range(500):
#     change_color(tim)

### Making random walK
# tim.pensize(15)
# tim.speed(7)
#
# for _ in range(200):
#     direction = randrange(1, 5)
#     if direction == 1:
#         tim.forward(30)
#     elif direction == 2:
#         tim.backward(30)
#     elif direction == 3:
#         tim.right(90)
#         up_down = randrange(1, 3)
#         if up_down == 1:
#             tim.forward(30)
#         else:
#             tim.backward(30)
#     else:
#         tim.left(90)
#         up_down = randrange(1, 3)
#         if up_down == 1:
#             tim.forward(30)
#         else:
#             tim.backward(30)
#     change_color(tim)

r = 100
heading_angle = 0
while heading_angle < 360:
    change_color(tim)
    tim.setheading(heading_angle)
    tim.circle(r)
    heading_angle += 2

screen = Screen()
screen.exitonclick()
