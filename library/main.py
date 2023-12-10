from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from form import LibraryForm, EditBookForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

# Initialize the app with the extension
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create all database tables
with app.app_context():
    db.create_all()


@app.route("/delete_item/<int:book_id>")
def delete_item(book_id):
    # Find the book with the given ID in the database
    book_to_delete = Books.query.get(book_id)

    if book_to_delete:
        # Delete the book from the database
        db.session.delete(book_to_delete)
        db.session.commit()

        return redirect(url_for("home"))
    else:
        # Handle the case where the book is not found
        return "Book not found", 404


@app.route("/edit", methods=["GET", "POST"])
def edit_rating():
    book_id = request.args.get('book_id')
    form = EditBookForm()
    book_details = Books.query.get(book_id)
    if form.validate_on_submit():
        new_rating = float(form.rating.data)
        book_details.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, details=book_details)


@app.route("/home")
@app.route('/')
def home():
    with app.app_context():
        all_books = Books.query.all()
    return render_template("index.html", data=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = LibraryForm()
    if form.validate_on_submit():
        with app.app_context():
            book = Books(
                title=form.name.data,
                author=form.author.data,
                rating=form.rating.data
            )
            db.session.add(book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
