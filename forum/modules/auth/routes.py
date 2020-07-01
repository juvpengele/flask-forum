from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from forum.modules.auth.form import RegistrationForm
from forum import bcrypt
from forum.models.User import User
from forum.utilities.functions import generate_random_str
from datetime import datetime

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


@auth_blueprint.route('/register', methods=["GET", "POST"])
def register():
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        name = registration_form.name.data
        email = registration_form.email.data
        password = bcrypt.generate_password_hash(registration_form.password.data).decode('utf-8')
        confirmation_token = generate_random_str(50)

        User.create(name=name, email=email, password=password, confirmation_token=confirmation_token, created_at=datetime.utcnow())
        
        flash("You have been registered successfully. Please valid your email", "success")
        redirect(url_for("main.index"))

    return render_template('auth/register.html', form=registration_form)