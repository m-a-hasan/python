from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LibraryForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book')


class EditBookForm(FlaskForm):
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Edit Book')