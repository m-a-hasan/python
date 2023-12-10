from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def login():
    return f"<h1>Firstname: {request.form['fname']} Lastname: {request.form['lname']}</h1>"


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
