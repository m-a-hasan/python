from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(100), nullable=True)
    ranking = db.Column(db.Integer)
