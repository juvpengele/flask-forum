from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Email, Length
from forum.database.models import User
from forum import bcrypt


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    password_confirmation = PasswordField("Password (Confirmation)", validators=[DataRequired(),  EqualTo("password")])
    submit = SubmitField("Register")

    def validate_email(form, field):
        if User.query.filter_by(email=field.data).first() != None:
            raise ValueError("The email is already used by another user")
        

class LoginForm(FlaskForm):

    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Login")

    def validate_email(form, field):
        
        user = User.query.filter_by(email=field.data).first()
    
        if user == None:
            raise ValueError("Your credentials do not match with our records")

        if form.password.data == "" or bcrypt.check_password_hash(user.password, form.password.data) == False:
            raise ValueError("Your credentials do not match with our records")

        if user.email_verified_at == None:
            raise ValueError("You must validate your email before login")
