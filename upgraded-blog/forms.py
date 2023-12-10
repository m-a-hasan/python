from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class AddRecord(FlaskForm):
    # id used only by update/edit
    title = StringField("Blog Post Title", [DataRequired()])
    subtitle = StringField("Subtitle", [DataRequired()])
    author = StringField("Your Name", [DataRequired()])
    img_url = URLField("Blog Image URL", [DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField('Submit Post')
