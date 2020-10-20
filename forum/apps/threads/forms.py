from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from forum.database.models import Category
from forum.src.utilities.helpers import cached_categories

try:
    categories_choices = [(category.get("id"), category.get("name")) for category in cached_categories()]
except:
    categories_choices = []



class ThreadCreationForm(FlaskForm):
    title = StringField("Question Title", validators=[DataRequired(), Length(max=100)])
    content = TextAreaField("Content", validators=[DataRequired(), Length(min=10)])
    category_id = SelectField("Category", validators=[DataRequired()], choices=categories_choices, coerce=int)
    submit = SubmitField("Create")


