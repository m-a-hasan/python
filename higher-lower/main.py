from flask import Flask
from random import randrange

app = Flask(__name__)
correct = randrange(10)

@app.route("/")
def main_screen():
    return ("<h1>Guess a number between 0 and 9 <br/> and type it at the end of the URL!</h1>"
            "<img src='https://media.giphy.com/media/xUn3CftPBajoflzROU/giphy.gif'>")


@app.route("/<int:number>")
def guess_number(number):
    if number > correct:
        return ("<h1 style='color:purple'>Too high, try again!</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    elif number < correct:
        return ("<h1 style='color:red'>Too low, try again!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
    else:
        return ("<h1 style='color:green'>You found me!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")


app.run()
