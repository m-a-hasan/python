from flask import Flask
from functools import wraps

app = Flask(__name__)


def make_bold(func):
    @wraps(func)
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper


def make_emphasis(func):
    @wraps(func)
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper


def make_underlined(func):
    @wraps(func)
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, I see you are {number} years old!"


app.run()
