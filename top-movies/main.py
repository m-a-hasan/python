import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import desc
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from models import db, Movie
from forms import EditMovie, AddMovie

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

TMDB_API_KEY = os.environ.get("TMDB_KEY")
all_movies_url = "https://api.themoviedb.org/3/search/movie"

# Initialize the app with the extension
db.init_app(app)

# Create all database tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    with app.app_context():
        all_movies = Movie.query.order_by(Movie.rating).all()
        total_movies = len(all_movies)
        for rank, movie in enumerate(all_movies, start=1):
            movie.ranking = total_movies - rank + 1
    return render_template("index.html", data=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit_rating():
    movie_id = request.args.get('id')
    form = EditMovie()
    details = Movie.query.get(movie_id)
    if form.validate_on_submit():
        new_rating = float(form.rating.data)
        new_review = form.review.data
        details.rating = new_rating
        details.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, details=details)


@app.route("/delete/<int:movie_id>")
def delete_item(movie_id):
    # Find the book with the given ID in the database
    movie_to_delete = Movie.query.get(movie_id)
    if movie_to_delete:
        # Delete the movie from the database
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        # Handle the case where the book is not found
        return "Book not found", 404


@app.route("/add", methods=["GET", "POST"])
def add_item():
    form = AddMovie()
    if form.validate_on_submit():
        title = form.title.data
        movies_params = {
            "api_key": TMDB_API_KEY,
            "accept": "application/json",
            "query": title
        }
        response = requests.get(all_movies_url, params=movies_params, verify=False)
        movie_data = []
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Process the API response (JSON format in this example)
            api_data = response.json()
            for movie in api_data["results"]:
                info = {
                    "tmdb_id": movie["id"],
                    "original_title": movie["original_title"],
                    "release_date": movie["release_date"]
                }
                movie_data.append(info)
            return render_template("select.html", data=movie_data)
        else:
            # Print an error message if the request was not successful
            response.raise_for_status()
    return render_template("add.html", form=form)


@app.route("/movie/details")
def movie_details():
    tmdb_id = request.args.get('id')
    movie_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}"
    movie_params = {
        "api_key": TMDB_API_KEY,
        "accept": "application/json"
    }
    response = requests.get(movie_url, params=movie_params, verify=False)
    if response.status_code == 200:
        # Process the API response (JSON format in this example)
        api_data = response.json()
        with app.app_context():
            movie = Movie(
                title=api_data['original_title'],
                year=api_data['release_date'],
                description=api_data['overview'],
                img_url=f"https://image.tmdb.org/t/p/original/{api_data['poster_path']}"
            )
            db.session.add(movie)
            db.session.commit()
            movie_id = movie.id
            return redirect(url_for("edit_rating", id=movie_id))
    else:
        # Print an error message if the request was not successful
        response.raise_for_status()


if __name__ == '__main__':
    app.run(debug=True)
