from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
turtles = []
index = 0
x = -230
y = -120
race_is_on = True

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                                                          "(red, orange, yellow, green, blue or purple): ")
winning_color = "red"

for turtle_color in colors:
    myTurtle = Turtle(shape="turtle")
    myTurtle.color(turtle_color)
    myTurtle.penup()
    myTurtle.goto(x=x, y=y)
    turtles.append(myTurtle)
    index += 1
    y += 50

while race_is_on:
    for turtle in turtles:
        turtle.forward(randint(1, 3))
    for turtle in turtles:
        if turtle.xcor() > 250:
            winning_color = turtle.color()
            race_is_on = False

if winning_color[0] == user_bet:
    print(f"You win! The {winning_color[0]} turtle is the winner.")
else:
    print(f"You lose. The {winning_color[0]} turtle is the winner.")
