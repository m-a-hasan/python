import turtle
import pandas

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

screen = turtle.Screen()
img = "australia.gif"
screen.addshape(img)
screen.setup(width=1000, height=800)

timmy = turtle.Turtle()
timmy.shape(img)


# Get screen co-ordinates (will be commented out after finding x and y)
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
#
# turtle.mainloop()

data = pandas.read_csv("states.csv")
data["guessed"] = 0
data["lower_state"] = data.state.str.lower()

for i in range(8):
    answer_state = turtle.textinput("State Guess Game", "Write down a state name")
    if (answer_state.lower() in data.lower_state.values and
            int(data.guessed[data.lower_state == answer_state.lower()].iloc[0]) == 0):
        x_cor = data.x[data["lower_state"] == answer_state.lower()]
        y_cor = data.y[data["lower_state"] == answer_state.lower()]

        data_index = data[data.lower_state == answer_state.lower()].index.values[0]

        data.at[data_index, "guessed"] = 1

        writer.goto(x=int(x_cor.iloc[0]), y=int(y_cor.iloc[0]))
        correct_state = data.state[data.lower_state == answer_state.lower()]
        writer.write(correct_state.to_string(index=False), font=("Arial", 10, "normal"))

writer.goto(-300, -200)
final_score = len(data[data.guessed == 1])
writer.write(f"Your score is: {final_score} out of 8", font=("Arial", 20, "normal"))

# States to learn
incorrect_states = data[data.guessed < 1]
learning_info = incorrect_states[["state", "x", "y"]]
learning_info.to_csv("states_to_learn.csv",index=False)

screen.exitonclick()
