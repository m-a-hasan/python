from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_resp = requests.get(blog_url)

if blog_resp.status_code == 200:
    blog_data = blog_resp.json()


@app.route("/post/<int:num>")
def get_post(num):
    # return render_template("post.html", details=blog_data[1])
    for blog in blog_data:
        if num == blog['id']:
            print(blog)
            return render_template("post.html", details=blog)


@app.route("/")
def home():
    if blog_data:
        return render_template("index.html", blog_data=blog_data)
    else:
        return f"Error: {blog_resp.status_code}"


if __name__ == "__main__":
    app.run()
