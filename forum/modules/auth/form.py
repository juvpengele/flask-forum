from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class RegistrationForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired(), Length(min=2)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    password_confirmation = PasswordField("Password (Confirmation)", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")