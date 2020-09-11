from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email, Required, Length, EqualTo
from flask_login import current_user
from forum import bcrypt

class AccountForm(FlaskForm):
    
    name = StringField("Name", validators=[Required(), Length(min=1)])
    email = StringField("Email", validators=[Required(), Email()])
    submit = SubmitField("Update")


class ChangePasswordForm(FlaskForm):

    current_password = PasswordField("Current password", validators=[Required(), Length(min=6)])
    new_password = PasswordField("New password", validators=[Required(), Length(min=6)])
    new_password_confirmation = PasswordField(
                                    "New password (confirmation)", 
                                    validators=[Required(), EqualTo("new_password")]
                                )
    submit = SubmitField("Update")

    def validate_current_password(form, field):
        if not bcrypt.check_password_hash(current_user.password, field.data):
            raise ValueError("You must provide your current password")
