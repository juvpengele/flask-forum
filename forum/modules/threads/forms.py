from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from forum.models import Category


categories_choices = [(category.id, category.name) for category in Category.query.all()]


class ThreadCreationForm(FlaskForm):
    title = StringField("Question Title", validators=[DataRequired(), Length(max=100)])
    content = TextAreaField("Content", validators=[DataRequired(), Length(min=10)])
    category_id = SelectField("Category", validators=[DataRequired()], choices=categories_choices, coerce=int)
    submit = SubmitField("Create")

