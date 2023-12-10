from flask import Flask, render_template, request
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/a62cc1e48874d8547641"
blog_resp = requests.get(blog_url)

if blog_resp.status_code == 200:
    blog_data = blog_resp.json()


@app.route("/contact", methods=['POST'])
def receive_data():
    print(request.form['name'])
    print(request.form['email'])
    print(request.form['phone'])
    print(request.form['description'])
    return render_template("contact.html", title="Successfully sent your message")


@app.route("/post/<num>")
def post(num):
    post_position = int(num) - 1
    title = blog_data[post_position]["title"]
    image_path = f"assets/img/{title.lower().replace(' ', '-')}.jpg"
    return render_template("post.html", blog=blog_data[post_position], file_path=image_path)


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Me")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/")
@app.route("/index.html")
def home():
    if blog_data:
        return render_template("index.html", blog_data=blog_data)
    else:
        return f"Error: {blog_resp.status_code}"


if __name__ == '__main__':
    app.run()


