from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email, Required, Length

class AccountForm(FlaskForm):
    
    name = StringField("Name", validators=[Required(), Length(min=1)])
    email = StringField("Email", validators=[Required(), Email()])
    submit = SubmitField("Update")