from turtle import Turtle, Screen
from random import choice
# import colorgram
#
# colors = colorgram.extract('src_painting.png', 30)
#
# color_list = []
# for color in colors:
#     palette = (color.rgb.r, color.rgb.g, color.rgb.b)
#     color_list.append(palette)
#
# print(color_list)

color_list = [(188, 19, 46), (244, 233, 61), (252, 230, 236), (217, 238, 244), (195, 76, 34),
              (218, 66, 106), (15, 142, 89), (196, 176, 19), (21, 125, 173), (108, 182, 209),
              (18, 167, 213), (209, 153, 90), (26, 40, 75), (36, 43, 110), (79, 175, 96),
              (181, 44, 65), (235, 231, 5), (216, 67, 48), (217, 129, 153), (125, 185, 119),
              (238, 161, 180), (8, 61, 38), (148, 209, 221), (9, 92, 53), (6, 87, 109),
              (160, 30, 27), (237, 169, 162), (159, 212, 183)]

tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)
tim.speed(7)

tim.penup()
x_pos = -250
y_pos = -200
tim.goto(x_pos, y_pos)
tim.color(choice(color_list))

for _ in range(10):
    for _ in range(10):
        tim.pendown()
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.color(choice(color_list))

    tim.penup()
    y_pos += 50
    tim.goto(x_pos, y_pos)


screen = Screen()
screen.exitonclick()
