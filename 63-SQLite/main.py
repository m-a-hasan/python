from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

# ##################### Use SQLite #######################

# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# ###################### Using SQLAlchemy ########################
# Create the app
app = Flask(__name__)

# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Initialize the app with the extension
db = SQLAlchemy(app)


# Define the Books model
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create all database tables
with app.app_context():
    db.create_all()

# Create a new book and add it to the database
with app.app_context():
    book = Books(
        title="Harry Potter",
        author="J. K. Rowling",
        rating=9.3,
    )

    db.session.add(book)
    db.session.commit()