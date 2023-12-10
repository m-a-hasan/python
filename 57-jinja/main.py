import random
from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


def gen_age(username):
    gen_url = 'https://api.genderize.io'
    gen_param = {'name': username}
    gen_resp = requests.get(gen_url, params=gen_param)

    if gen_resp.status_code == 200:
        gen_data = gen_resp.json()
    else:
        print(f"Error: {gen_resp.status_code}")

    age_url = 'https://api.agify.io'
    age_param = {'name': username}
    age_resp = requests.get(age_url, params=age_param)

    if age_resp.status_code == 200:
        age_data = age_resp.json()
    else:
        print(f"Error: {age_resp.status_code}")

    if gen_resp.status_code == 200 and age_resp.status_code == 200:
        return {
            "gender": gen_data["gender"],
            "age": age_data["age"]
        }
    else:
        return {}


@app.route("/blog")
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_resp = requests.get(blog_url)

    if blog_resp.status_code == 200:
        blog_data = blog_resp.json()
        return render_template("blog.html", blog_data=blog_data)

    else:
        return f"Error: {blog_resp.status_code}"


@app.route("/guess/<name>")
def welcome(name):
    payload = gen_age(name)
    if payload:
        return render_template("welcome.html",
                               name=name,
                               gender=payload["gender"],
                               age=payload["age"])
    else:
        return "Something went wrong"


@app.route("/")
def main():
    rand_num = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=rand_num, year=current_year)


if __name__ == '__main__':
    app.run()

