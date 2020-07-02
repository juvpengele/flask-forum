from datetime import datetime
from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from forum.modules.auth.form import RegistrationForm
from forum.modules.auth.form import LoginForm
from forum import bcrypt
from forum.models.User import User
from forum.utilities.functions import generate_random_str
from forum.mails.registration_mail import RegistrationMail


auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


@auth_blueprint.route('/register', methods=["GET", "POST"])
def register():
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        name = registration_form.name.data
        email = registration_form.email.data
        password = bcrypt.generate_password_hash(registration_form.password.data).decode('utf-8')
        confirmation_token = generate_random_str(50)

        user = User.create(name=name, email=email, password=password, confirmation_token=confirmation_token, created_at=datetime.utcnow())
        registration_mail = RegistrationMail(user)
        registration_mail.send()

        flash("You have been registered successfully. Please valid your email", "success")
        return redirect(url_for("main.index"))

    return render_template('auth/register.html', form=registration_form)


@auth_blueprint.route('/register/confirmation/<string:token>')
def register_confirmation(token):

    user = User.query.filter_by(confirmation_token=token).first_or_404()
    
    user.update({
        "confirmation_token":None,
        "email_verified_at":datetime.utcnow(),
        "updated_at": datetime.utcnow()
    })

    login_user(user)

    return redirect(url_for("main.index"))


@auth_blueprint.route('/login', methods=["GET", "POST"])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
                
        login_user(user)
        return redirect(url_for("main.index"))
        
    return render_template("auth/login.html", form=login_form)


@login_required
@auth_blueprint.route('/logout', methods=["POST"])
def logout():
    logout_user()

    flash("You are logged out successfully.", "success")
    return redirect(url_for('main.index'))